---
title: Exclude boards from RSS feeds
long_title: Exclude boards from RSS feeds - убираем ненужные разделы из RSS ленты
description: Как убрать некоторые разделы из RSS ленты форума SMF?
date: 2011-11-24
tags: [SMF 2.0, rss, разделы]
categories: [translations]
---

Убираем определенные разделы из RSS-ленты форума.

<!-- more -->

## Особенности

* В свойствах ненужных разделов достаточно поставить соответствующую галочку — «Исключить этот раздел из RSS-ленты».

{{ download('https://custom.simplemachines.org/index.php?mod=3186') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Exclude Boards from Feeds
    $txt['mboards_exclude_from_feed'] = 'Исключить этот раздел из RSS-ленты';
    ```
