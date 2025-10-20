---
title: Order Custom Profile Fields
long_title: Order Custom Profile Fields - изменение порядка дополнительных полей
description: Добавляем возможность менять местами дополнительные поля профиля.
date: 2010-06-12
tags: [SMF 2.0, поля, порядок, профиль]
categories: [translations]
---

Небольшой мод для изменения порядка дополнительных полей в профилях.

<!-- more -->

## Особенности

- Возможность ручного изменения порядка дополнительных полей.
- Мод не работает без предварительного включения функции "**Расширенные поля профиля**" в админке.

{{ download('https://custom.simplemachines.org/index.php?mod=1328') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Text for the Order Custom Profile Fields mod.
    $txt['OrderCustomProfileFields_up'] = 'Вверх';
    $txt['OrderCustomProfileFields_down'] = 'Вниз';
    $txt['OrderCustomProfileFields_dragdrop_desc'] = 'Строчки в этом списке можно менять местами. Для этого кликните на нужную строку и переместите на другую позицию.';
    ```
