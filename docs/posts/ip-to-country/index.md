---
title: IP to Country
long_title: IP to Country - узнаем страну пользователя по его IP
description: Как узнать страну проживания пользователя по его IP адресу.
date: 2012-03-29
tags: [ip, сообщения, страны, SMF 2.0]
categories: [translations]
---

Получение информации о стране пользователя по его IP.

<!-- more -->

## Особенности

- Справа от IP пользователя в сообщениях будет отображаться индекс страны (типа RU, UA и т. д.)
- На странице проверки IP отображается блок с полным названием страны

{{ note('После установки мода рекомендуется зайти в обслуживание и запустить задачу «Создать индекс IP-адресов» (для отображения названий стран в ранее опубликованных сообщениях).') }}

{{ download('https://custom.simplemachines.org/index.php?mod=3312') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // IP to Country
    $txt['iptocountry_title'] = '';
    $txt['iptocountry_na'] = '--';
    $txt['iptocountry_natitle'] = 'Нет в списке';
    $txt['maintain_recount_ip_index'] = 'Создать индекс IP-адресов, связанных с сообщениями';
    $txt['maintain_recount_ip_index_info'] = 'Используйте эту функцию для обновления индекса названий стран в ранее созданных сообщениях.';
    ```
