---
title: Play Media Attachments
long_title: Play Media Attachments - слушаем медиа файлы во вложениях
description: Слушаем аудио и видео файлы, прикреплённые к сообщениям, не скачивая на компьютер.
date: 2017-03-06
tags: [аудио, видео, вложения, сообщения, SMF 2.0, SMF 2.1]
categories: [translations]
related:
  - translations/simple-audio-video-embedder
  - reviews/video-embed
  - reviews/soundcloud-embed-widget
  - mods/jouele-4-smf
---

Чтобы каждый раз не скачивать файл, который захотелось прослушать или посмотреть, воспользуйтесь этой модификацией.

<!-- more -->

{{ img('Вот как это выглядит', 'play_media_attachments.png') }}

Медиа вложения будут преобразованы в аудио или видео проигрыватель.

## Поддерживаемые расширения

- mp3
- wav
- ogg
- oga
- mp4
- ogv
- webm

{{ download('https://custom.simplemachines.org/index.php?mod=4131') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (для SMF 2.0) или в `Themes/default/languages/Modifications.russian.php` (для SMF 2.1):

    ```php
    <?php

    // Play Media Attachments
    $txt['PMA_no_audio'] = 'Ваш браузер не поддерживает HTML элемент <strong>audio</strong>.';
    $txt['PMA_no_video'] = 'Ваш браузер не поддерживает HTML элемент <strong>video</strong>.';
    $txt['attachmentAudioPlayerWidth'] = 'Ширина аудио плеера <div class="smalltext">ПРИМЕЧАНИЕ: установите <strong>0</strong> для использования стандартных настроек браузера</div>';
    $txt['attachmentVideoPlayerWidth'] = 'Ширина видео плеера <div class="smalltext">ПРИМЕЧАНИЕ: установите <strong>0</strong> для использования стандартных настроек браузера</div>';
    $txt['attachment_redetect_mime'] = 'Перепроверка MIME-типов';
    $txt['attachment_redetect_mime_desc'] = 'Эта функция повторно проверит MIME-типы всех файлов, сохраненных в директории вложений.';
    ```
