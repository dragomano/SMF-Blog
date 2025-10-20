---
title: Disqus
long_title: Disqus - комментарии для форума
description: Как подключить Disqus комментарии к SMF? Превращение форума в социальную сеть.
date: 2011-10-21
tags: [SMF 2.0, disqus, комментарии]
categories: [translations]
---

Подключаем внешнюю систему комментариев к SMF. Для тех, кто хотел бы оформить форум в виде блога.

<!-- more -->

{{ img('Комментируем первое сообщение в каждой теме', 'disqus.png') }}

## Инструкция

* Устанавливаем мод, регистрируемся на сайте Disqus, затем заполняем настройки мода в админке SMF.
* Активируем мод в свойствах нужных разделов.
* Меняем профиль прав доступа разделов на «только для чтения», чтобы пользователи не могли создавать там новые темы и сообщения.
* После этого получаем вид сообщений как в блогах (см. скриншот).

{{ download('https://custom.simplemachines.org/index.php?mod=3211') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Disqus
    $txt['disqus_settings_title'] = 'Настройки Disqus';
    $txt['disqus_admin_menu'] = 'Disqus';
    $txt['disqus_settings_desc'] = 'Изменение конфигурации мода Disqus';
    $txt['disqus_allow'] = 'Включить систему комментариев Disqus?';
    $txt['disqus_board_enable'] = 'Подключить систему комментариев Disqus';
    $txt['disqus_board_enable_desc'] = '';
    $txt['disqus_id'] = 'Введите здесь \'short name\' (короткое имя), которое указали при регистрации форума в Disqus.';
    $txt['disqus_configure_desc'] = 'Перед подключением Disqus необходимо зарегистрироваться на сайте <a href="http://www.disqus.com" target="_blank">disqus.com</a>';
    ```
