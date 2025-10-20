---
title: Popular Topics
long_title: Popular Topics - шкала популярности тем форума
description: Как добавить шкалу популярности для тем на форуме SMF?
date: 2015-09-22
authors: [diego]
tags: [SMF 2.0, темы]
categories: [translations]
---

В зависимости от количества просмотров или ответов высчитывается соответствующий процент популярности темы.

<!-- more -->

{{ img('Мод в действии', 'popular_topics.png') }}

## Особенности

- Включается/отключается мод на вкладке *Настройки тем* в админке форума.
- Там же устанавливается процент популярности темы по количествам просмотров и по ответам.

{{ download('https://custom.simplemachines.org/index.php?mod=4066') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Popular Topics
    $txt['PopularTopics_enable'] = 'Включить мод Popular Topics';
    $txt['PopularTopics_enable_desc'] = 'Включает/отключает работу мода популярных тем.';
    $txt['percent'] = '%';
    $txt['PopularTopics_views_percent'] = 'Популярность по просмотрам';
    $txt['PopularTopics_views_percent_desc'] = 'По умолчанию 70%';
    $txt['PopularTopics_replies_percent'] = 'Популярность по ответам';
    $txt['PopularTopics_replies_percent_desc'] = 'По умолчанию 30%';
    ```
