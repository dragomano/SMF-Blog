---
title: Unread PM Favicon
long_title: Unread PM Favicon - счетчик непрочитанных личных сообщений в иконке сайта
description: Украшаем иконку сайта счетчиком непрочитанных личных сообщений на форуме.
date: 2012-04-08
authors: [sleepy]
tags: [favicon, лс, SMF 2.0]
categories: [translations]
---

На иконке сайта отображается количество непрочитанных личных сообщений.

<!-- more -->

{{ img('Иконка сайта с количеством непрочитанных личных сообщений', 'unread_pm_favicon.png') }}

## Особенности

* Возможность указать количество секунд — интервал между проверками счетчика ЛС.

{{ download('https://custom.simplemachines.org/index.php?mod=3389') }}

??? Русификация

    Добавить в файл `Themes\default\languages\Modifications.russian-utf8.php`:

    ```php
    <?php

    // Unread PM Favicon
    $txt['unreadPMstimeout'] = 'Счетчик непрочитанных личных сообщений в иконке сайта';
    $txt['unreadPMstimeout_post'] = 'сек. между проверками (слишком низкое значение может привести к падению производительности)';
    ```
