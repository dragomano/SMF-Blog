---
title: Show Event Dates
long_title: Show Event Dates - отображение дат событий
description: Как вывести даты событий на главной странице форума.
date: 2012-02-23
tags: [дата, календарь, события, SMF 2.0]
categories: [translations]
---

С помощью мода можно добавить отображение дат событий на вашем форуме.

<!-- more -->

{{ img('Выводим даты событий', 'show_event_dates_one.png') }}

## Особенности

* Даты событий будут отображаться на главной странице и внутри разделов, рядом с заголовками тем.
* Формат дат меняется в общих настройках модификаций.
* Для работы мода должен быть включен *Календарь*.

{{ download('https://custom.simplemachines.org/index.php?mod=3331') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Show event dates
    $txt['show_event_dates_format'] = 'Формат даты события';
    $txt['show_event_dates_formatting_help'] = 'справка по форматированию';
    $txt['show_event_dates_format_upcoming'] = $txt['show_event_dates_format'] . ' (в списке событий, на главной странице)';
    $txt['show_event_dates_format_board'] = $txt['show_event_dates_format'] . ' (после заголовков тем, в разделах)';
    ```
