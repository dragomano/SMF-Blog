---
title: Topic Descriptions
long_title: Topic Descriptions - описания для тем форума
description: Как заполнить короткое описание для темы на форуме SMF?
date: 2011-05-23
authors: [live627]
tags: [заметки, описания, темы, SMF 2.0, SMF 2.1]
categories: [translations]
---

Возможность создания и отображения коротких описаний для тем форума.

<!-- more -->

{{ img('Пример вывода описания темы', 'topic_descriptions.png') }}

{{ settings('Настройки модов → Описания тем.') }}

## Особенности

* Установка максимальной длины описаний.
* Отображение поля для ввода описаний только в заданных разделах.
* Отображение описаний тем внутри разделов (в списках тем).

{{ download('https://custom.simplemachines.org/index.php?mod=3012') }}

??? Русификация

    Создать файл `TopicDescriptions.russian-utf8.php` (2.0), или `TopicDescriptions.russian.php` (2.1) в кодировке UTF-8:

    ```php
    <?php

    // Topic Descriptions
    $txt['topic_descriptions'] = 'Описания тем';
    $txt['topic_description'] = 'Описание';
    $txt['error_long_description'] = 'Описание превышает максимально допустимую длину (%1$d символов).';
    $txt['topic_descriptions_maxlen'] = 'Максимальная длина описаний<div class="smalltext">По умолчанию: 25</div>';
    $txt['topic_descriptions_enable'] = 'Разрешить описания для тем?';
    $txt['topic_descriptions_post_desc'] = 'Описание (<i>не обязательно</i>):';
    $txt['select_boards_from_list'] = 'Выберите разделы, к которым применить';
    $txt['topic_descriptions_topics'] = 'Показывать описание внутри темы';
    ```
