---
title: Replies before Lock
long_title: Replies before Lock - закрываем тему после набора сообщений
description: Как автоматически закрыть тему при достижении заданного количества ответов в ней.
date: 2010-09-12
authors: [live627]
tags: [ответы, сообщения, темы, SMF 2.0]
categories: [translations]
---

С помощью этого мода легко настроить автоматическое закрытие тем при достижении заданного количества ответов.

<!-- more -->

## Настройки

{{ settings('Настройки тем.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=2685') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Replies before Topic Lock
    $txt['replies_before_lock'] = 'Количество ответов до закрытия темы';
    ```

    Для перевода справки добавить в файл `Help.russian-utf8.php`:

    ```php
    <?php

    // Replies before Topic Lock
    $helptxt['replies_before_lock'] = 'При достижении заданного количества ответов тема будет закрыта.';
    ```
