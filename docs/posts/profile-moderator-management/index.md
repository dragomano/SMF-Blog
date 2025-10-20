---
title: Profile Moderator Management
long_title: Profile Moderator Management - назначаем пользователей модераторами через профиль
description: Как быстро назначить пользователя модератором какого-либо раздела?
date: 2012-08-11
authors: [diego]
tags: [модератор, профиль, разделы, SMF 2.1]
categories: [translations]
---

Модификация для быстрого назначения пользователей модераторами разделов.

<!-- more -->

{{ img('Быстрый выбор разделов для модерирования', 'profile_moderator_management.png') }}

## Настройки

{{ settings('Профиль → Настройки профиля → Изменить профиль → Права модератора.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=833') }}

??? Русификация

    Добавить в файл `Profile.russian.php`:

    ```php
    <?php

    // Profile Moderator Management
    $txt['moderatorSettings_Headline'] = 'Выбор разделов для модерирования';
    $txt['moderatorSettings_info'] = 'Здесь можно выбрать разделы, в которых пользователь будет модератором.';
    $txt['moderatorSettings'] = 'Права модератора';
    $txt['moderatorSettings_selectBoards'] = 'Разделы для модерирования';
    ```
