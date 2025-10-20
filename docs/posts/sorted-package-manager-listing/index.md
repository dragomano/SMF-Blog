---
title: Sorted Package Manager Listing
long_title: Sorted Package Manager Listing - сортируем модификации
description: Управляем отображением модификаций в админке форума.
date: 2010-02-25
tags: [модификации, сортировка, список, SMF 2.0, SMF 2.1]
categories: [translations]
---

Сортировка всех имеющихся на форуме модификаций по определенным критериям.

<!-- more -->

{{ img('Страница пакетов модификаций', 'sorted_package_manager_listing.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=875') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (2.0) или в `Themes/default/languages/Modifications.russian.php` (2.1):

    ```php
    <?php

    // --- Sorted Package Manager Listing ---
    $txt['pkgstate_cannot_install'] = 'Неудачная установка';
    $txt['pkgstate_cannot_uninstall'] = 'Установленные - Неудаляемые (нет секции удаления для этой версии SMF)';
    $txt['pkgstate_cannot_uninstall_2'] = 'Установленные - Неудаляемые';
    $txt['pkgstate_cannot_upgrade'] = 'Необновляемые';
    $txt['pkgstate_install'] = 'Неустановленные';
    $txt['pkgstate_uninstall'] = 'Установленные';
    $txt['pkgstate_upgrade'] = 'Обновляемые';
    $txt['pkgstatehelp_cannot_install'] = 'Эти моды не могут быть установлены на используемую версию форума. Попробуйте связаться с автором каждого мода и попросить его обновить свой продукт для поддержки последней версии SMF.';
    $txt['pkgstatehelp_cannot_uninstall_2'] = 'Эти моды установлены, но авторы были настолько ленивы, что даже не сделали их удаляемыми. Вам придётся удалять эти моды вручную.';
    $txt['pkgstatehelp_cannot_upgrade'] = 'Эти моды установлены и для них доступны обновления. Однако что-то мешает им обновиться.';
    $txt['pkgstatehelp_install'] = 'Эти моды не установлены. Возможно, некоторые из них не совместимы с используемой версией SMF.';
    $txt['pkgstatehelp_uninstall'] = 'Эти моды уже установлены и могут быть удалены.';
    $txt['pkgstatehelp_upgrade'] = 'Установлены предыдущие версии этих модов. Установка новой версии мода обновит текущую.';
    ```
