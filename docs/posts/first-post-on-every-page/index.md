---
title: First Post on Every Page
long_title: First Post on Every Page - первое сообщение на каждой странице
description: Как вывести первое сообщение темы на каждой её странице?
date: 2010-03-16
authors: [live627]
tags: [SMF 2.0, сообщения, темы]
categories: [translations]
---

Отображение первого сообщения в каждой теме в качестве самого верхнего на всех страницах данной темы.

<!-- more -->

{{ img('Настройки мода', 'first_post.png') }}

{{ settings('Форум → Настройка сообщений.') }}

## Особенности

* Возможность активирования мода только в прикрепленных темах.

{{ download('https://custom.simplemachines.org/index.php?mod=1472') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // First Post on Every Page
    $txt['enableFirstPostOnEveryPage'] = 'Включить отображение самого первого сообщения на каждой странице';
    $txt['enableFirstPostOnlySticky'] = 'Активировать эту функцию (см. выше) только для прикреплённых тем';
    ```
