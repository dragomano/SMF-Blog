---
title: Как добавить кнопку
description: Как создать новую кнопку в главном меню, в разделах или в темах на форуме SMF.
date: 2011-09-10
slug: kak-dobavit-knopku
authors: [bugo]
tags: [кнопки, меню, хуки]
categories: [lessons]
---

Этот материал посвящен созданию произвольных кнопок для SMF: в главном меню, в разделах, в темах.

<!-- more -->

С момента публикации [статьи о хуках в SMF](http://www.simplemachines.ru/index.php?topic=12037.0) прошло много времени. Некоторые моменты остались за кадром. Рассмотрим на новом примере.

Итак, каждый хук — это вызов пользовательских функций в определённых местах исходного кода движка.

То есть сделали вы, допустим, функцию `showMyText()`, которая выводит какой-то текст, и теперь хотите отображать этот текст на каждой странице форума. Ищем [подходящий хук](/hooks), настраиваем вашу функцию для вызова через выбранный хук, и любуемся результатом. При этом как-либо вручную править файлы движка не придется, соответственно, при обновлении форума никакие ваши файлы не затрутся.

## Элементы главного меню

К примеру, захотели добавить кнопку в главное меню. Раньше (SMF 1.x) что для этого приходилось делать? Лезть в **index.template.php**, искать, править... А если на форуме использовалось много тем оформления? Править *index.template.php* в каждой из них? Позже (SMF 2.x) ситуация изменилась, править нужно было только один файл — **Subs.php**.

Но файл один, а количество модов, которые вносили в него изменения, с каждым днём увеличивается. И при установке каждого следующего ожидаемо возникновение проблем и ошибок. Поэтому разработчики ввели хук **[integrate_menu_buttons](/hooks/integrate-menu-buttons)** — функцию, принимающую в качестве параметра массив с кнопками меню.

Подключается так:

```php
<?php

$hooks = [
    'integrate_pre_include' => '$sourcedir/Subs-MyMod.php',
    'integrate_menu_buttons' => 'example_menu_buttons',
];

foreach ($hooks as $hook => $function) {
    add_integration_function($hook, $function);
}
```

Сначала описывается массив с хуками, которые нам нужны, а затем этот массив прогоняется через функцию *add_integration_function*. После этого в таблице *settings* в базе данных появятся новые строчки: **integrate_pre_include** со значением `$sourcedir/Subs-MyMod.php` и **integrate_menu_buttons** со значением `example_menu_buttons`.

Файл *Subs-MyMod.php* разместите в папке *Sources*. В этом файле описывается функция `example_menu_buttons`.

Привыкаем к созданию отдельных подключаемых файлов, которые никуда не пропадут и не обнулятся при очередном обновлении форума — полезная практика.

Изменённый *Subs-MyMod.php*:
```php
<?php

if (! defined('SMF'))
    die('No direct access...');

// Изменение или добавление пунктов меню
function example_menu_buttons(&$buttons)
{
// тут весь наш код
}
```

Обратите внимание на начало файла. Если не хотите, чтобы форум взломали через созданный вами файл, не забывайте указывать эти строчки:

```php
<?php

if (! defined('SMF'))
    die('No direct access...');
```

Продолжим. Цель: добавить новую кнопку в меню. Функция *example_menu_buttons* принимает в качестве параметра массив **$buttons**, поэтому нам остается создать новый элемент в этом массиве:

```php
<?php

global $txt;

$buttons['mybutton'] = [
    'title' => $txt['mybutton_text'], // переменная с названием кнопки
    'href' => $txt['mybutton_link'], // ссылка куда-нибудь
    'show' => true, // если не хотим показывать кнопку, пишем false
    'sub_buttons' => [], // вложенные пункты, по умолчанию отсутствуют
];
```

Используемые текстовые переменные — в данном случае `$txt['mybutton_text']` и `$txt['mybutton_link']` — обязательно описываем и сохраняем в языковом файле (например, в *Modifications.russian-utf8.php*). Так как мы работаем с хуками, то лучше и языковые файлы подключать отдельно, не трогая те, что есть. Сохраняем переменные мода в файл php, называем, как хотим (лучше, чтобы название совпадало с названием будущего мода, чтобы не запутаться), переносим в папочку *languages* (внутри темы *default*) и затем подключаем через функцию **loadLanguage**, там где требуется:
```php
<?php

global $txt;

loadLanguage('MyMod');

// Добавляем новый пункт в меню
$buttons['mybutton'] = [
    'title' => $txt['mybutton_text'], // переменная с названием кнопки
    'href' => $txt['mybutton_link'], // ссылка куда-нибудь
    'show' => true, // если не хотим показывать кнопку, пишем false
    'sub_buttons' => [], // вложенные пункты, по умолчанию отсутствуют
];
```

Да, кнопочку добавили, но только выводится она в конце. А если нужен вывод после пункта «Поиск»? Можно так:

```php
<?php

$counter = 0;
foreach ($buttons as $name => $array) {
    $counter++;
    if ($name == 'search')
        break;
}

$buttons = array_merge(
    array_slice($buttons, 0, $counter, TRUE),
    [
        'mybutton' => [
            'title' => $txt['mybutton_text'], // переменная с названием кнопки
            'href' => $txt['mybutton_link'], // ссылка куда-нибудь
            'show' => true, // если не хотим показывать кнопку, пишем false
            'sub_buttons' => [], // вложенные пункты, по умолчанию отсутствуют
        ],
    ],
    array_slice($buttons, $counter, NULL, TRUE)
);
```

{{ img('Своя кнопка в главном меню', 'l1_new_button.png') }}

Идём дальше. Требуется изменить готовые пункты меню? Например, добавим атрибут `target="_blank"` к кнопке «Помощь»:

```php
<?php

$buttons['help']['href'] .= '" target="_blank';
```

А ещё легко добавлять вложенные пункты меню. Например, добавим подпункт «Сайт», который появляется при наведении на пункт «Начало»:

```php
<?php

global $txt;

$buttons['home']['sub_buttons'] = [
    'site' => [
        'title' => $txt['mysite'],
        'href' => $txt['mysite_link'],
        'show' => true,
        'is_last' => true,
    ]
];
```

Названия кнопок и ссылки рекомендую хранить в языковых файлах, а не указывать прямо в коде. Тогда в будущем (а для кого и в настоящем) вам будет очень легко, например, для каждого языка выводить отдельную ссылку: для русских mysite.ru, для англоговорящих: mysite.ru/en и т. п.

## Добавляем кнопку внутри разделов

С помощью ещё одного полезного хука — **integrate_messageindex_buttons** — создаются кнопки на страницах разделов:

```php
<?php

function example_messageindex_buttons(&$normal_buttons)
{
    global $txt, $scripturl, $context;

    loadLanguage('MyMod');

    $normal_buttons['new_button'] = [
        'test' => 'can_post_new', // Проверка прав доступа (в данном примере идет проверка на возможность создавать новые темы)
        'text' => 'hook_messageindex_buttons', // Текст кнопки
        'image' => 'im_reply.gif', // Иконка
        'lang' => true,
        'custom' => 'title=""', // Всплывающая подсказка для кнопки
        'url' => $scripturl . '?action=new_action;board=' . $context['current_board'] . '.0' // Действие (URL) для кнопки, передача параметра $_GET['board']
    ];
}
```

## Наборы кнопок

В SMF 2.1 для вывода подготовленного набора кнопок со стандартным оформлением используется функция `template_quickbuttons($list_items, $list_class = null)`. Например, за вывод кнопок внутри каждого сообщения отвечает хук **[integrate_post_quickbuttons](/hooks/integrate-custom-quickbuttons)**.

Для отображения своего набора кнопок в произвольном месте шаблона в первую очередь определяем массив с кнопками:

```php
<?php

$context['my_quickbuttons'] = [
    'button_name1' => [
        'label' => $txt['my_button_1'],
        'href' => 'Ссылка куда-то',
        'icon' => 'quote', // См. определение стиля .main_icons.quote в index.css
        'show' => true // Права на просмотр этой кнопки
    ],
    'button_name2' => [
        'label' => $txt['my_button_2'],
        'class' => 'quick_edit', // Класс элемента списка
        'id' => 'id элемента списка',
        'custom' => '', // Дополнительные атрибуты строкой, если нужны (для элемента li)
        'javascript' => '', // Дополнительные элементы строкой, если нужны (для элемента a внутри li)
        'icon' => 'quick_edit_button',
        'show' => true
    ],
    'more' => [
        'report' => [
            'label' => $txt['my_button_3'],
            'href' => 'Ссылка куда-то',
            'icon' => 'error',
            'show' => true
        ],
    ],
    'button_name3' => [
        'class' => 'inline_mod_check',
        'content' => '<input type="checkbox" name="options[]">', // Используется, если хочется полностью вручную указать весь HTML-код конкретной кнопки
        'show' => true
    ]
];
```
Затем в шаблоне задействуйте функцию **template_quickbuttons**, указав ей созданный массив с кнопками, а также желаемый класс для списка **ul**:

```php
<?php

template_quickbuttons($context['my_quickbuttons'], 'someclass');
```

Результат:

{{ img('А вот и наш набор кнопочек', 'l1_custom_button_sets.png') }}

В виде HTML:

```html
<ul class="quickbuttons quickbuttons_someclass">
    <li>
        <a href="Ссылка куда-то">
            <span class="main_icons quote"></span>Кнопка 1
        </a>
    </li>
    <li class="quick_edit" id="id элемента списка">
        <a href="javascript:void(0);">
            <span class="main_icons quick_edit_button"></span>Кнопка 2
        </a>
    </li>
    <li class="post_options">
        <a href="javascript:void(0);">Ещё...</a>
        <ul style="display: none;">
            <li>
                <a href="Ссылка куда-то">
                    <span class="main_icons error"></span>Кнопка 3
                </a>
            </li>
        </ul>
    </li>
    <li class="inline_mod_check">
        <input type="checkbox" name="options[]">
    </li>
</ul>
```

Как видим, каждая кнопка отображается внутри элемента `li` списка `ul`. А если мы хотим навесить какие-то индивидуальные стили конкретно для этого блока кнопок, можно добавить правила для класса `.quickbuttons_someclass`. Теперь вы знаете, как формировать такие кнопки самостоятельно.

## Остальные кнопки

Аналогично для добавления кнопок на страницах тем (хук **integrate_display_buttons**):

```php
<?php

function example_display_buttons(&$normal_buttons)
{
    global $txt, $scripturl, $context;

    loadLanguage('MyMod');

    $normal_buttons['new_button'] = [
        'test' => 'can_reply', // Проверка прав доступа (в данном примере идет проверка на возможность отвечать в теме)
        'text' => 'hook_display_buttons', // Текст кнопки
        'image' => 'im_reply.gif', // Иконка
        'lang' => true,
        'custom' => 'title=""', // Всплывающая подсказка для кнопки, используется редко
        'url' => $scripturl . '?action=new_action;topic=' . $context['current_topic'] . '.0' // Действие (URL) для кнопки, передача параметра $_GET['topic']
    ];
}
```

{{ img('Кнопка на страницах тем', 'l1_display_buttons.png') }}

Кнопки в нижней части страницы создаются так же. Только на этот раз используется хук **integrate_mod_buttons**, а в качестве входного параметра принимается массив *$mod_buttons*:

```php
<?php

function example_mod_buttons(&$mod_buttons)
{
    global $txt, $scripturl, $context;

    loadLanguage('MyMod');

    // Обратите внимание — здесь уже используется массив $mod_buttons (а не $normal_buttons, как в двух функциях выше)
    $mod_buttons['new_button'] = [
        'test' => 'can_delete', // Проверка прав доступа (в данном примере идет проверка на возможность удалять темы)
        'text' => 'hook_mod_buttons', // Текст кнопки
        'image' => 'im_reply.gif', // Иконка
        'lang' => true,
        'custom' => 'title="' . $txt['hook_mod_buttons_title'] . '"', // Всплывающая подсказка для кнопки
        'url' => $scripturl . '?action=new_action;topic=' . $context['current_topic'] . '.0' // Действие (URL) для кнопки, передача параметра $_GET['topic']
    ];
}
```

{{ img('Модераторская кнопочка', 'l1_mod_buttons.png') }}

{{ note('', 'В качестве примера посмотрите [TopicRenamer](/reviews/topic-renamer)') }}

Кроме того, никто не запрещает использовать описанные выше хуки не по прямому назначению. Например, чтобы вывести заданный текст на страницах разделов, сразу под описанием, воспользуйтесь тем же хуком **integrate_messageindex_buttons**:

```php
<?php

function example_messageindex_buttons()
{
    global $txt;

    loadLanguage('MyMod');

    // Выводим что-нибудь на страницах разделов
    echo '<p class="description">' . $txt['hook_echo'] . $txt['integrate_messageindex_buttons'] . '</p>';
}
```

Поскольку кнопок мы не изменяем и не добавляем, входной параметр (в виде массива **$normal_buttons**) не обязателен. А результат на скриншоте:

{{ img('Выводим свой текст внутри раздела', 'l1_echo_on_boards.png') }}

Аналогичный вывод используется на страницах тем.
