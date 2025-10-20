---
title: Most Popular Topic Today
long_title: Most Popular Topic Today - вывод самой популярной темы
description: Как добавить блок с самой популярной темой на главной странице форума?
date: 2010-05-21
tags: [SMF 2.0, популярность, темы]
categories: [translations]
---

На главной странице форума отображается ссылка на самую популярную тему (за последние 24 часа).

<!-- more -->

{{ img('Блок с самой популярной темой', 'most_popular_topic_today.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=937') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Most Popular Topic Today
    $txt['most_popular_topic_today'] = 'Наиболее популярная тема';
    $txt['most_pop_top'] = 'Количество ответов в день:';
    $txt['most_pop_top_abs'] = 'Извините, сегодня никто не оставлял сообщений в теме';
    $txt['cant_read_mpt'] = 'Извините, у Вас нет доступа к этой теме';
    ```