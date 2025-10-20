---
title: Список всех хуков SMF 3.0
description: Все хуки, которые могут пригодиться при создании модов для SMF 3.0.
icon: octicons/gear-16
draft: true
tags:
  - хуки
---

SMF 3 всё ещё в процессе разработки, поэтому название и местоположение некоторых хуков могут к моменту релиза измениться.

## Sources/Actions/Admin/ACP.php

- integrate_prepare_db_settings (`&$config_vars`)
- integrate_validateSession (`&$types`)
- integrate_admin_include
- integrate_admin_areas (`&$this->admin_areas`)

## Sources/Actions/Admin/AntiSpam.php

- integrate_save_spam_settings (`&$save_vars`)
- integrate_spam_settings (`&$config_vars`)

## Sources/Actions/Admin/Attachments.php

- integrate_save_attachment_settings
- integrate_save_avatar_settings
- integrate_attachments_browse (`&$listOptions`, `&$titles`)
- integrate_attachment_remove (`&$filesRemoved`, `$attachments`)
- integrate_repair_attachments_nomsg (`&$ignore_ids`, `$_GET['substep']`, `$_GET['substep'] + 500`)
- integrate_modify_attachment_settings (`&$config_vars`)
- integrate_modify_avatar_settings (`&$config_vars`)
- integrate_manage_attachments (`&self::$subactions`)

## Sources/Actions/Admin/Bans.php

- integrate_ban_edit_list (`&$listOptions`)
- integrate_ban_edit_new
- integrate_ban_list (`&$ban_items`)
- integrate_manage_bans (`&self::$subactions`)
- integrate_edit_bans (`&$ban_info`, `empty($_REQUEST['bg'])`)
- integrate_edit_bans_post
- integrate_load_addtional_ip_ban (`&$search_list`)
- integrate_save_triggers (`&$ban_triggers`, `&$ban_group`)
- integrate_remove_triggers (`&$items_ids`, `$group_id`)

## Sources/Actions/Admin/Boards.php

- integrate_boards_main
- integrate_edit_category
- integrate_edit_board
- integrate_save_board_settings
- integrate_modify_board_settings (`&$config_vars`)
- integrate_manage_boards (`&self::$subactions`)

## Sources/Actions/Admin/Calendar.php

- integrate_save_calendar_settings
- integrate_modify_calendar_settings (`&$config_vars`)
- integrate_manage_calendar (`&self::$subactions`)

## Sources/Actions/Admin/Features.php

- integrate_save_basic_settings
- integrate_save_bbc_settings (`$bbcTags`)
- integrate_save_layout_settings
- integrate_apply_signature_settings (`&$sig`, `$sig_limits`, `$disabledTags`)
- integrate_save_signature_settings (`&$sig_limits`, `&$bbcTags`)
- integrate_save_likes_settings
- integrate_save_mentions_settings
- integrate_modify_basic_settings (`&$config_vars`)
- integrate_modify_bbc_settings (`&$config_vars`)
- integrate_layout_settings (`&$config_vars`)
- integrate_signature_settings (`&$config_vars`)
- integrate_likes_settings (`&$config_vars`)
- integrate_mentions_settings (`&$config_vars`)
- integrate_modify_features (`&self::$subactions`)

## Sources/Actions/Admin/Find.php

- integrate_admin_search (`&$this->language_files`, `&$this->include_files`, `&$this->settings_search`)

## Sources/Actions/Admin/Languages.php

- integrate_save_language_settings (`&$config_vars`)
- integrate_modifylanguages (`&$themes`, `&$lang_dirs`, `&$allows_add_remove`, `&$additional_string_types`)
- integrate_language_edit_helptext (`&$special_groups`)
- integrate_language_settings (`&$config_vars`)
- integrate_manage_languages (`&self::$subactions`)

## Sources/Actions/Admin/Logs.php

- integrate_prune_settings (`&$config_vars`, `&self::$prune_toggle`, `false`)
- integrate_manage_logs (`&self::$subactions`)

## Sources/Actions/Admin/Mail.php

- integrate_save_mail_settings
- integrate_modify_mail_settings (`&$config_vars`)
- integrate_manage_mail (`&self::$subactions`)

## Sources/Actions/Admin/Maintenance.php

- integrate_convert_msgbody (`$body_type`)
- integrate_reattribute_posts (`$memID`, `$email`, `$membername`, `$post_count`, `&$updated`)
- integrate_manage_maintenance (`&self::$subactions`)

## Sources/Actions/Admin/Membergroups.php

- integrate_pre_add_membergroup
- integrate_add_membergroup (`$id_group`, `$postCountBasedGroup`)
- integrate_view_membergroup
- integrate_save_membergroup_settings
- integrate_modify_membergroup_settings (`&$config_vars`)
- integrate_manage_membergroups (`&self::$subactions`)

