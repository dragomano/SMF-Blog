import yaml
import datetime
from mkdocs.structure.nav import Navigation, Page
from mkdocs.structure.files import Files, File
from collections import defaultdict
import os
import re

def on_config(config):
    config['extra']['page_navigation'] = {}
    return config

def on_files(files: Files, config):
    try:
        categories = defaultdict(list)
        docs_dir = config['docs_dir']

        for file in files:
            if not file.is_documentation_page():
                continue

            file_path = os.path.join(docs_dir, file.src_uri)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            meta = yaml.safe_load(parts[1]) or {}
                            # Convert date to string to ensure JSON-serializability
                            if 'date' in meta and isinstance(meta['date'], (datetime.date, datetime.datetime)):
                                meta['date'] = meta['date'].strftime('%Y-%m-%d')
                        else:
                            meta = {}
                    else:
                        meta = {}
            except Exception as e:
                meta = {}

            categories_list = meta.get('categories', [])
            if isinstance(categories_list, str):
                categories_list = [categories_list]
            basename_src = os.path.basename(file.src_uri)
            dirname = os.path.dirname(file.src_uri)
            dir_slug = os.path.basename(dirname) if dirname else ''
            slug = meta.get('slug') or dir_slug or os.path.splitext(basename_src)[0]
            if not categories_list:
                continue

            date = meta.get('date', datetime.datetime.min)
            if isinstance(date, str):
                try:
                    date = datetime.datetime.strptime(date, '%Y-%m-%d')
                except ValueError:
                    date = datetime.datetime.min

            primary_category = categories_list[0] if categories_list else 'uncategorized'
            url = f"{primary_category}/" if slug == '' else f"{primary_category}/{slug}/"
            normalized_url = file.url.strip('/')

            page_info = {
                'title': meta.get('title', os.path.splitext(os.path.basename(file.src_uri))[0]),
                'url': url,
                'file_url': normalized_url,
                'date': date
            }

            for category in categories_list:
                categories[category].append(page_info)

        for category in categories:
            categories[category].sort(
                key=lambda x: x['date'],
                reverse=False
            )

        config['extra']['categories_navigation'] = dict(categories)

        return files
    except Exception as e:
        raise

def on_nav(nav: Navigation, config, files: Files):
    # Group pages by category and set previous/next within categories
    category_groups = {}
    for page in nav.pages:
        meta = getattr(page, 'meta', {})
        categories_list = meta.get('categories', [])
        if isinstance(categories_list, str):
            categories_list = [categories_list]
        primary_category = categories_list[0] if categories_list else 'uncategorized'
        if primary_category not in category_groups:
            category_groups[primary_category] = []
        category_groups[primary_category].append(page)

    for category, pages_list in category_groups.items():
        pages_list.sort(key=lambda p: p.meta.get('date', datetime.datetime.min), reverse=False)
        for i, page in enumerate(pages_list):
            if i > 0:
                page.previous_page = pages_list[i - 1]
            else:
                page.previous_page = None

            if i < len(pages_list) - 1:
                page.next_page = pages_list[i + 1]
            else:
                page.next_page = None

    return nav

def on_page_context(context, page: Page, config, nav: Navigation):
    try:
        if page is None:
            context['previous_page'] = None
            context['next_page'] = None
            return context

        meta = getattr(page, 'meta', {})
        normalized_page_url = page.url.strip('/')
        page_navigation = {'previous_page': None, 'next_page': None}
        navigation_key = normalized_page_url  # always use page URL as key

        # Try to use categories navigation if available
        if meta and 'categories' in meta and meta['categories']:
            categories_list = meta['categories']
            if isinstance(categories_list, str):
                categories_list = [categories_list]
            primary_category = categories_list[0]

            categories_navigation = config['extra'].get('categories_navigation', {})
            category_pages = categories_navigation.get(primary_category, [])

            current_index = None
            for i, p in enumerate(category_pages):
                if normalized_page_url == p['url'].strip('/'):
                    current_index = i
                    break

            if current_index is not None:
                if current_index > 0:
                    prev_page_info = category_pages[current_index - 1]
                    page_navigation['previous_page'] = {
                        'title': prev_page_info['title'],
                        'url': prev_page_info['url']
                    }
                    context['previous_page'] = type('Page', (), {
                        'title': prev_page_info['title'],
                        'url': prev_page_info['url']
                    })()
                else:
                    page_navigation['previous_page'] = None
                    context['previous_page'] = None

                if current_index < len(category_pages) - 1:
                    next_page_info = category_pages[current_index + 1]
                    page_navigation['next_page'] = {
                        'title': next_page_info['title'],
                        'url': next_page_info['url']
                    }
                    context['next_page'] = type('Page', (), {
                        'title': next_page_info['title'],
                        'url': next_page_info['url']
                    })()
                else:
                    page_navigation['next_page'] = None
                    context['next_page'] = None
            else:
                # Page not found in categories navigation, use MkDocs navigation if within category
                prev_meta = getattr(page.previous_page, 'meta', {}) if page.previous_page else {}
                prev_categories = prev_meta.get('categories', [])
                if isinstance(prev_categories, str):
                    prev_categories = [prev_categories]
                if page.previous_page and prev_categories and prev_categories[0] == primary_category:
                    page_navigation['previous_page'] = {'title': page.previous_page.title, 'url': page.previous_page.url}
                    context['previous_page'] = page.previous_page
                else:
                    page_navigation['previous_page'] = None
                    context['previous_page'] = None

                next_meta = getattr(page.next_page, 'meta', {}) if page.next_page else {}
                next_categories = next_meta.get('categories', [])
                if isinstance(next_categories, str):
                    next_categories = [next_categories]
                if page.next_page and next_categories and next_categories[0] == primary_category:
                    page_navigation['next_page'] = {'title': page.next_page.title, 'url': page.next_page.url}
                    context['next_page'] = page.next_page
                else:
                    page_navigation['next_page'] = None
                    context['next_page'] = None
        else:
            # Use MkDocs built-in navigation for pages without categories
            if hasattr(page, 'previous_page') and page.previous_page:
                page_navigation['previous_page'] = {
                    'title': page.previous_page.title,
                    'url': page.previous_page.url
                }
                context['previous_page'] = page.previous_page
            else:
                context['previous_page'] = None

            if hasattr(page, 'next_page') and page.next_page:
                page_navigation['next_page'] = {
                    'title': page.next_page.title,
                    'url': page.next_page.url
                }
                context['next_page'] = page.next_page
            else:
                context['next_page'] = None

        config['extra']['page_navigation'][navigation_key] = page_navigation

        return context
    except Exception as e:
        raise
