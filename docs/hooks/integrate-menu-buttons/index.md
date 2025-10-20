---
title: Хук integrate_menu_buttons
description: Описание и пример использования хука integrate_menu_buttons в SMF.
date: 2019-03-23
tags: [хуки, меню, buttons]
---

Хук `integrate_menu_buttons` позволяет изменять главное меню форума: добавлять новые кнопки и подменю, удалять или настраивать текущие.

<!-- more -->

## Расположение

=== "SMF 2.x"

    `Sources/Subs.php`

    ```php
    <?php

    call_integration_hook('integrate_menu_buttons', array(&$buttons));
    ```

=== "SMF 3.0"

    `Sources/Theme.php`

    ```php
    <?php

    IntegrationHook::call('integrate_menu_buttons', [&$buttons]);
    ```

## Назначение

Хук принимает в качестве параметра массив `$buttons`, в котором содержится структура главного меню. Заметьте, что это меню кэшируется, а значит внесённые вами изменения могут отобразиться не сразу.

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
        add_integration_function('integrate_menu_buttons', self::class . '::menuButtons#', false, __FILE__);
    }

    public function menuButtons(array &$buttons): void
    {
        // Прячем пункт «Поиск»
        unset($buttons['search']);
    }
}
```

Никто не мешает использовать этот хук для вызова нужных вам функций, так как он выполняется на каждой странице форума — везде, где отображается главное меню. См. [статью с подробными примерами использования](/lessons/kak-dobavit-knopku).