## Sources/Actions/Admin/Members.php

- integrate_view_members_params (`&$params`)
- integrate_activate (`$member['username']`)
- integrate_manage_members (`&self::$subactions`)

## Sources/Actions/Admin/Mods.php

- integrate_save_general_mod_settings (`&$save_vars`)
- integrate_general_mod_settings (`&$config_vars`)
- integrate_modify_modifications (`&self::$subactions`)

## Sources/Actions/Admin/News.php

- integrate_save_news_settings
- integrate_modify_news_settings (`&$config_vars`)
- integrate_manage_news (`&self::$subactions`)

## Sources/Actions/Admin/Permissions.php

- integrate_save_permission_settings
- integrate_post_moderation_mapping (`&$this->postmod_maps`)
- integrate_modify_permission_settings (`&$config_vars`)
- [integrate_permissions_list](/hooks/integrate-permissions-list) (`&self::$permissions`)
  Рекомендованный способ добавления новых разрешений в SMF
- integrate_load_permission_levels (`&$group_levels`, `&$board_levels`)
- integrate_manage_permissions (`&self::$subactions`)
- integrate_load_permissions (`&self::$permission_groups`, `&$permissions_by_scope`, `&self::$left_permission_groups`, `&$hidden_permissions`, `&$relabel_permissions`)
- integrate_load_illegal_permissions
- integrate_load_illegal_guest_permissions

## Sources/Actions/Admin/Posts.php

- integrate_save_censors (`&$updates`)
- integrate_censors
- integrate_save_post_settings
- integrate_save_topic_settings
- integrate_modify_post_settings (`&$config_vars`)
- integrate_modify_topic_settings (`&$config_vars`)
- integrate_modify_draft_settings (`&$config_vars`)
- integrate_manage_posts (`&self::$subactions`)

## Sources/Actions/Admin/Registration.php

- integrate_save_registration_settings
- integrate_modify_registration_settings (`&$config_vars`)
- integrate_manage_registrations (`&self::$subactions`)

## Sources/Actions/Admin/RepairBoards.php

- integrate_repair_boards (`&$this->errorTests`)
  Возможность добавить пользовательские тесты, чтобы разрешить восстановление данных в таблицах модификаций

## Sources/Actions/Admin/Reports.php

- integrate_report_buttons
- integrate_reports_boardperm (`&$disabled_permissions`)
- integrate_reports_groupperm (`&$disabled_permissions`)
- integrate_report_types (`&self::$subactions`)

## Sources/Actions/Admin/Search.php

- integrate_save_search_settings
- integrate_modify_search_weights (`&$factors`)
- integrate_save_search_weights
- integrate_modify_search_settings (`&$config_vars`)
- integrate_manage_search (`&self::$subactions`)

## Sources/Actions/Admin/SearchEngines.php

- integrate_save_search_engine_settings
- integrate_modify_search_engine_settings (`&$config_vars`)
- integrate_manage_search_engines (`&self::$subactions`)

## Sources/Actions/Admin/Server.php

- integrate_save_general_settings
- integrate_save_database_settings
- integrate_save_cookie_settings
- integrate_save_general_security_settings
- integrate_save_cache_settings
- integrate_save_export_settings
- integrate_save_loadavg_settings
- integrate_general_settings (`&$config_vars`)
- integrate_database_settings (`&$config_vars`)
- integrate_cookie_settings (`&$config_vars`)
- integrate_general_security_settings (`&$config_vars`)
- integrate_modify_cache_settings (`&$config_vars`)
- integrate_export_settings (`&$config_vars`)
- integrate_loadavg_settings (`&$config_vars`)
- integrate_server_settings (`&self::$subactions`)

## Sources/Actions/Admin/Smileys.php

- integrate_save_smiley_settings
- integrate_modify_smiley_settings (`&$config_vars`)
- integrate_manage_smileys (`&self::$subactions`)

## Sources/Actions/Admin/Subscriptions.php

- integrate_delete_subscription (`Utils::$context['sub_id']`)
- integrate_save_subscription (`(Utils::$context['action_type'] == 'add' ? $id_subscribe : Utils::$context['sub_id'])`, `$_POST['name']`, `$_POST['desc']`, `$isActive`, `$span`, `$cost`, `$_POST['prim_group']`, `$addgroups`, `$isRepeatable`, `$allowpartial`, `$emailComplete`, `$reminder`)
- integrate_paidsubs_settings (`&$config_vars`)
- integrate_manage_subscriptions (`&self::$subactions`)

## Sources/Actions/Admin/Tasks.php

- integrate_save_scheduled_tasks_settings (`&$save_vars`)
- integrate_scheduled_tasks_settings (`&$config_vars`)
- integrate_manage_scheduled_tasks (`&self::$subactions`)

## Sources/Actions/Admin/Themes.php

