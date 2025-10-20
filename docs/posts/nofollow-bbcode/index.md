---
title: NoFollow BBCode
long_title: NoFollow BBCode - добавляем nofollow к ссылкам
description: Как добавить атрибут nofollow к ссылкам в сообщениях.
date: 2010-06-06
tags: [SMF 2.0, nofollow, ссылки]
categories: [translations]
---

Добавление специального тега для создания ссылок с атрибутом `nofollow`.

<!-- more -->

{{ img('В редакторе сообщений появляется соответствующая кнопка', 'nofollow_bbcode.png') }}

## Особенности

- Выборочное добавление к создаваемым ссылкам свойства `rel="nofollow"`.
- Для добавления **nofollow** ко всем ссылкам в сообщениях используйте мод [NoFollow All Links](https://custom.simplemachines.org/index.php?mod=1236).

{{ download('https://custom.simplemachines.org/index.php?mod=1237') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    $txt['nofollow'] = 'Гиперссылка с атрибутом rel="nofollow"';
    ```
