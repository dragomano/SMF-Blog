---
title: Tagging System For Topics
long_title: Tagging System For Topics - теги для тем форума
description: Добавляем поддержку тегов на форуме SMF. Облако тегов для форума.
date: 2010-03-04
tags: [темы, теги, SMF 2.0, SMF 2.1]
categories: [translations]
---

Многофункциональная система тегов для вашего форума.

<!-- more -->

{{ img('Пример страницы с тегами', 'tagging_system.png') }}

## Особенности

* Возможность добавлять теги к создаваемым темам.
* Поиск по тегам.
* Отдельная страница в меню для вывода тегов.
* Определение прав доступа на добавление, удаление и управление тегами.
* Детальная настройка облака тегов.

## Нестандартное оформление

Ниже приведен пример нестандартного оформления блока с тегами (взято с сайта idesignsmf.com).

Найти код в `Display.template.php`:

```php
<?php

// Tagging System
echo '
<div class="clearfix windowbg largepadding">
    <b>', $txt['smftags_topic'], '</b>';

    foreach ($context['topic_tags'] as $i => $tag) {
        echo '
    <a href="' . $scripturl . '?action=tags;tagid=' . $tag['ID_TAG']  . '">' . $tag['tag'] . '</a>&nbsp;';

        if (! $context['user']['is_guest'] && allowedTo('smftags_del')) {
            echo '
    <a href="' . $scripturl . '?action=tags;sa=deletetag;tagid=' . $tag['ID']  . '"><font color="#FF0000">[X]</font></a>&nbsp;';
        }
    }

    global $topic;

    if (! $context['user']['is_guest'] && allowedTo('smftags_add')) {
        echo '
    &nbsp;<a href="' . $scripturl . '?action=tags;sa=addtag;topic=',$topic, '">' . $txt['smftags_addtag'] . '</a>';
    }

echo '
</div>';
```

и заменить на:

```php
<?php

// Tagging System
echo '
<div class="clearfix windowbg largepadding">
    ', $txt['smftags_topic'], '';

foreach ($context['topic_tags'] as $i => $tag) {
    echo '
    <span class="smf_tags"><a href="' . $scripturl . '?action=tags;tagid=' . $tag['ID_TAG']  . '">' . $tag['tag'] . '</a></span>&nbsp;';

    if (! $context['user']['is_guest'] && allowedTo('smftags_del')) {
        echo '
        <a href="' . $scripturl . '?action=tags;sa=deletetag;tagid=' . $tag['ID']  . '"><font color="#FF0000">[X]</font></a>&nbsp;';
    }
}

if (! $context['user']['is_guest'] && allowedTo('smftags_add')) {
    echo '
    &nbsp;<a href="' . $scripturl . '?action=tags;sa=addtag;topic=', $context['current_topic'], '">' . $txt['smftags_addtag'] . '</a>';
}

echo '
</div><br />';
// End Tagging System
```

Добавить в `index.css` используемой темы этот код:

```css
.smf_tags a {
    background-color: #f9f9f9;
    color: #333333;
    padding: 10px 20px;
    font-size: 14px;
    margin: 2px;
    text-align: center;
    display: inline-block;
    text-transform: uppercase;
}
.smf_tags a:hover {
    background-color: #0984e3;
    color: #ffffff;
}
```

{{ download('https://custom.simplemachines.org/index.php?mod=579') }}
{{ translation('https://drive.proton.me/urls/9TVHDWCEF4#BaPZQdkROKoI') }}
