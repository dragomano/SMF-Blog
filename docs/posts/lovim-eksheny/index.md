---
title: Ловим экшены
description: Учимся отображать конкретные шаблоны в зависимости от выбранных экшенов.
date: 2023-04-27
slug: lovim-eksheny
authors: [bugo]
tags: [экшены]
categories: [lessons]
---

В этом уроке разбираемся с альтернативным подключением пользовательских шаблонов и подшаблонов (слоёв).

<!-- more -->

Есть в SMF полезная функция, `WrapAction` (Themes.php), которая позволяет без всяких хуков подключать шаблоны, подшаблоны, языковые файлы, нужные функции в конкретных PHP-файлах.

??? "Полный код функции"

    ```php
    <?php

    /**
     * Possibly the simplest and best example of how to use the template system.
     *  - allows the theme to take care of actions.
     *  - happens if $settings['catch_action'] is set and action isn't found
     *   in the action array.
     *  - can use a template, layers, sub_template, filename, and/or function.
     */
    function WrapAction()
    {
        global $context, $settings;

        // Load any necessary template(s)?
        if (isset($settings['catch_action']['template']))
        {
            // Load both the template and language file. (but don't fret if the language file isn't there...)
            loadTemplate($settings['catch_action']['template']);
            loadLanguage($settings['catch_action']['template'], '', false);
        }

        // Any special layers?
        if (isset($settings['catch_action']['layers']))
            $context['template_layers'] = $settings['catch_action']['layers'];

        // Any function to call?
        if (isset($settings['catch_action']['function']))
        {
            $hook = $settings['catch_action']['function'];

            if (!isset($settings['catch_action']['filename']))
                $settings['catch_action']['filename'] = '';

            add_integration_function('integrate_wrap_action', $hook, false, $settings['catch_action']['filename'], false);
            call_integration_hook('integrate_wrap_action');
        }
        // And finally, the main sub template ;).
        if (isset($settings['catch_action']['sub_template']))
            $context['sub_template'] = $settings['catch_action']['sub_template'];
    }
    ```

??? "Дословный перевод комментария к функции"

    Возможно, это самый простой и лучший пример использования системы шаблонов:

    * позволяет теме позаботиться о действиях
    * выполняется, если задан параметр `$settings['catch_action']`, а action не найден в массиве action
    * может использовать шаблон, слои, подшаблон, имя файла и/или функцию

Итак, по порядку, если у нас задана переменная `$settings['catch_action']` (судя по коду, это должен быть массив), то при заходе на заданный экшен можно подгрузить определённые файлы и функции. Например, создадим файл `Themes/default/Example.template.php`:

```php
<?php

function template_test()
{
    echo 'World!';
}
```

Далее, в вашем приложении (можно добавить, например, в конце функции `template_init` файла `index.template.php` темы оформления) определим следующий код:

```php
<?php

global $context, $settings;

// Подключаем шаблон Example.template.php и вызываем функцию template_test внутри него
if (isset($context['current_action']) && $context['current_action'] === 'my_action')
    $settings['catch_action'] = array(
        'template' => 'Example',
        'sub_template' => 'test',
        'layers' => [],
    );
```

Затем перейдем по адресу `http://ваш_форум/?action=my_action` и увидим белую страницу с текстом `World!`.

Чуть изменим код выше:

```php
<?php

global $context, $settings;

// Вызываем функцию test(), подключаем шаблон Example.template.php и вызываем функцию template_test внутри него
if (isset($context['current_action']) && $context['current_action'] === 'my_action')
    $settings['catch_action'] = array(
        'template' => 'Example',
        'function' => 'test',
        'sub_template' => 'test',
        'layers' => [],
    );
```

И далее в коде определим функцию `test`:

```php
<?php

function test()
{
    echo 'Hello ';
}
```

Обновим страницу и увидим текст `Hello World!`. Если функция `test` находится в другом файле, его также можно указать с помощью ключа `'filename' => 'file.php'`. Если нам нужно подключить не функцию, а метод внутри текущего класса, это указывается так:

```php
<?php

global $context, $settings;

// Вызываем функцию test(), подключаем шаблон Example.template.php и вызываем функцию template_test внутри него
if (isset($context['current_action']) && $context['current_action'] === 'my_action')
    $settings['catch_action'] = array(
        'template' => 'Example',
        'function' => __CLASS__ . '::test#', // уберите «решётку», если обращаетесь к статическому методу
        'sub_template' => 'test',
        'layers' => [],
    );
```

Далее добавим в файле `Example.template.php` ещё несколько функций:

```php
<?php

function template_example_layer_above()
{
    echo 'ВЕРХНИЙ СЛОЙ';
}

function template_example_layer_below()
{
    echo 'НИЖНИЙ СЛОЙ';
}
```

Изменим код выше:

```php
<?php

global $context, $settings;

// Вызываем функцию test(), подключаем шаблон Example.template.php и вызываем функцию template_test внутри него
if (isset($context['current_action']) && $context['current_action'] === 'my_action')
    $settings['catch_action'] = array(
        'template' => 'Example',
        'function' => __CLASS__ . '::test#', // уберите «решётку», если обращаетесь к статическому методу
        'sub_template' => 'test',
        'layers' => ['html', 'body', 'example_layer']
    );
```

{{ img('Пример отображения слоёв', 'layers_example.png') }}

Обновим страницу и увидим наш шаблон вместе со слоями. Последовательно уберите `html` и `body` из массива `layers` и посмотрите на результат.

{{ tip('Кстати, визуально увидеть начало и конец каждого слоя в любом шаблоне можно, добавив к текущему адресу параметр `debug`.') }}

Если в коде выше убрать условие `if (isset($context['current_action']) && $context['current_action'] === 'my_action')`, то выбранный нами шаблон будет подключаться при обращении к любому несуществующему экшену.

Также по коду функции `WrapAction` можно заметить, что в конце вызова нашей пользовательской функции `test` будет задействован и хук `integrate_wrap_action`.

{{ note("Больше примеров использования `$settings['catch_action']` можно найти в файлах темы оформления [Spirate](https://github.com/dhayzon/Spirate/blob/main/index.template.php#L89") }}

Итак, подытожим: шаблон — это файл вида `XXX.template.php`, подшаблон — функция вида `template_xxx` внутри файла шаблона, слои — парные функции вида `template_xxx_above` (отображается НАД основным контентом) и `template_xxx_below` (отображается ПОД основным контентом) в том же файле. Подробнее о слоях можно узнать в статье [Изучаем слои](/lessons/izuchaem-sloi).
