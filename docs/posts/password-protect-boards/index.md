---
title: Password Protect Boards
long_title: Password Protect Boards - пароли для разделов
description: Как защитить раздел форума на движке SMF паролем? Модификация.
date: 2011-10-02
tags: [SMF 2.0, пароль, разделы]
categories: [translations]
---

Защита разделов форума паролем. Доступ только для избранных.

<!-- more -->

{{ img('Указываем пароль в свойствах раздела', 'password_protect_boards_settings.png') }}

## Особенности

- Пароль устанавливается в свойствах конкретного раздела — то есть для каждого раздела можно ввести отдельный пароль.
- После защиты паролем разделы по-прежнему видны на главной странице, но для входа в защищенный раздел потребуется указать пароль.
- По истечении сессии потребуется повторный ввод пароля.

{{ download('https://custom.simplemachines.org/index.php?mod=2873') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Password Protected Board
    $txt['passwd_board'] = 'Введите пароль доступа, пожалуйста: ';
    $txt['mpasswd_board'] = 'Пароль для доступа к разделу';
    $txt['mpasswd_board_desc'] = 'Оставьте пустым, если не нужно';
    $txt['passwd_board_enter'] = 'Готово';
    $txt['passwd_board_notice'] = 'Раздел защищён';
    $txt['passwd_board_error'] = 'На раздел установлен пароль доступа, который необходимо ввести для просмотра тем внутри раздела.';
    ```
