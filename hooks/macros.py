def define_env(env):
    @env.macro
    def list_pages_from_categories(categories):
        result = ""
        pages = []

        # Используем files, но правильно обращаемся к метаданным
        for file in env.variables.files:
            if file.src_path.endswith('.md'):
                # Для File объектов метаданные могут быть в атрибуте page.meta
                if hasattr(file, 'page') and file.page and hasattr(file.page, 'meta'):
                    page_categories = file.page.meta.get('categories', [])
                    for cat in categories:
                        if cat in page_categories:
                            pages.append(file.page)
                            break

        # Удаляем дубликаты по URL
        unique_pages = []
        seen_urls = set()
        for page in pages:
            if page.url not in seen_urls:
                seen_urls.add(page.url)
                unique_pages.append(page)

        for page in sorted(unique_pages, key=lambda p: p.title.lower()):
            title = page.title
            long_title = page.meta.get('long_title', '')  # Получаем long_title
            url = page.url

            # Делаем URL абсолютным
            if not url.startswith('/'):
                url = '/' + url

            # Формируем заголовок: если есть long_title, используем его, иначе обычный title
            display_title = long_title if long_title else title

            result += f"- [{display_title}]({url})\n"
            result += "\n"

        return result

    @env.macro
    def debug_variables():
        # Выведем все ключи в variables для отладки
        keys = list(env.variables.keys())
        return f"Доступные ключи: {keys}"

    @env.macro
    def download(url: str, text: str = "Скачать") -> str:
        return f'[:octicons-download-16: {text}]({url}){{ .md-button }}'

    @env.macro
    def translation(url: str, text: str = "Скачать русификацию") -> str:
        return f'[:material-translate: {text}]({url}){{ .md-button .translation }}'

    @env.macro
    def note_link(url: str, text: str = "Примечание") -> str:
        return f'[:octicons-note-16: {text}]({url}){{ .md-button .extra }}'

    @env.macro
    def github(url: str, text: str = "GitHub") -> str:
        return f'[:octicons-mark-github-16: {text}]({url}){{ .md-button .github-link }}'

    @env.macro
    def ext_link(url: str, text: str = "") -> str:
        return f'[:octicons-link-external-16: {text}]({url}){{ .md-button }}'

    @env.macro
    def link(url: str, text: str = "") -> str:
        return f'[:material-link-variant: {text}]({url}){{ .md-button }}'

    @env.macro
    def alt_link(url: str, text: str = "") -> str:
        return f'[:material-link-variant: {text}]({url}){{ .md-button .extra }}'

    @env.macro
    def buy(price: str, url: str = "/about") -> str:
        return f'[:shopping_cart: Купить ({price})]({url}){{ .md-button .price }}'

    @env.macro
    def img(alt: str, path: str) -> str:
        return f'<figure markdown>\n![{alt}]({path}){{ loading=lazy }}\n</figure>'

    @env.macro
    def note(text: str, title: str = "Примечание") -> str:
        indented_text = '\n'.join(f'    {line}' for line in text.split('\n'))
        return f'!!! note "{title}"\n{indented_text}'

    @env.macro
    def warning(text: str, title: str = "Предупреждение") -> str:
        indented_text = '\n'.join(f'    {line}' for line in text.split('\n'))
        return f'!!! warning "{title}"\n{indented_text}'

    @env.macro
    def tip(text: str, title: str = "Совет") -> str:
        indented_text = '\n'.join(f'    {line}' for line in text.split('\n'))
        return f'!!! tip "{title}"\n{indented_text}'

    @env.macro
    def info(text: str, title: str = "Примечание") -> str:
        indented_text = '\n'.join(f'    {line}' for line in text.split('\n'))
        return f'!!! info "{title}"\n{indented_text}'

    @env.macro
    def settings(text: str) -> str:
        return '## Настройки\n\n!!! abstract "Как найти"\n\n    ' + text + '\n\n'