- integrate_theme_options
- integrate_theme_settings
- integrate_manage_themes (`&self::$subactions`)
- integrate_get_single_theme (`&$variables`, `$id`)
- integrate_get_all_themes (`&$themeValues`, `$enable_only`)
- integrate_get_installed_themes (`&$themeValues`)
- integrate_theme_install (`&Utils::$context['to_install']`, `$id_theme`)

## Sources/Actions/Admin/Warnings.php

- integrate_save_warning_settings (`&$save_vars`)
- integrate_warning_settings (`&$config_vars`)

## Sources/Actions/Moderation/Home.php

- integrate_moderation_home_blocks (`&$this->blocks`)
- integrate_mod_centre_blocks (`&$valid_blocks`)

## Sources/Actions/Moderation/Logs.php

- integrate_viewModLog (`&$listOptions`, `&$moderation_menu_name`)

## Sources/Actions/Moderation/Posts.php

- integrate_post_moderation (`&self::$subactions`)

## Sources/Actions/Moderation/ReportedContent.php

- integrate_reported\_`$this->type` (`&self::$subactions`)

## Sources/Actions/Moderation/Warnings.php

- integrate_warning_log_actions (`&self::$subactions`)

## Sources/Actions/Profile/Activate.php

- integrate_activate (`Profile::$member->username`)

## Sources/Actions/Profile/BuddyIgnoreLists.php

- integrate_remove_buddy (`Profile::$member->id`)
- integrate_add_buddies (`Profile::$member->id`, `&$new_buddies`)
- integrate_view_buddies (`Profile::$member->id`)

## Sources/Actions/Profile/Main.php

- integrate_verify_password (`Profile::$member->username`, `$password`, `false`)
- integrate_profile_areas (`&$this->profile_areas`)

## Sources/Actions/Profile/Notification.php

- integrate_alert_types (`&$this->alert_types`, `&$this->group_options`)

## Sources/Actions/Profile/Popup.php

- integrate_profile_popup (`&$this->profile_items`)

## Sources/Actions/Profile/ShowPosts.php

- integrate_profile_showPosts

## Sources/Actions/Profile/StatPanel.php

- integrate_profile_stats (`Profile::$member->id`, `&Utils::$context['text_stats']`)

## Sources/Actions/Profile/ThemeOptions.php

- integrate_theme_options

## Sources/Actions/Activate.php

- integrate_activate (`$row['member_name']`)

## Sources/Actions/AttachmentDownload.php

- integrate_pre_download_request
- integrate_download_request (`&$request`)

## Sources/Actions/AttachmentUpload.php

- integrate_attachment_upload

## Sources/Actions/AutoSuggest.php

- integrate_autosuggest (`&$suggest_types`)

## Sources/Actions/BoardIndex.php

- integrate_mark_read_button
- integrate_pre_boardindex (`&$selects`, `&$params`, `&$joins`, `&$where`, `&$order`)
- integrate_boardindex_board (`&$cat_boards`, `$row_board`)
- integrate_getboardtree (`$board_index_options`, `&Category::$loaded`)
- integrate_getboardtree (`$board_index_options`, `&$cat_boards`)
- integrate_boardindex_last_post (`&$last_post`, `$row_board`)

## Sources/Actions/Calendar.php

- integrate_calendar_buttons

## Sources/Actions/Credits.php

- integrate_credits

## Sources/Actions/Display.php

- integrate_prepare_display_context (`&$output`, `$message`, `$counter`)
- integrate_display_message_list (`&$this->messages`, `&$this->posters`)
- integrate_display_buttons (`&Utils::$context['normal_buttons']`) — Старайтесь не использовать этот хук, изменяя `Utils::$context['normal_buttons']` напрямую
- --integrate_mod_buttons (`&Utils::$context['mod_buttons']`)-- — Используйте `integrate_display_buttons`

## Sources/Actions/Feed.php

- integrate_xmlfeeds (`&self::$subactions`)
- integrate_xml_data (`&$data`, `&$metadata`, `&$namespaces`, `&$extraFeedTags`, `&$forceCdataKeys`, `&$nsKeys`, `$format`, `$subaction`, `&$doctype`)
- integrate_fix_url (`&$val`)

## Sources/Actions/Groups.php

- integrate_manage_groups (`&self::$subactions`)

## Sources/Actions/Help.php

- integrate_manage_help (`&$subactions`)

## Sources/Actions/HelpAdmin.php

- integrate_helpadmin

## Sources/Actions/JavaScriptModify.php

- integrate_post_JavascriptModify (`&$post_errors`, `$row`)
- integrate_jsmodify_xml
- integrate_jsmodify (`$row`, `&$is_new_edit`, `&$msgOptions`, `&$topicOptions`, `&$posterOptions`)

## Sources/Actions/Like.php

