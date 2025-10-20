---
title: Mod Version Checker
long_title: Mod Version Checker - проверка обновлений модификаций
description: Как одной кнопкой проверить обновления сразу всех установленных модификаций?
date: 2022-06-02
tags: [SMF 2.0, SMF 2.1, модификации, диспетчер]
categories: [translations]
---

Любите обновления? Эта модификация поможет вам следить за обновлениями установленных на вашем форуме модификаций.

<!-- more -->

{{ img('Пример страницы новостей', 'mod_updates.png') }}

## Особенности

- Ручная проверка обновлений (см. скриншот).
- Проверка по расписанию (см. соответствующий пункт в _Диспетчере задач_).

{{ download('https://custom.simplemachines.org/index.php?mod=4335') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian.php`:

    ```php
    <?php

    // Mod Version Checker
    $txt['modvc_checkforupdates'] = 'Проверить обновления модификаций';
    $txt['modvc_modificationsupdates'] = 'Обновления модификаций';
    $txt['modvc_downloadupdate'] = '[Скачать обновление]';
    $txt['modvc_oldversion'] = 'Установленная версия';
    $txt['modvc_latestversion'] = 'Последняя версия';
    $txt['modvc_modsitelink'] = 'Ссылка на сайт';
    $txt['modvc_visitmod'] = '[Перейти на страницу модификации]';
    $txt['modvc_noupdatesfound'] = 'Вы идете в ногу со временем! Обновления модификаций не найдены!';
    $txt['scheduled_task_scheduled_modvercheck'] = 'Проверка обновлений модификаций';
    $txt['scheduled_task_desc_scheduled_modvercheck'] = 'Сравнивает версии установленных модификаций с последними версиями модификаций, найденными на сайте simplemachines.org';
    // END Mod Version Checker
    ```
