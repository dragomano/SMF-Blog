---
title: Хук integrate_post_end
description: Описание и пример использования хука integrate_post_end в SMF.
date: 2020-06-07
tags: [хуки, посты]
---

Хук `integrate_post_end` позволяет изменять форму редактирования сообщений, а также загружать свои скрипты на странице редактирования.

<!-- more -->

## Расположение

=== "SMF 2.x"

    `Sources/Post.php`

    ```php
    <?php

    call_integration_hook('integrate_post_end');
    ```

=== "SMF 3.0"

    `Sources/Actions/Post.php`

    ```php
    <?php

    IntegrationHook::call('integrate_post_end');
    ```

Как видим, хук не имеет параметров; в нем доступны для использования любые переменные, определённые до его вызова.

## Назначение

Хук предоставляет возможность вклиниться в код движка непосредственно в конце отрисовки страницы с формой редактирования сообщения на форуме. В частности, с его помощью вы можете получить доступ к массиву `$context['posting_fields']`, содержащему набор полей формы.

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
        add_integration_function('integrate_post_end', self::class . '::postEnd#', false, __FILE__);
    }

    public function postEnd(): void
    {
        global $context, $modSettings;

        $context['posting_fields']['show_something']['label']['text'] = 'Показать кое-что...';
        $context['posting_fields']['show_something']['input'] = [
            'type' => 'checkbox',
            'attributes' => [
                'id'      => 'show_something',
                'checked' => ! empty($modSettings['show_something'])
            ]
        ];

        // Любой другой ваш код
    }
}
```

Подробнее о форме отправки сообщения можно почитать по [ссылке](/lessons/menjaem-formu-otpravki-soobshhenija).

Благодаря этому хуку, например, в моде [Optimus](/mods/optimus) в форму редактирования сообщений добавлены поля «Описание» и «Ключевые слова».
