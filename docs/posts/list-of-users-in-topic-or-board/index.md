---
title: List Of Users In Topic or Board
long_title: List Of Users In Topic or Board - пользователи, просматривающие тему или раздел
description: Как вывести список пользователей, просматривающих текущую тему или раздел.
date: 2015-01-12
tags: [пользователи, разделы, темы, SMF 2.0, SMF 2.1]
categories: [translations]
---

Добавление отдельного блока пользователей, находящихся внутри темы или раздела.

<!-- more -->

{{ img('Пример вывода списка пользователей, просматривающих тему', 'list_of_users.png') }}

## Особенности

- Доступ к списку пользователей настраивается отдельно для каждой группы пользователей — в *Правах доступа*

{{ download('https://custom.simplemachines.org/index.php?mod=4015') }}

??? Русификация

    === "SMF 2.0"

        Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

        ```php
        <?php

        // List Of Users In Topic or Board
        $txt['users_browsing_topic'] = $txt['users_browsing_board'] = 'Просматривают тему';
        $txt['users_browsing_board'] = 'Просматривают раздел';
        ```

        В файл `ManagePermissions.russian-utf8.php` добавляем блок:

        ```php
        <?php

        // List Of Users In Topic or Board
        $txt['permissionname_view_users_in_topic'] = 'Доступ к списку пользователей, просматривающих тему';
        $txt['permissionhelp_view_users_in_topic'] = 'Позволяет видеть пользователей, которые в данный момент находятся на страницах темы.';
        $txt['permissionname_view_users_in_board'] = 'Доступ к списку пользователей, просматривающих раздел';
        $txt['permissionhelp_view_users_in_board'] = 'Позволяет видеть пользователей, которые в данный момент находятся внутри раздела.';
        ```

    === "SMF 2.1"

        Добавить в файл `Themes/default/languages/Modifications.russian.php`:

        ```php
        <?php

        // List Of Users In Topic or Board
        $txt['users_browsing_topic'] = $txt['users_browsing_board'] = 'Просматривают тему';
        $txt['users_browsing_board'] = 'Просматривают раздел';
        ```

        В файл `ManagePermissions.russian.php` добавляем блок:

        ```php
        <?php

        // List Of Users In Topic or Board
        $txt['permissionname_view_users_in_topic'] = 'Доступ к списку пользователей, просматривающих тему';
        $txt['permissionhelp_view_users_in_topic'] = 'Позволяет видеть пользователей, которые в данный момент находятся на страницах темы.';
        $txt['permissionname_view_users_in_board'] = 'Доступ к списку пользователей, просматривающих раздел';
        $txt['permissionhelp_view_users_in_board'] = 'Позволяет видеть пользователей, которые в данный момент находятся внутри раздела.';
        ```
