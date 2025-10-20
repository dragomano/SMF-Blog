---
title: Хук integrate_load_permissions
description: Описание и пример использования хука integrate_load_permissions в SMF.
date: 2019-05-03
tags: [хуки, права, permissions]
---

Хук `integrate_load_permissions` позволяет добавлять новые права доступа, доступные для настройки в соответствующей секции форума.

<!-- more -->

## Расположение

=== "SMF 2.x"

    `Sources/ManagePermissions.php`

    ```php
    <?php

    call_integration_hook('integrate_load_permissions', array(&$permissionGroups, &$permissionList, &$leftPermissionGroups, &$hiddenPermissions, &$relabelPermissions));
    ```

=== "SMF 3.0"

    `Sources/Actions/Admin/Permissions.php`

    ```php
    <?php

    IntegrationHook::call('integrate_load_permissions', [&self::$permission_groups, &$permissions_by_scope, &self::$left_permission_groups, &$hidden_permissions, &$relabel_permissions]);
    ```
    Рекомендуется перейти на использование хука [integrate_permissions_list](/hooks/integrate-permissions-list)

## Назначение

Хук принимает несколько массивов, но обязательных из них два: `$permissionGroups` и `$permissionList`. В первом содержатся группы разрешений, во втором — списки. Остальные параметры используются реже, но примеры приведу и для них, в конце статьи.

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
        add_integration_function('integrate_load_permissions', self::class . '::loadPermissions#', false, __FILE__);
    }

    public function loadPermissions(&$permissionGroups, &$permissionList): void
    {
        global $context;

        // В массиве $context['non_guest_permissions'] содержатся права доступа, которые нельзя разрешать гостям:
        $context['non_guest_permissions'][] = 'your_permission';

        // Добавление вашего разрешения в категорию «Общие» в Основных правах доступа:
        $permissionList['membergroup']['your_permission'] = [false, 'general', 'view_basic_info'];

        // В SMF 2.0.x при просмотре прав доступа можно изменять вид отображения (простой или классический), поэтому нужно указывать параметры мода для каждого вида:
        $permissionGroups['membergroup']['simple']  = ['your_mod'];
        $permissionGroups['membergroup']['classic'] = ['your_mod'];

        // Далее перечисляются все добавляемые права доступа:
        $permissionList['membergroup']['your_mod_perm1'] = [false, 'your_mod', 'your_mod'];
        $permissionList['membergroup']['your_mod_perm2'] = [false, 'your_mod', 'your_mod'];
        $permissionList['membergroup']['your_mod_perm3'] = [false, 'your_mod', 'your_mod'];
        $permissionList['membergroup']['your_mod_perm4'] = [false, 'your_mod', 'your_mod'];
        $permissionList['membergroup']['your_mod_perm5'] = [false, 'your_mod', 'your_mod'];
        $permissionList['membergroup']['your_mod_perm6'] = [false, 'your_mod', 'your_mod'];
    }
}
```

#### Подробнее о массиве с параметрами

Если добавляемое вами разрешение универсальное (например, «Просмотр форума»), то указывайте первым атрибутом `false`:

```php
    ... = [false, 'forum_view'];
```

Если же нужно разделить настройку (например, для разрешения «Редактирование профиля»), указывайте `true`:

```php
    ... = [true, 'profile_edit'];
```

В последнем случае можно будет отдельно разрешить редактирование только своего профиля, только чужих профилей, или же и своего и чужих вместе.

{{ img("Пример секций в правах доступа, добавленных модами", "integrate_load_permissions.png") }}

### Расширенный пример

С использованием всех параметров хука (для SMF 2.1.x):

```php
<?php

if (! defined('SMF'))
    die('No direct access...');

class YourModName
{
    // Подключаем используемые хуки
    public function hooks(): void
    {
        add_integration_function('integrate_load_permissions', self::class . '::loadPermissions#', false, __FILE__);
    }

    public function loadPermissions(&$permissionGroups, &$permissionList, &$leftPermissionGroups, &$hiddenPermissions, &$relabelPermissions): void
    {
        global $modSettings;

        // Добавление секции с вашим модом в категорию «Основные права»:
        $permissionGroups['membergroup'][]  = 'your_mod_section';

        // Добавление нужных прав доступа в только что добавленную секцию:
        $permissionList['your_mod_perm1'] = [false, 'your_mod_section'];
        $permissionList['your_mod_perm2'] = [false, 'your_mod_section'];

        // Добавление секции с вашим модом в категорию «Права для разделов с глобальными привилегиями»:
        $permissionGroups['board'][] = 'your_mod_section';

        // Добавление нужных прав доступа в только что добавленную секцию:
        $permissionList['your_mod_perm3'] = [false, 'your_mod_section'];

        // Перечисленные в массиве $leftPermissionGroups группы разрешений отображаются всегда в левой колонке (при классическом виде раздела прав доступа):
        $leftPermissionGroups[] = 'your_mod_section';

        // Можно сделать так, что если какая-то опция выключена, некоторые права доступа не будут видны:
        if (empty($modSettings['your_mod_option_enabled'])) {
            $hiddenPermissions[] = 'your_mod_perm1';
            $hiddenPermissions[] = 'your_mod_perm2';
            $hiddenPermissions[] = 'your_mod_perm3';
        }

        // Также можно сделать, что в зависимости от включенных параметров мода некоторые права доступа будут называться иначе:
        if ($modSettings['your_mod_options'] == 1) {
            $relabelPermissions['your_mod_perm1'] = 'new_name1';
            $relabelPermissions['your_mod_perm2'] = 'new_name2';
        } elseif ($modSettings['your_mod_options'] == 2) {
            $relabelPermissions['your_mod_perm1'] = 'new_name3';
        }
    }
}
```

Не забываем подключить языковой файл с переводом добавляемых прав доступа:

```php
<?php

// Заголовок секции
$txt['permissiongroup_your_mod_section'] = 'Название вашего мода';

// Заголовок секции при простом виде отображения (в SMF 2.0.x)
$txt['permissiongroup_simple_your_mod_section'] = 'Название вашего мода';

// Названия прав доступа
$txt['permissionname_your_mod_section_perm1'] = 'Название разрешения 1';
$txt['permissionname_your_mod_section_perm2'] = 'Название разрешения 2';

// Названия прав доступа (используются в Генераторе отчётов)
$txt['group_perms_name_your_mod_section_perm1'] = 'Название разрешения 1';
$txt['group_perms_name_your_mod_section_perm2'] = 'Название разрешения 2';

// Если используется разрешение с раздельной настройкой:
$txt['permissionname_your_mod_section_perm3_own'] = 'Разрешение 3 - для своих элементов (например, «Редактирование своей подписи»)';
$txt['permissionname_your_mod_section_perm3_any'] = 'Разрешение 3 - для всех элементов (например, «Редактирование любых подписей»)';
```

Хук `integrate_load_permissions` пригодится для добавления новых прав доступа, необходимых для работы вашей модификации.
