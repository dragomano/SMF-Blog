---
title: Move Old Topics
long_title: Move Old Topics - перемещение старых тем
description: Как перенести заброшенные темы в определенный раздел форума?
date: 2010-12-16
authors: [live627]
tags: [обслуживание, перемещение, разделы, темы, SMF 2.0]
categories: [translations]
---

Возможность переноса тем, в которых давно не оставлялись сообщения, в определенные разделы форума.

<!-- more -->

{{ settings('Обслуживание форума → Удаление и перенос тем → Перенос старых тем.') }}

{{ download('https://custom.simplemachines.org/index.php?mod=503') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Move Old Posts
    $txt['move_maintain_old'] = 'Перенос старых тем';
    $txt['move_maintain_old_since_days1'] = 'Перенести все темы, которые не обновлялись в течение ';
    $txt['move_maintain_old_remove'] = 'Перенести';
    $txt['move_Destboard'] = 'Раздел назначения:';
    $txt['move_maintain_old_confirm'] = 'Вы действительно хотите ПЕРЕМЕСТИТЬ старые темы?';
    ```