- integrate_valid_likes (`$this->type`, `$this->content`, `$this->subaction`, `$this->js`, `$this->extra`)
- integrate_issue_like_before (`&$type`, `&$content`, `&$user`, `&$time`)
- integrate_issue_like (`$this`)
- integrate_likes_json_response (`&$print`)

## Sources/Actions/Login2.php

- integrate_validate_login (`$_POST['user']`, `$_POST['passwrd'] ?? null`, `Config::$modSettings['cookieTime']`)
- integrate_other_passwords (`&$other_passwords`)
- integrate_login (`User::$profiles[User::$my_id]['member_name']`, `null`, `Config::$modSettings['cookieTime']`)

## Sources/Actions/Logout.php

- integrate_logout (`User::$me->username`)

## Sources/Actions/Memberlist.php

- integrate_memberlist_buttons
- integrate_memberlist_subactions (`&self::$subactions`, `$this->sort_links`)

## Sources/Actions/MessageIndex.php

- integrate_pre_messageindex (`&$sort_columns`, `&$sort_joins`, `&$sort_asc_defaults`, `&$this->sort_default`)
- integrate_message_index (`&$selects`, `&$joins`, `&$params`, `&$main_where`, `&$topic_ids`, `&$sort_where`)
- integrate_messageindex_buttons (`&Utils::$context['normal_buttons']`)

## Sources/Actions/PersonalMessage.php

- integrate_pm_areas (`&$this->pm_areas`)

## Sources/Actions/Post.php

- integrate_post_subactions (`&self::$subactions`)
- integrate_post_start
- integrate_post_end
- integrate_getTopic_previous_post (`&$row`)
- integrate_preview_post (`&$this->form_message`, `&$this->form_subject`)
- integrate_post_errors (`&$this->errors`, `&$this->minor_errors`, `$this->form_message`, `$this->form_subject`)

## Sources/Actions/Post2.php

- integrate_post2_subactions (`&self::$subactions`)
- integrate_post2_start (`&$this->errors`)
- integrate_post2_pre (`&$this->errors`)
- integrate_post2_end

## Sources/Actions/QuickModeration.php

- integrate_quick_mod_actions_search (`self::$known_actions`)
- integrate_quick_mod_actions (`self::$known_actions`)

## Sources/Actions/QuoteFast.php

- integrate_quotefast (`$row`)

## Sources/Actions/Recent.php

- integrate_recent_RecentPosts

## Sources/Actions/Register2.php

- integrate_activate (`$reg_options['username']`)
- integrate_register_check (`&$reg_options`, `&$reg_errors`)
- integrate_register (`&$reg_options`, `&$theme_vars`, `&$known_ints`, `&$known_floats`)
- integrate_post_register (`&$reg_options`, `&$theme_vars`, `&$member_id`)
- integrate_register_after (`$reg_options`, `$member_id`)

## Sources/Actions/Reminder.php

- integrate_reset_pass (`$this->member->username`, `$this->member->username`, `$_POST['passwrd1']`)

## Sources/Actions/Search.php

- integrate_search

## Sources/Actions/Search2.php

- integrate_search_message_context (`&$output`, `&$message`, `$counter`)
- integrate_search_errors
- integrate_search_message_list (`&$this->messages`, `&$this->posters`)

## Sources/Actions/Stats.php

- integrate_forum_stats

## Sources/Actions/TopicMerge.php

- integrate_merge_topic (`$merged_topic`, `$updated_topics`, `$deleted_topics`, `$deleted_polls`)

## Sources/Actions/TopicMove2.php

- integrate_movetopic2_end

## Sources/Actions/TopicSplit.php

- integrate_split_topic (`$split1`, `$split2`, `$new_subject`, `$id_board`)

## Sources/Actions/TrackIP.php

- integrate_profile_trackip (`$ip_string`, `$ip_var`)

## Sources/Actions/Unread.php

- integrate_unread_list
- integrate_recent_buttons

## Sources/Actions/ViewQuery.php

- integrate_egg_nog

## Sources/Actions/Who.php

- integrate_whos_online (`$actions`)

## Sources/Actions/XmlHttp.php

- integrate_XMLhttpMain_subActions (`&self::$subactions`)

## Sources/Cache/CacheApi.php

- integrate_load_cache_apis (`&$loadedApis`)
- integrate_clean_cache
- pre_cache_quick_get (`&$key`, `&$file`, `&$function`, `&$params`, `&$level`)
- post_cache_quick_get (`&$cache_block`)
- cache_put_data (`&$key`, `&$value`, `&$ttl`)
- cache_get_data (`&$key`, `&$ttl`, `&$value`)

## Sources/Calendar/Event.php

