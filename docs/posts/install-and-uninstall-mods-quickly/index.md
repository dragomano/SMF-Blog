---
title: Install & Uninstall Mods Quickly
long_title: Install & Uninstall Mods Quickly - быстрая переустановка модов
description: Добавляем кнопку для быстрой установки мода заново, после удаления.
slug: install-and-uninstall-mods-quickly
date: 2010-08-12
tags: [модификации, админка, SMF 2.0]
categories: [translations]
---

Простенькая модификация, добавляющая ссылку на повторную установку мода, после его удаления.

<!-- more -->

{{ img('Вот как это выглядит', 'iumq-min.png') }}

{{ info('Пригодится тем, кто занимается тестированием различных модификаций для SMF.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=2670') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Install & Uninstall Mods Quickly
    $txt['iumq_enable'] = 'Показывать кнопку для быстрой переустановки модов?';
    $txt['iumq_click'] = '';
    $txt['iumq_reinstall'] = 'Переустановить';
    $txt['iumq_mod'] =' мод';
    ```
