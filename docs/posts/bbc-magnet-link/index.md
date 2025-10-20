---
title: BBC Magnet Link
long_title: BBC Magnet Link - магнитные ссылки в сообщениях
description: Как добавлять магнитные ссылки для скачивания торрентов на форуме SMF?
date: 2022-06-21
tags: [SMF 2.0, SMF 2.1, bbcode, торрент]
categories: [translations]
---

Модификация предоставляет возможность вставлять в сообщения форума магнитные ссылки на различные торрент-ресурсы.

<!-- more -->

{{ img('Выбираем теги с ограничениями', 'bbc_magnet_link.png') }}

{{ settings('Конфигурация → Настройки модов') }}

## Как пользоваться

* Находим в описании раздачи на торрент-ресурсе иконку магнита, копируем ссылку.
* С помощью форумного тега `[magnet]` вставляем эту ссылку в свое сообщение на форуме.

## Особенности

* Отображение описания раздачи, а также сидов и личеров для каждой вставленной ссылки.
* Дополнительные настройки.

{{ download('https://custom.simplemachines.org/index.php?mod=4327') }}

??? Русификация

    Создать в папке `Themes/default/languages` файл `bbc_magnet_link.russian.php` (или `bbc_magnet_link.russian-utf8.php`, если у вас SMF 2.0.x UTF-8):

    ```php
    <?php

    $txt['magnet_link_seeds'] = 'Сиды:';
    $txt['magnet_link_leeches'] = 'Личи:';
    $txt['magnet_link_downloaded'] = 'Загружено:';
    $txt['magnet_link_error_no_information'] = 'Нет информации о торрентах или нет активных http(s) трекеров';
    $txt['magnet_link_error_bad_magnet_link'] = 'Возможно, проблема с магнитной сылкой';
    $txt['magnet_link_error_lack_trackers'] = 'Трекеров не найдено';
    $txt['magnet_link_error_not_magnet_link'] = 'Это не магнитная ссылка';
    $txt['magnet_link_error_no_input_data'] = 'Магнитная ссылка не предоставлена';
    $txt['magnet_link_error_no_http_trackers'] = 'Магнитная ссылка не включает трекеры http(s)';
    $txt['magnet_link_average'] = 'В среднем из';
    $txt['magnet_link_trackers'] = 'трекеров';
    $txt['magnet_link_trackers_single'] = 'трекер';
    $txt['magnet_link_max_value'] = 'Наибольшее значение';

    $txt['magnet_mod_name'] = 'Магнитная ссылка';
    $txt['magnet_mod_description'] = 'Магнитная ссылка';
    $txt['magnet_basic_settings'] = 'Базовые настройки';
    $txt['magnet_attachments_settings'] = 'Настройки вложений';
    $txt['magnet_only_http'] = 'Включать только http(s) трекеры:';
    $txt['magnet_only_http_sup'] = 'Эта настройка позволит использовать только http(s) трекеры.';
    $txt['magnet_check_all'] = 'Проверять все:';
    $txt['magnet_check_all_sup'] = 'Эта настройка включит опрос всех трекеров, после чего данные будут отображаться в зависимости от выбранного ниже варианта.';
    $txt['magnet_check_all_display_type'] = 'Тип отображения:';
    $txt['magnet_check_all_display_type_sup'] = 'Выберите желаемый тип отображения данных.';
    $txt['magnet_check_all_options'] = [
        'Среднее значение для всего',
        'Среднее значение для сидов и личеров, наивысшее — для загрузки',
        'Наивысшие значения для всего',
    ];
    $txt['magnet_announce'] = 'Поиск по объявлениям:';
    $txt['magnet_announce_sup'] = 'Использовать announce вместо scrape для опроса трекеров.';
    $txt['magnet_max_scrape_time'] = 'Тайм-аут для каждого трекера:';
    $txt['magnet_max_scrape_time_sup'] = 'Этот параметр позволяет установить максимальное количество времени, необходимое для ответа трекера. (По умолчанию 0 - 2 секунды)';
    $txt['magnet_max_trackers_scrape'] = 'Максимум трекеров:';
    $txt['magnet_max_trackers_scrape_sup'] = 'Этот параметр позволит вам установить максимальное количество опрашиваемых трекеров. (По умолчанию 0 - все, если включена функция "Проверять все", это предел правильных запросов)';
    $txt['magnet_enable_support_for_attachments'] = 'Включить поддержку вложений:';
    $txt['magnet_enable_support_for_attachments_sup'] = 'Используйте этот параметр для включения поддержки обработки вложений (Не реализовано).';
    ```
