---
title: Personal Word Censor
long_title: Personal Word Censor - личная цензура в сообщениях
description: Как составить собственный список слов для автозамены в сообщениях на форуме SMF?
date: 2018-08-05
tags: [цензура, профиль, SMF 2.0, SMF 2.1]
categories: [translations]
---

Модификация помогает составлять собственные списки слов для автозамены. Например, если не нравится обилие слов-паразитов в сообщениях пользователя, добавьте эти слова в список и замените на другие, безобидные (например, "ну это самое" => "ква").

<!-- more -->

{{ img('Составляем собственный список нецензурных слов', 'personal_word_censor.png') }}

{{ settings('Профиль → Изменить профиль → Личная цензура.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=4176') }}

??? Русификация

    Добавить в файл `Profile.russian-utf8.php` (для SMF 2.0) или в `Profile.russian.php` (для SMF 2.1):

    ```php
    <?php

    // Personal Word Censor
    $txt['personal_censored_words'] = 'Личная цензура';
    ```
