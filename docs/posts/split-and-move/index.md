---
title: Split and Move
long_title: Split and Move - удобное разделение тем
description: Добавим больше функционала в стандартную функцию разделения тем.
date: 2012-01-16
tags: [темы, сообщения, SMF 2.0]
categories: [translations]
---

Расширенная функциональность при разделении тем.

<!-- more -->

{{ img('Использование шаблонов', 'split_and_move.png') }}

## Особенности

* При разделении появится выбор раздела для создания в нем новых тем.
* Возможность добавления предварительно созданных сообщений в новую и старую темы.

{{ download('https://custom.simplemachines.org/index.php?mod=3257') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Split and Move
    $txt['sam_post_split_notification'] = 'Оставлять сообщение при разделении тем';
    $txt['notify_bot_name'] = 'Имя пользователя (лучше бота), от которого будет приходить уведомление о переносе темы';
    $txt['notify_bot_email'] = 'Имейл пользователя (лучше бота)';
    $txt['sam_default_notify_message'] = 'Текст в последнем сообщении старой темы (после разделения)';
    $txt['sam_default_new_message'] = 'Текст в первом сообщении новой темы (после разделения)';
    $txt['sam_default_notify_bot_name'] = 'Уведомление';
    $txt['sam_default_message_note'] = 'Значение пока не сохранено. Никаких сообщений не опубликовано';
    ```

    Для перевода справки добавьте в файл `Help.russian-utf8.php`:

    ```php
    <?php

    // Split and Move
    $helptxt['sam_default_notify_message'] = 'Можно использовать следующие переменные:
    <ul>
    <li>{NEXT_TOPIC_URL} - адрес новой темы.</li>
    <li>{NEXT_TOPIC_SUBJECT} - заголовок новой темы.</li>
    <li>{NEXT_TOPIC_LINK} - ссылка на новую тему.</li>
    </ul>';
    $helptxt['sam_default_new_message'] = 'Можно использовать следующие переменные:
    <ul>
    <li>{PREV_TOPIC_URL} - адрес оригинальной темы.</li>
    <li>{PREV_TOPIC_SUBJECT} - заголовок оригинальной темы.</li>
    <li>{PREV_TOPIC_LINK} - ссылка на оригинальную тему.</li>
    </ul>';
    ```
