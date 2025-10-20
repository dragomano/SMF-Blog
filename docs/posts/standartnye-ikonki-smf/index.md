---
title: Стандартные иконки SMF
description: Шпаргалка по использованию интерфейсных иконок SMF 2.1.
date: 2022-02-17
slug: standartnye-ikonki-smf
authors: [bugo]
tags: [иконки, интерфейс, CSS]
categories: [lessons]
---

Шпаргалка по использованию иконок интерфейса SMF 2.1.

<!-- more -->

Для вставки любой из стандартных иконок SMF 2.1 в шаблоне используется следующий код:

```html
<span class="main_icons {icon_name}"></span>
```

Но никто не запрещает использовать тег `i` вместо `span`, как принято в наборах типа Font Awesome.

Каждая иконка определяется одним или несколькими ключевыми словами, иконки и ключевые слова могут отличаться в разных темах.

| Иконка | Код для вставки |
| :-: | :- |
| <i class="main_icons help"></i> | `<i class="main_icons help"></i>` |
| <i class="main_icons search"></i> | `<i class="main_icons search"></i>` |
| <i class="main_icons engines"></i> | `<i class="main_icons engines"></i>` |
| <i class="main_icons quick_edit_button"></i> | `<i class="main_icons quick_edit_button"></i>` |
| <i class="main_icons modify_button"></i> | `<i class="main_icons modify_button"></i>` |
| <i class="main_icons check"></i> | `<i class="main_icons check"></i>` |
| <i class="main_icons invalid"></i> | `<i class="main_icons invalid"></i>` |
| <i class="main_icons gender_2"></i> | `<i class="main_icons gender_2"></i>` |
| <i class="main_icons watch"></i> | `<i class="main_icons watch"></i>` |
| <i class="main_icons move"></i> | `<i class="main_icons move"></i>` |
| <i class="main_icons next_page"></i> | `<i class="main_icons next_page"></i>` |
| <i class="main_icons general"></i> | `<i class="main_icons general"></i>` |
| <i class="main_icons topics_views"></i> | `<i class="main_icons topics_views"></i>` |
| <i class="main_icons gender_1"></i> | `<i class="main_icons gender_1"></i>` |
| <i class="main_icons features"></i> | `<i class="main_icons features"></i>` |
| <i class="main_icons posters"></i> | `<i class="main_icons posters"></i>` |
| <i class="main_icons replies"></i> | `<i class="main_icons replies"></i>` |
| <i class="main_icons topics_replies"></i> | `<i class="main_icons topics_replies"></i>` |
| <i class="main_icons history"></i> | `<i class="main_icons history"></i>` |
| <i class="main_icons scheduled"></i> | `<i class="main_icons scheduled"></i>` |
| <i class="main_icons views"></i> | `<i class="main_icons views"></i>` |
| <i class="main_icons last_post"></i> | `<i class="main_icons last_post"></i>` |
| <i class="main_icons starters"></i> | `<i class="main_icons starters"></i>` |
| <i class="main_icons mlist"></i> | `<i class="main_icons mlist"></i>` |
| <i class="main_icons poll"></i> | `<i class="main_icons poll"></i>` |
| <i class="main_icons previous_page"></i> | `<i class="main_icons previous_page"></i>` |
| <i class="main_icons inbox"></i> | `<i class="main_icons inbox"></i>` |
| <i class="main_icons www"></i> | `<i class="main_icons www"></i>` |
| <i class="main_icons exit"></i> | `<i class="main_icons exit"></i>` |
| <i class="main_icons logout"></i> | `<i class="main_icons logout"></i>` |
| <i class="main_icons switch"></i> | `<i class="main_icons switch"></i>` |
| <i class="main_icons replied"></i> | `<i class="main_icons replied"></i>` |
| <i class="main_icons send"></i> | `<i class="main_icons send"></i>` |
| <i class="main_icons im_on"></i> | `<i class="main_icons im_on"></i>` |
| <i class="main_icons im_off"></i> | `<i class="main_icons im_off"></i>` |
| <i class="main_icons split_desel"></i> | `<i class="main_icons split_desel"></i>` |
| <i class="main_icons split_sel"></i> | `<i class="main_icons split_sel"></i>` |
| <i class="main_icons mail"></i> | `<i class="main_icons mail"></i>` |
| <i class="main_icons warning_mute"></i> | `<i class="main_icons warning_mute"></i>` |
| <i class="main_icons alerts"></i> | `<i class="main_icons alerts"></i>` |
| <i class="main_icons warning_moderate"></i> | `<i class="main_icons warning_moderate"></i>` |
| <i class="main_icons mail_new"></i> | `<i class="main_icons mail_new"></i>` |
| <i class="main_icons drafts"></i> | `<i class="main_icons drafts"></i>` |
| <i class="main_icons reply_all_button"></i> | `<i class="main_icons reply_all_button"></i>` |
| <i class="main_icons warning_watch"></i> | `<i class="main_icons warning_watch"></i>` |
| <i class="main_icons calendar_export"></i> | `<i class="main_icons calendar_export"></i>` |
| <i class="main_icons calendar"></i> | `<i class="main_icons calendar"></i>` |
| <i class="main_icons calendar_modify"></i> | `<i class="main_icons calendar_modify"></i>` |
| <i class="main_icons plus"></i> | `<i class="main_icons plus"></i>` |
| <i class="main_icons warning"></i> | `<i class="main_icons warning"></i>` |
| <i class="main_icons moderate"></i> | `<i class="main_icons moderate"></i>` |
| <i class="main_icons themes"></i> | `<i class="main_icons themes"></i>` |
| <i class="main_icons support"></i> | `<i class="main_icons support"></i>` |
| <i class="main_icons liked_users"></i> | `<i class="main_icons liked_users"></i>` |
| <i class="main_icons like"></i> | `<i class="main_icons like"></i>` |
| <i class="main_icons unlike"></i> | `<i class="main_icons unlike"></i>` |
| <i class="main_icons current_theme"></i> | `<i class="main_icons current_theme"></i>` |
| <i class="main_icons stats"></i> | `<i class="main_icons stats"></i>` |
| <i class="main_icons right_arrow"></i> | `<i class="main_icons right_arrow"></i>` |
| <i class="main_icons left_arrow"></i> | `<i class="main_icons left_arrow"></i>` |
| <i class="main_icons smiley"></i> | `<i class="main_icons smiley"></i>` |
| <i class="main_icons server"></i> | `<i class="main_icons server"></i>` |
| <i class="main_icons ban"></i> | `<i class="main_icons ban"></i>` |
| <i class="main_icons ignore"></i> | `<i class="main_icons ignore"></i>` |
| <i class="main_icons boards"></i> | `<i class="main_icons boards"></i>` |
| <i class="main_icons regcenter"></i> | `<i class="main_icons regcenter"></i>` |
| <i class="main_icons posts"></i> | `<i class="main_icons posts"></i>` |
| <i class="main_icons sort_down"></i> | `<i class="main_icons sort_down"></i>` |
| <i class="main_icons change_menu2"></i> | `<i class="main_icons change_menu2"></i>` |
| <i class="main_icons sent"></i> | `<i class="main_icons sent"></i>` |
| <i class="main_icons post_moderation_moderate"></i> | `<i class="main_icons post_moderation_moderate"></i>` |
| <i class="main_icons sort_up"></i> | `<i class="main_icons sort_up"></i>` |
| <i class="main_icons post_moderation_deny"></i> | `<i class="main_icons post_moderation_deny"></i>` |
| <i class="main_icons post_moderation_attach"></i> | `<i class="main_icons post_moderation_attach"></i>` |
| <i class="main_icons post_moderation_allow"></i> | `<i class="main_icons post_moderation_allow"></i>` |
| <i class="main_icons personal_message"></i> | `<i class="main_icons personal_message"></i>` |
| <i class="main_icons permissions"></i> | `<i class="main_icons permissions"></i>` |
| <i class="main_icons signup"></i> | `<i class="main_icons signup"></i>` |
| <i class="main_icons paid"></i> | `<i class="main_icons paid"></i>` |
| <i class="main_icons packages"></i> | `<i class="main_icons packages"></i>` |
| <i class="main_icons filter"></i> | `<i class="main_icons filter"></i>` |
| <i class="main_icons change_menu"></i> | `<i class="main_icons change_menu"></i>` |
| <i class="main_icons package_ops"></i> | `<i class="main_icons package_ops"></i>` |
| <i class="main_icons reports"></i> | `<i class="main_icons reports"></i>` |
| <i class="main_icons news"></i> | `<i class="main_icons news"></i>` |
| <i class="main_icons delete"></i> | `<i class="main_icons delete"></i>` |
| <i class="main_icons remove_button"></i> | `<i class="main_icons remove_button"></i>` |
| <i class="main_icons modifications"></i> | `<i class="main_icons modifications"></i>` |
| <i class="main_icons maintain"></i> | `<i class="main_icons maintain"></i>` |
| <i class="main_icons admin"></i> | `<i class="main_icons admin"></i>` |
| <i class="main_icons administration"></i> | `<i class="main_icons administration"></i>` |
| <i class="main_icons home"></i> | `<i class="main_icons home"></i>` |
| <i class="main_icons frenemy"></i> | `<i class="main_icons frenemy"></i>` |
| <i class="main_icons attachment"></i> | `<i class="main_icons attachment"></i>` |
| <i class="main_icons lock"></i> | `<i class="main_icons lock"></i>` |
| <i class="main_icons security"></i> | `<i class="main_icons security"></i>` |
| <i class="main_icons error"></i> | `<i class="main_icons error"></i>` |
| <i class="main_icons disable"></i> | `<i class="main_icons disable"></i>` |
| <i class="main_icons languages"></i> | `<i class="main_icons languages"></i>` |
| <i class="main_icons members_request"></i> | `<i class="main_icons members_request"></i>` |
| <i class="main_icons members_delete"></i> | `<i class="main_icons members_delete"></i>` |
| <i class="main_icons members"></i> | `<i class="main_icons members"></i>` |
| <i class="main_icons members_watched"></i> | `<i class="main_icons members_watched"></i>` |
| <i class="main_icons sticky"></i> | `<i class="main_icons sticky"></i>` |
| <i class="main_icons corefeatures"></i> | `<i class="main_icons corefeatures"></i>` |
| <i class="main_icons manlabels"></i> | `<i class="main_icons manlabels"></i>` |
| <i class="main_icons logs"></i> | `<i class="main_icons logs"></i>` |
| <i class="main_icons valid"></i> | `<i class="main_icons valid"></i>` |
| <i class="main_icons approve"></i> | `<i class="main_icons approve"></i>` |
| <i class="main_icons read_button"></i> | `<i class="main_icons read_button"></i>` |
| <i class="main_icons close"></i> | `<i class="main_icons close"></i>` |
| <i class="main_icons details"></i> | `<i class="main_icons details"></i>` |
| <i class="main_icons merge"></i> | `<i class="main_icons merge"></i>` |
| <i class="main_icons folder"></i> | `<i class="main_icons folder"></i>` |
| <i class="main_icons restore_button"></i> | `<i class="main_icons restore_button"></i>` |
| <i class="main_icons split_button"></i> | `<i class="main_icons split_button"></i>` |
| <i class="main_icons unapprove_button"></i> | `<i class="main_icons unapprove_button"></i>` |
| <i class="main_icons unread_button"></i> | `<i class="main_icons unread_button"></i>` |
| <i class="main_icons quote"></i> | `<i class="main_icons quote"></i>` |
| <i class="main_icons quote_selected"></i> | `<i class="main_icons quote_selected"></i>` |
| <i class="main_icons notify_button"></i> | `<i class="main_icons notify_button"></i>` |
| <i class="main_icons select_above"></i> | `<i class="main_icons select_above"></i>` |
| <i class="main_icons select_here"></i> | `<i class="main_icons select_here"></i>` |
| <i class="main_icons select_below"></i> | `<i class="main_icons select_below"></i>` |
| <i class="main_icons profile_hd"></i> | `<i class="main_icons profile_hd"></i>` |
| <i class="main_icons config_hd"></i> | `<i class="main_icons config_hd"></i>` |
| <i class="main_icons login_hd"></i> | `<i class="main_icons login_hd"></i>` |

