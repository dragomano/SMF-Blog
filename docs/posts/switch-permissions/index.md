---
title: Switch Permissions
long_title: Switch Permissions - переключение прав доступа
description: Как проверить набор прав доступа другого пользователя, не заходя на его аккаунт.
date: 2010-08-21
tags: [права, профиль, SMF 2.0]
categories: [translations]
---

Быстрый просмотр чужих прав доступа.

<!-- more -->

{{ img('Переключаемся на права другого пользователя', 'switch_permissions.png') }}

## Особенности

* Суть мода такова: вы, как администратор, можете быстро переключиться на чужой набор прав доступа и посмотреть на форум «глазами» конкретного пользователя.
* Переключение осуществляется в профиле нужного пользователя — достаточно нажать на ссылочку.

{{ download('https://custom.simplemachines.org/index.php?mod=2703') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Switch Permissions
    $txt['switch_permissions_button'] = 'Переключить права доступа';
    $txt['switch_permissions_notice'] = 'В данный момент Вы просматриваете форум, обладая правами пользователя <strong><a href="?action=profile;u=%1$s">%2$s</a></strong>. Для возвращения исходных прав доступа <strong><a href="?action=switchpermissions;%3$s=%4$s">нажмите здесь.</a></strong>';
    ```
