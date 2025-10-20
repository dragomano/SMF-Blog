---
title: Default signature
long_title: Default signature - подпись по умолчанию
description: Как настроить и отобразить подпись по умолчанию на форуме SMF?
date: 2010-10-05
authors: [live627]
tags: [SMF 2.0, подпись, пользователи]
categories: [translations]
---

Установка стандартной подписи для тех пользователей, у которых её нет.

<!-- more -->

{{ img('Указываем текст подписи по умолчанию', 'default_signature.png') }}

## Особенности

* Мотивация пользователей к созданию и использованию собственных подписей.
* Возможность зарабатывать на продаже ссылок в подписях.

{{ download('https://custom.simplemachines.org/index.php?mod=2516') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Default signatures
    $txt['def_sig_user_code'] = 'Подпись по умолчанию — для тех, у кого её нет (можно использовать ББ-теги)';
    ```
