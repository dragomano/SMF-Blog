---
title: Хук integrate_load_session
description: Описание и пример использования хука integrate_load_session в SMF.
date: 2020-02-07
tags: [хуки, сессии, session, настройки]
---

Хук `integrate_load_session` позволяет переопределить некоторые настройки PHP, устанавливаемые в SMF, связанные с сессиями.

<!-- more -->

## Расположение

=== "SMF 2.x"

    `Sources/Load.php`

    ```php
    <?php

    call_integration_hook('integrate_load_session');
    ```

=== "SMF 3.0"

    `Sources/Security.php`

    ```php
    <?php

    IntegrationHook::call('integrate_load_session');
    ```

Хук расположен в функции `loadSession`, сразу после определения следующих PHP параметров:

```php
<?php

ini_set('session.use_cookies', true);
ini_set('session.use_only_cookies', false);
ini_set('url_rewriter.tags', '');
ini_set('session.use_trans_sid', false);
ini_set('arg_separator.output', '&');
```

## Назначение

Хук вызывается без параметров, но позволяет изменять настройки сессий через `ini_set`. Полезен для настройки безопасности сессий, например, для установки `session.use_only_cookies` в true для предотвращения сессионных атак.

## Использование

[Как подключать хуки](/lessons/kak-podklyuchat-huki)

```php
<?php

if (! defined('SMF'))
    die('No direct access...');

class YourModName
{
    // Подключаем используемые хуки
    public function hooks(): void
    {
        add_integration_function('integrate_load_session', self::class . '::loadSession#', false, __FILE__);
    }

    // Переопределяем нужную опцию
    public function loadSession(): void
    {
        // Устанавливаем использование только cookie для сессий
        ini_set('session.use_only_cookies', true);

        // Можно добавить другие настройки
        ini_set('session.cookie_secure', true); // Только HTTPS
        ini_set('session.cookie_httponly', true); // Защита от XSS
    }
}
```

Таким образом, если вам нужно изменить или добавить определённые PHP опции для сессий, попробуйте воспользоваться этим хуком.
