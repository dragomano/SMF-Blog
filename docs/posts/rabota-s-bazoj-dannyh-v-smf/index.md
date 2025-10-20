---
title: Работа с базой данных в SMF
description: Описание функций для работы с таблицами форумного движка SMF.
date: 2022-05-10
slug: rabota-s-bazoj-dannyh-v-smf
authors: [bugo]
tags: [база данных, SQL, функции]
categories: [lessons]
---

В этой статье мы разберём функции SMF для создания и изменения таблиц в базе данных.

<!-- more -->

## Подготовка

Если хотите проверить все рассматриваемые функции в деле, потребуется тестовая площадка:

- [Установленный форум](/lessons/ustanovka-smf-2-1) (чтобы было, на чем тестировать вживую)
- [VarDumper for SMF](https://custom.simplemachines.org/index.php?mod=4302) или [SMF Tracy Debugger](/mods/smf-tracy-debugger) (чтобы была возможность использовать функцию `dump()`)

## $smcFunc

Все нужные методы для работы с таблицами в базе данных находятся в глобальном ассоциативном массиве `$smcFunc`, который устанавливается в корневом `index.php`, заполняется в `Load.php` и дополняется в файлах `DbExtra-mysql.php`, `DbExtra-postgresql.php`, `DbPackages-mysql.php`, `DbPackages-postgresql.php`, `DbSearch-mysql.php`, `DbSearch-postgresql.php`, `Subs-Db-mysql.php` и `Subs-Db-postgresql.php`, в зависимости от типа используемой базы данных. А поскольку массив глобальный, не забывайте объявлять `global $smcFunc` в своих функциях/методах.

{{ warning('В массиве `$smcFunc` хранятся не только функции для работы с базой данных, но также и различные хелперы, с которыми мы обязательно познакомимся в одном из будущих уроков.', 'Важно') }}

## Базовые функции

Набор основных функций для работы с запросами находится в `Subs-Db-mysql.php`|`Subs-Db-postgresql.php`. Рассмотрим их подробнее.

### $smcFunc['db_query']

Универсальная функция для обработки запросов любой сложности. Вторым аргументом можно передать любой запрос. Например, получим все записи из таблицы:

```php
<?php

global $smcFunc;

$request = $smcFunc['db_query']('', 'SELECT * FROM {db_prefix}members');

dump($smcFunc['db_fetch_all']($request));
```

### $smcFunc['db_quote']

Как и `db_query`, экранирует и заключает в кавычки строку, но не выполняет запрос. Пример:

```php
<?php

global $smcFunc;

$userQuery = $smcFunc['db_quote'](
    '(m.id_member IN ({array_int:matched_members}) OR (m.id_member = {int:id_member_guest} AND ({raw:match_possible_guest_names})))',
    [
        'matched_members' => [1, 2, 3],
        'id_member_guest' => 0,
        'match_possible_guest_names' => 'm.poster_name LIKE ' . implode(' OR m.poster_name LIKE ', ['Test1', 'Test2', 'Test3']),
    ]
);

dump($userQuery);
```

Результат:

```sql
'(m.id_member IN (1, 2, 3) OR (m.id_member = 0 AND (m.poster_name LIKE Test1 OR m.poster_name LIKE Test2 OR m.poster_name LIKE Test3)))'
```

### $smcFunc['db_fetch_assoc']

Возвращает следующую строку результата запроса в виде ассоциативного массива. Пример:

```php
<?php

global $smcFunc;

$request = $smcFunc['db_query']('', 'SELECT * FROM {db_prefix}members');

while ($row = $smcFunc['db_fetch_assoc']($request)) {
    dump($row);
}
```

### $smcFunc['db_fetch_row']

Возвращает следующую строку результата запроса в виде обычного массива. Пример:

```php
<?php

global $smcFunc;

$request = $smcFunc['db_query']('', '
    SELECT * FROM {db_prefix}members
    WHERE id_member = {int:id}
    LIMIT 1',
    [
        'id' => 1
    ]
);

dump($smcFunc['db_fetch_row']($request));
```

Результат будет выглядеть как-то так:

```php
<?php

array(
    0 => '1'
    1 => 'Test'
    2 => '1631176348'
    3 => '54'
    4 => '1'
    5 => 'russian'
    6 => '1651629543'
    ...
)
```

### $smcFunc['db_fetch_all']

Возвращает все строки результата запроса в виде ассоциативного массива. См. пример использования `$smcFunc['db_query']`.

### $smcFunc['db_free_result']

Освобождает память от результата запроса `$request`. Указывайте после каждого использования `$smcFunc['db_fetch_assoc']`, `$smcFunc['db_fetch_all']` и `$smcFunc['db_free_result']`:

```php
<?php

global $smcFunc;

$smcFunc['db_free_result']($request);
```

### $smcFunc['db_insert']

Добавляет новую запись в указанную таблицу. Пример:

```php
<?php

global $smcFunc;

$smcFunc['db_insert']('',
    '{db_prefix}messages',
    $message_columns,
    $message_parameters,
    ['id_msg']
);
```

Чтобы получить идентификатор добавленной записи, можно указать `1` в качестве последнего параметра или использовать `$smcFunc['db_insert_id']` (см. ниже):

```php
<?php

global $smcFunc;

$id = $smcFunc['db_insert']('',
    '{db_prefix}messages',
    $message_columns,
    $message_parameters,
    ['id_msg'],
    1
);
```

### $smcFunc['db_insert_id']

Возвращает идентификатор только что добавленной записи. Пример:

```php
<?php

global $smcFunc;

$smcFunc['db_insert']('',
    '{db_prefix}messages',
    $message_columns,
    $message_parameters,
    ['id_msg']
);

dump($smcFunc['db_insert_id']());
```

### $smcFunc['db_num_rows']

Возвращает количество строк результата запроса. Пример:

```php
<?php

global $smcFunc;

$request = $smcFunc['db_query']('', 'SELECT * FROM {db_prefix}members');

dump($smcFunc['db_num_rows']($request));
```

### $smcFunc['db_data_seek']

Переходит к заданной строке `$i` в результирующем наборе `$request`. Пример:

```php
<?php

global $smcFunc;

$smcFunc['db_data_seek']($request, $i);
```

{{ info('Пример использования на практике см. в файле `Sources/Memberlist.php`.') }}

### $smcFunc['db_num_fields']

Возвращает количество полей результата запроса. Пример:

```php
<?php

global $smcFunc;

$request = $smcFunc['db_query']('', 'SELECT * FROM {db_prefix}members');

dump($smcFunc['db_num_fields']($request));
```

### $smcFunc['db_escape_string']

Возвращает строку с экранированными специальными символами, для использования в выражениях SQL. Пример:

```php
<?php

global $smcFunc;

$test = "'123'";

dump($smcFunc['db_escape_string']($test));
```

Результат:

```
'\'123\''
```

### $smcFunc['db_unescape_string']

Удаляет экранирование символов. Синоним для функции `stripslashes`. Пример:

```php
<?php

global $smcFunc;

$test = "\'123\'";

dump($smcFunc['db_unescape_string']($test));
```

Результат:

```
"'123'"
```

### $smcFunc['db_server_info']

Возвращает версию используемого сервера базы данных. Пример:

```php
<?php

global $smcFunc;

dump($smcFunc['db_server_info']());
```

Результат будет выглядеть как-то так:

```
'5.5.5-10.6.7-MariaDB'
```

### $smcFunc['db_affected_rows']

Возвращает число строк, затронутых последним запросом INSERT, UPDATE, REPLACE или DELETE. Пример:

```php
<?php

global $smcFunc;

$smcFunc['db_query']('', '
    DELETE FROM {db_prefix}members
    WHERE id_member IN ({array_int:ids})',
    [
        'ids' => [12, 13, 14]
    ]
);

dump($smcFunc['db_affected_rows']());
```

### $smcFunc['db_transaction']

Осуществляет один из этапов [транзакции](https://habr.com/ru/post/537594/) (`begin`, `commit`, `rollback`). Пример:

```php
<?php

global $smcFunc;

// Инициализация транзакции
$smcFunc['db_transaction']('begin');

$id = $smcFunc['db_insert']('',
    '{db_prefix}messages',
    $message_columns,
    $message_parameters,
    ['id_msg'],
    1
);

// далее могут быть другие запросы

if (empty($id)) {
    // Откат изменений (все запросы выше откатываются, как будто их и не было)
    $smcFunc['db_transaction']('rollback');
    return;
}

// Фиксация изменений (все запросы подтверждаются)
$smcFunc['db_transaction']('commit');
```

{{ tip('Пример использования на практике можно увидеть в [исходном коде Light Portal](https://github.com/dragomano/Light-Portal).') }}

### $smcFunc['db_error']

Возвращает строку с описанием последней ошибки. Пример:

```php
<?php

global $smcFunc;

dump($smcFunc['db_error']($db_connection));
```

### $smcFunc['db_select_db']

Устанавливает базу данных для выполняемых запросов. Вряд ли пригодится, но вдруг вам захочется подключиться к другой базе данных во время работы с SMF? Пример:

```php
<?php

global $smcFunc;

// Выбираем базу данных
$smcFunc['db_select_db']('other_database');

// Осуществляем другие запросы
```

### $smcFunc['db_title']

Возвращает название используемого движка базы данных. Пример:

```php
<?php

global $smcFunc;

dump($smcFunc['db_title']());
```

### $smcFunc['db_escape_wildcard_string']

Экранирует знаки подстановки и возвращает строку с произведёнными заменами. Пример:

```php
<?php

global $smcFunc;

$test = '%some_text%';

dump($smcFunc['db_escape_wildcard_string']($test));
```

Результат:

```
'\%some\_text\%'
```

### $smcFunc['db_custom_order']

Конструирует оптимизированную строку пользовательского заказа как улучшенная альтернатива `find_in_set()`. Пример:

```php
<?php

global $smcFunc;

dump($smcFunc['db_custom_order']('status', [1, 0]));
```

Результат:

```sql
'CASE status WHEN 1 THEN 0 WHEN 0 THEN 1 END'
```

### $smcFunc['db_cte_support']

Возвращает `true`, если база данных поддерживает _Common Table Expression_ (Общие Табличные Выражения). Пример подобного выражения:

```sql
SELECT * FROM smf_members;
WITH cte_members AS (
    SELECT COUNT(*) as total
    FROM smf_members
    WHERE is_activated = "1" GROUP BY is_activated
)
SELECT total as `Всего активных пользователей`
FROM cte_members;
```

{{ info('Пример других CTE-запросов доступны [здесь](https://andreyex.ru/bazy-dannyx/bd-mysql/with-v-mysql-obshhee-tablichnoe-vyrazhenie-cte/).') }}

## Функции, специально разработанные для использования в модах

{{ warning('Перед использованием этой группы функций нужно подготовить массив `$smcFunc` с помощью вызова `db_extend(\'packages\');`.', 'Важно') }}

### $smcFunc['db_add_column']

Добавляет столбец в указанную таблицу. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

$smcFunc['db_add_column'](
    '{db_prefix}my_table',
    [
        'name'     => 'content',
        'type'     => 'text',
        'null'     => false,
        'not_null' => true
    ],
    [],
    'do_nothing'
);
```

### $smcFunc['db_add_index']

Добавляет индекс в указанную таблицу. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

$table_name = '{db_prefix}my_table';
$index_info = [
    'name' => 'my_index',
    'type' => 'index', // 'index', 'unique', 'primary'
    'columns' => [
        'column1', 'column2'
    ]
];
$smcFunc['db_add_index']($table_name, $index_info);
```

К сожалению, не все типы индексов можно добавить таким образом. Некоторые (например, `FULLTEXT`) добавляются лишь «по старинке», с помощью обычного SQL:

```php
<?php

global $smcFunc;

$smcFunc['db_query']('', '
    ALTER TABLE {db_prefix}table_name
    ADD FULLTEXT index_name (column_name)',
    []
);
```

### $smcFunc['db_calculate_type']

Возвращает массив с указанными именем и типом столбца. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

dump($smcFunc['db_calculate_type']('varchar', 255));
```

Результат:

```php
<?php

array(
    0 => 'varchar'
    1 => 255
)
```

### $smcFunc['db_change_column']

Изменяет столбец в указанной таблице. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

$column_info = [
    'name' => 'new_name',
    'type' => 'new_type',
    // ... и т. д.
];
$smcFunc['db_change_column']('{db_prefix}my_table', 'column_name', $column_info);
```

### $smcFunc['db_create_table']

Создаёт таблицу с заданными столбцами, каждый из которых представляет собой массив. Пример:

```php
<?php

global $smcFunc;

$tables[] = [
    'name' => 'my_table',
    'columns' => [
        [
            'name'     => 'id',
            'type'     => 'int',
            'size'     => 10,
            'unsigned' => true,
            'auto'     => true
        ],
        [
            'name'     => 'title',
            'type'     => 'varchar',
            'size'     => 255,
            'null'     => false,
            'not_null' => true
        ],
        [
            'name'     => 'created_at',
            'type'     => 'int',
            'size'     => 10,
            'unsigned' => true
        ]
    ],
    'indexes' => [
        [
            'type'    => 'primary',
            'columns' => ['id']
        ],
    ]
];

db_extend('packages');

foreach ($tables as $table) {
    $smcFunc['db_create_table']('{db_prefix}' . $table['name'], $table['columns'], $table['indexes']);
}
```

### $smcFunc['db_drop_table']

Удаляет указанную таблицу. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

$smcFunc['db_drop_table']('{db_prefix}my_table');
```

### $smcFunc['db_table_structure']

Возвращает структуру таблицы. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

dump($smcFunc['db_table_structure']('{db_prefix}messages'));
```

Результат:

```php
<?php

array(4)
    'name'    => 'smf_messages'
    'columns' => array(18)
    'indexes' => array(11)
    'engine'  => 'InnoDB'
```

### $smcFunc['db_list_columns']

Возвращает информацию о столбцах указанной таблицы. Второй параметр отвечает за отображение подробных сведений о столбцах. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

dump($smcFunc['db_list_columns']('{db_prefix}messages', true));
```

### $smcFunc['db_list_indexes']

Возвращает информацию об индексах указанной таблицы. Второй параметр отвечает за отображение подробных сведений о столбцах. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

dump($smcFunc['db_list_indexes']('{db_prefix}messages', true));
```

### $smcFunc['db_remove_column']

Удаляет заданный столбец из указанной таблицы. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

$smcFunc['db_remove_column']('{db_prefix}my_table', 'column_name');
```

### $smcFunc['db_remove_index']

Удаляет заданный индекс из указанной таблицы. Пример:

```php
<?php

global $smcFunc;

db_extend('packages');

$smcFunc['db_remove_index']('{db_prefix}my_table', 'index_name');
```

## Функции, связанные с поиском

{{ warning('Перед использованием этой группы функций нужно подготовить массив `$smcFunc` с помощью вызова `db_extend(\'search\');`.', 'Важно') }}

