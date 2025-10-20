---
title: notCaptcha
long_title: notCaptcha - головоломка вместо капчи
description: Добавляем дополнительную защиту при регистрации - с помощью небольшой головоломки.
date: 2011-02-15
tags: [SMF 2.0, капча, регистрация, антиспам]
categories: [translations]
related:
  - translations/are-you-human
---

Нетрадиционный captcha-мод, требующий человеческого интеллекта для решения небольшой головоломки.

<!-- more -->

{{ img('Вид кнопки меняется в настройках', 'notcaptcha.png') }}

## Особенности

- Пользователю необходимо расположить три картинки по вертикали, поворачивая их с помощью ползунков.
- Возможность использовать свои изображения (файл createOwnPics_INFO.zip на странице загрузки, инструкция прилагается).

{{ download('https://custom.simplemachines.org/index.php?mod=2932') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // notCaptcha
    $txt['notcaptcha_gd_not_enabled'] = '<p style="color:maroon">ОШИБКА: GD-модуль обработки изображений отсутствует!</p>';
    $txt['notcaptcha_jpegpnggif'] = '<p style="color:maroon">ОШИБКА: функция создания изображений (imagepng/imagejpeg/imagegif) отсутствует!</p>';
    $txt['notcaptcha_form1'] = 'Комбинация:';
    $txt['notcaptcha_form2'] = 'Расположите иконки <b>вертикально</b>';
    $txt['notcaptcha_reload'] = 'Обновить картинки';
    $txt['notcaptcha_move_em'] = 'Поворачивайте картинки с помощью ползунков';
    $txt['notcaptcha_nojs'] = '<b>ОШИБКА:</b> для хранения cookie в браузере должен быть включен JavaScript!';
    $txt['notcaptcha_error_notdone'] = '<strong>ОШИБКА</strong>: Пожалуйста, завершите комбинацию.';
    $txt['notcaptcha_error_toomuch'] = '<strong>ОШИБКА</strong>: Вы сделали слишком много попыток составить комбинацию. Вернитесь на предыдущую страницу, <b>перезагрузите картинки</b> и попытайтесь снова.';
    $txt['notcaptcha_error_session'] = '<strong>ОШИБКА</strong>: Некорректная сессия. Пожалуйста, обновите страничку.';
    $txt['notcaptcha_error_fail'] = '<strong>ОШИБКА</strong>: Вы составили неправильную комбинацию.';
    ```
