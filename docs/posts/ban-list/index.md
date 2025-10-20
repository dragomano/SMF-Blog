---
title: Ban List
long_title: Ban List - список забаненных
description: Выводим список забаненных пользователей на отдельной странице.
date: 2010-01-12
tags: [SMF 2.0, бан, пользователи]
categories: [translations]
---

Страница, отображающая список забаненных пользователей форума.

<!-- more -->

## Особенности

* Отдельный список всех забаненных пользователей, с возможностью просмотра не только администраторами.
* Установка разрешений на просмотр списка забаненных.

{{ download('https://custom.simplemachines.org/index.php?mod=1198') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Ban List
    global $scripturl;

    $txt['banlist_menu'] = 'Пользователи в бане';
    $txt['permissionname_view_banlist'] = 'Просмотр списка забаненных пользователей';
    $txt['permissionhelp_view_banlist'] = 'В этом списке перечислены все игроки, которые проявили себя на этом форуме не должным образом.';
    $txt['cannot_view_banlist'] = 'У Вас нет разрешения на просмотр этого списка.';
    $txt['whoallow_banlist'] = 'Просматривает <a href="' . $scripturl . '?action=banlist">список забаненных пользователей</a>.';
    ```
