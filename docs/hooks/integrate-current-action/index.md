---
title: Хук integrate_current_action
description: Описание и пример использования хука integrate_current_action в SMF.
date: 2020-06-06
tags: [хуки, меню, подсветка]
---

Хук `integrate_current_action` для подсвечивания нужного пункта в главном меню форума.

## Расположение

=== "SMF 2.x"

    `Subs.php`

    ```php
    <?php

    call_integration_hook('integrate_current_action', [&$current_action]);
    ```

=== "SMF 3.0"

    `Sources/Theme.php`

    ```php
    <?php

    IntegrationHook::call('integrate_current_action', [&$current_action]);

    ```

## Назначение

Этот хук появился в SMF 2.1 и работает совместно с хуком `integrate_menu_buttons`, если для какой-нибудь кнопки указан атрибут **action_hook**.

При переходе на любой из пунктов в главном меню соответствующий пункт подсвечивается как активный. Хук `integrate_current_action` позволяет это регулировать.

## Использование

[Как подключать хуки](/lessons/kak-podklyuchat-huki)

Например, ваша модификация добавляет на форум область _Задачи_ (`action=tasks`), но без кнопки в главном меню. При этом вы хотите, чтобы когда пользователь находился на странице задач, в меню подсвечивался пункт _Начало_. Реализуем это:

```php
<?php

if (! defined('SMF'))
    die('No direct access...');

class YourModName
{
    // В этой функции подключаем используемые хуки
    public function hooks(): void
    {
        add_integration_function('integrate_menu_buttons', self::class . '::menuButtons#', false, __FILE__);
        add_integration_function('integrate_current_action', self::class . '::currentAction#', false, __FILE__);
    }

    // Определяем подключение хука integrate_current_action для пункта «Начало» в меню
    public function menuButtons(array &$buttons): void
    {
        if (! empty($buttons['home'])) {
            $buttons['home']['action_hook'] = true;
        }
    }

    // А здесь получаем подсвечиваемый пункт меню, при заходе на страницу «Задачи»
    public function currentAction(string &$current_action): void
    {
        global $context;

        if ($context['current_action'] == 'tasks') {
            $current_action = 'home';
        }
    }
}
```

Как видите, этот хук пригодится для взаимодействия с главным меню форума.
