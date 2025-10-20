---
title: Posting Announcement
long_title: Posting Announcement - объявления при создании сообщений
description: Как добавить предупреждение при создании сообщения?
date: 2010-02-24
tags: [SMF 2.0, объявления, предупреждения, редактор]
categories: [translations]
---

Возможность настроить отображение предупреждения при создании сообщений.

<!-- more -->

{{ img('Пример предупреждения', 'posting_announcement.png') }}

## Особенности

- Возможность использовать BBC и HTML-теги для оформления.

{{ download('https://custom.simplemachines.org/index.php?mod=1484') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Start Posting Announcement mod by Nas
    $txt['enable_announcement'] = 'Показывать объявление в верхней части редактора сообщений <div class="smalltext">Например, напоминание о необходимости прочтения правил форума </div>';
    $txt['text_announcement'] = 'Текст объявления <div class="smalltext">Можно использовать HTML и BBCode.</div>';
    // End Posting Announcement mod by Nas
    ```
