---
title: Advanced Signature
long_title: Advanced Signature - подписи в случайном порядке
description: Добавляем возможность отображения нескольких подписей у каждого пользователя.
date: 2011-02-12
tags: [SMF 2.0, подпись, пользователи, профиль]
categories: [translations]
---

Возможность создания более одной подписи, с дальнейшим отображением в случайном порядке.

<!-- more -->

{{ settings('Характеристики и настройки → Подписи') }}

## Особенности

* Установка максимального количества подписей.
* Создание подписей в профилях пользователей.
* Три варианта использования:
    * обычная,
    * без подписи,
    * случайная.

{{ github('https://github.com/emanuele45/Advanced-Signature') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Advanced Signature
    global $boardurl;

    $txt['random_signature'] = 'Показывать случайную подпись';
    $txt['signature'] = $txt['signature'] ?? 'Подпись';
    $txt['nosignature'] = 'Без подписи';
    $txt['randomsignature'] = 'Случайная';
    $txt['restoresignatures'] = 'Сбросить количество подписей';
    $txt['choose_signature'] = 'Используемый вариант подписи';
    $txt['normal_signature'] = 'Обычная';
    $txt['signatures_still_missing'] = 'Необработанное количество подписей: [MISSING_SIGNATURES].<br>Процесс остановлен во избежание перегрузки сервера.';
    $txt['signature_continue'] = 'Продолжить';
    $txt['signatures_restored'] = 'Подписи всех пользователей были восстановлены до одного экземпляра';
    $txt['max_numberofSignatures'] = 'Максимальное количество подписей для каждого пользователя<div class="smalltext">(не меньше 1)<br>Пожалуйста, перед удалением мода используйте опцию на <a href="' . $boardurl . '/index.php?action=admin;area=maintain;sa=members">странице обслуживания пользователей</a>, чтобы сбросить количество до 1</div>';
    ```
