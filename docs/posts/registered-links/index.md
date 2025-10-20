---
title: Registered Links
long_title: Registered Links - скрываем ссылки от гостей
description: Скрываем ссылки на форуме от незарегистрированных пользователей.
date: 2009-12-10
tags: [гости, регистрация, ссылки, SMF 2.0, SMF 2.1]
categories: [translations]
---

Скрытие ссылок на форуме от незарегистрированных пользователей.

<!-- more -->

{{ download('https://custom.simplemachines.org/index.php?mod=342') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (для SMF 2.0) или в `Themes/default/languages/Modifications.russian.php` (для SMF 2.1):

    ```php
    <?php

    // Registered Links
    $txt['no_view_links'] = 'Вам не разрешено просматривать ссылки<br>';
    $txt['txt_reg_links_register'] = ' Зарегистрируйтесь';
    $txt['txt_reg_links_login'] = 'войдите на форум';
    $txt['txt_reg_links_or'] = 'или';
    ```
