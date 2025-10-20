---
title: Recent Forum Topics on Board Index
long_title: Recent Forum Topics on Board Index - сайдбар с выбором разделов или категорий
description: Как вывести список тем на форуме SMF только из выбранных разделов или категорий?
date: 2023-03-24
tags: [разделы, сайдбар, SMF 2.1]
categories: [translations]
---

Модификация добавляет на главную страницу форума боковую панель, с возможностью быстрой сортировки тем по разделам и категориям.

<!-- more -->

{{ img('Пример боковой панели, добавляемой модом', 'recent_forum_topics.png') }}

## Особенности

- Отображение всех тем из выбранных разделов/категорий.
- Кастомизация положения и сортировки.
- Отображение аватарок пользователей с помощью мода [Avatars Display Integration](/translations/avatars-display-integration)

{{ download('https://custom.simplemachines.org/index.php?mod=4356') }}

??? Русификация

    Создать в папке `Themes/default/languages` файл `RecentTopicsBoardIndex.russian.php`:

    ```php
    <?php

    $txt['rtbi_title'] = 'Последние темы';
    $txt['rtbi_filter_b'] = 'Фильтровать по разделу';
    $txt['rtbi_filter_c'] = 'Фильтровать по категории';
    $txt['rtbi_forum_filter'] = 'Фильтр';
    $txt['rtbi_forum_filter_board'] = 'Фильтр по разделу: ';
    $txt['rtbi_forum filter category'] = 'Фильтр по категории: ';
    $txt['rtbi_topic_by'] = '%1$s %2$s в <em>%3$s</em>';
    $txt['rtbi_align_left'] = 'Темы слева, разделы справа';
    $txt['rtbi_align_right'] = 'Темы справа, разделы слева';
    $txt['rtbi_align_top'] = 'Темы вверху, разделы внизу (по умолчанию)';
    $txt['rtbi_align_col'] = 'Темы вверху, разделы внизу в 2 столбца';
    $txt['rtbi_topics_page'] = '5 тем на странице';
    $txt['rtbi_topic_starter_time'] = 'Дата создания';
    $txt['rtbi_topic_legend'] = 'Обозначения';
    $txt['rtbi_topic_icons'] = 'Иконки тем';
    $txt['rtbi_first_poster_avatar'] = 'Аватарка автора темы';
    $txt['rtbi_last_poster_avatar'] = 'Аватарка автора последнего сообщения';
    ```
