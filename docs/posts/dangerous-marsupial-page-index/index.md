---
title: Dangerous Marsupial Page Index
long_title: Dangerous Marsupial Page Index - меняем стиль указателя страниц
description: Как поменять оформление указателя страниц на форуме SMF 2.0?
date: 2020-02-14
tags: [SMF 2.0, пагинация]
categories: [translations]
---

Замена стандартного указателя страниц SMF красивым выпадающим списком, для удобного доступа как с компьютеров, так и с мобильных устройств.

<!-- more -->

{{ img('Пример нового оформления пагинации', 'dangerous_marsupial_page_index_sample.png') }}

## Особенности

Настроек нет — мод работает сразу после установки.

{{ download('https://custom.simplemachines.org/index.php?mod=4247') }}

??? Русификация

    Для русификации поместите в файл `Themes/default/languages/Modifications.russian.php` (или `Themes/default/languages/Modifications.russian-utf8.php`) указанные ниже строчки:

    ```php
    // Dangerous Marsupial Page Index
    $txt['antPages_select']   = 'Страница %1$d';
    $txt['antPages_selected'] = 'Страница %1$d из %2$d';
    $txt['antPages_previous'] = 'Предыдущая страница';
    $txt['antPages_next']     = 'Следующая страница';
    ```
