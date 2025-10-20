---
title: Membergroup Prefixes
long_title: Membergroup Prefixes - префиксы для групп пользователей
description: Как добавить различные префиксы для пользовательских групп.
date: 2011-06-14
authors: [suki]
tags: [группы, пользователи, префиксы, SMF 2.0]
categories: [translations]
---

Модификация позволяет добавлять префиксы к группам пользователей, отображаемые перед названиями групп.

<!-- more -->

{{ img('Для каждой группы можно добавить префикс', 'membergroup_prefixes.png') }}

{{ settings('Группы пользователей → Редактирование групп.') }}

## Особенности

- *Управление префиксами* производится на странице групп: нужно выбрать желаемую группу и нажать «Изменить»

{{ download('https://custom.simplemachines.org/index.php?mod=3031') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Membergroup Prefixes
    $txt['group_prefix_title'] = 'Префиксы групп';
    $txt['enable_group_prefix'] = 'Разрешить префиксы для групп';
    $txt['prefix'] = 'Префикс';
    $txt['prefix2'] = 'Префикс группы';
    ```
