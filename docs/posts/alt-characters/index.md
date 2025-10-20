---
title: Alt Characters
long_title: Alt Characters - использование спецсимволов
description: Добавляем в редактор кнопки для вставки спецсимволов.
date: 2011-07-08
tags: [SMF 2.0, bbcode, редактор, символы]
categories: [translations]
---

Добавление дополнительных кнопок для вставки специальных символов в сообщения.

<!-- more -->

{{ img('Кнопки, добавляемые модом в редактор', 'alt_characters.png') }}

## Особенности

* В редакторе сообщений появляется несколько новых кнопок для вставки символов:
    * знак копирайта,
    * плюс/минус,
    * дроби и т.п.

{{ download('https://custom.simplemachines.org/index.php?mod=3054') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Alt Characters
    $txt['degree'] = 'Степень';
    $txt['quarter'] = 'Одна четвертая';
    $txt['half'] = 'Одна вторая';
    $txt['3qtrs'] = 'Три четвертых';
    $txt['copywrt'] = 'Copyright';
    $txt['ocirc'] = 'Маленькая o с циркумфлексом';
    $txt['ediae'] = 'Маленькая e с диерезисом';
    $txt['idiae'] = 'Маленькая i с диерезисом';
    $txt['micro'] = 'Micro';
    $txt['plusminus'] = 'Плюс/Минус';
    ```
