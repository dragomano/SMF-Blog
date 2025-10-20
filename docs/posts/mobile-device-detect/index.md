---
title: Mobile Device Detect
long_title: Mobile Device Detect - смена темы оформления для мобильных устройств
description: Как сменить тему оформления при просмотре форума с мобильных устройств.
date: 2012-03-14
tags: [SMF 2.0, шаблоны]
categories: [translations]
---

Загрузка определенной темы оформления при просмотре форума с мобильных устройств.

<!-- more -->

{{ settings('Конфигурация → Темы оформления → Управление и установка.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=3349') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Mobile Device Detect
    $txt['mobile_theme_id'] = 'Тема при использовании мобильных устройств';
    ```
