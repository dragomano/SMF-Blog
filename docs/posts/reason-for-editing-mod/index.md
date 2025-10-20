---
title: Reason For Editing Mod
long_title: Reason For Editing Mod - причина редактирования сообщения
description: Как добавить возможность указывать причину редактирования сообщений.
date: 2010-03-23
tags: [пользователи, правка, сообщения, SMF 2.0]
categories: [translations]
---

После установки этого мода выбранные группы пользователей смогут указывать причину редактирования каждого своего сообщения.

<!-- more -->

{{ img('Просмотр причины редактирования сообщения', 'reason_editing.png') }}

## Особенности

- Настройка прав для каждой из имеющихся групп на указание причины правки сообщений.

{{ download('https://custom.simplemachines.org/index.php?mod=349') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Reason For Editing Mod
    $txt['reason'] = 'Причина';
    $txt['reason_edit'] = 'Причина редактирования';
    $txt['permissionname_reason_edit'] = 'Указание причины редактирования сообщений';
    $txt['permissionhelp_reason_edit'] = 'Предоставление пользователям из этой группы возможности указывать причину редактирования сообщений.';
    ```
