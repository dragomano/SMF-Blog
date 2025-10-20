---
title: DevCenter
long_title: DevCenter - помощник админа
description: Быстрый доступ к отладочной информации и количеству ошибок в логах.
date: 2017-05-18
authors: [diego]
tags: [SMF 2.1, логи, ошибки, отладка, phpinfo, админка]
categories: [translations]
---

Модификация пригодится разработчикам, поможет быстро включить отладочную информацию, покажет количество ошибок в логах и другие полезные сведения.

<!-- more -->

{{ img('Скромные настройки DevCenter', 'devcenter_settings.png') }}

{{ settings('Настройки модов → Настройки DevCenter.') }}

## Особенности

* Вывод счётчика ошибок в логах (в правой части пункта меню *Админка*, а также в правой части подпункта *Админка → Логи ошибок*).
* Отображение отладочной информации в подвале форума, без необходимости вручную править *Settings.php*: сведения об используемых шаблонах, языковых файлах, стилях, запросах к базе.
* Просмотр сведений об используемой версии PHP и подключенных библиотеках, по адресу: `<адрес форума>?action=phpinfo`.
* Просмотр сведений о текущей загрузке сервера (в подвале форума).

{{ download('https://custom.simplemachines.org/index.php?mod=3481') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // DevCenter mod -- Settings
    $txt['mods_cat_modifications_devcenter'] = $txt['devcenter'] = 'Настройки DevCenter';
    $txt['devcenter_menu_count_log_entries'] = 'Отображать количество ошибок в логах (см. в меню <em>Админка -> Логи ошибок</em> [<strong>счётчик</strong>])';
    $txt['devcenter_dont_show_when_0'] = 'Не отображать счётчик, если ошибок нет';
    $txt['devcenter_direct_printing_error'] = 'Отображать отладочную информацию (включая ошибки — будут видны каждому пользователю!)';
    $txt['devcenter_show_phpinfo'] = 'Отображать информацию phpinfo() при вызове экшена \'<a href="?action=phpinfo" target="_blank">phpinfo</a>\'';
    $txt['devcenter_displayserverload'] = 'Отображать в подвале сведения о загрузке сервера <strong>(не поддерживается Windows!)</strong>';
    $txt['devcenter_load'] = 'Нагрузка на сервер за последние 5, 10 и 15 минут соответственно: %s, %s, %s';
    ```
