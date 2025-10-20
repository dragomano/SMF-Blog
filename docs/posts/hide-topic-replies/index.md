---
title: Hide Topic Replies
long_title: Hide Topic Replies - скрываем ответы в темах
description: Как спрятать ответы в темах от гостей. Модификация для SMF.
date: 2010-05-11
tags: [SMF 2.0, ответы, сообщения, темы]
categories: [translations]
---

Полезная модификация, дающая возможность скрывать ответы в темах от незарегистрированных пользователей форума.

<!-- more -->

{{ img('Пример работы мода', 'hide_topic_replies_view.png') }}

{{ settings('Форум → Настройки тем.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=2082') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Hide Topic Replies Mod.
    $txt['hideTopicReplies'] = 'Скрывать ответы в темах от гостей';
    $txt['hideTopicReplies_notify'] = 'Здравствуйте, Гость! В этой теме %1$d ответ(ов), но увидеть их могут только зарегистрированные пользователи.';
    ```
