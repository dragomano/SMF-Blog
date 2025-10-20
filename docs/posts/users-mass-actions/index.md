---
title: Users Mass Actions
long_title: Users Mass Actions - действия с несколькими пользователями
description: Добавляем возможность применения основных администраторских действий сразу с несколькими пользователями.
date: 2011-08-21
tags: [бан, группы, пользователи, SMF 2.0]
categories: [translations]
---

На странице управления пользователями в админке появляется список для выполнения массовых действий.

<!-- more -->

{{ settings('Админка → Пользователи → Все пользователи.') }}

## Особенности

* Отмечаем нужных пользователей и выбираем в раскрывающемся списке ниже необходимые действия.
* Среди доступных действий: изменение основной/дополнительной групп, бан по именам/имейлам/IP и удаление пользователей.

{{ download('https://custom.simplemachines.org/index.php?mod=3104') }}

??? Русификация

    Добавить в файл `Themes\default\languages\Modifications.russian-utf8.php`:

    ```php
    <?php

    // Users mass actions
    $txt['admin_change_primary_membergroup'] = 'Изменить основную группу';
    $txt['admin_change_secondary_membergroup'] = 'Изменить/добавить дополнительную группу';
    $txt['confirm_remove_membergroup'] = 'Выбрав это, вы удалите все пользовательские группы! Уверены?';
    $txt['confirm_change_primary_membergroup'] = 'Хотите изменить основную группу для выбранных пользователей?';
    $txt['confirm_change_secondary_membergroup'] = 'Хотите изменить дополнительную группу для выбранных пользователей?';
    $txt['admin_ban_usernames'] = 'Бан по именам';
    $txt['admin_ban_useremails'] = 'Бан по имейлу';
    $txt['admin_ban_userips'] = 'Бан по IP';
    $txt['admin_ban_usernames_and_emails'] = 'Бан по именам и имейлам';
    $txt['users_mass_action_ban_name'] = 'Название списка банов для использования при массовом бане';
    ```
