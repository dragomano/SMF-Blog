---
title: Highlight Search Keywords
long_title: Highlight Search Keywords - подсветка ключевых слов
description: Как сделать подсветку ключевых слов при поиске на форуме.
date: 2010-01-18
tags: [SMF 2.0, подсветка, поиск]
categories: [translations]
---

Модификация добавляет подсветку ключевых слов при поиске.

<!-- more -->

{{ img('Ключевые слова подсвечиваются', 'highlight_search.png') }}

{{ settings('Форум → Поиск → Подсветка ключевых слов.') }}

## Особенности

* Возможность установить свой цвет для неограниченного количества ключевых слов.

{{ download('https://custom.simplemachines.org/index.php?mod=1259') }}

??? Русификация

    Добавить в файл `Themes/default/languages/Modifications.russian-utf8.php`:

    ```php
    // Highlight Search Keywords Mod Text
    $txt['HighlightSearchKeywords_tab_heading'] = 'Подсветка ключевых слов';
    $txt['HighlightSearchKeywords_color'] = 'Цвет в 16-ричной системе';
    $txt['HighlightSearchKeywords_heading'] = '<strong>Назначенные цвета для ключевых слов:</strong>';
    $txt['HighlightSearchKeywords_explanation'] = 'Цвета должны иметь длину в 6 символов, без пробелов, с использованием <a href="http://en.wikipedia.org/wiki/Web_colors">цветовых кодов RGB Hexadecimal Web</a>.';
    $txt['HighlightSearchKeywords_save_button'] = 'Сохранить и добавить новый';
    // Highlight Search Keywords Mod Text END
    ```
