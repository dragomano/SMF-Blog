---
title: Хук integrate_display_topic
description: Описание и пример использования хука integrate_display_topic в SMF.
date: 2020-07-21
tags: [хуки, темы, display, topic]
---

Хук `integrate_display_topic` позволяет изменять или дополнять выборку при получении данных о просматриваемой теме форума.

<!-- more -->

## Расположение

=== "SMF 2.x"

    `Sources/Display.php`

    ```php
    <?php

    call_integration_hook('integrate_display_topic', array(&$topic_selects, &$topic_tables, &$topic_parameters));
    ```

=== "SMF 3.0"

    `Sources/Topic.php`

    ```php
    <?php

    IntegrationHook::call('integrate_display_topic', [&$topic_selects, &$topic_joins, &$topic_parameters]);
    ```

## Назначение

Хук принимает в качестве параметров массивы `$topic_selects`, `$topic_tables` и `$topic_parameters`. С помощью них можно получать дополнительные столбцы из таблиц `smf_topics`, `smf_messages`, `smf_members`, а также из других, перечисленных в переменной `$topic_tables`. Переменная `$topic_parameters` используется для указания дополнительных параметров запроса.

## Использование

[Как подключать хуки](/lessons/kak-podklyuchat-huki)

```php
<?php

if (! defined('SMF'))
    die('No direct access...');

class YourModName
{
    // Подключаем используемые хуки
    public function hooks(): void
    {
        add_integration_function('integrate_display_topic', self::class . '::displayTopic#', false, __FILE__);
    }

    // Получаем дополнительные сведения при просмотре темы
    public function displayTopic(&$topic_selects, &$topic_tables, &$topic_parameters): void
    {
        // Запрашиваемый столбец
        $topic_selects[] = 'your_column_name';

        // Запрашиваемая таблица, связанная с smf_tables
        $topic_tables[] = 'LEFT JOIN {db_prefix}your_table AS yt ON (yt.id_topic = t.id_topic AND yt.other_column_name = {string:your_parameter})';

        // Требуемое значение параметра (если нужно)
        $topic_parameters['your_parameter'] = 'your_value';
    }

    // Далее в коде можно будет обращаться к полученному столбцу через $context['topicinfo']['your_column_name']
}
```

Благодаря этому хуку можно получать сведения об описании, ключевых словах, а также о первом вложении текущей просматриваемой темы. Ну и заодно выводить что-то на страницах тем.
