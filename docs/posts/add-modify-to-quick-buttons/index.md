---
title: Add Modify to Quick Buttons menu
long_title: Add Modify to Quick Buttons menu - меняем быстрое редактирование на полное
description: Как заменить кнопку быстрого редактирования на вызов полной формы редактирования.
date: 2024-09-30
tags: [SMF 2.1, интерфейс]
categories: [translations]
---

Модификация перемещает кнопку «Изменить» из раскрывающегося списка в одни ряд с кнопками «Цитировать» и «Редактировать».

<!-- more -->

{{ img('Вот как это выглядит', 'add_modify_to_quickbuttons_menu.png') }}

## Особенности

- Позволяет максимально быстро переходить к полной форме редактирования сообщения
- Избавляет ленивых пользователей от необходимости нажимать на кнопку «Ещё...»
- При желании можно полностью скрыть кнопку быстрого редактирования

{{ download('https://custom.simplemachines.org/index.php?mod=4406') }}

??? Русификация

    Создайте файл `Themes/default/languages/AM2QBM.russian.php`:

    ```php
    <?php

    // Add Modify to Quick Buttons menu
    $txt['AM2QBM_remove'] = '<strong><em>Добавить команду «Изменить» в меню «Быстрые кнопки»</em></strong><br>Удалить команду <em> «Редактировать»</em>';
    ```
