---
title: Anti-Spam Links
long_title: Anti-Spam Links - борьба со спамом в сообщениях
description: Избавляемся от ссылочного спама в сообщениях форума на движке SMF.
date: 2010-05-21
tags: [SMF 2.0, nofollow, гости, антиспам, ссылки]
categories: [translations]
---

Данный мод помогает бороться со ссылочным спамом в сообщениях.

<!-- more -->

{{ img('Пример обработки ссылок', 'anti-spam-links.png') }}

## Особенности

* Возможность установить лимит на количество сообщений, после достижения которого пользователи смогут публиковать внешние ссылки.
* Публикация внешних ссылок с неактивном состоянии, с соответствующей пометкой (активны только для администратора).
* Публикация внешних ссылок с автоматическим выставлением атрибута `rel="nofollow"`.
* Внутренние ссылки публикуются как обычно.
* Отдельные настройки для гостей.

{{ download('https://custom.simplemachines.org/index.php?mod=2404') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Anti-Spam Links
    global $boardurl;
    $txt['anti_spam_links'] = 'Настройки мода Anti-Spam-Links';
    $txt['error_anti_spam_links_nolinks_guest'] = 'Извините, гостям не разрешена публикация внешних ссылок.';
    $txt['error_anti_spam_links_nolinks_member'] = 'Извините, Вам не разрешена публикация внешних ссылок.';
    $txt['anti_spam_links_newbielink'] = ' ссылка новичка: ';
    $txt['anti_spam_links_nonactive'] = '[не активна]';
    $txt['anti_spam_links_newbielinks_info'] = 'Для предотвращения спама внешние ссылки показываются с пометкой [не активна] — пока пользователи не наберут %1$s сообщений';
    $txt['anti_spam_links_nofollowlinks_info'] = 'Для предотвращения спама внешние ссылки получают свойство [nofollow] (то есть при переходе по ним PR передаваться не будет) — пока пользователи не наберут %1$s сообщений';
    $txt['anti_spam_links_nofollow'] = '[nofollow]';
    $txt['anti_spam_links_nolinks'] = 'При достижении указанного кол-ва сообщений пользователи смогут публиковать внешние ссылки';
    $txt['anti_spam_links_newbielinks'] = 'При достижении указанного кол-ва сообщений внешние ссылки будут размещаться активными';
    $txt['anti_spam_links_nofollowlinks'] = 'При достижении указанного кол-ва сообщений внешние ссылки не будут иметь свойство rel="nofollow"';
    $txt['anti_spam_links_zero_disable'] = '[Исключая любые внутренние ссылки вида ' . $boardurl . ']<br>(Используйте 0 для отключения)';
    $txt['anti_spam_links_guests'] = 'Поведение мода по отношению к гостям... ';
    $txt['anti_spam_links_guests_opt0'] = '(Отключить мод для гостей)';
    $txt['anti_spam_links_guests_opt1'] = 'Гости не могут размещать ссылки';
    $txt['anti_spam_links_guests_opt2'] = 'Ссылки показываются, но не активны';
    $txt['anti_spam_links_guests_opt3'] = 'Ссылки получают свойство [nofollow]';
    ```
