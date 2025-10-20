---
title: Кнопки в редакторе сообщений
description: Добавляем новую кнопку в редактор сообщений SMF. Учебный пример.
date: 2011-09-19
slug: knopki-v-redaktore-soobshhenij
authors: [bugo]
tags: [редактор, кнопки, бб-коды]
categories: [lessons]
---

Этот материал научит вас создавать новые кнопки в редакторе сообщений SMF.

Также вы узнаете, как использовать хуки **integrate_bbc_codes** и **integrate_bbc_buttons**.

<!-- more -->

Возьмем в качестве примера интеграции веб-плеер [Plyr](https://plyr.io).

{{ img('Пример роликов Youtube и Vimeo вместе', 'example.png') }}

Итак, создадим пару тегов — **plyr-youtube** и **plyr-vimeo**. И сделаем в редакторе сообщений кнопки для вставки этих тегов.

## Подключение хуков

Используемые функции опишем в файле **Class-Plyr.php** и реализуем подключение при установке мода.

Можете использовать [Simple Mod Maker](/mods/simple-mod-maker) для генерации шаблона мода, либо творить вручную:

```xml
<?xml version="1.0"?>
<!DOCTYPE package-info SYSTEM "http://www.simplemachines.org/xml/package-info">
<package-info xmlns="http://www.simplemachines.org/xml/package-info" xmlns:smf="http://www.simplemachines.org/">
    <id>Bugo:Plyr</id>
    <name>Plyr</name>
    <version>0.1</version>
    <type>modification</type>

    <install for="2.1.*">
        <hook hook="integrate_pre_load" function="Bugo\Plyr::hooks#" file="$sourcedir/Class-Plyr.php"/>
        <require-file name="Sources/Class-Plyr.php" destination="$sourcedir">Adding main source file</require-file>
        <require-dir name="Themes/default" destination="$themes_dir">Adding languages and images</require-file>
    </install>

    <uninstall for="2.1.*">
        <hook hook="integrate_pre_load" function="Bugo\Plyr::hooks#" file="$sourcedir/Class-Plyr.php" reverse="true"/>
        <remove-file name="$sourcedir/Class-Plyr.php">Removing main source file</remove-file>
        <remove-file name="$imagesdir/bbc/plyr-yotube.png" />
        <remove-file name="$imagesdir/bbc/plyr-vimeo.png" />
        <remove-file name="$languagedir/Plyr.english.php" />
        <remove-file name="$languagedir/Plyr.russian.php" />
    </uninstall>
</package-info>
```

Сформируем метод `hooks` в нашем классе:

```php
<?php

public function hooks(): void
{
    add_integration_function('integrate_load_theme', self::class . '::loadTheme#', false, __FILE__);
    add_integration_function('integrate_bbc_codes', self::class . '::bbcCodes#', false, __FILE__);
    add_integration_function('integrate_bbc_buttons', self::class . '::bbcButtons#', false, __FILE__);
}
```

## Подключение скрипта

Создадим метод loadTheme, для загрузки скрипта плеера:

```php
<?php

public function loadTheme(): void
{
    // Подключаем внешний JS-файл
    loadJavaScriptFile('https://cdn.plyr.io/3.8.3/plyr.js', ['external' => true]);

    // Подключаем внешнюю таблицу стилей
    loadCSSFile('https://cdn.plyr.io/3.8.3/plyr.css', ['external' => true]);

    // Добавляем небольшой скрипт
    addInlineJavaScript('const players = Array.from(document.querySelectorAll(".plyr")).map((p) => new Plyr(p));', true);
}
```

## Обработка тегов

Содержимое элемента **content** берем со [страницы плеера на GitHub](https://github.com/sampotts/plyr). Только вместо ссылки на файл используем переменную **$1** (то, что между тегами).

Вставляем это в метод **bbcCodes**, дописываем некоторые мелочи и получаем:

```php
<?php

public function bbcCodes(array &$codes): void
{
    $codes[] = [
        'tag' => 'plyr-youtube',
        'type' => 'unparsed_content',
        'content' => '<div class="plyr" data-plyr-provider="youtube" data-plyr-embed-id="$1"></div>',
        'disabled_content' => '<a href="https://www.youtube.com/watch?v=$1" target="_blank" rel="noopener noreferrer">https://www.youtube.com/watch?v=$1</a>',
        'block_level' => true,
    ];

    $codes[] = [
        'tag' => 'plyr-vimeo',
        'type' => 'unparsed_content',
        'content' => '<div class="plyr" data-plyr-provider="vimeo" data-plyr-embed-id="$1"></div>',
        'disabled_content' => '<a href="https://vimeo.com/$1" target="_blank" rel="noopener noreferrer">https://vimeo.com/$1</a>',
        'block_level' => true,
    ];
}
```

Теперь теги audio и video обрабатываются. Но для удобства пользователей не хватает вставки этих тегов через редактор сообщений.

## Кнопки в редакторе сообщений

С помощью хука **integrate_bbc_buttons** подключаем функцию *bbcCodes*, в которой добавляем новые элементы в массив кнопок ($buttons):

```php
<?php

public function bbcButtons(array &$buttons): void
{
    global $txt;

    // Языковой файл
    loadLanguage('Plyr');

    $buttons[] = [
        'image' => 'plyr-youtube',
        'code' => 'plyr-youtube',
        'before' => '[plyr-youtube]',
        'after' => '[/plyr-youtube]',
        'description' => $txt['plyr_youtube'],
    ];

    $buttons[] = [
        'image' => 'plyr-vimeo',
        'code' => 'plyr-vimeo',
        'before' => '[plyr-vimeo]',
        'after' => '[/plyr-vimeo]',
        'description' => $txt['plyr_vimeo'],
    ];
}
```

В этом массиве каждая кнопка хранится в виде следующих элементов:

* **image** — название gif-изображения (без расширения) кнопки, которое хранится в директории bbc (внутри папки images)
* **code** — тег, для вставки которого предназначена эта кнопка
* **before** — открывающий тег, вставляемый в сообщение при нажатии на кнопку
* **after** — закрывающий тег, вставляемый в сообщение при нажатии на кнопку
* **description** — всплывающая подсказка, появляющаяся при наведении указателя мышки

Теперь вам нужно найти картинки для кнопочек, сохранить их под названием `audio.png` и `video.png` в директории `Themes/default/images/bbc`.

Также создайте языковой файл `Themes/default/languages/Plyr.russian.php` со следующим содержимым:

```php
<?php

$txt['plyr_youtube'] = 'Ссылка на ролик Youtube';
$txt['plyr_vimeo'] = 'Ссылка на ролик Vimeo';
```

В настройках плеера (на официальном сайте), в разделе «Служебные», не забудьте включить опцию «Заменять стандартные теги на странице».

Осталось упаковать это всё в архив и установить через _Менеджер пакетов_.

Не понравился этот плеер? Можете попробовать прикрутить другие, их много. Например:

* [PlayerJS](https://playerjs.com)
* [Video.js](https://videojs.com)
* [MediaElement.js](https://www.mediaelementjs.com)
