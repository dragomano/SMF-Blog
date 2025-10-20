---
title: Forum Visitors
long_title: Forum Visitors - просмотр посетителей раздела
description: Как узнать, кто из пользователей заходил в конкретный раздел форума?
date: 2019-03-18
tags: [SMF 2.0, разделы, пользователи]
categories: [translations]
---

Модификация добавляет кнопку внутри каждого раздела, при нажатии на которую отображается список посетителей раздела.

<!-- more -->

{{ img('Кнопка "Журнал посителей"', 'forum_visitors.png') }}

## Особенности

* Настроек нет, кнопка отображается модераторам.

{{ download('https://custom.simplemachines.org/index.php?mod=4212') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Forum Visitors
    $txt['forumvisitors_link'] = 'Журнал посетителей';
    $txt['board_visitors'] = 'Список всех пользователей, заходивших в раздел';
    ```
