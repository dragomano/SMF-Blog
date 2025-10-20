---
title: Delete Unactivated Members
long_title: Delete Unactivated Members - удаление неактивных учётных записей
description: Как настроить автоматическое удаление неактивированных учётных записей на форуме SMF?
date: 2017-11-28
tags: [SMF 2.0, SMF 2.1, пользователи, аккаунт, диспетчер]
categories: [translations]
---

Модификация помогает настроить автоматическое удаление неактивированных учётных записей по истечении заданного интервала.

<!-- more -->

{{ settings('Пользователи → Регистрация → Настройки.') }}

## Особенности

* По указанному выше пути добавляются два новых параметра:
  * Дней перед удалением неактивированных учётных записей
  * Уведомлять пользователей, чьи учетные записи удаляются
* Укажите количество дней, по истечении которых будет запускаться удаление неактивных аккаунтов.
* Дополнительно, в _Диспетчере задач_ появляется соответствующая задача, с настройкой запуска в заданное время.

{{ download('https://custom.simplemachines.org/index.php?mod=4163') }}

??? Русификация

    === "SMF 2.0"

        Добавить в файл `Admin.russian-utf8.php`:

        ```php
        <?php

        // Delete Unactivated Members
        $txt['DUMD_days'] = 'Дней перед удалением неактивированных учётных записей:<div class="smalltext">ПРИМЕЧАНИЕ: Используйте <strong>0</strong> для отключения.</div>';
        $txt['DUMD_notify_users'] = 'Уведомлять пользователей, чьи учетные записи удаляются?';
        ```

        Дополнительно, добавить в файл `ManageScheduledTasks.russian-utf8.php`:

        ```php
        <?php

        // Delete Unactivated Members
        $txt['scheduled_task_delete_unactivated'] = 'Удаление неактивированных учётных записей';
        $txt['scheduled_task_desc_delete_unactivated'] = !empty($modSettings['DUMD_days']) ? 'Удаляет неактивных пользователей, которые зарегистрировались больше, чем ' . $modSettings['DUMD_days']  . ' дней назад.' : '<strong>ПРИМЕЧАНИЕ:</strong> <a href="' . $boardurl . '?action=admin;area=regcenter;sa=settings">Задача отключена. Перейдите сюда, чтобы установить количество дней.</a>';
        ```

    === "SMF 2.1"

        Добавить в файл `Admin.russian.php`:

        ```php
        <?php

        // Delete Unactivated Members
        $txt['DUMD_days'] = 'Дней перед удалением неактивированных учётных записей:<div class="smalltext">ПРИМЕЧАНИЕ: Используйте <strong>0</strong> для отключения.</div>';
        $txt['DUMD_notify_users'] = 'Уведомлять пользователей, чьи учетные записи удаляются?';
        ```

        Дополнительно, добавить в файл `ManageScheduledTasks.russian.php`:

        ```php
        <?php

        // Delete Unactivated Members
        $txt['scheduled_task_delete_unactivated'] = 'Удаление неактивированных учётных записей';
        $txt['scheduled_task_desc_delete_unactivated'] = !empty($modSettings['DUMD_days']) ? 'Удаляет неактивных пользователей, которые зарегистрировались больше, чем ' . $modSettings['DUMD_days']  . ' дней назад.' : '<strong>ПРИМЕЧАНИЕ:</strong> <a href="' . $boardurl . '?action=admin;area=regcenter;sa=settings">Задача отключена. Перейдите сюда, чтобы установить количество дней.</a>';
        ```
