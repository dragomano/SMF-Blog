---
title: BBC Message Boxes
long_title: BBC Message Boxes - цветные блоки сообщений
description: Оформляем сообщения на форуме с помощью цветных CSS-блоков.
date: 2020-03-21
authors: [live627]
tags: [SMF 2.1, css, блоки, оформление, сообщения]
categories: [translations]
---

Ещё одна модификация для оформления сообщений с помощью красивых цветных блоков.

<!-- more -->

{{ img('Цветные блоки сообщений', 'bbc_message_boxes.png') }}

## Особенности

* Кнопки для вставки блоков в редакторе сообщений.
* Никаких настроек и прав доступа — установите мод и все пользователи смогут им пользоваться.

{{ download('https://custom.simplemachines.org/index.php?mod=4248') }}

??? Русификация

    Добавить в файл `MessageBoxes.russian.php` (в кодировке UTF-8):

    ```php
    <?php

    $txt['error_bbc'] = 'Добавить блок ошибки';
    $txt['warning_bbc'] = 'Добавить блок предупреждения';
    $txt['okay_bbc'] = 'Добавить блок "Ок"';
    $txt['info_bbc'] = 'Добавить блок информации';
    ```
