---
title: Хук integrate_permissions_list
description: Описание и пример использования хука integrate_permissions_list в SMF.
date: 2024-01-25
tags: [хуки, права, permissions]
---

Хук `integrate_permissions_list` — это новый хук в SMF 3.0, предлагаемый на замену сразу двум предыдущим хукам: `integrate_load_permissions` и `integrate_load_illegal_guest_permissions`, используемым до SMF 3.0.

<!-- more -->

## Расположение

=== "SMF 2.x"

    Хук доступен только в SMF 3.0 и выше. В SMF 2.x используйте [integrate_load_permissions](/hooks/integrate-load-permissions).

=== "SMF 3.0"

    `Sources/Permissions/Permission.php`

    ```php
    <?php

    IntegrationHook::call('integrate_permissions_list', [&self::$permissions]);
    ```

Хук принимает в качестве единственного параметра массив `$permissions`, через изменение которого можно добавить необходимые разрешения для вашего мода.

## Назначение

Хук позволяет добавлять новые права доступа в систему разрешений SMF 3.0. Он заменяет старые хуки, предоставляя более унифицированный и мощный способ управления разрешениями.

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
        add_integration_function('integrate_permissions_list', self::class . '::permissionsList#', false, __FILE__);
    }

    public function permissionsList(array &$permissions): void
    {
        // В языковом файле должна быть строка $txt['permissionname_your_permission']

        // Добавление вашего разрешения в группу «Общие»
        $permissions['your_permission'] = [
            'view_group' => 'general',
            'scope' => 'global',
            // Добавляем `'never_guests' => true`, чтобы разрешение было недоступно гостям
            'never_guests' => true
        ];
    }
}
```

### Расширенный пример

До появления этого хука нужно было использовать хуки `integrate_load_permissions` и `integrate_load_illegal_guest_permissions`. Как-то так:

```php
<?php

final class Integration
{
    // Подключение хуков
    public function hooks(): void
    {
        add_integration_function('integrate_load_illegal_guest_permissions', self::class . '::loadIllegalGuestPermissions#', false, __FILE__);
        add_integration_function('integrate_load_permissions', self::class . '::loadPermissions#', false, __FILE__);
    }

    // Указываем разрешения, которые не должны быть доступны гостям
    public function loadIllegalGuestPermissions(): void
    {
        global $context;

        $context['non_guest_permissions'] = array_merge(
            $context['non_guest_permissions'],
            [
                'light_portal_manage_pages_own',
                'light_portal_manage_pages_any',
                'light_portal_manage_pages',
                'light_portal_approve_pages',
            ]
        );
    }

    // Добавляем разрешения в левый столбец в разделе с названием «Light Portal»
    public function loadPermissions(array &$permissionGroups, array &$permissionList, array &$leftPermissionGroups): void
    {
        global $txt;

        $txt['permissiongroup_light_portal'] = LP_NAME;

        $permissionList['membergroup']['light_portal_view']          = [false, 'light_portal'];
        $permissionList['membergroup']['light_portal_manage_pages']  = [true, 'light_portal'];
        $permissionList['membergroup']['light_portal_approve_pages'] = [false, 'light_portal'];

        $permissionGroups['membergroup'][] = $leftPermissionGroups[] = 'light_portal';
    }
}
```

{{ img("Пример секций в правах доступа, добавленной через этот хук", "integrate_permissions_list.png") }}

А вот как выглядит замена всего этого в SMF 3.0:

```php
<?php

use SMF\Actions\Admin\Permissions;

final class Integration
{
    // Подключение хука
    public function hooks(): void
    {
        add_integration_function('integrate_permissions_list', self::class . '::permissionsList#', false, __FILE__);
    }

    // Реализация разрешений
    public function permissionsList(array &$permissions): void
    {
        // Заголовок группы
        Lang::$txt['permissiongroup_light_portal'] = LP_NAME;

        // Объявляем отдельную группу разрешений
        Permissions::$permission_groups['global'][] = 'light_portal';

        // Помещаем её в левый столбец
        Permissions::$left_permission_groups[] = 'light_portal';

        // Просмотр элементов портала, можно настроить для всех
        $permissions['light_portal_view'] = [
            'view_group' => 'light_portal',
            'scope' => 'global',
        ];

        // Дальнейшие разрешения недоступны гостям (`'never_guests' => true`)

        // Управление собственными страницами
        $permissions['light_portal_manage_pages_own'] = [
            'generic_name' => 'light_portal_manage_pages',
            'own_any' => 'own',
            'view_group' => 'light_portal',
            'scope' => 'global',
            'never_guests' => true,
        ];

        // Управление любыми страницами
        $permissions['light_portal_manage_pages_any'] = [
            'generic_name' => 'light_portal_manage_pages',
            'own_any' => 'any',
            'view_group' => 'light_portal',
            'scope' => 'global',
            'never_guests' => true,
        ];

        // Публикация страниц без модерации
        $permissions['light_portal_approve_pages'] = [
            'view_group' => 'light_portal',
            'scope' => 'global',
            'never_guests' => true,
        ];
    }
}
```

Как видите, реализация прав доступа через хук `integrate_permissions_list` выглядит объёмной, зато всё можно сделать в одном хуке. Однако вы по-прежнему можете пользоваться прежними хуками, если этот вас пугает. Но в одной из следующих версий (после SMF 3.0) они будут удалены.
