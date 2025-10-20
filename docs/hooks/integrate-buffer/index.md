---
title: Хук integrate_buffer
description: Описание и пример использования хука integrate_buffer в SMF.
date: 2020-03-01
tags: [хуки, буфер, контент]
---

Хук `integrate_buffer` позволяет модифицировать окончательный HTML-буфер страницы прямо перед его отправкой в браузер пользователя. Это «последний шанс» внести изменения в готовую страницу.

## Расположение

=== "SMF 2.x"

    `Subs.php`

    ```php
    <?php

    if (isset($modSettings['integrate_buffer'])) {
        $buffers = array_merge(explode(',', $modSettings['integrate_buffer']), $buffers);
    }
    ```

=== "SMF 3.0"

    `Sources/Utils.php`

    ```php
    <?php

    if (isset(Config::$modSettings['integrate_buffer'])) {
        $buffers = array_merge(explode(',', Config::$modSettings['integrate_buffer']), $buffers);
    }
    ```

SMF собирает весь генерируемый HTML-код (заголовки, меню, контент, боковые панели, футер) в одну переменную — `$buffers`. Только когда вся страница полностью сгенерирована, этот буфер отправляется браузеру.

## Назначение

Хук `integrate_buffer` предоставляет точку для перехвата и изменения этого финального HTML-кода. Это идеально для задач, которые требуют работы со всей страницей целиком, например:

* Добавление/удаление/изменение любых HTML-тегов.
* Поиск и замена текста или кода во всем выводе.
* Сжатие HTML-кода (удаление лишних пробелов, переносов строк).
* Добавление кастомного JavaScript или CSS-кода в конец страницы (лучше используйте [integrate_load_theme](/hooks/integrate-load-theme) и [специальные функции](/lessons/funkcii-dlya-podklyucheniya-stiley-i-skriptov-v-smf)).
* Внедрение сторонних сервисов (виджетов, аналитики, чатов) на все страницы (лучше используйте [integrate_load_theme](/hooks/integrate-load-theme) и [специальные функции](/lessons/funkcii-dlya-podklyucheniya-stiley-i-skriptov-v-smf)).

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
        add_integration_function('integrate_buffer', self::class . '::buffer#', false, __FILE__);
    }

    // Меняем содержимое буфера (функция обязательно должна возвращать строку — с изменениями или без)
    public function buffer(string $buffers): string
    {
        if (isset($_REQUEST['xml'])) {
            return $buffers;
        }

        // Например, тег h1 заменим на тег h2
        return str_replace('<h1>', '<h2>', $buffers);
    }
}
```

Хук `integrate_buffer` — это мощный, но требующий осторожности инструмент для финальной обработки страницы. Он работает с уже готовым HTML, поэтому любые ошибки могут «сломать» отображение всей страницы.
