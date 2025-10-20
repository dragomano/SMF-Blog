import os
import yaml

def on_page_markdown(markdown, page, config, files, **kwargs):
    # Добавляем секцию "Похожие моды" на основе метаданных 'related'
    if hasattr(page, 'meta') and 'related' in page.meta:
        result = []
        # Обрабатываем каждый путь из списка 'related' (например, mods/optimus или /mods/optimus)
        for link in page.meta['related']:
            found_page = find_page_by_link(link, files, config)
            if found_page:
                title = get_page_title(found_page, config)
                url = ensure_absolute_url(found_page.url)
                result.append(f"- [{title}]({url})")

        # Если найдены связанные посты, добавляем секцию в Markdown
        if result:
            markdown += f"\n\n## Похожие моды\n\n" + "\n".join(result)

    return markdown

def ensure_absolute_url(url):
    # Преобразуем URL в абсолютный, добавляя '/' в начало и сохраняя конечный слеш
    if not url:
        return url
    if not url.startswith('/'):
        url = '/' + url
    if not url.endswith('/'):
        url += '/'  # Добавляем конечный слеш для соответствия use_directory_urls
    return url

def find_page_by_link(link, files, config):
    # Нормализуем путь из 'related', убирая начальный слеш (например, /mods/optimus → mods/optimus)
    normalized_link = link.lstrip('/').replace('/', os.sep).replace('\\', os.sep)
    docs_dir = config['docs_dir']  # Путь к папке docs

    # Извлекаем slug, удаляя категорию (например, mods/optimus → optimus)
    slug = normalized_link
    if os.sep in normalized_link:
        slug = normalized_link.split(os.sep)[-1]
        # Поддержка путей вида posts/optimus
        if normalized_link.startswith('posts' + os.sep):
            parts = normalized_link.split(os.sep)
            if len(parts) >= 2:  # Например, posts/optimus
                slug = parts[-1]

    # Формируем возможные пути файла, учитывая структуру posts/<slug>/index.md
    possible_paths = [
        os.path.join('posts', slug, 'index.md'),  # posts/optimus/index.md
        os.path.join('posts', slug + '.md'),      # posts/optimus.md
        normalized_link + '.md',                  # mods/optimus.md (для обратной совместимости)
        os.path.join(normalized_link, 'index.md'), # mods/optimus/index.md
        normalized_link                           # posts/optimus
    ]

    # Ищем файл в коллекции files
    for test_path in possible_paths:
        for f in files:
            if f.src_path == test_path:
                return f
    return None

def get_page_title(file, config):
    # Извлекаем заголовок страницы из метаданных или имени файла
    try:
        # Читаем метаданные из файла
        file_path = os.path.join(config['docs_dir'], file.src_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    meta = yaml.safe_load(parts[1]) or {}
                    title = meta.get('title')
                    if title:
                        return title
        # Если заголовок не найден, формируем из имени файла или папки
        base_name = os.path.splitext(os.path.basename(file.src_path))[0]
        if base_name == 'index':
            base_name = os.path.basename(os.path.dirname(file.src_path))
        return base_name.replace('-', ' ').replace('_', ' ').title()
    except Exception:
        return "Страница без заголовка"