### $smcFunc['db_search_query']

Синоним `$smcFunc['db_query']`.

### $smcFunc['db_search_support']

Возвращает `true`, если базой данных поддерживается указанный тип поиска. Пример:

```php
<?php

dump($smcFunc['db_search_support']('fulltext'));
```

### $smcFunc['db_create_word_search']

Используется для создания пользовательской таблицы с индексами слов (см. _Поисковое индексирование_ в настройках поиска).

### $smcFunc['db_search_language'] (только для PostgreSQL)

Возвращает язык для индекса текстового поиска. Пример:

```php
<?php

dump($smcFunc['db_search_language']())
```

{{ note('Пример использования на практике можно увидеть в [исходном коде Similar Topics](https://github.com/dragomano/Similar-Topics).') }}

## Редко используемые функции

{{ warning('Перед использованием этой группы функций нужно подготовить массив `$smcFunc` с помощью вызова `db_extend(\'extra\');` или просто `db_extend()` (`extra` является значением по умолчанию).', 'Важно') }}

### $smcFunc['db_backup_table']

Создает резервную копию указанной таблицы. Пример:

```php
<?php

$smcFunc['db_backup_table']('{db_prefix}members', 'backup_members');
```

### $smcFunc['db_optimize_table']

Оптимизирует указанную таблицу. Пример:

