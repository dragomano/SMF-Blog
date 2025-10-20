---
title: Name History on Profile
long_title: Name History on Profile - история переименований в профиле
description: Как увидеть список всех изменений имен пользователя в SMF?
date: 2018-09-30
authors: [sycho]
tags: [SMF 2.0, пользователи, профиль]
categories: [translations]
---

Модификация помогает увидеть хронику переименований пользователей через профили.

<!-- more -->

{{ img('Как это выглядит, пример в профиле', 'name_history.png') }}

{{ settings('Настройки модов → Настройки истории переименований.') }}

## Особенности

- Управление работой мода через соответствующую опцию в настройках.
- Отображение истории переименований в виде блока или раскрывающегося списка.
- Лимит на максимальное количество отображаемых переименований.

{{ download('https://custom.simplemachines.org/index.php?mod=4188') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // NameHistory Mod By SychO
    $txt['namehistory_title'] = "История переименований";
    $txt['namehistory_modsettings'] = "Настройки истории переименований";
    $txt['namehistory_show'] = "Показывать историю переименований в профиле";
    $txt['namehistory_limit'] = "Максимальное количество изменений для отображения";
    $txt['namehistory_permission'] = "Группы с правом просмотра истории переименований";
    $txt['namehistory_dropmenu'] = "Показывать историю переименований в виде раскрывающегося списка вместо блока";
    $txt['namehistory_before'] = "До";
    $txt['namehistory_after'] = "После";
    $txt['namehistory_date'] = "Дата";
    ```
