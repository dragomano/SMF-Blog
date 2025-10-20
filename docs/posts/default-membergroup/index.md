---
title: Default Membergroup
long_title: Default Membergroup - группа по умолчанию
description: Как назначить определенную группу пользователю сразу после регистрации.
date: 2009-12-12
tags: [SMF 2.0, SMF 2.1, группы, пользователи, регистрация]
categories: [translations]
---

Возможность указания идентификатора группы по умолчанию в настройках регистрации форума, чтобы все новые участники автоматически зачислялись в эту группу.

<!-- more -->

{{ settings('Регистрация → Настройки.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=1804') }}
{{ download('https://custom.simplemachines.org/index.php?mod=4271') }}

??? Русификация

    === "SMF 2.0"

        Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

        ```php
        <?php

        // Start Default membergroup by Nas
        $txt['default_group'] = 'Группа по умолчанию <div class="smalltext">ID группы, в которую будут входить все новые пользователи после регистрации.</div>';
        // End Default membergroup by Nas
        ```

    === "SMF 2.1"

        Добавить в файл `Themes/default/languages/Modifications.russian.php`:

        ```php
        <?php

        // Start Default membergroup
        $txt['default_groupindex'] = 'Группа по умолчанию <div class="smalltext">ID группы, в которую будут входить все новые пользователи после регистрации.</div>';
        // End Default membergroup
        ```
