---
title: Telegram Notify
long_title: Telegram Notify - отправка уведомлений форума через мессенджер
description: Как настроить отправку почтовых уведомлений с форума SMF в мессенджер Telegram?
date: 2022-04-11
tags: [SMF 2.1, телеграм, уведомления]
categories: [reviews]
related:
  - translations/telegram-bot-auto-post
  - mods/notify-board-reply
  - mods/notify-on-members-actions
  - mods/enotify
---

Надоело искать уведомления форума в почтовом ящике? Настройте их отправку в Телеграм!

<!-- more -->

## Настройки

* Для работы мода нужно [создать бота](https://core.telegram.org/bots#6-botfather) и указать его токен и имя в настройках.
* Затем перейдите в браузере по адресу `https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook?url=https://YOUR_FORUM_URL/index.php?action=tg_bot` (здесь нужно заменить переменные `YOUR_BOT_TOKEN` и `YOUR_FORUM_URL` своими значениями). Вы должны увидеть сообщение: `{"ok":true,"result":true,"description":"Webhook was set"}`.
* После этого можно зайти в _Профиль => Настройки уведомлений_ и настроить связь с Телеграм.

{{ img('Установка связи с Телеграм', 'telegram_notify_profile.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=4320') }}
