---
title: Contact Page
long_title: Contact Page - страница контактов
description: Добавляем страницу для связи с администрацией на форуме SMF.
date: 2010-01-12
tags: [SMF 2.0, SMF 2.1, контакты, связь]
categories: [translations]
---

Страница контактов (форма для связи с администрацией форума) для SMF.

<!-- more -->

## Особенности

* Отдельный пункт в меню («**Контакты**»).
* Возможность настроить шаблон оформления страницы контактов по собственному вкусу.

{{ download('https://custom.simplemachines.org/index.php?mod=377') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php` (для SMF 2.0) или в `Themes/default/languages/Modifications.russian.php` (для SMF 2.1):

    ```php
    // Contact Page
    $txt['smfcontact_contact'] = 'Контакты';
    $txt['permissionname_view_contact'] = 'Просмотр страницы контактов';
    $txt['permissionhelp_view_contact'] = 'Разрешить пользователям просматривать страницу контактов и отправлять письма.';
    $txt['cannot_view_contact'] = 'Вы не можете просматривать страницу контактов.';
    $txt['smfcontact_name'] = 'Имя (или ник):';
    $txt['smfcontact_subject'] = 'Тема сообщения:';
    $txt['smfcontact_body'] = 'Текст сообщения:';
    $txt['smfcontact_emailaddress'] = 'Имейл:';
    $txt['smfcontact_sendemail'] = 'Отправить';
    $txt['smfcontact_messagesent'] = 'Письмо успешно отправлено!';
    $txt['smfcontact_messagesent_click'] = 'Письмо отправлено! Нажмите ';
    $txt['smfcontact_messagesent_return'] = 'здесь для возвращения на форум.';
    $txt['smfcontact_errname'] = 'Надо указать имя (или ник).';
    $txt['smfcontact_errsubject'] = 'Укажите тему сообщения.';
    $txt['smfcontact_errmessage'] = 'А текст за вас бабушка писать будет?';
    $txt['smfcontact_erremail'] = 'Укажите свой имейл. Мало ли, вдруг вам захотят ответить.';
    $txt['smfcontact_titlesent'] = ' - Сообщение отправлено';
    $txt['smfcontact_form'] = 'Страница контактов форума ';
    $txt['smfcontact_formname'] = "Имя (ник): ";
    $txt['smfcontact_formemail'] = "Имейл: ";
    $txt['smfcontact_ip'] = "IP: ";
    $txt['smfcontact_formmessage'] =  "Сообщение: \n\n";
    ```
