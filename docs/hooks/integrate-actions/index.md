---
title: Хук integrate_actions
description: Описание и пример использования хука integrate_actions в SMF.
date: 2019-04-09
tags: [экшены, actions, хуки]
---

Хук `integrate_actions` позволяет разработчикам модов добавлять собственные экшены (_actions_) в движок форума без необходимости редактирования ядра SMF.

## Расположение

=== "SMF 2.x"

    `index.php` (в корне форума)

    ```php
    <?php

    call_integration_hook('integrate_actions', [&$actionArray]);
    ```

=== "SMF 3.0"

    `Sources/Forum.php`

    ```php
    <?php

    IntegrationHook::call('integrate_actions', [&self::$actions]);
    ```

Хук принимает в качестве параметра массив, в котором содержится список экшенов, перехватываемых переменной `$_REQUEST['action']`. Например, запись `$actionArray['calendar'] = ['Calendar.php', 'CalendarMain']` означает, что при переходе по адресу `/index.php?action=calendar` происходит вызов функции _CalendarMain_ из файла _Calendar.php_.

## Назначение

В SMF весь пользовательский интерфейс построен на работе с экшенами. Экшен — это конкретная операция или страница, которая вызывается через параметр `?action=something` в URL.

Примеры стандартных экшенов в SMF: _login_, _register_, _profile_, _pm_, _admin_ и многие другие.

Хук `integrate_actions` нужен, чтобы сообщить движку о существовании вашего нового, кастомного экешна. Вы «регистрируете» его в системе.

Без этого хука, если вы просто создадите файл и попытаетесь перейти по ссылке `?action=my_action`, SMF выдаст ошибку `Unknown action`, потому что он не зарегистрирован в списке допустимых экшен движка.

## Использование

[Как подключать хуки](/lessons/kak-podklyuchat-huki)

```php
<?php

if (! defined('SMF'))
	die('No direct access...');

class YourModName
{
	// В этой функции подключаем используемые хуки
	public function hooks(): void
	{
		add_integration_function('integrate_actions', self::class . '::actions#', false, __FILE__);
	}

	// Регистрируем собственный экшен
	public function actions(array &$actions): void
	{
		// Подключаем метод из этого же класса
		$actions['my_page'] = [false, [$this, 'myPageAction']];

		// Альтернативный синтаксис, в котором указываем файл в директории Sources
		// и функцию, которая должна вызываться
		// $actions['my_page'] = ['YourModName.php', 'myFunction'];
	}

	// Эта функция вызывается при переходе по адресу /index.php?action=my_page
	public function myPageAction(): void
	{
		// Здесь можно подключить свой шаблон и выполнить любые другие действия
		print_r('Моя страница');
	}
}
```

Хук `integrate_actions` — это важный инструмент для расширения функционала SMF. Он является мостом, который соединяет ваши кастомные страницы (экшены) с маршрутизацией движка. Без него система просто не узнает о существовании вашего `?action=something` и не поймет, какой код нужно выполнить.
