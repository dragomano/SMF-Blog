---
title: Force Topic Read on Login
long_title: Force Topic Read on Login - редирект на заданную тему
description: Как при входе на форуме сделать перенаправление на определенную тему?
date: 2009-12-08
tags: [SMF 2.0, переадресация, редирект, темы]
categories: [translations]
---

Мод предоставляет возможность установить тему, в которую будут перенаправлены все пользователи при заходе на форум, при условии, что они не читали её ранее.

<!-- more -->

{{ img('Настройки мода в админке', 'force_topic_read.png') }}

{{ settings('Настройки модов.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1364') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Start Force Read Topic on Login Mod
    $txt['force_read_enable'] = 'Активировать переадресацию после авторизации на форуме?<br><span class="smalltext" style="font-weight: bold;">(Все пользователи будут принудительно перенаправлены к теме с указанным ниже ID, если они не читали её ранее)</span>';
    $txt['force_read_topic_id'] = 'Введите ID темы';
    // End Force Read Topic on Login Mod
    ```

    Для перевода справки добавьте в файл `Help.russian-utf8.php` следующий текст:

    ```php
    // Start Force Read Topic on Login Mod
    $helptxt['force_read_topic_id'] = 'Чтобы узнать ID нужной темы, сделайте следующее:<br>-Откройте эту тему.<br>-Скопируйте URL из адресной строки браузера. Этот адрес имеет такой формат: http://yoursite.com/forum/index.php?topic=<b>123456</b>.0<br>-Скопируйте ID темы (выделенные жирным цифры: <b>123456</b>)<br>-Перейдите в "Характеристики и настройки" > "Настройки модификаций" в панели управления<br>-Вставьте ID темы (<b>123456</b>) в соответствующее поле';
    // End Force Read Topic on Login Mod
    ```
