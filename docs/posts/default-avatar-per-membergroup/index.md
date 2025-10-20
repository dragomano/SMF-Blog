---
title: Default Avatar Per Membergroup
long_title: Default Avatar Per Membergroup - аватары по умолчанию для групп пользователей
description: Как назначить аватар по умолчанию для определенной группы пользователей.
date: 2012-07-11
tags: [SMF 2.0, аватары, группы, пользователи]
categories: [translations]
---

Устанавливаем аватар по умолчанию для каждой группы пользователей.

<!-- more -->

{{ img('Аватар по умолчанию указывается при создании группы', 'default_avatar_per_membergroup.png') }}

## Особенности

* Аватар указывается в настройках конкретной группы, либо при создании новой.
* При включении опции «*Принудительное использование аватара*» выбранное изображение заменит уже имеющиеся у пользователей аватары.

{{ download('https://custom.simplemachines.org/index.php?mod=3403') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Default Avatar Per Membergroup
    $txt['def_avatar_url'] = 'Аватар по умолчанию для этой группы:';
    $txt['def_avatar_settings'] = 'Установка аватара по умолчанию';
    $txt['def_avatar_first_msg'] = ' URL любого, поддерживаемого браузером, изображения';
    $txt['def_avatar_force'] = ' Принудительное использование указанного аватара';
    $txt['def_avatar_copy'] = 'Web Development by ForumMods.org';
    ```
