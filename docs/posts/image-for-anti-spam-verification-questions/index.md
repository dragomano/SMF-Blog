---
title: Image for Anti-Spam Verification Questions
long_title: Image for Anti-Spam Verification Questions - проверочное изображение при регистрации
description: Как добавить проверочное изображение для контрольных вопросов при регистрации на форуме SMF?
date: 2021-01-09
tags: [антиспам, вопросы, SMF 2.0, SMF 2.1]
categories: [translations]
---

Использование своего изображения вместе с контрольными вопросами для защиты от спама при регистрации.

<!-- more -->

{{ img('Пример проверочного изображения при регистрации', 'image_for_antispam_preview.png') }}

{{ settings('Админка → Конфигурация → Безопасность и модерация → Антиспам.') }}

{{ img('Настраиваем изображение и контрольные вопросы', 'image_for_antispam_settings.png') }}

{{ tip('Рекомендуется сохранить используемое изображение в папке `images` темы оформления.', 'Рекомендация') }}

## Особенности

- Изображение будет отображаться только при положительном количестве проверочных вопросов
- При указании неверного пути к изображению пользователи увидят ссылку для связи с администрацией форума
- При нажатии на миниатюру изображения отобразится полноразмерная версия (если картинка больше 300×300 px)

{{ download('https://custom.simplemachines.org/index.php?mod=4278') }}

??? Русификация

    Добавить в файл `ManageSettings.russian-utf8.php`:

    ```php
    <?php

    $txt['setting_qa_verification_image_url'] = 'URL-адрес проверочного изображения:';
    $txt['setting_qa_verification_image_url_desc'] = '<strong>Примечание:</strong> Если адрес не задан <strong>или</strong> <em>\'Количество проверочных вопросов\'</em> равно <em>\'0\'</em>, проверочное изображение <strong>не</strong> будет отображаться.';
    $txt['setting_qa_verification_image_invalid'] = '<strong class="alert largetext">ОШИБКА<br />URL для изображения недействителен!</strong>';
    ```

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    global $webmaster_email;

    $txt['verification_image_help'] = '<a href="mailto:' . $webmaster_email . '"><strong class="alert" style="font-size: 120%;">Помогите - я не вижу проверочного изображения!</strong></a>';
    ```
