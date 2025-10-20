---
title: Are You Human
long_title: Are You Human - дополнительный вопрос при регистрации
description: Дополнительная проверка пользователей во время регистрации на форуме.
date: 2024-07-02
tags: [SMF 2.0, SMF 2.1, антиспам, регистрация]
categories: [translations]
related:
  - mods/notcaptcha
---

Модификация добавляет случайный вопрос при регистрации, для проверки пользователя.

<!-- more -->

{{ img('Пример работы мода', 'are_you_human.png') }}

## Особенности

- Настройки отсутствуют.
- Один случайный вопрос из трёх.

{{ download('https://custom.simplemachines.org/index.php?mod=999') }}

??? Русификация

    Добавить в файл `Themes/default/languages/AreYouHuman.russian.php`:

    ```php
    <?php

    $txt['areyou_human'] = 'Вы человек?';
    $txt['areyou_bot'] = 'Вы бот?';
    $txt['areyou_spammer'] = 'Вы спамер?';
    $txt['areyou_yes'] = 'Да';
    $txt['areyou_no'] = 'Нет';
    $txt['areyou_maybe'] = 'Может быть';
    $txt['areyou_description'] = 'Докажите, что вы человек, ответив на следующий вопрос.';
    $txt['areyou_nothuman'] = 'Чтобы зарегистрироваться на этом форуме, вы должны быть человеком.';
    ```
