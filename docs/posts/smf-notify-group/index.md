---
title: SMF Notify Group
long_title: SMF Notify Group - управление уведомлениями пользователей
description: Как вручную подписать пользователя на уведомления в каких-либо темах или разделах.
date: 2012-01-07
tags: [SMF 2.0, группы, пользователи, уведомления]
categories: [translations]
---

Подписка на уведомления о новых сообщениях в темах или в разделах, для групп или конкретных пользователей.

<!-- more -->

## Особенности

- В разделах и темах появляется новая кнопочка — "Уведомления".
- Мод пригодится, если захочется подписать целую группу (или каких-то отдельных пользователей) на обновления в нужном разделе или в теме.

{{ download('https://custom.simplemachines.org/index.php?mod=2310') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // SMF Notify Group
    $txt["notifygroup"] = "Уведомления";
    $txt["select_topic"] = "Выберите раздел или тему";
    $txt["reset"] = "Сброс";
    $txt["go_to_topic"] = "Перейти в тему";
    $txt["go_to_board"] = "Перейти в раздел";
    $txt["reselect_group"] = "Отменить выбор";
    $txt["select_group"] = "Выбранные группы ";
    $txt["select_member"] = "Выбранных пользователей ";
    $txt["notify"] = "Уведомлять";
    $txt["denotify"] = "Не уведомлять";
    $txt["receiving_notification"] = "Группы/пользователи, подписанные на уведомления в ";
    $txt['notifygroup_prefUpdated'] = 'Настройки обновлены для пользователя: ';
    $txt['notifygroup_emailNotExist'] = 'Извините, этот имейл не существует.';
    $txt['notifygroup_enterEmail'] = 'Введите имейл для обновления настроек.';
    $txt['notifygroup_setOff'] = 'Отключить уведомления';
    $txt['notifygroup_setOn'] = 'Включить уведомления';
    ```