```php
<?php

$smcFunc['db_optimize_table']('{db_prefix}members');
```

### $smcFunc['db_table_sql']

Выводит в виде дампа SQL-схему CREATE для указанной таблицы. Пример:

```php
<?php

dump($smcFunc['db_table_sql']('{db_prefix}user_likes'));
```

Результат будет выглядеть как-то так:

```sql
DROP TABLE IF EXISTS `smf_user_likes`;

CREATE TABLE `smf_user_likes` (
  `id_member` mediumint(8) unsigned NOT NULL default 0,
  `content_type` char(6) NOT NULL default '',
  `content_id` int(10) unsigned NOT NULL default 0,
  `like_time` int(10) unsigned NOT NULL default 0,
  PRIMARY KEY (`content_id`, `content_type`, `id_member`),
  KEY `content` (`content_id`, `content_type`),
  KEY `liker` (`id_member`)
) ENGINE=InnoDB'
```

### $smcFunc['db_list_tables']

Выводит список всех таблиц в базе данных. Вторым параметром можно указать фильтр (имя проверяемой таблицы или маску поиска).

Пример 1 — получаем массив с именами всех таблиц в текущей базе данных:

```php
<?php

dump($smcFunc['db_list_tables']());
```

Пример 2 — получаем пустой массив, если таблицы `my_table` в базе данных `my_database` нет:

```php
<?php

dump($smcFunc['db_list_tables']('my_database', '{db_prefix}my_table'));
```

### $smcFunc['db_get_version']

Выводит версию используемого движка базы данных. Пример:

```php
<?php

dump($smcFunc['db_get_version']());
```

Результат будет выглядеть как-то так:

```
'10.6.7-MariaDB'
```

### $smcFunc['db_get_vendor']

Возвращает название используемого движка базы данных. Пример:

```php
<?php

dump($smcFunc['db_get_vendor']());
```

Результат будет выглядеть как-то так:

```
'MariaDB'
```

### $smcFunc['db_allow_persistent']

Возвращает `true`, если разрешено постоянное соединение с базой данных.

## Полезные ссылки

* [Вспомогательные утилиты для администраторов SMF](https://github.com/sbulen/sjrbTools)
