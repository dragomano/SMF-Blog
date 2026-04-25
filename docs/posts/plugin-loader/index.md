---
title: Plugin Loader
long_title: Plugin Loader - удобный загрузчик автономных плагинов для SMF
description: Добавляем загрузчик плагинов для форума SMF
date: 2026-04-25
authors: [bugo]
tags: [SMF 2.1, плагины]
categories: [mods]
---

Добавляем новую секцию в админке - Менеджер плагинов, для установки маленьких и независимых плагинов в один клик.

<!-- more -->

{{ img('Панель управления плагинами', 'plugin_loader.png') }}

{{ settings('Админка → Начало → Менеджер плагинов.') }}

## Кому и когда это может пригодиться?

Представьте, что у вас за годы работы с SMF накопилось множество мелких хаков, которые вы заново переносите при каждом обновлении форума. Для создания полноценной модификации эти хаки кажутся вам слишком маленькими, либо вам лень заморачиваться. А с помощью этой модификации можно будет оформить эти ваши хаки в небольшие автономные плагины, которые вы в любой момент сможете отключать/включать в один клик.

Любой ваш хак, который можно реализовать с помощью хуков SMF, можно оформить в виде автономного плагина для этой модификации.

## Требования

- PHP 8.2 или выше
- PHP-расширения `ext-libxml`, `ext-simplexml` и `ext-zip` для работы с плагинами

## Особенности

Этот концепт-мод вдохновлён системой плагинов [Wedge](/articles/wedge/). Он добавляет поддержку самостоятельных плагинов в SMF.

{{ info('Плагины — это автономные модификации, которым не требуется установка или удаление через Менеджер пакетов. Они не вносят изменения в файлы SMF и работают полностью на хуках.') }}

Точкой входа каждого плагина является **plugin.php** с анонимным классом внутри. Также в директории каждого плагина должен находиться файл **plugin-info.xml**, содержащий ключевые данные плагина:

    * название
    * описание
    * версия плагина
    * имя автора
    * ссылка на сайт автора (не обязательно)
    * имейл автора (не обязательно)
    * используемая лицензия
    * ссылка на сайт плагина

Плагины включаются и выключаются одним нажатием кнопки. Для установки достаточно скачать архив с плагином через панель управления или поместить папку плагина с правильной структурой в директорию **Plugins**.

Список текущих активных плагинов форума хранится в глобальной переменной **$plugins** в файле _Settings.php_. Для отключения проблемного плагина достаточно _удалить его название из переменной $plugins_, либо _переименовать папку плагина_, либо _переименовать файл plugin.php_ плагина.

## Важные ограничения

- Менеджер плагинов читает метаданные каждого плагина из файла **plugin-info.xml**. Если XML-файл пустой или повреждённый, такой плагин пропускается в списке и не будет включён, пока файл не исправят.
- При включении плагина имя его директории добавляется в **$plugins** в _Settings.php_. Если в **plugin-info.xml** указан скрипт в узле `<database>`, он выполняется при включении плагина.
- При выключении плагина имя его директории удаляется из **$plugins** в _Settings.php_. Файлы плагина на диске остаются, поэтому его можно включить снова позже.
- При удалении плагина удаляется его директория из **Plugins**. Удалять можно только выключенные плагины; включённый плагин сначала нужно выключить.

## Пример структуры плагина

```
example_plugin/
  images/
    example.png
    index.php
  languages/
    english.php
    index.php
    russian.php
  sources/
    index.php
    plugin.php
  templates/
    index.php
    Example.template.php
  scripts/
    index.php
    example.js
  styles/
    index.php
    example.css
  index.php
  license.txt
  plugin-info.xml
```

## Пример файла plugin-info.xml

```xml
<?xml version="1.0" standalone="yes" ?>
<plugin id="Author:Example">
  <name>Example</name>
  <description>
    <english>Description...</english>
    <russian>Описание...</russian>
  </description>
  <version>0.1</version>
  <author email="noreply@site.com" url="https://author-site.com">Author</author>
  <license url="https://license-site.com">License name</license>
  <website>https://plugin-site.com</website>
  <settings>
    <setting name="key1" type="text" default="" />
    <setting name="key2" type="large_text" default="" />
    <setting name="key3" type="check" default="1" />
    <setting name="key4" type="int" default="1" />
  </settings>
</plugin>
```

Плагины, требующие для своей работы создание таблиц в базе данных, должны содержать узел `<database>имя_файла.php</database>` в **plugin-info.xml**. В указанном файле можно разместить скрипт создания нужных таблиц при включении плагина, если они ещё не созданы.

## Пример файла plugin.php

```php
<?php

/**
 * @package Example
 * @link https://plugin-site.com
 * @author Author https://author-site.com
 * @copyright 2026 Author
 * @license https://opensource.org/licenses/MIT The MIT License
 */

use Bugo\PluginLoader\Attributes\Hook;
use Bugo\PluginLoader\Plugin;

if (! defined('SMF'))
  die('No direct access...');

return new class extends Plugin
{
  public const NAME = 'example';

  #[Hook('integrate_load_theme')]
  public function loadTheme(): void
  {
    // Ваш код

    // Используем языковые строчки
    // $this->loadLanguage();
    // var_dump($this->txt['key'])

    // Используем шаблон
    // $this->loadTemplate('Example'); // будет загружен /templates/Example.template.php

    // Используем другой source-файл того же плагина
    // $this->loadSource('other); // будет загружен /sources/other.php

    // Используем CSS-файл
    // $this->loadCSS('test'); // будет загружен /styles/test.css

    // Используем JS-файл
    // $this->loadJS('test'); // будет загружен /scripts/test.js

    // Используем настройки плагина
    // var_dump($this->getSettings());
  }

  #[Hook('integrate_menu_buttons')]
  public function menuButtons($buttons): void
  {
    // var_dump($buttons);
  }
};

```

Как видите, все требуемые плагином хуки определяются с помощью атрибута `Hook`.

## Пример языкового файла плагина

```php
<?php

return [
  'key1' => 'Текст 1',
  'key2' => 'Текст 2',
];

```

## Вспомогательные методы

Для работы внутри классов плагинов предусмотрены следующие методы:

- `loadLanguage($lang_name = '')` - подключение языкового PHP-файла `$lang_name` из поддиректории `languages` текущего плагина (по умолчанию `$lang_name = $context['user']['language']`)
- `loadTemplate($template_name)` - подключение PHP-файла шаблона `$template_name` из поддиректории `templates` текущего плагина
- `loadCSS($css_name)` - подключение CSS-файла `$css_name` из поддиректории `styles` текущего плагина
- `loadJS($js_name)` - подключение JS-файла `$js_name` из поддиректории `scripts` текущего плагина
- `loadSource($source_name)` - подключение PHP-файла `$source_name` из поддиректории `sources` текущего плагина
- `getUrl($sub_directory = '')` - возвращает URL-путь к директории текущего плагина, включая `$sub_directory` (если указана)

## Примеры рабочих плагинов

- [Profile Starsigns](https://drive.proton.me/urls/8ZX5G1QXSR#WG0Yl99C0NJw)
- [Font Awesome](https://drive.proton.me/urls/ABF7BBDC80#Eo0cVWRbrbxi)
- [Yandex Metrica](https://drive.proton.me/urls/16ZEE2PCKW#UI0yxQoG7BKP)

{{ download('https://github.com/dragomano/Plugin-Loader/releases/download/v0.8/plugin_loader_0.8.zip') }}
{{ github('https://github.com/dragomano/Plugin-Loader') }}
