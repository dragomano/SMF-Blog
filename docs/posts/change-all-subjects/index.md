---
title: Change All Subjects
long_title: Change All Subjects - изменяем заголовки всех сообщений сразу
description: Как изменить заголовки всех сообщений в теме одновременно.
date: 2010-09-10
authors: [live627]
tags: [SMF 2.0, сообщения, темы, заголовки]
categories: [translations]
---

Добавление возможности одновременного изменения заголовков всех сообщений одной темы при изменении названия темы.

<!-- more -->

{{ img('Пункт, добавляемый модом', 'change_all_subjects.png') }}

## Особенности

* Изменение всех заголовков сообщений при редактировании первого сообщения своей/любой темы (см. *Права доступа*).

{{ download('https://custom.simplemachines.org/index.php?mod=1165') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Change All Subjects
    $txt['changeallsubject'] = 'Изменить заголовки всех сообщений.';
    $txt['permissionname_change_all_subjects'] = 'Изменение заголовков всех сообщений';
    $txt['permissionhelp_change_all_subjects'] = 'Позволяет пользователям изменять заголовки всех сообщений сразу при редактировании названия темы.';
    $txt['permissionname_change_all_subjects_own'] = 'В собственной теме';
    $txt['permissionname_change_all_subjects_any'] = 'В любой теме';
    ```
