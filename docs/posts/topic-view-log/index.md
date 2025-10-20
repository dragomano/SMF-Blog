---
title: Topic View Log
long_title: Topic View Log - статистика просмотров темы
description: Как узнать, кто заходил в вашу тему, и когда. Модификация для SMF.
date: 2016-01-26
authors: [live627]
tags: [просмотры, статистика, темы, SMF 2.0]
categories: [translations]
---

Статистика просмотров любой темы — кто заходил на страницу, когда заходил.

<!-- more -->

## Особенности

* После установки не забудьте настроить права доступа для тех групп пользователей, которым хотите разрешить просмотр лога тем.
* Кнопочка «Статистика» находится на странице просмотра каждой темы.

{{ download('https://custom.simplemachines.org/index.php?mod=4060') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Topic View Log
    global $scripturl;

    $txt['tvl_title'] = 'Статистика';
    $txt['tvl_times'] = 'Последнее посещение';
    $txt['tvl_lastView'] = 'Последний просмотр';
    $txt['permissionname_tvl_view'] = 'Просмотр статистики темы';
    $txt['permissionhelp_tvl_view'] = 'Данное разрешение дает возможность пользователям просматривать лог тем (узнавать, кто и когда смотрел тему).';
    $txt['permissionname_tvl_view_own'] = 'Собственная тема';
    $txt['permissionname_tvl_view_any'] = 'Любая тема';
    $txt['permissionname_simple_tvl_view_own'] = 'Просмотр статистики своей темы';
    $txt['permissionname_simple_tvl_view_any'] = 'Просмотр статистики любой темы';
    $txt['tvl_no_topic_id'] = 'ID темы не указан.';
    $txt['tvl_no_topic'] = 'Тема не существует.';
    $txt['who_topiclog'] = 'Просматривает статистику темы <a href="' . $scripturl . '?action=topiclog;id=%d.0">%s</a>.';
    $txt['cannot_tvl_view_own'] = 'Вы не можете просматривать статистику собственной темы.';
    $txt['cannot_tvl_view_any'] = 'Вы не можете просматривать статистику указанной темы.';
    ```
