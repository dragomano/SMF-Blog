---
title: Quick Buddies
long_title: Quick Buddies - быстрое добавление пользователей в друзья
description: Добавляем пользователей форума в друзья, кликая на специальную иконку.
date: 2014-07-25
tags: [SMF 2.0, SMF 2.1, друзья, пользователи]
categories: [translations]
---

В списке пользователей, а также в других частях форума появляется кнопочка для быстрого добавления конкретных пользователей в список друзей.

<!-- more -->

{{ img('По клику на плюсик пользователь добавится в друзья', 'quick_buddies.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=3900') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (для SMF 2.0) или в `Themes/default/languages/Modifications.russian.php` (для SMF 2.1):

    ```php
    <?php

    // Quick Buddies
    $txt['buddy_add'] = "Добавить пользователя '%s' в список друзей";
    $txt['buddy_remove'] = "Удалить пользователя '%s' из списка друзей";
    ```