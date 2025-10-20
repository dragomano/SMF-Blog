---
title: Отображение элементов галереи
description: Выводим элементы галереи в отдельных блоках на форуме.
date: 2010-01-27
slug: otbrazhenie-elementov-galerei
authors: [bugo]
tags: [галерея, блоки]
categories: [lessons]
---

В этой статье рассматривается вывод элементов галереи [Aeva Media](/translations/aeva-media) (изображений и видео) в произвольных областях форума.

<!-- more -->

При работе с вашим порталом создайте новый PHP-блок и вставьте туда следующий код:

```php
<?php

function show_aeva_media_block()
{
    global $sourcedir;

    // Set amount visible
    $visible = 5;

    // Load the language file
    loadLanguage('Aeva');

    // Grab the file.
    if (file_exists($sourcedir . '/Aeva-Subs.php')) {
        require_once($sourcedir . '/Aeva-Subs.php');
    } else {
        echo '<b>You don\'t have Aeva installed! Unable to continue!</b>';
        return;
    }

    // Use aeva functions to show the media.
    $images = aeva_listItems(aeva_getMediaItems(0, $visible, 'RAND()'), true, '', 0);

    echo '
        <div id="aeva_pics" style="width: 100%; overflow: visible;">
            <div align="center">', $images, '</div>
        </div>';
}

show_aeva_media_block();
```

Строчка `$visible = 5;` здесь отвечает за количество показываемых элементов.

Либо используйте второй вариант:

```php
<?php

global $sourcedir;

loadLanguage('Aeva');

require_once($sourcedir . '/Aeva-Subs.php');

echo '
    <div id="aeva_pics" style="width: 100%; overflow: visible;">
        <div align="center">', aeva_listItems(aeva_getMediaItems(0, 5, 'RAND()'), true, '', 0), '</div>
    </div>';
```

Цифра «5» в предпоследней строчке отвечает за количество выводимых элементов.

А с помощью этого кода элементы галереи разместятся в столбик (в левом или в правом блоках портала):

```php
<?php

function show_aeva_media_block()
{
    global $sourcedir;

    // Load the language file
    loadLanguage('Aeva');

    // Grab the file.
    if (file_exists($sourcedir . '/Aeva-Subs.php')) {
        require_once($sourcedir . '/Aeva-Subs.php');
    } else {
        echo '<b>You don\'t have Aeva installed! Unable to continue!</b>';
        return;
    }

    // Use aeva functions to show the media.
    echo aeva_listItems(aeva_getMediaItems(0, 6, 'RAND()'), false, '', 1);
}

// Run the function.;
show_aeva_media_block();
```
