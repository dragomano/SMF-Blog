---
title: Хук integrate_sceditor_options
description: Описание и пример использования хука integrate_sceditor_options в SMF.
date: 2025-11-01
tags: [хуки, sceditor, цвета]
---

Хук `integrate_sceditor_options` позволяет изменять текущие параметры редактора сообщений SMF.

## Расположение

=== "SMF 2.x"

    `Sources/Subs-Editor.php`

    ```php
    <?php

    call_integration_hook('integrate_sceditor_options', [&$sce_options]);
    ```

=== "SMF 3.0"

    `Sources/Editor.php`

    ```php
    <?php

    IntegrationHook::call('integrate_sceditor_options', [&$this->sce_options]);
    ```

## Назначение

Можно изменить любые доступные параметры редактора. Например:

* ширина (`width`)
* высота (`height`)
* текущий стиль (`style`)
* список цветов (`colors`)
* список плагинов (`plugins`)
* локаль (`locale`)
* автофокус (`autofocus`)

Подробности смотрите в исходном коде.

## Использование

[Как подключать хуки](/lessons/kak-podklyuchat-huki)

```php
<?php

if (! defined('SMF'))
    die('No direct access...');

class YourModName
{
    // В этой функции подключаем используемые хуки
    public function hooks(): void
    {
        add_integration_function('integrate_sceditor_options', self::class . '::sceditorOptions#', false, __FILE__);
    }

    // Изменяем параметры редактора
    public function sceditorOptions(array &$sce_options): void
    {
        // Например, добавим дополнительные цвета для текущей палитры
        $sce_options['colors'] .= ',LightCoral,Crimson,DarkRed,HotPink,MediumVioletRed,Coral,Tomato,DarkKhaki';
    }
}
```
