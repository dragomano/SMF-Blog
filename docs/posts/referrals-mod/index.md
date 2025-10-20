---
title: Referral System
long_title: Referral System - реферальная система для SMF
description: Как сделать реферальную систему при регистрации на форуме SMF.
date: 2010-02-08
tags: [пользователи, рефералы, SMF 2.0]
categories: [translations]
---

Мод добавляет функцию рефералов (приглашения других участников по специальной ссылке) на форум.

<!-- more -->

## Особенности

- Вся информация находится в профиле конкретного пользователя.

{{ download('https://custom.simplemachines.org/index.php?mod=1114') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Refferals System
    $txt['ref_admin'] = 'Система рефералов';
    $txt['ref_settings'] = 'Настройки';
    $txt['ref_save_settings'] = 'Сохранить настройки';
    $txt['ref_refferals'] = 'Рефералов:';
    $txt['ref_refferal_link'] = 'Реферальная ссылка:';
    $txt['ref_reffered_by'] = 'Имя пригласившего вас пользователя:';
    $txt['ref_showreflink'] = 'Показывать реферальные ссылки в профилях';
    $txt['ref_showonpost'] = 'Показывать рефералов на страницах тем';
    $txt['ref_trackcookiehits'] = 'Отслеживать переходы по реферальным ссылкам';
    $txt['ref_cookietrackdays'] = 'Сколько дней должен храниться cookie-файл для отслеживания рефералов';
    ```
