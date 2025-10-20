---
title: SMF Cumulus
long_title: SMF Cumulus - облако популярных тем на форуме SMF
description: Добавляем на форум SMF облако с популярными темами или тегами.
date: 2011-02-11
authors: [bugo]
tags: [облако, теги, темы, SMF 2.1]
categories: [mods]
---

Мод добавляет на главную страницу форума блок с популярными темами или тегами.

<!-- more -->

{{ img('Пример облака тегов', 'cumulus_congestus.png') }}

## Особенности

* Мод создан на основе плагина [TagCanvas](https://www.goat1000.com/tagcanvas.php).
* Выбор оформления заголовка блока.
* Установка критерия популярности: по количеству просмотров или по количеству ответов.
* Управление размерами облака.
* Установка цветов ссылок в блоке, управление размером шрифта.
* Установка скорости вращения заголовков тем (или тегов) в облаке.
* Поддержка [Topic Rating Bar](/mods/topic-rating-bar), объявлений [Simple Classifieds](/mods/simple-classifieds) и ключевых слов, созданных с помощью [Optimus](/mods/optimus).

{{ note('Чтобы отобразить облако тегов в PHP-блоке портала, используйте код: `echo Cumulus::show(true);`', 'Для порталов') }}

{{ download('https://custom.simplemachines.org/index.php?mod=2936') }}