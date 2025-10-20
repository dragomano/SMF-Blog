---
title: Automatic Package Version Emulation
long_title: Automatic Package Version Emulation - автовключение эмуляции при установке модов
description: Как установить мод устаревшей версии на SMF 2.0.x? Эмуляция при установке.
date: 2016-09-17
tags: [SMF 2.0, модификации, эмуляция]
categories: [translations]
---

Включаем/выключаем эмуляцию при установке/удалении модификаций с неподходящей или устаревшей версией.

<!-- more -->

{{ img('Включение и отключение эмуляции в списке имеющихся модификаций', 'automatic-package-version-emulation.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=4086') }}

??? Русификация

    Добавить в файл `Packages.russian-utf8.php`:

    ```php
    <?php

    // Automatic Package Version Emulation
    $txt['install_emulating'] = 'Включить эмуляцию';
    $txt['uninstall_emulating'] = 'Отключить эмуляцию';
    $txt['upgrade_emulating'] = 'Обновить эмуляцию';
    ```
