---
title: Хук integrate_post_quickbuttons
description: Описание и пример использования хука integrate_post_quickbuttons в SMF.
date: 2021-08-21
tags: [хуки, кнопки, быстрые действия]
---

Хук `integrate_post_quickbuttons` позволяет дополнять/изменять наборы кнопок в быстрых меню. Это кнопки вида «Цитировать», «Редактировать» и т. д. (внутри сообщений).

## Расположение

=== "SMF 2.x"

    `Themes/default/index.template.php`

    ```php
    <?php

    if (!empty($list_class)) {
        call_integration_hook('integrate_' . $list_class . '_quickbuttons', [&$list_items]);
    }
    ```

=== "SMF 3.0"

    `Themes/default/index.template.php`

    ```php
    <?php

    if (!empty($list_class)) {
        IntegrationHook::call('integrate_' . $list_class . '_quickbuttons', [&$list_items]);
    }
    ```

Хук вызывается в случае, если параметр **$list_class** (имя класса) при вызове функции `template_quickbuttons` не пуст.

## Назначение

Этот хук позволяет кастомизировать быстрые кнопки действий в различных частях форума:

* Кнопки внутри каждого сообщения — хук `integrate_post_quickbuttons`
* Кнопки внутри каждого личного сообщения — хук `integrate_pm_quickbuttons`
* Кнопки внутри [созданного самостоятельно набора](/lessons/kak-dobavit-knopku#h-2) — хук `integrate_{ваш_класс}_quickbuttons`

{{ info('Быстрые кнопки позволяют пользователям быстро выполнять действия с сообщениями, личными сообщениями или другими элементами без необходимости перехода на отдельные страницы. Хук дает возможность добавить новые действия или модифицировать существующие.', 'Дополнительная информация (из документации SMF)') }}

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
        add_integration_function('integrate_post_quickbuttons', self::class . '::postQuickButtons#', false, __FILE__);
    }

    // Добавляем внутри каждого поста кнопку-ссылку на произвольный сайт:
    public function postQuickButtons(array &$list_items): void
    {
        $list_items['my_button'] = [
            'label' => 'Перейти на сайт',
            'href'  => 'https://dragomano.ru',
            'icon'  => 'home',
            'show'  => true
        ];
    }
}
```

{{ img("Результат", "integrate_post_quickbuttons.png") }}

{{ tip('С другими подобными хуками работа полностью аналогичная. Примеры кнопок смотрите в исходных файлах движка SMF в функции `template_quickbuttons()`.') }}
