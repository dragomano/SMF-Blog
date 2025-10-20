---
title: Jouele 4 SMF
long_title: Jouele 4 SMF - простой и красивый плеер
description: Добавляем на форум SMF очень простой и красивый jQuery проигрыватель.
date: 2016-07-24
authors: [bugo]
tags: [SMF 2.1, плеер, аудио]
categories: [mods]
related:
  - translations/simple-audio-video-embedder
  - reviews/video-embed
  - reviews/soundcloud-embed-widget
  - mods/play-media-attachments
---

Добавляем на форум SMF простой и красивый jQuery проигрыватель аудио файлов.

<!-- more -->

{{ img('Пример плейлиста Jouele', 'jouele_4_smf.png') }}

## Особенности

- Интеграция плеера [Jouele](https://ilyabirman.ru/jouele/) в SMF.
- Из доступных настроек только смена темы оформления — светлая или тёмная, подбирайте на вкус.
- Кнопочки для вставки новых тегов: `[audio]` и `[plaudio]`, в редакторе сообщений.
- Проигрыватель подхватывает и одиночные аудиозаписи, и плейлисты.
- Нажимая пробел на странице с треком, можно включать и выключать воспроизведение.
- После начала воспроизведения в правой части полоски индикатора появляется длина записи.

## Как использовать

Вставка ссылки на аудио-файл:

```bbcode
[audio]ссылка на файл[/audio]
[audio link=ссылка на файл]Название трека[/audio]
```

Указание длины записи вручную:

```bbcode
[audio length=мин:сек]ссылка на файл[/audio]
[audio link=ссылка на файл length=мин:сек]Название трека[/audio]
```

Плейлист:

```bbcode
[plaudio]Название плейлиста
[audio link=ссылка на файл]Название трека[/audio]
[audio link=ссылка на файл]Название трека[/audio]
[audio link=ссылка на файл]Название трека[/audio]
[/plaudio]
```

{{ download('https://drive.proton.me/urls/WWJ7Y6P37C#uW2osM0rCZTI') }}
