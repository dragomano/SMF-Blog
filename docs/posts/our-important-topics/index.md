---
title: Our Important Topics
long_title: Our Important Topics - отмечаем тему как важную
description: Как добавить важную тему на форуме SMF в отдельный список?
date: 2018-03-26
tags: [SMF 2.0, SMF 2.1, темы, закладки]
categories: [translations]
---

Модификация разрешает выбранным группам пользователей создавать списки закладок на интересные темы.

<!-- more -->

{{ img('Страница с важными темами пользователя', 'our_important_topics.png') }}

{{ settings('Конфигурация → Настройки модов...') }}

## Особенности

- В нижней части тем появляется новая кнопка — "Пометить тему как важную".
- Расположение ссылки на важные темы настраивается (по умолчанию — отдельный пункт в главном меню).
- В правах доступа настраиваются разрешения на пометку и просмотр важных тем — выставьте нужным группам.

{{ download('https://custom.simplemachines.org/index.php?mod=4133') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (для SMF 2.0) или в `Themes/default/languages/Modifications.russian.php` (для SMF 2.1):

    ```php
    <?php

    // Our Important Topics
    $txt['itm_important_topics'] = 'Важные темы';
    $txt['itm_no_important_topics'] = 'Важных тем пока нет...';
    $txt['itm_unmark_as_important'] = 'Пометить как неважную';
    $txt['itm_unmark_confirm'] = 'Удалить выбранные темы из списка важных?';
    $txt['itm_mark_as_important'] = 'Пометить как важную';
    $txt['itm_menu_top_level'] = 'Главное меню';
    $txt['itm_menu_under_level'] = 'Под "%s"';
    $txt['itm_menu_home'] = 'Где разместить ссылку "%s"';
    $txt['permissionname_mark_important'] = 'Пометка тем как важных';
    $txt['permissionname_view_important'] = 'Просмотр тем, помеченных как важные';
    ```