<style>
/* Some lovely generic icons.
------------------------------------------------- */
.main_icons::before {
    content: "";
    width: 16px;
    height: 16px;
    display: inline-block;
    background: url(/standartnye-ikonki-smf/main_icons_sprite_hd.png) no-repeat -5px -5px / 260px auto;
    vertical-align: middle;
}
.main_icons.alerts::before {
    background: url(/standartnye-ikonki-smf/bell_hd.png);
    background-size: 16px;
}
.main_icons.profile_hd::before {
    background: url(/standartnye-ikonki-smf/profile_hd.png) no-repeat;
    background-size: 16px;
}
.main_icons.config_hd::before {
    background: url(/standartnye-ikonki-smf/config_hd.png) no-repeat;
    background-size: 16px;
}
.main_icons.login_hd::before {
    background: url(/standartnye-ikonki-smf/login_hd.png) no-repeat;
    background-size: 16px;
}

@media screen and (max-width: 680px) {
    code {
        font-size: 12px !important;
    }
}

/* Top row */
.main_icons.help::before {
    background-position: -5px -5px;
}
.main_icons.search::before, .main_icons.engines::before {
    background-position: -31px -5px;
}
.main_icons.quick_edit_button::before, .main_icons.modify_button::before {
    background-position: -57px -5px;
}
.main_icons.check::before {
    background-position: -83px -5px;
}
.main_icons.invalid::before {
    background-position: -109px -5px;
}
.main_icons.gender_2::before {
    background-position: -135px -5px;
}
.main_icons.watch::before {
    background-position: -239px -5px;
}
/* 2nd row */
.main_icons.move::before, .main_icons.next_page::before {
    background-position: -5px -31px;
}
.main_icons.general::before, .main_icons.boards::before, .main_icons.topics_views::before {
    background-position: -31px -31px;
}
.main_icons.gender_1::before {
    background-position: -57px -31px;
}
.main_icons.features::before {
    background-position: -83px -31px;
}
.main_icons.posters::before {
    background-position: -109px -31px;
}
.main_icons.replies::before, .main_icons.topics_replies::before {
    background-position: -135px -31px;
}
.main_icons.history::before, .main_icons.time_online::before, .main_icons.scheduled::before {
    background-position: -161px -31px;
}
.main_icons.views::before {
    background-position: -187px -31px;
}
.main_icons.last_post::before {
    background-position: -213px -31px;
}
.main_icons.starters::before, .main_icons.people::before, .main_icons.membergroups::before, .main_icons.mlist::before {
    background-position: -239px -31px;
}
/* 3rd Street Saints */
.main_icons.poll::before {
    background-position: -5px -57px;
}
.main_icons.previous_page::before {
    background-position: -31px -57px;
}
.main_icons.inbox::before {
    background-position: -57px -57px;
}
.main_icons.www::before {
    background-position: -83px -57px;
}
.main_icons.exit::before, .main_icons.logout::before {
    background-position: -109px -57px;
}
.main_icons.switch::before {
    background-position: -135px -57px;
}
.main_icons.replied::before, .main_icons.send::before {
    background-position: -161px -57px;
}
.main_icons.im_on::before {
    background-position: -187px -57px;
}
.main_icons.im_off::before {
    background-position: -213px -57px;
}
.main_icons.split_desel::before {
    background-position: -239px -57px;
}
/* 4th Row */
.main_icons.split_sel::before {
    background-position: -5px -83px;
}
.main_icons.mail::before {
    background-position: -31px -83px;
}
.main_icons.warning_mute::before {
    background-position: -57px -83px;
}
.main_icons.warn_button::before,
.main_icons.warning_moderate::before {
    background-position: -83px -83px;
}
.main_icons.mail_new::before {
    background-position: -109px -83px;
}
.main_icons.drafts::before,
.main_icons.reply_button::before,
.main_icons.reply_all_button::before {
    background-position: -135px -83px;
}
.main_icons.warning_watch::before {
    background-position: -161px -83px;
}
.main_icons.calendar_export::before {
    background-position: -187px -83px;
}
.main_icons.calendar::before {
    background-position: -213px -83px;
}
.main_icons.calendar_modify::before {
    background-position: -239px -83px;
}
/* 5th Row */
.main_icons.plus::before {
    background-position: -5px -109px;
}
.main_icons.warning::before, .main_icons.moderate::before {
    background-position: -31px -109px;
}
.main_icons.themes::before {
    background-position: -57px -109px;
}
.main_icons.support::before {
    background-position: -83px -109px;
}
.main_icons.liked_users::before, .main_icons.liked_messages::before, .main_icons.like::before {
    background-position: -109px -109px;
}
.main_icons.unlike::before {
    background-position: -135px -109px;
}
.main_icons.current_theme::before {
    background-position: -161px -109px;
}
.main_icons.stats::before {
    background-position: -187px -109px;
}
.main_icons.right_arrow::before {
    background-position: -213px -109px;
}
.main_icons.left_arrow::before {
    background-position: -239px -109px;
}
/* 6th Row */
.main_icons.smiley::before {
    background-position: -5px -135px;
}
.main_icons.server::before {
    background-position: -31px -135px;
}
.main_icons.ban::before, .main_icons.ignore::before {
    background-position: -57px -135px;
}

