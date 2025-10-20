---
title: Paragrapher
long_title: Paragrapher - умные абзацы
description: Как использовать правильные абзацы вместо переноса строки на форуме SMF?
date: 2020-07-10
authors: [sesq]
tags: [SMF 2.0, SMF 2.1, сообщения, абзацы]
categories: [translations]
---

Paragrapher заменяет переносы строк (`<br>`) в сообщениях семантически правильными элементами абзацев (тег `<p>`).

<!-- more -->

{{ img('Нормальные параграфы в сообщениях форума', 'paragrapher.png') }}

{{ settings('Админка → Настройки модификаций.') }}

## Особенности

- Конвертация переносов строк в абзацы.
- Нормализация макета при форматировании абзацев
- Содержимое тегов `[code][/code]` и `[pre][/pre]` не затрагивается.
- Сообщения в базе данных не меняются.
- Влияет на отображение сообщений на форуме, личных сообщений, RSS-лент и через SSI.
- Простая интеграция с другими модами.

{{ download('https://custom.simplemachines.org/index.php?mod=4074') }}

??? Русификация

    Создать файл `Paragrapher.russian.php` (для SMF 2.1), или `Paragrapher.russian-utf8.php` (для SMF 2.0 UTF8):

    ```php
    <?php

    $txt['paragrapher_normalize_layout'] = 'Нормализация макета при форматировании абзацев';
    $txt['paragrapher_single_br'] = 'Использовать <strong>br</strong> для создания новых абзацев';
    $txt['paragrapher_never'] = 'Никогда';
    $txt['paragrapher_always'] = 'Всегда';
    $txt['paragrapher_smart'] = 'Если нужно';
    ```