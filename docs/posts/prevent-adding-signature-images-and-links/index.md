---
title: Prevent Adding Signature Images And Links
long_title: Prevent Adding Signature Images And Links - запрещаем ссылки и изображения в подписях
description: Как запретить вставку ссылок и изображений в подписях на форуме.
date: 2011-12-17
tags: [изображения, подпись, ссылки, SMF 2.0]
categories: [translations]
---

Модификация поможет ограничить новых пользователей в использовании ссылок и изображений в подписях.

<!-- more -->

## Настройки

{{ settings('Конфигурация → Свойства и параметры → Подписи.') }}

## Особенности

- После включения запретов даже если кто-нибудь и вставит ссылку или картинку в свою подпись, после сохранения они будут заменены на соответствующие предупреждения.
- Возможность задать количество сообщений, после достижения которого все запреты будут сняты. Отличная стимуляция для пользователей.

{{ download('https://custom.simplemachines.org/index.php?mod=1242') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Prevent Adding Signature Images And Links
    $txt['signature_allow_links'] = 'Разрешать ссылки в подписях';
    $txt['signature_links_posts'] = 'Количество сообщений, до достижения которого вставка ссылок будет запрещена.';
    $txt['signature_allow_images'] = 'Разрешать изображения в подписях';
    $txt['signature_images_posts'] = 'Количество сообщений, до достижения которого вставка изображений будет запрещена.';
    $txt['signature_links_posts_desc'] = '(0 — блокировать ссылки у всех, кроме администраторов)';
    $txt['signature_images_posts_desc'] = '(0 — блокировать изображения у всех, кроме администраторов)';
    $txt['signature_req_links_removed'] = 'Любые ссылки будут удалены.';
    $txt['signature_req_images_removed'] = 'Любые изображения будут удалены.';
    $txt['signature_req_links'] = 'Для использования ссылок необходимо иметь не менее %1$d сообщений.';
    $txt['signature_req_images'] = 'Для использования изображений необходимо иметь не менее %1$d сообщений.';
    $txt['signature_link_removed'] = '*Ссылка удалена*';
    $txt['signature_image_removed'] = '*Изображение удалено*';
    ```
