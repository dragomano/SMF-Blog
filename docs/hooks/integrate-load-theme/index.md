---
title: 'Хук integrate_load_theme'
date: 2019-03-07
description: 'Описание и пример использования хука integrate_load_theme в SMF.'
tags: [хуки, шаблоны, CSS, JS]
---

Хук `integrate_load_theme` один из часто используемых хуков, вызываемый в конце подключения темы оформления SMF.

## Расположение

=== "SMF 2.x"

    `Load.php`

    ```php
    <?php

    call_integration_hook('integrate_load_theme');
    ```

=== "SMF 3.0"

    `Sources/Theme`

    ```php
    <?php

    IntegrationHook::call('integrate_load_theme');
    ```

Как видим, хук не имеет параметров; в нем доступны для использования любые переменные, определенные до его вызова.

## Назначение

Этот хук вызывается после полной загрузки темы оформления, но до вывода контента страницы. Он идеально подходит для:

* Подключения дополнительных CSS и JavaScript файлов
* Загрузки языковых файлов модификаций
* Инициализации глобальных переменных
* Выполнения действий, требующих доступа к теме и настройкам форума

{{ info('Хук `integrate_load_theme` гарантирует, что все переменные темы (`$settings`, `$context`) и настройки форума уже загружены и доступны. Это отличает его от хука `integrate_pre_load_theme`, который вызывается до загрузки темы.', 'Дополнительная информация (из документации SMF)') }}

{{ warning('Избегайте использования этого хука для тяжелых операций, так как он выполняется на каждой странице форума и может повлиять на производительность.', 'Важно') }}

## Использование

[Как подключать хуки](/lessons/kak-podklyuchat-huki)

```php
<?php

if (! defined('SMF'))
    die('No direct access...');

class YourModName
{
    // В этой функции подключаем хуки
    public function hooks(): void
    {
        add_integration_function('integrate_load_theme', self::class . '::loadTheme#', false, __FILE__);
    }

    public function loadTheme(): void
    {
        global $context, $settings;

        // Подключение языкового файла /Themes/default/languages/MyApplication.{язык пользователя}.php
        loadLanguage('MyApplication');

        // Подключение языкового файла /Themes/default/languages/MyApplication/.{язык пользователя}.php
        loadLanguage('MyApplication/');

        // Подключение произвольного CSS-файла в шапке страницы
        $context['html_headers'] .= '
        <link rel="stylesheet" type="text/css" href="' . $settings['default_theme_url'] . '/css/style.css" />';

        // Подключение произвольного JS-файла в подвале страницы
        $context['insert_after_template'] .= '
        <script src="//code.jquery.com/jquery.min.js" type="text/javascript"></script>';

        // Вызов произвольной функции
        other_function();

        // И другие нужные вам действия
    }
}
```

{{ tip('В SMF 2.1 для подключения CSS и JS файлов добавлены [специальные функции](/lessons/funkcii-dlja-podkljuchenija-stiley-i-skriptov-v-smf).', 'Рекомендация') }}

Если в вашем приложении требуется что-то сделать перед подключением темы оформления, используйте вспомогательный хук [integrate_pre_load_theme](/hooks/integrate-pre-load-theme).
