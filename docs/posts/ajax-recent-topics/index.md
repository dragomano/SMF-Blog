---
title: AJAX Recent Topics
long_title: AJAX Recent Topics - обновляемая страничка с последними темами
description: Добавляем отдельную, автоматически обновляемую, страницу для вывода последних тем форума.
date: 2010-06-10
authors: [live627]
tags: [SMF 2.0, SMF 2.1, ajax, темы]
categories: [translations]
---

Отдельная страница, с периодическим обновлением, для просмотра последних тем форума.

<!-- more -->

{{ img('Список тем', 'ajax_recent_topics.png') }}

## Особенности

* Возможность настроить количество последних тем для отображения, а также задать интервал обновлений.

{{ download('https://custom.simplemachines.org/index.php?mod=1284') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // AJAX Recent Topics
    $txt['recent_topics'] = 'Последние темы';
    $txt['minutes_ago'] = ' минут назад';
    $txt['number_recent_topics_interval'] = 'Задержка времени (в секундах) между проверкой обновлённых тем';
    $txt['number_recent_topics_interval_desc'] = 'Не слишком низкое значение, 5-10 секунд будет достаточно';
    $txt['number_recent_topics'] = 'Количество тем для отображения на странице «Последние темы»';
    ```
