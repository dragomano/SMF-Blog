---
title: Custom Action Mod
long_title: Custom Action Mod - создаем свои странички на форуме
description: Как добавить отдельные страницы с произвольным содержимым на форум SMF.
date: 2010-12-11
tags: [SMF 2.0, bbcode, HTML, PHP, страницы]
categories: [translations]
---

Модификация для создания дополнительных страниц, вписывающихся в дизайн вашего форума.

<!-- more -->

{{ img('Создаем HTML-страничку', 'custom_action_edit_page.png') }}

{{ settings('Конфигурация → Характеристики и настройки → Дополнительные страницы.') }}

## Особенности

* Выбор из трех типов страниц: HTML, BBC, PHP (какой тип выбрали, такой код и вводим).
* Вывод ссылки в меню, которая будет вести на созданную страничку.
* Права доступа для просмотра созданных страниц тоже предусмотрены.

{{ download('https://custom.simplemachines.org/index.php?mod=331') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Custom Action Mod
    $txt['custom_action_shorttitle'] = 'Дополнительные страницы';
    $txt['core_settings_item_ca'] = 'Дополнительные страницы';
    $txt['core_settings_item_ca_desc'] = 'Здесь можно создавать страницы, легко вписывающиеся в дизайн форума.';
    $txt['custom_action_desc'] = 'В этом разделе можно создавать и изменять ваши собственные страницы.';
    $txt['custom_action_title'] = 'Дополнительные страницы';
    $txt['custom_action_title_sub'] = '"%1$s": вложенные страницы';
    $txt['custom_action_none'] = 'На данный момент никаких страниц нет!';
    $txt['custom_action_none_sub'] = 'Для страницы "%1$s" пока не создано никаких подстраниц!';
    $txt['custom_action_name'] = 'Название страницы';
    $txt['custom_action_type'] = 'Тип';
    $txt['custom_action_type_0'] = 'HTML';
    $txt['custom_action_type_1'] = 'BBC';
    $txt['custom_action_type_2'] = 'PHP';
    $txt['custom_action_sub_actions'] = 'Подстраниц';
    $txt['custom_action_enabled'] = 'Активна';
    $txt['custom_action_make_new'] = 'Новая страница';
    $txt['custom_action_make_new_sub'] = 'Новая подстраница';
    $txt['custom_action_not_found'] = 'Запрашиваемая страница не найдена.';
    $txt['custom_action_invalid_url'] = 'Пожалуйста, используйте олько буквы, цифры и знак подчеркивания.';
    $txt['custom_action_settings'] = 'Настройки страницы';
    $txt['custom_action_url_desc'] = 'Только буквы, цифры и знак подчеркивания.';
    $txt['custom_action_permissions_mode'] = 'Права доступа для страницы';
    $txt['custom_action_permissions_mode_0'] = 'Видима для всех';
    $txt['custom_action_permissions_mode_1'] = 'Видима для выбранных групп';
    $txt['custom_action_permissions_mode_2'] = 'Такие же, как у родительской страницы';
    $txt['custom_action_body'] = 'Тело';
    $txt['custom_action_body_html'] = 'Тело HTML';
    $txt['custom_action_body_php'] = 'Код шаблона';
    $txt['custom_action_delete_sure'] = 'Вы действительно хотите удалить эту страницу?';
    $txt['custom_action_header'] = 'Шапка HTML';
    $txt['custom_action_source'] = 'Исходный код';
    $txt['custom_action_source_desc'] = 'Этот код будет обрабатываться перед отображением любых шаблонов.<br>Если Вы не понимаете сути, просто размещайте весь свой код в поле ниже.';
    $txt['custom_action_header_desc'] = 'Этот код отображается в секции head.';
    $txt['custom_action_body_html_desc'] = 'Этот код отображается в секции body.';
    $txt['custom_action_body_php_desc'] = 'Все выходные данные размещаем здесь.';
    $txt['custom_action_body_desc'] = 'Содержание вашей страницы.';
    $txt['custom_action_url'] = 'URL-адрес страницы';
    $txt['custom_action_settings_code'] = 'Код страницы';
    $txt['custom_action_menu'] = 'Показывать кнопку в меню';
    ```
