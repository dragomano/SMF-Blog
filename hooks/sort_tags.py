def on_page_context(context, page, config, nav):
    if 'tags' in context and context['tags']:
        tags = context['tags']
        priority_order = ['SMF 2.0', 'SMF 2.1', 'SMF 3.0', 'хуки']
        priority_order_lower = [s.lower() for s in priority_order]
        priority_tags = []
        remaining_tags = []

        # Разделяем теги на приоритетные и остальные
        for tag in tags:
            tag_str = str(tag['name']).lower() if isinstance(tag, dict) and 'name' in tag else str(tag).lower()
            if tag_str in priority_order_lower:
                priority_tags.append(tag)
            else:
                remaining_tags.append(tag)

        # Сортируем приоритетные теги в порядке priority_order
        priority_tags_sorted = []
        for prio_tag in priority_order:
            for tag in priority_tags:
                if (isinstance(tag, dict) and 'name' in tag and str(tag['name']).lower() == prio_tag.lower()) or \
                    (not isinstance(tag, dict) and str(tag).lower() == prio_tag.lower()):
                    priority_tags_sorted.append(tag)
                    break

        # Сортируем остальные теги по алфавиту
        remaining_tags_sorted = sorted(remaining_tags, key=lambda x: str(x['name']).lower() if isinstance(x, dict) and 'name' in x else str(x).lower())
        sorted_tags = priority_tags_sorted + remaining_tags_sorted

        # Обновляем context['tags']
        context['tags'] = sorted_tags

    return context