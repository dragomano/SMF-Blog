---
title: Admin ban button in post
long_title: Admin ban button in post - кнопка для бана в сообщениях
description: Добавляем кнопку для быстрой отправки в бан на форуме SMF.
date: 2011-02-07
tags: [SMF 2.0, бан, пользователи, сообщения]
categories: [translations]
---

В сообщениях пользователей появляется кнопочка, позволяющая осуществить быстрый бан пользователя.

<!-- more -->

{{ img('Вот как это выглядит', 'admin_ban_button.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1962') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Admin ban button in post
    $txt['admin_ban_button'] = 'Забанить';
    ```
