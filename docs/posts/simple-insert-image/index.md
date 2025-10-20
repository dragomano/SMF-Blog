---
title: Simple Insert Image
long_title: Simple Insert Image - быстрая вставка изображений в сообщения
description: Как упростить вставку изображений в текст сообщений, без указания размеров?
date: 2023-07-17
tags: [изображения, вложения, SMF 2.1]
categories: [translations]
---

Благодаря этой модификации каждое изображение автоматически вставляется в сообщение одним щелчком мыши (без обязательного указания ширины/высоты).

<!-- more -->

{{ img('Как мод выглядит в действии', 'simple_insert_image.png') }}

## Особенности

- Изображения вставляются с использованием максимальных значений ширины/высоты, заданных в «Настройках вложений».
- Возможность вернуть стандартное поведение индивидуально для каждого пользователя, при включении опции «Вставка изображений с указанием ширины/высоты» в разделе «Встраиваемые изображения» в профиле (вкладка «Оформление»).

{{ download('https://custom.simplemachines.org/index.php?mod=4367') }}

??? Русификация

    Создать в папке `Themes/default/languages/SII` файл `SII-Profile.russian.php`:

    ```php
    <?php

    // SMF 2.1 Simple Insert Image Mod.
    global $modSettings;

    $txt['theme_opt_sii'] = 'Встраиваемые изображения';
    $txt['custom_inline_width_height'] = 'Вставка изображений с указанием ширины/высоты';

    $max_image_width = !empty($modSettings['max_image_width']) ? $modSettings['max_image_width'] : '';
    $max_image_height = !empty($modSettings['max_image_height']) ? $modSettings['max_image_height'] : '';
    if ($max_image_width)
        $txt_max_width = $txt_max_wh = 'максимальной шириной ' . $max_image_width . 'px';
    if ($max_image_height)
        $txt_max_height = $txt_max_wh = 'максимальной высотой ' . $max_image_height . 'px';
    if ($max_image_width && $max_image_height)
        $txt_max_wh = $txt_max_width . ' и ' . $txt_max_height;
    if ($max_image_width || $max_image_height)
        $txt['custom_inline_width_height'] .= '<div class="smalltext"><strong>Примечание:</strong> Встраиваемые изображения ограничены ' . $txt_max_wh . '.</div>';
    ```
