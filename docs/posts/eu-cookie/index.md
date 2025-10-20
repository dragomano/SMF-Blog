---
title: EU Cookie
long_title: EU Cookie - уведомление об использовании файлов куки
description: Применяем закон о персональных данных к форуму на движке SMF.
date: 2017-08-22
tags: [SMF 2.0, cookie]
categories: [translations]
---

Модификация добавляет плавающее окошко в нижней части страницы, с предупреждением об использовании файлов куки на форуме.

<!-- more -->

{{ img('Пример обработки ссылок', 'eu_cookie.png') }}

{{ settings('Конфигурация → Настройки модов... → EU Cookie') }}

## Особенности

* Предупреждение отображается всем, кроме администраторов.
* Выбор оформления для окошка с уведомлением (чёрный или белый цвет фона).
* Произвольный текст уведомления.
* Вставка ссылки на страницу с описанием политики использования куки.

{{ download('https://custom.simplemachines.org/index.php?mod=3693') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // EU Cookie
    $txt['mods_cat_eucookie'] = 'EU Cookie';
    $txt['enable_eucookie'] = 'Активировать мод';
    $txt['eucookie_color'] = 'Цвет сообщения';
    $txt['eucookie_black'] = 'Чёрный';
    $txt['eucookie_white'] = 'Белый';
    $txt['eucookie_notice'] = 'Текст сообщения';
    $txt['eucookie_text'] = '';
    $txt['eucookie_policy'] = 'Ссылка на политику использования файлов cookie';
    $txt['eucookie_more'] = 'Подробности';
    ```
