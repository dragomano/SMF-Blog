---
title: Show BBCode to guests
long_title: Show BBCode to guests - прячем бб теги от гостей
description: Как скрыть содержание некоторых BB тегов от гостей форума.
date: 2010-03-02
tags: [bbcode, гости, права, SMF 2.0]
categories: [translations]
---

Скрытие содержания выбранных тегов от гостей — достаточно отметить нужные в настройках.

<!-- more -->

## Настройки

{{ settings('Форум → Сообщения и темы → BB код.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=2861') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Show BBCode to guests
    $txt['hiddenBBC'] = 'ББ-теги, доступные гостям';
    $txt['bbcTagsToHide_select'] = 'Выберите теги, содержимое которых будет доступно гостям';
    $txt['mod_not_allowed_see'] = 'Извините, вам не разрешено просматривать этот текст.';
    ```
