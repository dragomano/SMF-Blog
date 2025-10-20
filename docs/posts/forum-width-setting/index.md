---
title: Forum Width Setting
long_title: Forum Width Setting - изменение ширины форума
description: Как изменить ширину форума SMF 2.1?
date: 2019-04-23
authors: [sycho]
tags: [SMF 2.1, css, шаблоны]
categories: [translations]
---

Если используемый шаблон кажется слишком узким или, наоборот, широким — попробуйте этот мод. Он поможет установить нужную ширину форума, не трогая CSS файлы.

<!-- more -->

{{ img('Новая опция в настройках темы оформления', 'forum_width_setting_preview.png') }}

{{ settings('Админка → Конфигурация → Текущая тема оформления.') }}

## Особенности

* Установка ширины в пикселях или процентах.
* Возможность изменить ширину любой из установленных тем оформления (но не с каждой эта опция может заработать).

{{ download('https://custom.simplemachines.org/index.php?mod=4223') }}

??? Русификация

    Для русификации создайте файл `Themes/default/languages/ForumWidth.russian.php` со следующим содержанием:

    ```php
    <?php

    $txt['forum_width'] = 'Ширина форума';
    $txt['forum_width_desc'] = 'Укажите ширину форума в пикселях или процентах. Например: 950px, 80%, 1240px.';
    $txt['forum_width_warning'] = '<br><span class="error">Может не работать на этой теме!</span>';
    ```
