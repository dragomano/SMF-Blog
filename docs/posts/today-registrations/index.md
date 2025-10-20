---
title: Today Registrations
long_title: Today Registrations - просмотр последних регистраций за сутки
description: Как вывести список пользователей, зарегистрировавшихся за последние сутки?
date: 2018-03-05
tags: [регистрация, SMF 2.0]
categories: [translations]
---

В нижней части главной страницы форума появляется дополнительный блок, с перечислением пользователей, которые зарегистрировались за последние сутки.

<!-- more -->

{{ img('Просмотр сообщений за последние сутки', 'today_registrations.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=4171') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Today Registrations
    $txt['today_registrations'] = 'Зарегистрировались сегодня';
    ```
