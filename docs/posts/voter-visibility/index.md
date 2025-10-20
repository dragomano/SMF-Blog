---
title: Voter Visibility
long_title: Voter Visibility - просмотр голосов в опросе
description: Как узнать, кто и как ответил в голосовании на форуме SMF.
date: 2012-05-05
tags: [опросы, результаты, SMF 2.0]
categories: [translations]
---

Возможность узнать, кто за что проголосовал, с дополнительными параметрами.

<!-- more -->

{{ img('Просмотр голосов', 'vote_visibility.png') }}

## Особенности

* Модификация добавляет 3 возможных типа для каждого опроса — общий, раздельный и частный.
* Результаты общего голосования доступны всем; результаты раздельного — только автору темы/голосования и/или администраторам.
* Результаты частного опроса доступны только администратору форума.
* Кроме того, доступно комментирование отдельных вариантов каждого голосования (то есть пользователи должны будут пояснять свой выбор).

{{ download('https://custom.simplemachines.org/index.php?mod=3373') }}

??? Русификация

    Добавить в файл `Themes\default\languages\Modifications.russian-utf8.php`:

    ```php
    <?php

    // Voter Visibility
    $txt['poll_vv_opt'] = 'Просмотр списка проголосовавших';
    $txt['poll_vv_opt_ro'] = '(только для чтения)';
    $txt['poll_vv_opt_public'] = 'ОТКРЫТЫЙ';
    $txt['poll_vv_opt_discrete'] = 'РАЗДЕЛЬНЫЙ';
    $txt['poll_vv_opt_private'] = 'ЧАСТНЫЙ';
    $txt['poll_vv_opt_public_txt'] = 'Результаты доступны всем.';
    $txt['poll_vv_opt_discrete_txt'] = 'Результаты доступны только автору и админам.';
    $txt['poll_vv_opt_private_txt'] = 'Результаты доступны только админам.';
    $txt['poll_vv_vlog_empty'] = 'Никто пока не голосовал.';
    $txt['poll_vv_vlog_title'] = 'Лог голосов';
    $txt['poll_vv_vlog_button'] = 'Просмотр голосов';
    $txt['poll_vv_vlog_for'] = 'Ответы на %1$s опрос:';
    $txt['poll_vv_vlog_th_tstamp'] = 'Дата';
    $txt['poll_vv_vlog_th_member'] = 'Пользователь';
    $txt['poll_vv_vlog_th_choicenum'] = 'Выбор';
    $txt['poll_vv_vlog_th_choicelbl'] = 'Текст';
    $txt['poll_vv_vlog_th_comment'] = 'Комментарий';
    $txt['poll_vv_vlog_err_discrete'] = 'Опрос является РАЗДЕЛЬНЫМ, а вы не автор и не администратор!';
    $txt['poll_vv_vlog_err_private'] = 'Опрос является ЧАСТНЫМ, а вы не администратор!';
    $txt['poll_vv_vlog_vote_warning'] = 'Это %1$s опрос. %2$s';
    $txt['poll_vv_vlog_guest_or_unknown'] = '(Гость или удаленный пользователь)';
    $txt['poll_vv_shwcmt_opt'] = 'Разрешить комментарии';
    $txt['poll_vv_reqcmt_opt'] = 'Требовать комментарий для вариантов';
    $txt['poll_vv_reqcmt_warn'] = '(требуется комментарий)';
    $txt['poll_vv_cmt_label'] = 'Комментарий';
    $txt['poll_vv_cmt_missing_required'] = 'При выборе варианта %1$d: "%2$s" его нужно обязательно прокомментировать.';
    ```
