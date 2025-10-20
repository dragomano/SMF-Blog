---
title: Alternate Email
long_title: Alternate Email - имейл для уведомлений
description: Добавляем имейл отправителя для уведомлений с форума.
date: 2011-06-20
tags: [SMF 2.0, рассылки, уведомления]
categories: [translations]
---

Установка произвольного имейла в качестве отправного при рассылке писем с форума, в целях защиты от спама.

<!-- more -->

{{ img('Вот как это выглядит', 'alternate_email.png') }}

## Особенности

* Имейл указывается в настройках сервера, рядом с имейлом админа.
* Указанный имейл используется в качестве адреса отправителя, для уведомлений, рассылаемых форумом.

{{ download('https://custom.simplemachines.org/index.php?mod=3062') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Alternate Email
    $txt['mail_from'] = 'Имейл для уведомлений';
    ```
