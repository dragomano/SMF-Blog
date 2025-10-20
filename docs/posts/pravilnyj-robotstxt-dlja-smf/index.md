---
title: Правильный robots.txt для SMF
description: Настраиваем robots.txt для индексации форума SMF. Как составить файл robots.txt для форума на движке SMF?
date: 2011-09-03
slug: pravilnyj-robotstxt-dlja-smf
authors: [bugo]
categories: [articles]
---

Попробуем создать файл `robots.txt` для только что установленного и настроенного форума, без учёта дополнительных SEO-модов типа Pretty URLs и прочих.

<!-- more -->

{{ warning('На самом деле правильного варианта не существует, всё зависит от конфигурации форума и ваших требований.', 'Предупреждение') }}

```ini
User-agent: *
Disallow: /*action #Адреса типа /index.php?action=
Disallow: /*topic=*.msg #Адреса типа /index.php?topic=49.msg209#new
Disallow: /*topic=*.new
Disallow: /*; #Адреса типа /index.php?board=1.0;sort=views
Disallow: /*PHPSESSID #Адреса с параметром PHPSESSID
Allow: /$ #Индексация главной страницы форума
Allow: /*board #Индексация всех разделов
Allow: /*topic #Индексация всех тем
```

Если требуется разрешить индексацию не только первых страниц тем и разделов, но и индексацию остальных страниц, используйте универсальный блок правил (см. ниже), для роботов.

## Редирект

Не забудьте настроить в **.htaccess** переадресацию адресов с `www` на адреса без `www` (если необходимо).

А так настраивается редирект с `/index.php` на `/`:

```apache
RewriteEngine On
RewriteCond %{REQUEST_URI} ^\/index.php$
RewriteCond %{QUERY_STRING} ^$
RewriteRule ^(.*)$ / [L,R=301]
```

## Поддержка других модов

При установке мода [Sitemap](/translations/sitemap) и включении новостей XML\RSS в админке набор правил не меняется, но добавляется пара строчек:

```ini
User-agent: *
Disallow: /*action
Disallow: /*topic=*.msg
Disallow: /*topic=*.new
Disallow: /*;
Disallow: /*PHPSESSID
Allow: /$
Allow: /*board
Allow: /*topic
Allow: /*action=.xml #Разрешаем индексацию ленты новостей
Allow: /*sitemap #Разрешаем индексацию карты

Sitemap: https://dragomano.ru/sitemap.xml #Полный URL к карте сайта
```

Если ещё поставили [Aeva Media](/translations/aeva-media) или какой-нибудь портал, правила опять дорабатываются:

```ini
User-agent: *
Disallow: /*action
Disallow: /*topic=*.msg
Disallow: /*topic=*.new
Disallow: /*;
Disallow: /*PHPSESSID
Allow: /$
Allow: /*board
Allow: /*topic
Allow: /*forum$ #Индексация главной страницы форума
Allow: /*page*page #Индексация страниц портала
Allow: /*media$ #Индексация главной страницы галереи
Allow: /*media*item #Индексация элементов галереи
Allow: /*media*album #Индексация альбомов галереи
Allow: /*action=.xml
Allow: /*sitemap

Sitemap: https://dragomano.ru/sitemap.xml #Полный URL к карте сайта
```

Заметьте: если у вас форум в поддиректории, то к слэшам в путях добавляется название директории (например: `Disallow: /forum` вместо `Disallow: /`).

Остальные страницы, для которых не описаны правила, не попадут в индекс благодаря тегу **canonical**, который поддерживается популярными поисковиками.

Модификация, которая поможет автоматизировать описанный выше процесс — [Optimus](/mods/optimus). Пользуйтесь.

## Нейросети

Если вы не хотите, чтобы страницы вашего форума использовали в качестве источника ответов сервиса [Нейро от Яндекса](https://webmaster.yandex.ru/blog/yandeks-zapustil-neyro-kak-on-rabotaet), добавьте в `robots.txt` следующие строчки:

```ini
User-Agent: YandexAdditional
Disallow: /
```

Также есть [директива `Content-Signal`](https://contentsignals.org), с помощью которой можно отдельно запретить или разрешить обучение моделей, поиск по вашему сайту и ввод данных с помощью ИИ:

```ini
User-Agent: *
Content-Signal: ai-train=no, search=yes, ai-input=no
Allow: /
```

## Полезные ресурсы

* [SMF Bot Hygiene](https://github.com/sbulen/SMF-bot-hygiene) — примеры `robots.txt` и `.htaccess` для SMF
