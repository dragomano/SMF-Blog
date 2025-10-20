---
title: Unanswered Topics
long_title: Unanswered Topics - непрочитанные темы
description: Как добавить ссылку на непрочитанные темы. Модификация для SMF.
date: 2016-04-26
tags: [темы, ответы, SMF 2.0, SMF 2.1]
categories: [translations]
---

В блоке приветствия на форуме появляется ссылка на темы без ответов.

<!-- more -->

{{ img('Ссылка на список тем без ответов', 'unanswered_topics.png') }}

## Особенности

* В общих настройках модификаций указывается количество дней, за которое будет происходить выборка тем.
* Там же можно выбрать способ отображения тем без ответов — в виде сообщений, либо в виде заголовков.

{{ download('https://custom.simplemachines.org/index.php?mod=4088') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (2.0) или в `Themes/default/languages/Modifications.russian.php` (2.1):

    ```php
    <?php

    // Unanswered Topics
    $txt['unanswered_topics'] = 'Темы без ответов';
    $txt['show_unanswered_topics'] = 'Показывать все темы без ответов.';
    $txt['show_unanswered_topics_limit'] = 'Темы без ответов за последние %d дней.';
    $txt['unanswered_topics_visit_none'] = 'Тем без ответов за последние %d дней не найдено.';
    $txt['unanswered_view_topics'] = 'Показывать как темы';
    $txt['unanswered_view_posts'] = 'Показывать как сообщения';
    ```

    В файл `ManageSettings.russian-utf8.php` (2.0) или в `ManageSettings.russian.php` (2.1) добавьте пару строчек:

    ```php
    <?php

    // Unanswered Topics
    $txt['unanswered_time_limit'] = 'Выборка тем без ответов:<div class="smalltext">(0 для отключения)</div>';
    $txt['unanswered_default_view'] = 'Как выводить темы без ответов:';
    ```
