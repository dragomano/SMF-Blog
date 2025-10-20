---
title: Restrict Email Providers on Registration
long_title: Restrict Email Providers on Registration - запрет определенных почтовых доменов при регистрации
description: Как запретить регистрацию на форуме при указании определенных имейлов?
date: 2010-01-24
slug: restrict-email-providers
tags: [SMF 2.0, почта, регистрация]
categories: [translations]
---

Возможность ограничить использование определённых почтовых доменов при регистрации на форуме.

<!-- more -->

## Особенности

- Запрет на использование выбранных почтовых доменов.
- Разрешение на использование только указанных доменов.

{{ download('https://custom.simplemachines.org/index.php?mod=1493') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Restrict Email Providers on Registration
    $txt['restricted'] = 'К сожалению, указанный вами адрес электронной почты не может быть использован для регистрации на этом форуме.<br>Попробуйте указать какой-нибудь другой.';
    $txt['enable_restrict_EmailProvider'] = 'Включить ограничения на используемые имейлы при регистрации';
    $txt['restricted_provider'] = 'Использование каких провайдеров должно быть ограничено? <br><i> (например, для запрета на использование электронных адресов <b><font color="red">hotmail</font> и <font color="red">gmail</font></b> нужно написать так: @hotmail.com,@gmail.com)</i>';
    $txt['accepted_provider'] = 'Использование каких провайдеров допустимо? <br><i> (например, чтобы разрешить использование адресов <b><font color="red">hotmail</font> и <font color="red">gmail</font></b>, нужно написать так: @hotmail.com,@gmail.com)</i><br><font color="red"><b>Обратите внимание: либо список запрещённых адресов, либо список разрешённых — один из них должен быть пустым</b></font>';
    ```