---
title: Как подключать хуки
description: В статье раскрываются различные способы подключения хуков в SMF.
date: 2019-09-26
slug: kak-podklyuchat-huki
authors: [bugo]
tags: [хуки, модификации]
categories: [lessons]
---

Данный материал является вспомогательным для раздела [Список хуков](/hooks). Здесь рассмотрены оптимальные варианты подключения и вызова хуков в модификациях для SMF.

<!-- more -->

## Основы

Когда вы используете хуки в своих модификациях, их требуется либо добавлять в базу данных при установке, либо вызывать при запуске вашего приложения.

В SMF 2.1 появилась возможность указывать используемые хуки непосредственно в _package-info.xml_:

```xml
<install for="2.1.*">
    <require-file name="Class-YourModName.php" destination="$sourcedir">Core file</require-file>
    <hook hook="integrate_pre_load" function="YourModName::hooks#" file="$sourcedir/Class-YourModName.php" />
</install>

<uninstall for="2.1.*">
    <hook hook="integrate_pre_load" function="YourModName::hooks#" file="$sourcedir/Class-YourModName.php" reverse="true" />
    <remove-file name="$sourcedir/Class-YourModName.php">OK</remove-file>
</uninstall>
```

{{ note('Символ решётки (`#`) указывает на использование нестатического метода класса. Хотите работать со статическими методами — убирайте решётку.') }}

Название файла — `Class-YourModName.php` — выбираете сами, в зависимости от названия мода.

```php
<?php

class YourModName
{
    public function hooks(): void
    {
        // Обратите внимание на решётку после названия метода
        add_integration_function('НАЗВАНИЕ_ХУКА', self::class . '::НАЗВАНИЕ_МЕТОДА#', false);
    }

    public function НАЗВАНИЕ_МЕТОДА(/* параметры, если есть */)
    {
        // Ваш код
    }
}
```

Скачивайте шаблон для создания модификаций, меняйте код на свое усмотрение, творите.

{{ download('https://drive.proton.me/urls/F2PK4ZA7FM#d9Wa1kyjBoa4', 'Шаблон модификации для SMF 2.1') }}
