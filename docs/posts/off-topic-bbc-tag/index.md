---
title: Off-Topic BBC Tag
long_title: Off-Topic BBC Tag - кнопка оффтопик для форума
description: Добавляем кнопку оффтопик для выделения текста, не относящегося к теме сообщений.
date: 2010-05-15
tags: [SMF 2.0, bbcode, кнопки, оформление, оффтоп, редактор]
categories: [translations]
related:
  - mods/spoiler
  - mods/quick-spoiler
---

Добавление в редактор сообщений новой кнопки, для оформления текста, не относящегося к обсуждаемой теме.

<!-- more -->

{{ img('Хотите уклониться от темы? Используйте оффтоп', 'off-topic.png') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1458') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Start Off-Topic BBC by Nas
    $txt['off-topic'] = 'Оффтопик:';
    $txt['off-topic_desc'] = 'Оффтоп';
    // End Off-Topic BBC by Nas
    ```
