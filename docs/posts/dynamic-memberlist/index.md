---
title: Dynamic Memberlist
long_title: Dynamic Memberlist - стильное оформление списка пользователей
description: Меняем стандартное оформление списков пользователей на более красивое.
date: 2010-03-21
tags: [SMF 2.0, пользователи, списки]
categories: [translations]
---

Динамическая сортировка пользователей по разным параметрам, с красивым оформлением списка.

<!-- more -->

{{ img('Изящное оформление списка пользователей', 'dynamic_memberlist.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1718') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    /* Dynamic Memberlist mod */
    $txt['joined'] = 'Регистрация';
    $txt['last_active'] = 'Последняя активность';
    /* End Dynamic Memberlist mod */
    ```
