---
title: Recent Topics On Board Index
long_title: Recent Topics On Board Index - последние темы вместо сообщений
description: Как вывести последние темы вместо последних сообщений на главной странице форума?
date: 2010-11-08
tags: [сообщения, темы, SMF 2.0]
categories: [translations]
---

Отображение последних тем на главной странице форума (вместо последних сообщений).

<!-- more -->

{{ img('Последние темы вместо последних сообщений', 'recent_topics_on_board_index.png') }}

## Особенности

- Данный мод заменяет вывод последних сообщений (при условии, что соответствующая настройка активна — в свойствах текущей темы оформления)

{{ download('https://custom.simplemachines.org/index.php?mod=1314') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Text for the Recent Topics On Board Index.
    $txt['RecentTopicsOnBoardIndex_recenttopics'] = 'Последние темы';
    ```
