---
title: Recent Post Settings
long_title: Recent Post Settings - скрываем некоторые сообщения на главной странице
description: Добавляем возможность запретить вывод последних сообщений из выбранных тем, разделов, категорий.
date: 2011-09-06
tags: [инфоцентр, сообщения, SMF 2.0]
categories: [translations]
---

Возможность запретить вывод последних сообщений из выбранных тем, разделов, категорий.

<!-- more -->

## Настройки

{{ settings('Настройки модов → Блок "Последние сообщения".') }}

{{ download('https://custom.simplemachines.org/index.php?mod=2975') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Recent Post Settings
    $txt['hide'] = 'Блок "Последние сообщения"';
    $txt['hide_categories'] = 'Не показывать выбранные <i><b>категории</b></i>';
    $txt['hide_boards'] = 'Не показывать выбранные <i><b>разделы</b></i>';
    $txt['hide_topics'] = 'Не показывать выбранные <i><b>темы</b></i>';
    $txt['guide_hide'] = 'Несколько значений разделяйте запятыми, без всяких пробелов!';
    ```