.main_icons.boards::before {
    background-position: -83px -135px;
}
.main_icons.regcenter::before {
    background-position: -109px -135px;
}
.main_icons.posts::before {
    background-position: -135px -135px;
}
.main_icons.sort_down::before {
    background-position: -161px -135px;
}
.main_icons.change_menu2::before, .main_icons.sent::before {
    background-position: -187px -135px;
}
.main_icons.post_moderation_moderate::before {
    background-position: -213px -135px;
}
.main_icons.sort_up::before {
    background-position: -239px -135px;
}
/* 7th Row */
.main_icons.post_moderation_deny::before {
    background-position: -5px -161px;
}
.main_icons.post_moderation_attach::before {
    background-position: -31px -161px;
}
.main_icons.post_moderation_allow::before {
    background-position: -57px -161px;
}
.main_icons.personal_message::before {
    background-position: -83px -161px;
}
.main_icons.permissions::before, .main_icons.login::before {
    background-position: -109px -161px;
}
.main_icons.paid::before {
    background-position: -135px -161px;
}
.main_icons.packages::before {
    background-position: -161px -161px;
}
.main_icons.filter::before {
    background-position: -187px -161px;
    margin: 0 5px 0 0;
}
.main_icons.change_menu::before {
    background-position: -213px -161px;
}
.main_icons.package_ops::before {
    background-position: -239px -161px;
}
/* 8th Row */
.main_icons.reports::before {
    background-position: -5px -187px;
}
.main_icons.news::before {
    background-position: -31px -187px;
}
.main_icons.delete::before, .main_icons.hide_popup::before, .main_icons.prune::before, .main_icons.remove_button::before {
    background-position: -57px -187px;
}
.main_icons.modifications::before {
    background-position: -83px -187px;
}
.main_icons.maintain::before, .main_icons.admin::before {
    background-position: -109px -187px;
}
.main_icons.administration::before, .main_icons.home::before {
    background-position: -135px -187px;
}
.main_icons.frenemy::before {
    background-position: -161px -187px;
}
.main_icons.attachment::before {
    background-position: -187px -187px;
}
.main_icons.lock::before, .main_icons.security::before {
    background-position: -213px -187px;
}
.main_icons.error::before, .main_icons.disable::before {
    background-position: -239px -187px;
}
/* 9th Row */
.main_icons.languages::before,
.main_icons.recent_posts::before {
    background-position: -5px -213px;
}
.main_icons.members_request::before {
    background-position: -31px -213px;
}
.main_icons.members_delete::before {
    background-position: -57px -213px;
}
.main_icons.members::before {
    background-position: -83px -213px;
}
.main_icons.members_watched::before {
    background-position: -109px -213px;
}
.main_icons.sticky::before {
    background-position: -135px -213px;
}
.main_icons.corefeatures::before, .main_icons.settings::before, .main_icons.manrules::before, .main_icons.manlabels::before {
    background-position: -161px -213px;
}
.main_icons.calendar::before {
    background-position: -187px -213px;
}
.main_icons.logs::before {
    background-position: -213px -213px;
}
.main_icons.valid::before {
    background-position: -239px -213px;
}
/* 10th Row */
.main_icons.approve::before, .main_icons.enable::before,
.main_icons.approve_button::before,
.main_icons.read_button::before {
    background-position: -5px -239px;
}
.main_icons.close::before {
    background-position: -31px -239px;
}
.main_icons.details::before {
    background-position: -57px -239px;
}
.main_icons.merge::before {
    background-position: -83px -239px;
}
.main_icons.folder::before {
    background-position: -109px -239px;
}
.main_icons.restore_button::before {
    background-position: -135px -239px;
}
.main_icons.split_button::before {
    background-position: -161px -239px;
}
.main_icons.unapprove_button::before,
.main_icons.unread_button::before {
    background-position: -187px -239px;
}
.main_icons.quote::before, .main_icons.quote_selected::before {
    background-position: -213px -239px;
}
.main_icons.notify_button::before {
    background-position: -239px -239px;
}

.main_icons.select_above::before {
    background-position: -161px -5px;
}
.main_icons.select_here::before {
    background-position: -187px -5px;
}
.main_icons.select_below::before {
    background-position: -213px -5px;
}
</style>

## Источники

* [SMF2.1 Customizer Guide - Icons][source] (English)

[source]: https://sycho9.github.io/smf-docs/#/frontend/icons
