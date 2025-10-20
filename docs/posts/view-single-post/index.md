---
title: View Single Post
long_title: View Single Post - ссылка на отдельное сообщение каждой темы
description: Как сделать ссылку конкретно на какой-либо пост внутри темы.
date: 2010-07-21
authors: [live627]
tags: [сообщения, темы, SMF 2.0]
categories: [translations]
---

Добавление ссылки на каждый отдельный пост в теме.

<!-- more -->

{{ img('Где брать эту ссылку', 'view_single_post.png') }}

## Особенности

* Пользователи получат возможность ссылаться на отдельный пост в каждой теме, который будет отображаться отдельно от остальных сообщений.

{{ download('https://custom.simplemachines.org/index.php?mod=541') }}

??? Русификация

    Добавить в файл `Themes\default\languages\Modifications.russian-utf8.php`:

    ```php
    <?php

    // View Single Post
    $txt['topic-start'] = 'Первое сообщение';
    ```
