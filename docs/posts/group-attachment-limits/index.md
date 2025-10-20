---
title: Group attachment limits
long_title: Group attachment limits - лимит на размер вложений для разных групп
description: Как установить лимиты на размер и количество вложений для разных групп пользователей.
date: 2013-03-04
tags: [SMF 2.0, вложения, группы, ограничения, пользователи]
categories: [translations]
---

Возможность установить ограничения на максимальный размер и количество вложений для каждой группы отдельно.

<!-- more -->

{{ img('Настройки мода', 'group_attachment_limits.png') }}

{{ settings('Вложения и аватары → Лимиты вложений.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=3621') }}

??? Русификация

    Добавить в файл `Admin.russian-utf8.php`:

    ```php
    // Group Attachment Limits mod RUS
    $txt['attachment_limits'] = 'Лимиты вложений';
    $txt['attachment_limit_settings'] = 'Настройки мода Attachment Limit';
    $txt['attachment_limit_desc'] = 'Здесь можно установить ограничения на размер и количество вложений для каждой группы пользователей отдельно. Значения по умолчанию, установленные на странице "Свойства вложений", выделены курсивом.<br>Для снятия ограничений введите 0. Для сброса к установкам по умолчанию просто очистите нужное поле и сохраните изменения.';
    $txt['attachmentPostGroupLimit'] = 'Максимальный размер всех вложений<br>в одном сообщении, в килобайтах)';
    $txt['attachmentSizeGroupLimit'] = 'Максимальный размер<br>одного вложения, в килобайтах';
    $txt['attachmentNumPerPostGroupLimit'] = 'Максимальное количество<br>вложений в одном сообщении';
    ```
