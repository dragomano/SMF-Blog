---
title: Меняем иконки разделов
description: Как изменить иконки разделов на форуме SMF?
date: 2022-05-01
slug: menyaem-ikonki-razdelov
authors: [bugo]
tags: [иконки, разделы, CSS]
categories: [lessons]
---

Учимся ставить свои иконки для разделов, вместо стандартных. Движок — SMF 2.1.

<!-- more -->

## Как это работает

По умолчанию все варианты иконок разделов хранятся в файле `Themes/default/images/boardicons.png`. Этот файл представляет собой спрайт, с 4 различными состояниями. В `Themes/default/css/index.css` есть код, отвечающий за применение этого спрайта:

```css
.board_icon a {
    background: url(../images/boardicons.png) no-repeat 0 0 / 90px;
    display: inline-block;
    width: 45px;
    height: 45px;
}

.board_icon a.board_on2 {
    background-position: -45px 0;
}

.board_icon a.board_off {
    background-position: 0 -45px;
}

.board_icon a.board_redirect {
    background-position: -45px -45px;
}
```

В нестандартной теме оформления этот код может выглядеть иначе, как и сами иконки могут быть другими. Самый простой вариант замены иконок, который будет работать для всех установленных тем оформления — использовать мод [FA Board Icons](/reviews/fa-board-icons).

## Вариант первый — замена всех иконок

Если же вам не нравятся иконки Font Awesome и хочется использовать свои собственные изображения, измените код выше на этот (размер иконки `45x45` можно заменить на свой):

```css
.board_icon a {
    background: none;
    width: 45px;
    height: 45px;
}
```

и добавьте это правило для каждого раздела, для которого у вас есть иконка:

```css
#board_1 .board_icon a {
    background: url(../images/board_icons/1.png) no-repeat;
    background-size: cover;
}
```

Обратите внимание, что вместо `#board_1` и `1.png` нужно указать свои значения. В данном случае единичка — это идентификатор первого раздела. То есть в конечном итоге ваш вариант будет выглядеть как-то так:

```css
#board_1 .board_icon a {
    background: url(../images/board_icons/1.png) no-repeat;
    background-size: cover;
}

#board_2 .board_icon a {
    background: url(../images/board_icons/2.png) no-repeat;
    background-size: cover;
}

#board_3 .board_icon a {
    background: url(../images/board_icons/3.png) no-repeat;
    background-size: cover;
}

/* и так далее */
```

Соответственно, сами иконки нужно загрузить по адресу `Themes/default/images/board_icons`.

Также можно добавить отдельные эффекты для иконок, когда в разделе нет непрочитанных сообщений, и когда они есть:

```css
.board_icon a.board_off {
    /* новых сообщений нет */
}

.board_icon a.board_on {
    /* есть новые сообщения */
}

.board_icon a.board_on2 {
    /* есть новые сообщения в подразделе */
}

.board_icon a.board_redirect {
    /* раздел-перенаправление */
}
```

{{ img('Вкусные иконки', 'boards_with_custom_icons.png') }}

## Вариант второй — замена только некоторых иконок

Если вы хотите заменить только некоторые иконки, оставив для остальных разделов иконки по умолчанию, просто добавьте CSS-стили для выбранных разделов, не внося остальные правки, указанные в первом варианте:

```css
#board_1 .board_icon a {
    background: url(../images/board_icons/1.png) no-repeat;
    background-size: cover;
}

#board_2 .board_icon a {
    background: url(../images/board_icons/2.png) no-repeat;
    background-size: cover;
}

#board_3 .board_icon a {
    background: url(../images/board_icons/3.png) no-repeat;
    background-size: cover;
}

/* и так далее */
```

## На десерт

В качестве бонуса — [готовые варианты иконок](https://www.simplemachines.org/community/index.php?topic=581196.0), в нескольких цветовых вариациях. Лайкните автора, скачайте архив, приложенный к сообщению (потребуется регистрация), выберите желаемый `boardicons.png` и замените им свой, стандартный.

{{ img('Иконки на любой вкус', 'board_variants.png') }}
