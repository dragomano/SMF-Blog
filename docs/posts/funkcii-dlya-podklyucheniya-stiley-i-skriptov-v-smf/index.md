---
title: Функции для подключения стилей и скриптов в SMF
description: Описание и примеры использования новых функций для подключения CSS и JS файлов в SMF.
date: 2019-03-06
slug: funkcii-dlya-podklyucheniya-stiley-i-skriptov-v-smf
authors: [bugo]
tags: [CSS, JavaScript, стили, скрипты]
categories: [lessons]
---

Познакомимся с несколькими функциями, призванными облегчить подключение внешних и внутренних CSS/JS файлов на вашем форуме.

<!-- more -->

## loadCSSFile

Варианты подключения файла `Themes/default/css/style.css`:

```php
<?php

// 1
loadTemplate(false, 'style');

// 2
$context['html_headers'] .= '<link rel="stylesheet" type="text/css" href="' . $settings['default_theme_url'] . '/css/style.css" />';

// 3
loadCSSFile('style.css');
```

SMF 2.1 поддерживает все три варианта, SMF 2.0 — только первые два.

Функция `loadCSSFile` поддерживает параметры. Самые популярные:

### `external`

Значение по умолчанию: `false`

Установите значение `true`, если хотите загрузить внешний файл стилей:

```php
<?php

loadCSSFile('https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6/css/fontawesome.min.css', ['external' => true]);
```

### `order_pos`

Значение по умолчанию: `3000`

Определяет порядок загрузки файла стилей (до или после базового `index.css`, у которого `order_pos` равен 1):

```php
<?php

loadCSSFile('style.css', ['order_pos' => 5000]);
```

### `attributes`

Значение по умолчанию: `[]`

Возможность указать атрибуты HTML-тега `link` в виде массива:

```php
<?php

loadCSSFile('style.css', ['attributes' => ['id' => 'some_id']]);
```

Об остальных параметрах можно узнать из комментариев к функции в файле `_Load.php_`.

## addInlineCss

Варианты добавления небольшого набора CSS-стилей:

```php
<?php

// 1
$context['html_headers'] .= '
<style type="text/css">
    .my_rule {
        display: none;
    }
</style>';

// 2
addInlineCss('
.my_rule {
    display: none;
}');
```

SMF 2.1 поддерживает оба варианта, SMF 2.0 — только первый.

## loadJavaScriptFile

Варианты подключения файла `Themes/default/scripts/myscript.js`:

```php
<?php

// 1, подключение скрипта в шапке страницы
$context['html_headers'] .= '<script src="' . $settings['default_theme_url'] . '/scripts/myscript.js" type="text/javascript"></script>';

// 2, подключение скрипта в подвале страницы
$context['insert_after_template'] .= '<script src="' . $settings['default_theme_url'] . '/scripts/myscript.js" type="text/javascript"></script>';

// 3, подключение скрипта в шапке страницы
loadJavaScriptFile('myscript.js', ['minimize' => true]);
```

SMF 2.1 поддерживает все три варианта, SMF 2.0 — только первые два.

## addInlineJavaScript

Варианты добавления небольшого набора JS-скриптов:

```php
<?php

// 1
$context['insert_after_template'] .= '
<script type="text/javascript">
    alert("Привет, мир!");
</script>';

// 2
addInlineJavaScript('
alert("Привет, мир!");', true);
```

SMF 2.1 поддерживает оба варианта, SMF 2.0 — только первый. Если при вызове функции _addInlineJavaScript_ не указывать второй параметр или указать false вместо true, скрипт будет добавлен в верхней части страницы (внутри тегов `<head></head>`).

В SMF 2.1 по умолчанию используется HTML5, поэтому указывать тип (атрибут `type`) в тегах `style` и `script` не обязательно:

```php
<?php

$context['html_headers'] .= '
<style>
    .my_rule {
        display: none;
    }
</style>';

$context['insert_after_template'] .= '
<script>
    alert("Привет, мир!");
</script>';
```

## addJavaScriptVar

Эта функция добавляет нужную вам JS-переменную в шапку страницы, внутри тегов `<script></script>`:

```php
<?php

addJavaScriptVar('имя переменной', 'значение переменной', true);
```

Третий параметр — необязательный, если он установлен в true, то значение переменной экранируется с помощью функции _JavaScriptEscape_.
