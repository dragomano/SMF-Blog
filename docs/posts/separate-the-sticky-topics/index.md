---
title: Separate the sticky topics
long_title: Separate the sticky topics - четкое разделение важных и обычных тем
description: Как визуально отделить закрепленные темы от обычных.
date: 2012-01-11
tags: [темы, SMF 2.0, SMF 2.1]
categories: [translations]
---

Удобное разделение прикрепленных и обычных тем.

<!-- more -->

{{ img('Прикрепленные темы теперь действительно привлекают внимание', 'separate_the_sticky_topics.png') }}

## Особенности

- После установки мода закрепленные темы будут подняты вверх, с надписью «Важные темы», а все остальные будут располагаться внизу, под меткой «Обычные».
- Разница по сравнению со стандартным режимом отображения — только в наличии надписей. Но так выглядит гораздо лучше, не так ли?

{{ download('https://custom.simplemachines.org/index.php?mod=3300') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (2.0) или в `Themes/default/languages/Modifications.russian.php` (2.1):

    ```php
    <?php

    // Separate the sticky topics
    $txt['costa_topico_fixo'] = 'Важные темы';
    $txt['costa_topico_normal'] = 'Обычные темы';
    ```
