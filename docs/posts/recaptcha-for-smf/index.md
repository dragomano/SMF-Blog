---
title: reCAPTCHA for SMF
long_title: reCAPTCHA for SMF - система визуальной проверки
description: Как добавить визуальную проверку reCAPTCHA на форуме SMF?
date: 2010-03-14
tags: [recaptcha, антибот, антиспам, регистрация, SMF 2.0]
categories: [translations]
---

Мод заменяет стандартную систему визуальной проверки при регистрации на знаменитую reCAPTCHA.

<!-- more -->

## Настройки

{{ settings('Безопасность и модерирование → Антиспам.') }}

## Особенности

- Для работы с модом требуются публичный и приватный ключи, получить которые можно на сайте [recaptcha.net](https://www.google.com/recaptcha/intro/)
- Несколько стилей капчи.

{{ download('https://custom.simplemachines.org/index.php?mod=1044') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // reCAPTCHA for SMF
    $txt['recaptcha_configure'] = 'Система визуальной проверки reCAPTCHA';
    $txt['recaptcha_configure_desc'] = 'Использование мода reCAPTCHA. Нет своего ключа для reCAPTCHA? <a href="https://www.google.com/recaptcha/admin">Получите его здесь</a>.';
    $txt['recaptcha_enabled'] = 'Включить защиту';
    $txt['recaptcha_enable_desc'] = '(Заменяет стандартную систему визуальной проверки)';
    $txt['recaptcha_theme'] = 'Стиль reCAPTCHA';
    $txt['recaptcha_theme_light'] = 'Светлый';
    $txt['recaptcha_theme_dark'] = 'Тёмный';
    $txt['recaptcha_public_key'] = 'Публичный ключ reCAPTCHA';
    $txt['recaptcha_private_key'] = 'Приватный ключ reCAPTCHA';
    $txt['recaptcha_no_key_question'] = 'Нет ключа?';
    $txt['recaptcha_get_key'] = 'Получите ключ здесь.';
    ```

{{ warning('В SMF 2.1 этот мод не нужен, Recaptcha встроена в движок.') }}
