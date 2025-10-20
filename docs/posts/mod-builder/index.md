---
title: Mod Builder — сборщик модов для SMF
description: С помощью какой программы можно создать модификацию для SMF?
date: 2018-06-25
slug: mod-builder
authors: [bugo]
tags: [модификации, сборщик]
categories: [lessons]
---

В продолжение темы [Шаблон для создания модификации](/lessons/shablon-dlja-sozdanija-modifikacii), а также как обзор программы **Mod Builder** — сборщика модификаций для SMF.

<!-- more -->

## Что это?

Программа, разработанная Rick "Yoshi2889" Kerkhof для облегчения создания модов для Simple Machines Forum.

## Где взять?

См. кнопку-ссылку внизу статьи.

## Учебный пример

Создадим модификацию **Funny Converter**, выполняющую замену файлов collapse.gif и expand.gif аналогичными картинками в PNG формате. Запускаем Mod Builder, заходим в _Tools =&gt; Options_, устанавливаем имя пользователя (ник), которое будет использоваться в проектах в качестве имени автора модификаций. Затем на вкладке **Debugging** указываем путь к файлам SMF (нужно указать ту версию, для которой создаем модификацию), и на вкладке **PHP Code Checking** — путь к файлу php.exe (необязательно, но пригодится для тестирования). Затем сохраняем настройки и возвращаемся на главное окошко программы. Выбираем «_Create a new project_».

На вкладке **Mod Details** указываем основные параметры мода: название, версию, тип, линейку версий SMF, для которой разрабатываем модификацию. После этого выбираем в меню _File =&gt; Save Project_, указываем или создаем директорию для файлов мода и переходим к следующему шагу.

{{ img('Mod Builder - детали', 'mod_builder_details.png') }}

На вкладке **Readme** можно создать небольшое описание модификации, указать лицензию и пр. ББ-теги поддерживаются.

{{ img('Mod Builder - readme', 'mod_builder_readme.png') }}

Вкладку **Source Edits** пропускаем, так как там прописываются изменения напрямую в файлах движка, а у нас мод целиком на хуках. Поэтому ставим внизу галочку &laquo;_Skip this step on build_&raquo;. Теперь открываем папку с проектом, находим там папку Source и создаем в ней подпапки `Sources` и `Themes/default/images`. Создаем файл `/Sources/Subs-Funny.php` со следующим содержимым:
```php
<?php

if (! defined('SMF'))
    die('No direct access...');

function funny_buffer($buffer)
{
    $replacements = [];

    $collapse                = 'collapse.gif';
    $new_collapse            = 'collapse.png';
    $replacements[$collapse] = $new_collapse;

    $expand                  = 'expand.gif';
    $new_expand              = 'expand.png';
    $replacements[$expand]   = $new_expand;

    if (isset($_REQUEST['xml']))
        return $buffer;

    return str_replace(array_keys($replacements), array_values($replacements), $buffer);
}
```

Функция funny_buffer, вызываемая хуком integrate_buffer, на лету заменяет все вхождения collapse.gif и expand.gif в коде страницы на collapse.png и expand.gif.

В директорию `Themes/default/images` складываем подходящие вам картинки `collapse.png` и `expand.png`. После этого на вкладке **Files to extract/delete** в правом блоке (_Extracting files to the forum_) в раскрывающемся списке выбираем директорию `Sources` и указываем путь распаковки (Destination) `$boarddir` (корень форума). Затем нажимаем «_Create a new instruction_», чтобы подтвердить наш выбор. Повторяем процесс, выбрав в списке директорию `Themes` и путь распаковки `$boarddir`. См. скриншот для сравнения:

{{ img('Mod Builder - пути и распаковка', 'mod_builder_extract.png') }}

На вкладке **Installation code** в раскрывающихся списках внизу выбираем предустановленный шаблон Hooks и оформляем его, как на скрине ниже. При установке мода будет добавляться хук __funny_buffer__ из файла `Subs-Funny.php`, а при удалении мода — соответственно, будет удаляться и хук.

{{ img('Mod Builder - хуки', 'mod_builder_code.png') }}

## Компиляция и проверка

Другие вкладки пропускаем (на вкладке **Database altering code** можно прописать код добавления необходимых таблиц в базу данных), они нам пока не нужны. Выбираем в меню _Project — Compile_, указываем имя файла архива и получаем готовый для загрузки мод. Тестируем:

{{ img('Mod Builder - установка мода', 'mod_builder_test.png') }}

{{ img('Mod Builder - аж глазу приятно', 'mod_builder_result.png') }}

На этом всё, пользуйтесь на здоровье :)

{{ github('https://github.com/NanoSector/ModManager/releases', 'Mod Builder') }}
{{ download('https://drive.proton.me/urls/35S6ND8V64#qtBErmlfPnT5', 'Файлы проекта') }}
