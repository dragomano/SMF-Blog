---
title: Telegram Bot Auto Post
long_title: Telegram Bot Auto Post - автопостинг в чат Телеграма
description: Как сделать оповещения в чат Телеграма о новых пользователях, сообщениях и темах на форуме SMF?
date: 2020-04-11
tags: [телеграм, бот, SMF 2.1]
categories: [translations]
related:
  - reviews/telegram-notify
  - mods/notify-board-reply
  - mods/notify-on-members-actions
  - mods/enotify
---

Полнофункциональный мод для автопостинга уведомлений в чат Телеграма. Уведомлять можно о новых регистрациях на форуме, о сообщениях и темах в определенных разделах.

<!-- more -->

{{ img('Настройки автопостинга', 'telegram_bot_autopost.png') }}

{{ settings('Настройки автопостинга в Телеграм → Настройки автопостинга в Телеграм → Настройки автопостинга в Телеграм.') }}

## Особенности

* Настройка уведомлений о новых регистрациях.
* Настройка уведомлений о новых сообщениях.
* Настройка уведомлений о новых темах в указанных разделах.

{{ download('https://custom.simplemachines.org/index.php?mod=4254') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian.php`:

    ```php
    <?php

    // Telegram Bot Auto Post
    $txt['telegram_admin'] = 'Настройки автопостинга в Телеграм';
    ```

    Также нужно создать файл `telegram.russian.php` со следующим содержимым:

    ```php
    <?php

    $txt['telegram_txt_settings'] = $txt['settings'];
    $txt['telegram_txt_settings_desc'] = 'Здесь можно настроить отправку уведомлений о новых сообщениях, темах и пользователях на форуме в чат Телеграма.';
    $txt['telegram_txt_savesettings'] = $txt['save'];
    $txt['telegram_admin'] = 'Настройки автопостинга в чат Телеграма';
    $txt['telegram_enable_bot_auth_token'] = 'Токен бота &nbsp;';
    $txt['telegram_enable_bot_auth_token_desc'] = 'Как узнать токен бота? <a href="https://clck.ru/Mvabu" target="_blank">Спросить у Яши</a>.';
    $txt['telegram_enable_chat_id'] = 'Идентификатор чата &nbsp;';
    $txt['telegram_enable_chat_id_desc'] = 'Как получить идентификатор чата? <a href="https://clck.ru/Mvaa2" target="_blank">Спросить у Яши</a>.';
    $txt['telegram_guest'] = 'Гость';
    $txt['telegram_enable_push_registration'] = 'Включить уведомления о новых регистрациях &nbsp;';
    $txt['telegram_enable_push_topic'] = 'Включить уведомления о новых темах &nbsp;';
    $txt['telegram_enable_push_post'] = 'Включить уведомления о новых сообщениях &nbsp;';
    $txt['telegram_boardstopush'] = 'Разделы, об обновлении которых нужно уведомлять &nbsp;';
    $txt['telegram_boardstopush_desc'] = 'Зажмите Shift или Ctrl для выбора нескольких разделов сразу';
    $txt['telegram_dateformat'] = 'Формат даты &nbsp;';
    $txt['telegram_dateformat_desc'] = 'Вы можете изменить формат даты на любой из перечисленных в <a href="https://php.net/manual/ru/function.date.php" target="_blank" rel="noopener">документации</a>.';
    $txt['telegram_msg_reg'] = 'Уведомление о новой регистрации &nbsp;';
    $txt['telegram_msg_topic'] = 'Уведомление о новой теме &nbsp;';
    $txt['telegram_msg_post'] = 'Уведомление о новом сообщении &nbsp;';
    $txt['telegram_botname_reg'] = 'Имя бота в уведомлениях о новых регистрациях &nbsp;';
    $txt['telegram_botname_topic'] = 'Имя бота в уведомлениях о новых темах &nbsp;';
    $txt['telegram_botname_post'] = 'Имя бота в уведомлениях о новых сообщениях &nbsp;';
    ```
