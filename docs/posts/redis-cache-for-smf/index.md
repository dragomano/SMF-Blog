---
title: Redis Cache for SMF
long_title: Redis Cache for SMF - подключаем кэширование
description: Используем Redis для хранения кэша в SMF.
date: 2022-04-01
authors: [bugo]
tags: [кэширование, redis]
categories: [mods]
---

SMF, начиная с версии 2.1, содержит удобное API для добавления акселераторов кэширования. Redis в комплекте нет, поэтому попробуем добавить его поддержку.

<!-- more -->

{{ img('Настройки кэширования', 'redis_settings.png') }}

{{ settings('Обслуживание → Настройки сервера → Кэширование.') }}

## Требования

Убедитесь, что Redis установлен на вашем сервере. В `php.ini` должна быть расскоментирована строка:

```ini
extension = redis
```

Если хотите хранить не только кэш, но и PHP-сессии в хранилище Redis, добавьте следующие строки:

```ini
session.save_handler = "redis"
session.save_path    = "tcp://127.0.0.1:6379"
```

Это можно попробовать сделать и через `.htaccess` в корне вашего сайта:

```apacheconf
php_value session.save_handler "redis"
php_value session.save_path "tcp://127.0.0.1:6379"
```

После этого Redis должен появиться в раскрывающемся списке акселераторов в настройках.

{{ download('https://drive.proton.me/urls/MJ342SDSAC#dkd1IZ0MPZnE') }}
{{ github('https://github.com/dragomano/Redis-Cache-for-SMF') }}
