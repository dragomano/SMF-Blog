---
title: CountryFlags
long_title: CountryFlags - флаги стран
description: Добавляем выбор страны пользователя в профиле или при регистрации.
date: 2010-02-12
tags: [SMF 2.0, SMF 2.1, страны, флаги]
categories: [translations]
---

Возможность указывать страну проживания в профиле пользователя или при регистрации на форуме, с дальнейшим отображением флага выбранной страны (под аватаром, в сообщениях).

<!-- more -->

{{ img('Выбор страны', 'countryflags.png') }}

## Особенности

* Страна проживания выбирается в профиле либо при регистрации.

{{ download('https://custom.simplemachines.org/index.php?mod=417') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Country Flag mod
    $txt['country_flag_label'] = 'Пожалуйста, выберите свою страну';
    $txt['country_flag_error_required'] = 'Вы должны выбрать страну, в которой живёте';
    $txt['country_flag_ask'] = 'Показывать список выбора стран';
    $txt['country_flag_disabled'] = 'Не показывать (Выключено)';
    $txt['country_flag_profile'] = 'В профиле';
    $txt['country_flag_registration'] = 'При регистрации';
    $txt['country_flag_both'] = 'В профиле и при регистрации';
    $txt['country_flag_required'] = 'Требовать, чтобы пользователи указывали свое расположение?';
    $txt['country_flag_show'] = 'Показывать флаги стран в сообщениях (под аватарами).';
    $txt['country_flag'] = 'Страна';
    ```
