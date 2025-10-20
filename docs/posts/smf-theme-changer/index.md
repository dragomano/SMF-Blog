---
title: SMF Theme Changer
long_title: SMF Theme Changer - быстрое переключение активных шаблонов
description: Как быстро сменить шаблон форума, не заходя в админку.
date: 2012-04-30
tags: [шаблоны, SMF 2.0, SMF 2.1]
categories: [translations]
---

Добавление списка для быстрого переключения шаблонов.

<!-- more -->

## Особенности

* Список для выбора шаблонов закрепляется либо в верхней, либо в нижней частях форума. Либо и вверху, и внизу сразу (в зависимости от настроек).

{{ download('https://custom.simplemachines.org/index.php?mod=3356') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (2.0) или в `Themes/default/languages/Modifications.russian.php` (2.1):

    ```php
    <?php

    // SMF Theme Changer
    $txt['cls-head'] = 'Выберите тему';
    $txt['cls_title'] = 'Переключатель шаблонов';
    $txt['change_theme_check_top'] = 'Разместить наверху';
    $txt['change_theme_check_bot'] = 'Разместить внизу';
    ```
