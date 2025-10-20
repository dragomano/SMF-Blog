---
title: Хук integrate_prepare_display_context
description: Описание и пример использования хука integrate_prepare_display_context в SMF.
date: 2020-07-21
tags: [хуки, сообщения, display, context]
---

Хук `integrate_prepare_display_context` позволяет работать с сообщениями в темах форума, изменяя как сами посты, так и контент между ними.

<!-- more -->

## Расположение

=== "SMF 2.x"

    `Sources/Display.php`

    ```php
    <?php

    call_integration_hook('integrate_prepare_display_context', array(&$output, &$message, $counter));
    ```

=== "SMF 3.0"

    `Sources/Actions/Display.php`

    ```php
    <?php

    IntegrationHook::call('integrate_prepare_display_context', [&$output, $message, $counter]);
    ```

## Назначение

Хук принимает в качестве параметров массивы `$output`, `$message` и `$counter`. В них содержатся, соответственно, _отображаемое сообщение_ (конечный результат), _текущее сообщение_ темы (исходный вариант) и _счётчик_ (порядковый номер отображаемого сообщения, начинающийся с нуля на каждой странице темы).

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
        add_integration_function('integrate_prepare_display_context', self::class . '::prepareDisplayContext#', false, __FILE__);
    }

    // Вызывается для каждого сообщения темы, перед отображением на странице
    public function prepareDisplayContext(array &$output, array &$message, int $counter): void
    {
        // Просмотр всех данных текущего сообщения
        var_dump($message);

        // Замена содержания сообщения при отображении (как пример)
        $output['body'] = 'Новый текст сообщения';

        // Отображение текущего порядкового номера сообщения на странице
        var_dump($counter);
    }
}
```

### Пример с цветом группы

А вот так, например, можно добавить полоски с цветом группы автора каждого сообщения:

```php
<?php

public function prepareDisplayContext(array &$output): void
{
    if (! empty($output['member']['group_color'])) {
        echo '
        <style>
            #msg' . $output['id'] . ' .inner,
            #msg' . $output['id'] . ' .custom_fields_above_signature {
                border-top: 1px solid ' . $output['member']['group_color'] . ';
            }
        </style>';
    }
}
```

{{ img("Пример", "group_colors.png") }}

Хук чрезвычайно полезен при работе с сообщениями темы. С помощью него можно выводить дополнительную информацию, изменять содержимое постов или добавлять стили. Например, в моде [Karma Post Rating](/mods/karma-post-rating) благодаря этому хуку отображаются рейтинг каждого сообщения и кнопки для изменения рейтинга.
