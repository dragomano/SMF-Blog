---
title: nCode Image Resizer
long_title: nCode Image Resizer - превью изображений в сообщениях
description: Как сделать просмотр оригинального изображения при клике на его превью в сообщении.
date: 2010-06-05
tags: [SMF 2.0, изображения, миниатюры, превью]
categories: [translations]
---

Отображение уменьшенных копий изображений с рамкой наверху, при клике на которую показывается полный вариант изображения.

<!-- more -->

{{ img('Образец', 'ncode_image_resizer.png') }}

{{ settings('Свойства и параметры.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1197') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // --- Begin added code - nCode Image Resizer ---
    $txt['ncode_imageresizer_warning_small'] = 'Нажмите сюда, чтобы увеличить изображение.';
    $txt['ncode_imageresizer_warning_filesize'] = 'Это уменьшенное изображение. Оригинальный размер: %1$sx%2$sх%3$sKB.';
    $txt['ncode_imageresizer_warning_no_filesize'] = 'Это уменьшенное изображение. Оригинальный размер: %1$sx%2$s.';
    $txt['ncode_imageresizer_warning_fullsize'] = 'Нажмите сюда, чтобы уменьшить изображение.';
    $txt['ncode_imageresizer_mode'] = 'Режим изменения размеров изображений';
    $txt['ncode_imageresizer_original'] = 'Сохранять оригинальный размер';
    $txt['ncode_imageresizer_enlarge_same'] = 'Расширять в том же окне';
    $txt['ncode_imageresizer_open_same'] = 'Открывать в том же окне';
    $txt['ncode_imageresizer_open_new'] = 'Открывать в новом окне';
    $txt['ncode_imageresizer_max_width'] = 'Максимальная ширина';
    $txt['ncode_imageresizer_max_height'] = 'Максимальная высота<br><span class="smalltext">Оставьте пустым для использования любой высоты.</span>';
    // --- End added code ---
    ```
