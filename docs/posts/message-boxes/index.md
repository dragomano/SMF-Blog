---
title: Message Boxes
long_title: Message Boxes - красивые сообщения
description: Добавляем красивое оформление для сообщений с помощью CSS.
date: 2010-01-18
authors: [diego]
tags: [SMF 2.1, CSS, блоки, оформление, сообщения]
categories: [translations]
---

Дополнительные ББ-теги для красивого оформления сообщений.

<!-- more -->

{{ img('Пример оформления блоков', 'css_message_boxes.png') }}

## Особенности

- 4 новые кнопки в редакторе сообщений.
- Возможность оформлять не только текст, но и изображения и пр.

{{ download('https://custom.simplemachines.org/index.php?mod=2078') }}

??? Русификация

    Создать файл `Themes/default/languages/mboxes/.russian.php`:

    ```php
    <?php

    // BBC
    $txt['error_bbc'] = 'Добавить бокс со значком ошибки';
    $txt['warning_bbc'] = 'Добавить бокс со значком предупреждения';
    $txt['okay_bbc'] = 'Добавить бокс со значком подтверждения';
    $txt['info_bbc'] = 'Добавить бокс со значком информации';

    // Settings
    $txt['mboxes_settings'] = 'Настройки мода Message Boxes';
    $txt['permissiongroup_mboxes_use'] = 'Права доступа Message Boxes';
    $txt['permissionname_mboxes_use'] = 'Выбор блоков сообщений в редакторе';
    $txt['permissionname_mboxes_use_desc'] = 'Это не помешает пользователям вручную вводить ББ-теги';
    $txt['groups_mboxes_use'] = 'Выбор блоков сообщений в редакторе';
    $txt['permissionhelp_mboxes_use'] = 'Укажите группы пользователей, которым разрешено выбирать блоки сообщений.';
    $txt['permissionhelp_groups_mboxes_use'] = 'Определяет, может ли пользователь выбирать блоки сообщений.';
    $txt['cannot_mboxes_use'] = 'Вам не разрешено пользоваться блоками сообщений.';
    $txt['mboxes_style'] = 'Иконки блоков';
    $txt['mboxes_types']  = [
    	'classic' => 'Классические',
    	'modern'  => 'Современные',
    	'octagon' => 'Современные восьмиугольные',
    ];
    ```
