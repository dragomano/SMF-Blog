---
title: Additional Profile Permissions
long_title: Additional Profile Permissions - расширенные права доступа
description: Настраиваем возможность избранным группам редактировать поля в профилях.
date: 2011-12-24
tags: [SMF 2.0, права, профиль]
categories: [translations]
---

Добавление дополнительных прав доступа для изменения некоторых полей в профиле.

<!-- more -->

## Особенности

* После установки мода появится несколько дополнительных прав доступа:
    * Редактирование подписи.
    * Редактирование информации о веб-сайте и расположении.
    * Редактирование профилей.
    * Редактирование паролей и секретных вопросов.
    * Редактирование надписей над аватарами.

{{ download('https://custom.simplemachines.org/index.php?mod=3237') }}

??? Русификация

    Добавить в файл `ManagePermissions.russian-utf8.php`:

    ```php
    <?php

    // Additional Profile Permissions
    $txt['permissionname_profile_signature'] = 'Редактирование подписей';
    $txt['permissionhelp_profile_signature'] = 'Пользователи смогут изменять подпись в профилях.';
    $txt['permissionname_profile_signature_own'] = 'Собственная подпись';
    $txt['permissionname_profile_signature_any'] = 'Любая подпись';
    $txt['permissionname_profile_forum'] = 'Редактирование профилей';
    $txt['permissionhelp_profile_forum'] = 'Включение этой опции позволит пользователям редактировать профили на форуме.';
    $txt['permissionname_profile_forum_own'] = 'Собственный профиль';
    $txt['permissionname_profile_forum_any'] = 'Любой профиль';
    $txt['permissionname_profile_other'] = 'Изменение веб-сайта и расположения';
    $txt['permissionhelp_profile_other'] = 'Пользователи смогут редактировать информацию о сайте и расположении в профилях.';
    $txt['permissionname_profile_other_own'] = 'Собственный профиль';
    $txt['permissionname_profile_other_any'] = 'Любой профиль';
    $txt['permissionname_profile_password'] = 'Смена паролей';
    $txt['permissionhelp_profile_password'] = 'Пользователи смогут изменять пароли или секретные вопросы в профилях.';
    $txt['permissionname_profile_password_own'] = 'Собственный профиль';
    $txt['permissionname_profile_password_any'] = 'Любой профиль';
    $txt['permissionname_profile_blurb'] = 'Редактирование надписей над аватарами';
    $txt['permissionhelp_profile_blurb'] = 'Включение этой опции позволит пользователям изменять надписи над аватарами.';
    $txt['permissionname_profile_blurb_own'] = 'Собственный профиль';
    $txt['permissionname_profile_blurb_any'] = 'Любой профиль';
    ```
