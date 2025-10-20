---
title: Transparent Offline Avatars
long_title: Transparent Offline Avatars - прозрачные аватарки для пользователей офлайн
description: Сделаем аватарки пользователей, не находящихся онлайн, прозрачными.
date: 2011-05-13
tags: [аватары, онлайн, пользователи, SMF 2.0]
categories: [translations]
---

Модификация позволяет сделать прозрачными аватары пользователей, не находящихся онлайн.

<!-- more -->

{{ settings('Настройки модов → Transparent Offline Avatars.') }}

## Особенности

* Возможность установки уровня прозрачности (в процентах).

{{ download('https://custom.simplemachines.org/index.php?mod=2995') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Transparent Offline Avatars
    $txt['enable_transparent_avatars'] = 'Включить прозрачность для аватаров пользователей, не находящихся онлайн';
    $txt['transparent_avatars_tab'] = 'Transparent Offline Avatars';
    $txt['avatar_transparency_level'] = 'Уровень прозрачности<div class="smalltext">Например: 20 (чем меньше процент, тем меньше видимость).</div>';
    ```
