---
title: Stop Forum Spam
long_title: Stop Forum Spam - как справиться со спамом?
description: Использование популярного API Stop Forum Spam для защиты от спама на форуме SMF.
date: 2025-03-28
authors: [sleepy]
tags: [SMF 2.0, SMF 2.1, антиспам, регистрация]
categories: [reviews]
related:
  - mods/stop-spammer
  - mods/bad-behavior
---

Обнаружение спама с помощью API Stop Forum Spam.

<!-- more -->

{{ img('', 'stop_forum_spam.png') }}

{{ settings('Настройки модов → Stop Forum Spam.') }}

## Особенности

* Возможность проверки по имейлу, имени пользователя, IP-адресу
* Настройка географического региона (Глобальный, США, Европа)
* Проверка при регистрации, при отправке сообщений и жалоб
* Возможность блокировки пользователей, пользующихся TOR, если они занесены в базу данных
* Лог для просмотра отслеживаемых действий (_Админка ⇒ Обслуживание ⇒ Журналы ⇒ Журнал SFS_)

{{ download('https://custom.simplemachines.org/index.php?mod=4311') }}
{{ translation('https://github.com/jdarwood007/smfmod_sfs/blob/master/language/StopForumSpam.russian.php') }}
