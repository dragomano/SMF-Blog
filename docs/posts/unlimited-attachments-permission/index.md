---
title: Unlimited Attachments Permission
long_title: Unlimited Attachments Permission - загрузка вложений без ограничений
description: Как выдать пользователю разрешение на загрузку вложений без ограничений?
date: 2019-03-26
authors: [sesq]
tags: [вложения, права, SMF 2.1]
categories: [translations]
---

Иногда некоторым пользователям требуются специфические права на загрузку вложений, в обход заданных в настройках форума. Этот мод предназначен как раз для этого.

<!-- more -->

## Особенности

* Управление через права доступа (см. категорию «Права для разделов с глобальными привилегиями» => «Вложения» => «Освободить от ограничений при загрузке файлов»).

{{ download('https://custom.simplemachines.org/index.php?mod=4215') }}

??? Русификация

    Создать файл `Themes/default/languages/UnlimitedAttachmentsPermission.russian.php` со следующим содержанием:

    ```php
    <?php

    $txt['permissionname_unlimited_attachments'] = 'Освободить от ограничений при загрузке файлов';
    $txt['permissionhelp_unlimited_attachments'] = 'На пользователей с этим разрешением не действуют следующие ограничения при загрузке вложений:
    <ul class="bbc_list">
      <li>' . $txt['attachmentNumPerPostLimit'] . '</li>
      <li>' . $txt['attachmentSizeLimit'] . '</li>
      <li>' . $txt['attachmentPostLimit'] . '</li>
      <li>' . $txt['attachmentExtensions'] . '</li>
    </ul>
    <br>
    Это разрешение полезно, если включена опция «' . $txt['permissionname_post_attachment'] . '».';
    ```
