---
title: Footnotes
long_title: Footnotes - сноски к тексту
description: Как добавить сноску к тексту в сообщении на форуме SMF?
date: 2010-02-13
tags: [SMF 2.0, сноска, сообщения]
categories: [translations]
---

Добавление в редактор сообщений кнопки для создания сносок к тексту.

<!-- more -->

{{ img('Пример сноски в сообщении', 'footnotes.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1771') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Footnotes
    $txt['noisen_footnote'] = 'Сноска';
    ```
