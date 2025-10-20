---
title: Post History
long_title: Post History - история изменений сообщения
description: Как посмотреть историю изменений любого сообщения на форуме.
date: 2010-02-10
tags: [SMF 2.0, изменения, история, сообщения]
categories: [translations]
---

Мод добавляет возможность просматривать историю изменений сообщений пользователей.

<!-- more -->

{{ img('Пример истории изменений сообщения', 'post_history.png') }}

## Особенности

- Настройка прав доступа для просмотра истории измененных сообщений.
- Информация об авторе изменений.
- Просмотр всех версий сообщений (исходное, текущее).
- Возможность восстанавливать предыдущие версии сообщений.

{{ download('https://custom.simplemachines.org/index.php?mod=1841') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Post History Start
    $txt['core_settings_item_posthistory'] = 'История изменений';
    $txt['core_settings_item_posthistory_desc'] = 'Сохранение истории изменений содержания сообщений в базе данных.';
    $txt['view_post_history'] = 'Просмотр правок сообщения';
    $txt['title_view_post_history'] = 'Просматривает правки сообщения %1$s';
    $txt['ph_last_edit'] = 'Автор изменений';
    $txt['ph_last_time'] = 'Время правки';
    $txt['ph_view_edit'] = 'Просмотр';
    $txt['ph_original_edit'] = 'исходное';
    $txt['ph_current_edit'] = 'текущее';
    $txt['ph_current_original_edit'] = 'текущее, исходное';
    $txt['ph_no_edits'] = 'Пока никто не редактировал это сообщение';
    $txt['compare_selected'] = 'Сравнить выделенные';
    $txt['restore'] = 'Восстановить';
    $txt['permissionname_posthistory_view'] = 'Просмотр истории изменений сообщений';
    $txt['permissionhelp_posthistory_view'] = 'Разрешить пользователям просмотр старых версий сообщений';
    $txt['permissionname_posthistory_view_own'] = 'Собственное сообщение';
    $txt['permissionname_posthistory_view_any'] = 'Любое сообщение';
    $txt['permissionname_posthistory_restore'] = 'Восстановление старых версий';
    $txt['permissionhelp_posthistory_restore'] = 'Разрешить пользователям редактирование старых версий сообщений.';
    $txt['permissionname_posthistory_restore_own'] = 'Собственное сообщение';
    $txt['permissionname_posthistory_restore_any'] = 'Любое сообщение';
    $txt['permissionname_simple_posthistory_view_own'] = 'Просмотр истории изменений своих сообщений';
    $txt['permissionname_simple_posthistory_view_any'] = 'Просмотр истории изменений любых сообщений';
    $txt['permissionname_simple_posthistory_restore_own'] = 'Восстановление старых версий своих сообщений';
    $txt['permissionname_simple_posthistory_restore_any'] = 'Восстановление старых версий любых сообщений';
    $txt['cannot_posthistory_view_any'] = 'Вам не разрешён просмотр правок данного сообщения!';
    $txt['cannot_posthistory_restore_own'] = 'Вам не разрешено редактирование старых версий своих сообщений!';
    $txt['cannot_posthistory_restore_any'] = 'Вам не разрешено какое бы то ни было редактирование старых версий сообщений!';
    ```
