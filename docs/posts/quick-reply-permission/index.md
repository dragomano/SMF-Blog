---
title: Quick Reply Permission
long_title: Quick Reply Permission - разрешаем быстрый ответ не всем
description: Предоставляем возможность использовать быстрый ответ только определенным группам пользователей.
date: 2010-03-12
tags: [SMF 2.0, ответ, разрешения]
categories: [translations]
---

Добавление отдельного разрешения для использования быстрого ответа для выбранных групп пользователей.

<!-- more -->

{{ download('https://custom.simplemachines.org/index.php?mod=2482') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Quick Reply
    $txt['permissionname_can_quick_reply'] = 'Быстрый ответ';
    $txt['permissionhelp_can_quick_reply'] = 'Пользователи получают возможность быстрого ответа в темах, без перехода к полной форме.';
    $txt['permissiongroup_qr'] = 'Быстрый ответ';
    $txt['permissiongroup_simple_can_qr'] = 'Пользователи могут использовать быстрый ответ';
    ```
