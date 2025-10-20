---
title: Permissions Info
long_title: Permissions Info - блок с доступными текущему пользователю правами
description: Как вывести разрешения, доступные текущему пользователю (как в vBulletin).
date: 2011-01-20
tags: [vBulletin, гости, пользователи, права, разделы, разрешения, темы, SMF 2.0]
categories: [translations]
---

Отображение в разделах и в темах основных прав, доступных и недоступных пользователям и гостям (как в vBulletin).

<!-- more -->

{{ img('Список прав, доступных и недоступных пользователю', 'permissions_info.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1118') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Permission Info
    $txt['permissions_info'] = 'Ваши права в разделе';
    $txt['post_new_topic_permission_yes'] = 'Вы <b>можете</b> создавать новые темы.';
    $txt['post_new_topic_permission_no'] = 'Вы <b>не можете</b> создавать новые темы.';
    $txt['reply_permission_yes'] = 'Вы <b>можете</b> отвечать в темах.';
    $txt['reply_permission_no'] = 'Вы <b>не можете</b> отвечать в темах.';
    $txt['attachment_permission_yes'] = 'Вы <b>можете</b> прикреплять вложения.';
    $txt['attachment_permission_no'] = 'Вы <b>не можете</b> прикреплять вложения.';
    $txt['modify_permission_yes'] = 'Вы <b>можете</b> изменять свои сообщения.';
    $txt['modify_permission_no'] = 'Вы <b>не можете</b> изменять свои сообщения.';
    $txt['bbc'] = 'ББ-теги';
    $txt['smiley'] = 'Смайлы';
    $txt['img'] = 'Тег [img]';
    $txt['html'] = 'HTML';
    $txt['enabled'] = '<b>Вкл.</b>';
    $txt['disabled'] = '<b>Выкл.</b>';
    ```
