---
title: PM to New Members
long_title: PM to New Members - личное сообщение новичку на форуме
description: Как отправить приветственное сообщение пользователю после регистрации на форуме.
date: 2010-04-26
tags: [SMF 2.0, пользователи, регистрация, лс]
categories: [translations]
---

После регистрации на форуме пользователь получает личное сообщение, составленное администратором.

<!-- more -->

{{ img('Настройки мода в админке', 'pm_to_new_members.png') }}

{{ settings('Регистрация → Настройки.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1517') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // PM to New Members
    $txt['pm_register'] = 'Отправлять новым пользователям ЛС';
    $txt['pm_register_id'] = 'Укажите ID отправителя';
    $txt['pm_register_username'] = 'Укажите имя отправителя';
    $txt['pm_register_subject'] = 'Тема личного сообщения';
    $txt['pm_register_body'] = 'Текст сообщения (можно использовать BBC теги)';
    $txt['pm_register_body_desc'] = 'Составьте текст сообщения, которое будет отправляться каждому пользователю, зарегистрировавшемуся на форуме. Для вставки имени пользователя используйте переменную "<b>{$username}</b>". Для вставки названия форума используйте "<b>{$forumname}</b>".';
    ```
