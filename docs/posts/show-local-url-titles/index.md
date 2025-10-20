---
title: Show Local Url Titles
long_title: Show Local Url Titles - превращаем ссылки в заголовки страниц
description: Как преобразовать внутренние ссылки форума в заголовки страниц.
date: 2010-11-22
tags: [заголовки, ссылки, SMF 2.0]
categories: [translations]
---

Модификация для преобразования всех внутренних ссылок форума в соответствующие названия.

<!-- more -->

{{ note('Вместо ссылки на категорию будет отображено название категории (сама ссылка никуда не исчезнет, к ней лишь добавится атрибут `title`).', 'Пример' )}}

{{ download('https://custom.simplemachines.org/index.php?mod=1293') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Language strings for the Show Local Url Titles mod.
    $txt['ShowLocalUrlTitles_heading'] = 'Настройки мода Show Local Url Titles';
    $txt['ShowLocalUrlTitles_parsebbc'] = 'Отображать заголовки локальных адресов внутри разделов? (не рекомендуется)';
    $txt['ShowLocalUrlTitles_posting'] = 'Отображать заголовки локальных адресов в сообщениях? (рекомендуется)';
    $txt['ShowLocalUrlTitles_autolink'] = 'Автовставка ссылок в сообщениях? (требуется для обработки автоссылок)';
    $txt['ShowLocalUrlTitles_parse_existing'] = 'Кликните здесь для обработки внутренних ссылок во всех существующих сообщениях (обязательно перед этим создайте резервную копию базы данных!)';
    $txt['ShowLocalUrlTitles_parse_existing_confirmation'] = 'Вы действительно хотите это сделать?\n\nПроцесс невозможно будет отменить!';
    ```
