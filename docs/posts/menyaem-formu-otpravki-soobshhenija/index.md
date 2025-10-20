---
title: Меняем форму отправки сообщения
description: Как добавить свои поля в форму отправки сообщения SMF?
date: 2019-11-18
slug: menyaem-formu-otpravki-soobshhenija
authors: [bugo]
tags: [форма, поля, message]
categories: [lessons]
---

В SMF 2.1 можно кастомизировать форму отправки сообщения по своему вкусу. Для этого предназначен массив `$context['posting_fields']`, объявляющийся в Post.php.

<!-- more -->

## Структура массива

По умолчанию он содержит два элемента: **subject** (поле заголовка) и **icon** (раскрывающийся список для выбора иконки сообщения). Рассмотрим их структуру:

```php
<?php

global $context, $txt;

$context['posting_fields']['subject'] = [
    'label' => [
        'text' => $txt['subject'],
        'class' => isset($context['post_error']['no_subject']) ? 'error' : '',
    ],
    'input' => [
        'type' => 'text',
        'attributes' => [
            'size' => 80,
            'maxlength' => ! empty($topic) ? 84 : 80,
            'value' => $context['subject'],
            'required' => true,
        ],
    ],
];

$context['posting_fields']['icon'] = [
    'label' => [
        'text' => $txt['message_icon'],
    ],
    'input' => [
        'type' => 'select',
        'attributes' => [
            'id' => 'icon',
            'onchange' => 'showimage();',
        ],
        'options' => [],
        'after' => ' <img id="icons" src="' . $context['icon_url'] . '">',
    ],
];

foreach ($context['icons'] as $icon) {
    $context['posting_fields']['icon']['input']['options'][$icon['name']] = [
        'value' => $icon['value'],
        'selected' => $icon['value'] == $context['icon'],
    ];
}
```

Метки **label** и элементы **input** обязательны. Текст **label** и тип **input** также нужно указывать. У поля **subject** тип _text_, у поля **icon** — _select_.
С помощью массива **attributes** указываются атрибуты элементов: id, size, value и т. п.
У метки элемента **subject** также указан класс (_class_), а у элемента **icon** в свойстве `after` размещено изображение, которое отображается справа от списка.

Каждый добавляемый в массив `$context['posting_fields']` элемент должен быть одного из следующих типов:
    * text, password, color, date, datetime-local, email, month, number, range, tel, time, url, week
    * textarea
    * checkbox
    * select
    * radio_select

Когда тип элемента _text_, _password_, _color_, _date_, _datetime-local_, _email_, _month_, _number_, _range_, _tel_, _time_, _url_, _week_, _textarea_ или _checkbox_, свойство **attributes** используется для задания начального значения элемента, а также для установки любых других HTML-элементов, необходимых в конкретной ситуации.

```php
<?php

global $context;

// Поле для вызова цветовой палитры
$context['posting_fields']['color'] = [
    'label' => [
        'text' => 'Цвет',
    ],
    'input' => [
        'type' => 'color',
        'attributes' => [
            'value' => '#ff0000', // Выбранный цвет по умолчанию
        ],
    ],
];

// Поле для указания времени и даты
$context['posting_fields']['datetime-local'] = [
    'label' => [
        'text' => 'Дата и время',
    ],
    'input' => [
        'type' => 'datetime-local',
    ],
];

```

{{ img('Реализация кода выше', 'custom_posting_fields.png') }}

{{ warning('Некоторые типы элемента `input` поддерживаются не всеми браузерами!') }}

Когда тип элемента _select_ или *radio_select*, в свойстве **options** перечисляется список параметров, доступных для выбора пользователем.
Каждый параметр в массиве **options** также является массивом, содержащим список атрибутов.

```php
<?php

global $context;

$context['posting_fields']['mood'] = [
    'label' => [
        'text' => 'Настроение',
    ],
    'input' => [
        'type' => 'select',
        'options' => [
            'Хорошее' => [
                'value' => 'good',
                'selected' => true,
            ],
            'Так себе' => [
                'value' => 'so_so',
                'selected' => false,
            ],
            'Плохое' => [
                'value' => 'bad',
                'selected' => false
            ]
        ],
    ],
];
```

Кроме того, как label, так и input могут иметь атрибуты `before` и/или `after`, содержащие HTML-код, отображаемый, соответственно, слева или справа от элемента.
Наконец, если нужно, отображение элементов label и input можно переопределить с помощью свойства `html`. Но используйте это в самом крайнем случае!

Пример переопределения:

```php
<?pnp

global $context, $txt;

$context['posting_fields']['subject'] = [
    'label' => [
        'html' => '<label for="subject" id="caption_subject">' . $txt['subject'] . '</label>'
    ],
    'input' => [
        'html' => '<input type="text" id="subject" name="subject" value="' . $context['subject'] . '" size="80" maxlength="80" required>'
    ]
];
```

{{ tip("Чтобы не редактировать файл _Post.php_, используйте хук **[integrate_post_end](/hooks/integrate-post-end)**, в котором можно переопределить массив `$context['posting_fields']`.") }}