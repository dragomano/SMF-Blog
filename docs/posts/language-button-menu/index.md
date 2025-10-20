---
title: Language Button Menu
long_title: Language Button Menu - выбор языка форума
description: Как вывести список языков форума, для удобного переключения.
date: 2010-10-02
tags: [языки, SMF 2.0]
categories: [translations]
---

Добавление над полем поиска кнопки для быстрого переключения между языками форума.

<!-- more -->

{{ img('Кнопки для переключения текущего языка форума', 'language_button_menu.png') }}

## Особенности

- Выбор шаблона оформления переключателя языков:
    - список,
    - кнопки,
    - флажки
- Индивидуальные обозначения для выбранных языков
- Ближайший аналог: [Language Drop Down](https://custom.simplemachines.org/index.php?mod=598)

{{ download('https://custom.simplemachines.org/index.php?mod=2705') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Language Button Menu
    $txt['language_menu'] = 'Языковое меню';
    $txt['language_menu_select_language'] = 'Язык: ';
    $txt['language_menu_settings'] = 'Настройки языкового меню';
    $txt['language_menu_activate'] = 'Активировать меню с выбором языков';
    $txt['language_menu_change_tamplate'] = 'Оформление меню:';
    $txt['language_menu_tamplate'] = 'Шаблон:';
    $txt['language_menu_drop_menu'] = 'Раскрывающийся список';
    $txt['language_menu_button_menu'] = 'В виде кнопок';
    $txt['language_menu_icon_menu'] = 'В виде флажков';
    $txt['language_menu_icon_width'] ='Ширина флажков';
    $txt['language_menu_icon_height'] = 'Высота флажков';
    $txt['language_menu_activate_custom_labels'] = 'Разрешить изменение названий';
    $txt['language_menu_choose_label'] = 'Индивидуальные обозначения языков';
    $txt['language_menu_default_label'] = 'Язык: ';
    $txt['language_menu_custom_label'] = 'Обозначение: ';
    $txt['language_menu_template_error'] = '<span class="error">Ошибка: шаблон не найден</span>';
    ```
