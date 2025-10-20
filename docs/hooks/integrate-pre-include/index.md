---
title: Хук integrate_pre_include
description: Описание и пример использования хука integrate_pre_include в SMF.
date: 2019-03-08
tags: [хуки, включение, include, preload]
---

По сути, перед нами некий аналог php-функции *require_once*, подключающий нужный вам файл на страницах форума.

<!-- more -->

## Расположение

=== "SMF 2.x"

    `Sources/Load.php`

    ```php
    <?php

    if (!empty($modSettings['integrate_pre_include']))
    {
        $pre_includes = explode(',', $modSettings['integrate_pre_include']);
        foreach ($pre_includes as $include)
        {
            $include = strtr(trim($include), array('$boarddir' => $boarddir, '$sourcedir' => $sourcedir));
            if (file_exists($include))
                require_once($include);
        }
    }
    ```

=== "SMF 3.0"

    `Sources/Config.php`

    ```php
    <?php

    if (!empty(self::$modSettings['integrate_pre_include'])) {
        $pre_includes = explode(',', self::$modSettings['integrate_pre_include']);

        foreach ($pre_includes as $include) {
            $include = strtr(trim($include), ['$boarddir' => self::$boarddir, '$sourcedir' => self::$sourcedir]);

            if (file_exists($include)) {
                require_once self::canonicalPath($include);
            }
        }
    }
    ```

Как видим, хук не имеет параметров; с помощью него авторы модов могут подключать свои файлы с используемыми функциями.

## Назначение

`integrate_pre_include` — это один из многих хуков в системе модификаций SMF. Его ключевая особенность и главное отличие от других хуков в том, что он выполняется очень рано, ещё до загрузки большинства системных файлов и инициализации основных компонентов форума.

Это «хук-загрузчик», основная задача которого — подключить ваш собственный PHP-файл до того, как начнется основная обработка запроса.

## Использование

[Как подключать хуки](/lessons/kak-podklyuchat-huki)

{{ warning('Подключение хука путём вызова в PHP-файле неприменимо.', 'Важно') }}

## Важные замечания и лучшие практики

Не используйте этот хук для подключения файлов, которые нужны только на странице администрирования (для этого есть `integrate_admin_include`) или только в действиях (для этого есть [integrate_actions](/hooks/integrate-actions)). Это позволяет экономить ресурсы.

Осторожность с кодом: Поскольку хук выполняется до загрузки ядра SMF, у вас нет доступа к большинству функций SMF. Ваш код должен быть максимально автономным или проверять, доступна ли уже нужная функция.

Проверка на существование: Всегда проверяйте, существует ли ваша функция или класс, прежде чем их объявлять, чтобы избежать конфликтов с другими модами.

`integrate_pre_include` — это мощный инструмент для загрузки необходимого кода на самом раннем этапе работы SMF. Его основное предназначение — обеспечить доступность ваших кастомных функций и классов для всех последующих хуков и логики форума. Используйте его осознанно, когда вашему моду требуется ранняя инициализация.
