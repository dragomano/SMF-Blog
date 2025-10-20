---
title: Topic Solved
long_title: Topic Solved - помечаем тему раскрытой
description: Как отметить тему форума полностью раскрытой. Модификация для SMF.
date: 2010-09-11
tags: [вопросы, ответы, разделы, сообщения, темы, SMF 2.0]
categories: [translations]
---

Интересный мод, направленный на создание разделов-вопросников, в которых пользователи могут помечать темы раскрытыми/решенными.

<!-- more -->

{{ img('Кнопка, добавляемая модом на страницы тем', 'topic_solved_message.png') }}

## Особенности

* После установки мода требуется включить соответствующую функцию в свойствах нужного раздела.
* В правах доступа для групп отметьте, кто может помечать темы раскрытыми/не раскрытыми, свои или любые.

{{ download('https://custom.simplemachines.org/index.php?mod=1601') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    <?php

    // Topic Solved
    $txt['topic_solved'] = 'Тема раскрыта';
    $txt['topic_not_solved'] = 'Тема не раскрыта';
    $txt['topic_solved_quick'] = 'Отметить выделенные как решенные';
    $txt['topic_solved_quick_confirm'] = 'Вы действительно хотите пометить выделенные темы как решенные?';
    $txt['topic_solved_board'] = 'Раздел тем-вопросов';
    $txt['topic_solved_board_desc'] = 'Включение для данного раздела функции "Тема раскрыта/не раскрыта"';
    $txt['topic_solved_log'] = 'Логи решенных тем';
    $txt['topic_solved_no_log'] = 'Записей не найдено.';
    $txt['topic_solved_desc'] = 'Список действий, выполненных модераторами форума.';
    $txt['modlog_topicsolved_log_desc'] = 'Ниже перечислены все действия модераторов форума в разделах с функцией "Тема раскрыта/не раскрыта".<br><b>Обратите внимание:</b> Записи не могут быть удалены из списка логов, пока не пройдет 24 часа.';
    $txt['modlog_ac_solve'] = 'Тема "{topic}" раскрыта';
    $txt['modlog_ac_not_solve'] = 'Тема "{topic}" помечена как нерешенная';
    $txt['permissionname_solve_topic'] = 'Пометка тем раскрытыми/не раскрытыми';
    $txt['permissionhelp_solve_topic'] = 'Это разрешение позволяет пользователям отмечать выбранные темы раскрытыми (решенными).';
    $txt['permissionname_solve_topic_own'] = 'Собственных тем';
    $txt['permissionname_solve_topic_any'] = 'Любых тем';
    $txt['permissionname_simple_solve_topic_own'] = 'Пометка собственных тем раскрытыми';
    $txt['permissionname_simple_solve_topic_any'] = 'Пометка любых тем раскрытыми/не раскрытыми';
    $txt['topic_solved_error_no_board'] = 'Извините, но в этом разделе данная функция отключена.';
    $txt['cannot_support_tools_solve_topic_own'] = 'Вы не можете отмечать свои темы раскрытыми.';
    $txt['cannot_support_tools_solve_topic_any'] = 'Вы не можете отмечать темы раскрытыми.';
    ```
