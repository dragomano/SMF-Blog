---
title: Show Recent Topics by 24h 48h 72h
long_title: Recent Topics by 24h 48h 72h Filter - просмотр последних сообщений за 1-2-3 дня
description: Как просмотреть сообщения за последние 1-2-3 дня?
date: 2018-02-05
slug: recent-topics-filter
tags: [сообщения, SMF 2.0]
categories: [translations]
---

В шапке шаблона появляются дополнительные ссылки для просмотра недавних сообщений за сутки, два дня или три дня.

<!-- more -->

{{ img('Просмотр сообщений за последние сутки', 'recent_topics.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=3288') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Recent Topics by 24h 48h 72h Filter
    $txt['show_recent_topics'] = 'Показать темы за последние: ';
    $txt['recent_topics'] = 'Темы за последние %d ч.';
    $txt['recent_topics_none'] = 'За прошедшие %d ч. не было новых/обновленных тем';
    ```
