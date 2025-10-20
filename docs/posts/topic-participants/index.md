---
title: Topic Participants
long_title: Topic Participants - список участников темы
description: Как отобразить список участников текущей темы?
date: 2023-09-04
authors: [live627]
tags: [участники, темы, SMF 2.0, SMF 2.1]
categories: [translations]
---

Отображение списка участвующих в обсуждении пользователей, в нижней части каждой темы.

<!-- more -->

{{ img('Пример блока участников', 'topic_participants.png') }}

{{ settings('Настройки модификаций.') }}

## Особенности

* Установка максимального количества участников, отображаемых в блоке (все остальные будут отображены по клику на дополнительной ссылке)
* Добавление разрешения «Просмотр участников тем» в разделе _Права доступа по группам — Права для разделов с глобальными привилегиями_

{{ download('https://custom.simplemachines.org/index.php?mod=4374') }}

??? Русификация

    Создать файл `TopicParticipants.russian.php` (2.1) или `TopicParticipants.russian-utf8.php` (2.0):

    ```php
    <?php

    $txt['topic_participants'] = 'Участники';
    $txt['topic_participants_num'] = 'Количество пользователей, участвующих в обсуждении, для отображения ниже темы';
    $txt['topic_participants_num_subtext'] = '(0 — показать всех)';
    $txt['permissionname_view_topic_participants'] = 'Просмотр участников тем';
    $txt['permissionname_view_topic_participants_own'] = 'В своей теме';
    $txt['permissionname_view_topic_participants_any'] = 'В любой теме';
    $txt['permissionname_simple_view_topic_participants_own'] = 'Отображение участников в темах, начатых этими людьми';
    $txt['permissionname_simple_view_topic_participants_any'] = 'Отображение участников в темах, начатых другими людьми';
    $txt['permissionhelp_view_topic_participants'] = 'Позволяет просмотр списка пользователей, участвующих в темах.';
    ```