- integrate_construct_event (`$id`, `&`$props`)
- integrate_constructed_event (`$this`)
- integrate_create_event (`$this`, `&$columns`, `&$params`)
- integrate_modify_event (`$this->id`, `$this`, `&$set`, `&$params`)
- integrate_query_event (`&$selects`, `&$params`, `&$joins`, `&$where`, `&$order`, `&$group`, `&$limit`)
- integrate_remove_event (`$id`)
- integrate_handle_special_rrule (`$id`, `&$props`)

## Sources/Localization/AsciiTransliterator.php

- integrate_ascii_transliterator_id (`&$id`)
- integrate_ascii_transliterator_chars (`$chars`, `&$new_chars`)

## Sources/PackageManager/PackageManager.php

- integrate_modification_types
- integrate_package_download
- integrate_package_upload
- integrate_packages_sort_id (`&$sort_id`, `&$packages`)
- --integrate_package_get (`&$temp`)-- — Используйте `integrate_manage_packages`
- integrate_manage_packages (`&$this->subactions`)

## Sources/Parsers/BBCodeParser.php

- integrate_autolinker_schemes (`&self::$schemes`)
  Используется автолинкером
- integrate_attach_bbc_validate (`&$return_context`, `$current_attachment`, `$tag`, `$data`, `$disabled`, `$params`)
  Настраивает HTML, созданный BB-тегом `attach`
- integrate_bbc_print (`&$this->disabled`)
  Для BB-тегов, требующих особого поведения в режиме печати
- integrate_bbc_codes (`&self::$codes`, `&self::$no_autolink_tags`)
  Используется для добавления или изменения BB-тегов

## Sources/Parsers/MarkdownParser.php

- integrate_markdown (`&$this->block_types`, `&$this->render_methods`)

## Sources/Parsers/SmileyParser.php

- integrate_smileys (`&$this->smiley_preg_search`, `&$this->smiley_preg_replacements`)
  Используется для альтернативной обработки смайлов

## Sources/PersonalMessage/Folder.php

- integrate_prepare_pm_context (`&$output`, `&$message`, `$counter`)
- integrate_conversation_buttons

## Sources/PersonalMessage/PM.php

- integrate_pm_post
- integrate_personal_message (`&$recipients`, `&$from`, `&$subject`, `&$message`)
- integrate_personal_message_after (`&$id_pm`, `&$log`, `&$recipients`, `&$from`, `&$subject`, `&$message`)
- integrate_pm_error

## Sources/PersonalMessage/Search.php

- integrate_search_pm_context

## Sources/PersonalMessage/SearchResult.php

- integrate_pm_search_result (`&$output`)

## Sources/Search/SearchApi.php

- integrate_load_search_apis (`&$loadedApis`)
- integrate_search_weights (`&self::$weight_factors`)
- integrate_search_blacklisted_words (`&$this->blacklisted_words`)
- integrate_search_params (`&$this->params`)
- integrate_search_sort_columns (`&$this->sort_columns`)
- integrate_subject_only_search_query (`&$subject_query`, `&$subject_query_params`)
- integrate_subject_search_query (`&$subject_query`)
- integrate_main_search_query (`&$main_query`)

## Sources/Tasks/DailyMaintenance.php

- integrate_daily_maintenance

## Sources/Tasks/ExportProfileData.php

- integrate_export_xslt_variables (`&$xslt_variables`, `$this->_details['format']`)
  Позволяет настроить переменные XSLT
- integrate_export_xslt_stylesheet (`&$this->xslt_stylesheet`, `$this->_details['format']`)
  Позволяет корректировать таблицу стилей XSLT
- integrate_pre_css_output
- integrate_pre_javascript_output (`false/true`)

## Sources/Tasks/Likes_Notify.php

- integrate_find_like_author (`$this->_details['content_type']`, `$this->_details['content_id']`)

## Sources/Tasks/SendDigests.php

- integrate_daily_digest_lang (`&$langtxt`, `$lang`)

## Sources/Tasks/WeeklyMaintenance.php

- integrate_weekly_maintenance

## Sources/Alert.php

- integrate_fetch_alerts (`&$loaded`, `&self::$link_formats`)
- integrate_alert_icon (`&$this->icon`, `(array) $this`)

## Sources/Attachment.php

- integrate_attachment_load (`&$selects`, `&$params`, `&$from`, `&$joins`, `&$where`, `&$order`, `&$limit`)
- integrate_attachment_loadbymsg (`&$selects`, `&$params`, `&$from`, `&$joins`, `&$where`, `&$order`, `&$limit`)
- integrate_attachment_loadbymember (`&$selects`, `&$params`, `&$from`, `&$joins`, `&$where`, `&$order`, `&$limit`)
- integrate_attachment_upload
- integrate_createAttachment (`&$attachmentOptions`, `&$attachmentInserts`)
- integrate_assign_attachments (`&$attachIDs`, `&$msgID`)
- integrate_approve_attachments (`$attachments`)
- integrate_remove_attachments (`$attach`)
- integrate_pre_parseAttachBBC (`$attachID`, `$msgID`)
- integrate_post_parseAttachBBC (`&$attachContext`)

## Sources/Autolinker.php

- integrate_autolinker_schemes (`&self::$schemes`)
- integrate_autolinker_fix_tags (`&self::$tags_to_fix`)

## Sources/Autoloader.php

- integrate_autoload (`&$class_map`)

## Sources/Board.php

- integrate_modify_board (`$this->id`, `$boardOptions`, `&$set`, `&$params`)
- integrate_pre_modify_board (`$board_id`, `&$boardOptions`)
- integrate_create_board (`&$boardOptions`, `&$board_columns`, `&$board_parameters`)
- integrate_delete_board (`$boards_to_remove`, `&$moveChildrenTo`)
- integrate_load_board (`&$selects`, `&$params`, `&$joins`, `&$where`, `&$order`)
- integrate_board_info (`&$props`, `$row`)

## Sources/Category.php

- integrate_pre_modify_category (`$cat_id`, `&$catOptions`)
- integrate_modify_category (`$cat_id`, `&$catUpdates`, `&$catParameters`)
- integrate_create_category (`&$catOptions`, `&$cat_columns`, `&$cat_parameters`)
- integrate_delete_category (`$categories`, `&$moveBoardsTo`)
- integrate_pre_boardtree (`&$selects`, `&$params`, `&$joins`, `&$where`, `&$order`)
- integrate_boardtree_board (`$row`)

## Sources/Config.php

- integrate_load_average (`self::$modSettings['load_average']`)
- integrate_pre_include
- integrate_pre_load
- integrate_update_settings_file (`&self::$settings_defs`)

## Sources/Cookie.php

- integrate_cookie_data (`$data`, `&$this->custom_data`)
  Позволяет добавлять пользовательскую информацию в файлы cookie
- integrate_cookie (`$this->name`, `$value`, `$this->expires`, `$this->path`, `$this->domain`, `$this->secure`, `$this->httponly`, `$this->samesite`)
  Этот хук просто передает полезную информацию о файлах cookie. Если вы хотите изменить данные cookie, используйте хук выше

## Sources/Editor.php

- integrate_load_message_icons (`&$icons`)
- integrate_bbc_buttons (`&self::$bbc_tags`, `&$editor_tag_map`, `&self::$disabled_tags`)
  Позволяет изменять кнопки для вставки BB-тегов
- integrate_sceditor_options (`&$this->sce_options`)
  Позволяет изменять `$this->sce_options`, что может пригодиться при добавлении различных плагинов для SCEditor

## Sources/ErrorHandler.php

- integrate_output_error (`$message`, `$error_type`, `$error_level`, `$file`, `$line`)
- integrate_error_types (`&$other_error_types`, `&$error_type`, `$error_message`, `$file`, `$line`)
  Позволяет изменять тип ошибки и узнавать об ошибках

## Sources/Forum.php

- integrate_actions (`&self::$actions`)
- --integrate_pre_log_stats (`&self::$unlogged_actions`)-- — Используйте `ActionInterface::isSimpleAction()`
- --integrate_guest_actions (`&self::$guest_access_actions`)-- — Используйте `ActionInterface::isRestrictedGuestAccessAllowed()`
- integrate_default_action
- integrate_fallback_action

## Sources/Group.php

- integrate_pre_add_membergroup
- integrate_add_membergroup (`$this->id`, `$this->min_posts > -1`)
- integrate_save_membergroup (`$this->id`)
- integrate_add_members_to_group (`$members`, `$this->id`, `&$group_names`)
- integrate_getMembergroupList (`&$groupCache`, `$group`)

## Sources/ItemList.php

- integrate\_`$options['id']` (`&$options`)
  Возможность переопределить параметры при создании списка

## Sources/Lang.php

- integrate_word_censor (`&$text`)

## Sources/Logging.php

- integrate_log_types (`&$log_types`, `&$always_log`)
- integrate_online_stats (`&$membersOnlineStats`)

## Sources/Mail.php

- integrate_outgoing_email (`&$subject`, `&$message`, `&$headers`, `&$to_array`)

## Sources/MailAgent/MailAgent.php

- integrate_load_mail_agents (`&$loaded_apis`)

## Sources/Menu.php

- integrate\_`$this->current_action`\_areas (`&$this->data`)
  Позволяет изменение любого меню (`integrate_moderate_areas`, `integrate_pm_areas` и т. д.)

## Sources/Msg.php

- integrate_format_msg (`&$this->formatted`, `$this->id`)
- integrate_query_message (`&$selects`, `&$joins`, `&$params`, `&$where`, `&$order`, `&$group`, `&$limit`)
- integrate_preparsecode (`&$message`, `$previewing`)
- integrate_unpreparsecode (`&$message`)
- integrate_create_post (`&$msgOptions`, `&$topicOptions`, `&$posterOptions`, `&$message_columns`, `&$message_parameters`)
- integrate_after_create_post (`$msgOptions`, `$topicOptions`, `$posterOptions`, `$message_columns`, `$message_parameters`)
  Возможность экспортировать созданное сообщение в стороннюю CMS, внешний скрипт и т. д.
- integrate_before_create_topic (`&$msgOptions`, `&$topicOptions`, `&$posterOptions`, `&$topic_columns`, `&$topic_parameters`)
- integrate_create_topic (`&$msgOptions`, `&$topicOptions`, `&$posterOptions`)
- integrate_modify_topic (`&$topics_columns`, `&$update_parameters`, `&$msgOptions`, `&$topicOptions`, `&$posterOptions`)
- integrate_modify_post (`&$messages_columns`, `&$update_parameters`, `&$msgOptions`, `&$topicOptions`, `&$posterOptions`, `&$messageInts`, `&$possible_topic_columns`)
- integrate_after_approve_posts (`$approve`, `$msgs`, `$topic_changes`, `$member_post_changes`)
- integrate_pre_remove_message (`$message`, `$decreasePostCount`, `$row`)
- integrate_remove_message (`$message`, `$row`, `$recycle`)
  Возможность удаления данных, связанных с сообщениями (лайки и т. д.)

## Sources/QueryString.php

- integrate_rewrite_as_queryless (`&$buffer`)
- integrate_route_parsers
- integrate_build_route (`&$route_base`, `$params`)

## Sources/Parser.php

- integrate_parser_output_handlers (`&$handlers`)
- integrate_parser_options (`&$options`)
- integrate_pre_parsebbc (`&$string`, `&$smileys`, `&$options['cache_id']`, `&$options['parse_tags']`)
  Позволяет вносить изменения перед парсингом
- integrate_post_parsebbc (`&$string`, `$smileys`, `$options['cache_id']`, `$options['parse_tags']`)
  Предоставляет доступ к результатам парсинга
- integrate_parser_cache (`&$cache_key_extras`, `$input_types`, `$output_type`, `$options`)

## Sources/Poll.php

- integrate_poll_buttons
- integrate_poll_add_edit (`$this->id`, `$is_edit`)
- integrate_poll_vote (`$poll->id`, `$choices`)
- integrate_poll_remove (`$poll->id`)

## Sources/Profile.php

- integrate_reset_pass (`$this->username`, `$value`, `$_POST['passwrd1']`)
- integrate_load_profile_fields (`&$this->standard_fields`)
- integrate_load_custom_profile_fields (`$this->id`, `$area`)
- integrate_setup_profile_context (`&$fields`)
- integrate_profile_save (`&Profile::$member->new_data`, `&Profile::$member->save_errors`, `Profile::$member->id`, `Profile::$member->data`, `Menu::$loaded['profile']->current_area`)
- integrate_profile_profileSaveGroups (`$value`, `$additional_groups`)
- integrate_save_custom_profile_fields (`&$this->new_cf_data['updates']`, `&$this->log_changes`, `&$this->cf_save_errors`, `true`, `$this->id`, `$area`, `!self::$member->post_sanitized`, `&$deletes`)

## Sources/Security.php

- integrate_spam_protection (`&$timeOverrides`)

## Sources/ServerSideIncludes.php

- integrate_ssi_queryPosts (`&$posts`)
- integrate_ssi_recentTopics (`&$posts`)
- integrate_ssi_topPoster (`&$return`)
- integrate_ssi_topBoards (`&$boards`)
- integrate_ssi_topTopics (`&$topics`, `$type`)
- integrate_ssi_queryMembers (`&$members`)
- integrate_ssi_boardStats (`&$totals`)
- integrate_ssi_whosOnline (`&$return`)
- integrate_ssi_recentPoll (`&$return`, `$topPollInstead`)
- integrate_ssi_showPoll (`&$return`)
- integrate_ssi_news
- integrate_ssi_calendar (`&$return`, `$eventOptions`)
- integrate_ssi_boardNews (`&$return`)
- integrate_ssi_recentEvents (`&$return`)
- integrate_ssi_recentAttachments (`&$attachments`)
- integrate_SSI

## Sources/Session.php

- integrate_load_session
  Возможность добавлять/изменять настройки PHP (с помощью `@ini_set`)
- integrate_session_handlers

## Sources/Slug.php

- integrate_make_slug (`$string`, `&$this->slug`)
  Возможность изменить слаг переданной строки
- integrate_slug_redirect_patterns (`&self::$redirect_patterns`)

## Sources/TaskRunner.php

- integrate_scheduled_tasks (`&self::$scheduled_tasks`)
  Добавление запланированных задач

## Sources/Theme.php

- integrate_pre_load_theme (`&$id`)
- integrate_theme_context
- integrate_menu_buttons (`&$buttons`)
  Редактирование пунктов меню
- integrate_current_action (`&$current_action`)
- integrate_security_files (`&$securityFiles`)
- integrate_pre_javascript_output (`&$do_deferred`)
  Мминимизация/оптимизация файлов и переменных Javascript
- integrate_pre_css_output
  Мминимизация/оптимизация файлов CSS
- integrate_wrap_action
- integrate_theme_include
- integrate_load_theme
- --integrate_simple_actions (`&$this->simpleActions`, `&$this->simpleAreas`, `&$this->simpleSubActions`, `&$this->extraParams`, `&$this->xmlActions`)-- — Используйте `ActionInterface::isSimpleAction()`

## Sources/TimeZone.php

- integrate_metazones (`&self::$metazones`, `$when`)
- integrate_country_timezones (`&self::$sorted_tzids`, `$country_code`, `$when`)
- integrate_timezone_fallbacks (`&self::$fallbacks`, `&$missing`, `$tzids`, `$when`)

## Sources/Topic.php

- integrate_remove_topics_before (`$topics`, `$recycle_board`)
- integrate_remove_topics (`$topics`)
- integrate_display_topic (`&$topic_selects`, `&$topic_joins`, `&$topic_parameters`)

## Sources/Url.php

- integrate_proxy (`$this->url`, `&$proxied->url`)
  Реализация альтернативных прокси

## Sources/User.php

- integrate_member_context (`&$this->formatted`, `$this->id`, `$display_custom_fields`)
- integrate_mod_cache
- integrate_post_ban_permissions (`&self::$post_ban_permissions`)
- integrate_warn_permissions (`&self::$warn_permissions`)
  Изменение выбранных разрешений
- integrate_validateSession (`&$types`)
- integrate_verify_password (`$this->username`, `$_POST[$type . '_pass']`, `false`)
- integrate_allowed_to_general (`&$user_permissions`, `$permission`)
  Переопределение общих разрешений
- integrate_allowed_to_board (`&$return`, `$permission`, `$boards`, `$any`)
  Переопределение прав доступа к форуму
- integrate_heavy_permissions_session (`&self::$heavy_permissions`)
- integrate_boards_allowed_to (`&$boards`, `$deny_boards`, `$permissions`, `$check_access`, `$simple`)
  Переопределение прав доступа к разделам
- integrate_set_avatar_data (`&$image`, `&$data`)
- integrate_change_member_data (`$member_names`, `$var`, `&$data[$var]`, `&self::$knownInts`, `&self::$knownFloats`)
- integrate_delete_members (`$users`)
- integrate_validatePassword (`$password`, `$username`, `$restrict_in`, `&$pass_error`)
- integrate_validate_username (`$username`, `&$errors`)
  Добавление дополнительных проверок при валидации пользователя
- integrate_check_name (`$checkName`, `&$is_reserved`, `$current_id_member`, `$is_name`)
  Добавление дополнительных проверок на то, не входит ли имя пользователя в список зарезервированных имён
- integrate_groups_allowed_to (`&$member_groups[$permission]`, `$permission`, `$board_id`)
  Переопределение списка разрешённых групп
- integrate_user_info
  При работе с этим хуком рекомендуется заменить любое использование переменной `$user_info` структурой `SMF\User::$me`, либо использовать хук, указанный ниже
- integrate_user_properties (`$this`) (^3.0 Alpha 1)
  Устанавливает свойства объекта на основе данных в `User::$profiles[$this->id]`.
- integrate_verify_user
  Позволяет проверять личность текущего пользователя
- integrate_force_tfasetup (`&$force_tfasetup`)
  Проверка двухфакторной аутентификации при `force_tfasetup = true`
- integrate_verify_tfa (`self::$my_id`, `self::$profiles[self::$my_id]`)
  Валидация двухфакторной аутентификации
- integrate_load_member_data (`&$select_columns`, `&$select_tables`, `&$dataset`)
  Позволяет добавлять данные о выбранных участниках
- integrate_load_min_user_settings (`&self::$profiles`)

## Sources/Utils.php

- integrate_download_headers
- integrate_redirect (`&$setLocation`, `&$refresh`, `&$permanent`)
- integrate_buffer
- integrate_exit (`$do_footer`)

## Sources/Verifier.php

- integrate_create_control_verification_pre (`&$options`, `$do_test`)
- integrate_create_control_verification_post (`&$this->errors`, `$do_test`)
- integrate_create_control_verification_test (`$this`, `&$this->errors`)
- integrate_create_control_verification_refresh (`$this`)

## Themes/default/index.template.php

- integrate\_`$list_class`\_quickbuttons (`&$list_items`)
