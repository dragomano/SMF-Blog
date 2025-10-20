---
title: Redirector
long_title: Redirector - редирект внешних ссылок
description: Как сделать перенаправление внешних ссылок через внутреннюю страницу форума?
date: 2016-09-04
authors: [digger]
tags: [SMF 2.0, SMF 2.1, редирект, ссылки]
categories: [reviews]
---

Избавляемся от внешних ссылок на форуме с помощью редиректа через специальную внутреннюю страницу.

<!-- more -->

{{ img('Страница мода', 'redirector.png') }}

{{ settings('Настройки модов → Перенаправление ссылок.') }}

## Особенности

* Включение перенаправления только для гостей (опционально).
* Белый список доменов (для которых редирект не действует).
* Скрытие ссылок от гостей.

{{ warning('Если в SMF 2.1 у вас крякозябры, удалите файл `Themes/default/languages/Redirector/Redirector.russian.php`, а файл `Themes/default/languages/Redirector/Redirector.russian-utf8.php` переименуйте в `Themes/default/languages/Redirector/Redirector.russian.php`.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=4148') }}
