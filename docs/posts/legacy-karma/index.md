---
title: Legacy Karma
long_title: Legacy Karma - отображение кармы в SMF 2.1
description: Как показать старую карму после обновления до SMF 2.1?
date: 2020-05-21
authors: [digger]
tags: [SMF 2.1, карма, репутация]
categories: [reviews]
related:
  - reviews/karma
  - mods/likes-aka-karma
---

Накопленную в SMF 2.0 карму можно отобразить после обновления до SMF 2.1.

<!-- more -->

Для этого при обновлении не удаляйте данные кармы, чтобы в таблице **smf_members** сохранились два поля, __karma_good__ и __karma_bad__, содержащие пользовательскую репутацию.

{{ img('Отображение старой кармы', 'legacy_karma.png') }}

## Особенности

* Мод включается в общих настройках модификаций.
* Там же можно поменять заголовок поля. По умолчанию отображается «Karma».

{{ github('https://github.com/realdigger/SMF-Legacy-Karma') }}
