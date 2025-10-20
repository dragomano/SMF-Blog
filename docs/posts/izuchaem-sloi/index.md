---
title: Изучаем слои
description: Учимся работать со слоями в шаблонах форума на движке SMF.
date: 2012-01-18
slug: izuchaem-sloi
authors: [bugo]
tags: [шаблоны, слои]
categories: [lessons]
---

Продолжаем осваивать SMF. И сегодня рассмотрим такое понятие как **слои**.

<!-- more -->

Слои (layers) — функции, содержащие некоторую часть шаблона. Чтобы увидеть текущие слои, авторизуйтесь в качестве администратора и добавьте к адресу параметр *debug*. Например: `http://mysite.local/index.php?debug`. Текущие слои выделятся рамочкой. Верхний слой (*html_above*) содержит шапку шаблона. Подвал содержится в слое *html_below*. В слоях *body_above* и *body_below* содержится тело страницы. Загляните в `index.template.php` и поищите функции с окончанием `_above`, `_below` — это и есть стандартные слои шаблона.

Рассмотрим, как добавить блок в верхнюю или нижнюю часть сайта. Файлы движка и база данных останутся без изменений.

## Как это сделать?

Для начала создадим шаблон (`Your.template.php`) и поместим в папку `Themes/default`. Содержание файла:

```php
<?php

function template_layer_name_above()
{
	// тут ваш код
}

function template_layer_name_below()
{
	// и тут ваш код
}
```

{{ tip('`layer_name` в названиях функций можно заменить на что-то свое.') }}

Теперь, если требуется разместить блок в верхней части шаблона, html-контент добавляется в функцию `template_layer_name_above`, а для добавления в нижнюю часть — в функцию `template_layer_name_below`. Никто не запрещает использовать обе функции даже с одинаковым содержимым.

{{ warning('Функции `template_layer_name_above` и `template_layer_name_below` обязательно должны присутствовать в файле шаблона, даже если они пустые! Иначе получим ошибку.') }}

Затем, чтобы подключить наш шаблон к общему потоку SMF, добавим в нужный файл соответствующий вызов:

```php
<?php

// подключение файла Your.template.php
loadTemplate('Your');

// вызов функций template_layer_name_above и template_layer_name_below из подключенного шаблона
$context['template_layers'][] = 'layer_name';
```

После этого созданные слои отобразятся вместе со встроенными слоями текущего шаблона SMF.

{{ warning('Слои это не сетка, вы не можете разместить два слоя в ряд, они всегда идут друг за другом.', 'Предупреждение') }}

{{ img('Результат', 'layers.png') }}

## Взаимодействие с другими слоями

Если мы хотим вставить наш слой после какого-то другого, можно воспользоваться этим кодом:

```php
<?php

$search = 'имя другого слоя';
$replace = 'имя нашего слоя';

if (empty($key = array_search($search, $context['template_layers']))) {
    $context['template_layers'][] = $replace;
    return;
}

$context['template_layers'] = array_merge(
    array_slice($context['template_layers'], 0, $key, true),
    [$replace],
    array_slice($context['template_layers'], $key, null, true)
);
```
