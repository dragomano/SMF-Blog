---
title: Список всех хуков SMF 2.1
description: Все хуки, которые могут пригодиться при создании модов для SMF 2.1.
icon: octicons/webhook-16
tags:
  - хуки
---

> Хук — функция-перехватчик, с помощью которой можно внедрять свой код без изменения исходных файлов движка.

## index.php

| Хук | Параметры |
|-----|-----------|
| [integrate_autoload](/hooks/integrate-autoload) | `&$classMap` |
| integrate_pre_log_stats | `&$no_stat_actions` |
| integrate_default_action | |
| [integrate_actions](/hooks/integrate-actions) | `&$actionArray` |
| integrate_fallback_action | |

## SSI.php

| Хук | Параметры |
|-----|-----------|
| [integrate_autoload](/hooks/integrate-autoload) | `&$classMap` |
| integrate_SSI | |
| integrate_ssi_queryPosts | `&$posts` |
| integrate_ssi_recentTopics | `&$posts` |
| integrate_ssi_topPoster | `&$return` |
| integrate_ssi_topBoards | `&$boards` |
| integrate_ssi_topTopics | `&$topics`, `$type` |
| integrate_ssi_queryMembers | `&$members` |
| integrate_ssi_boardStats | `&$totals` |
| integrate_ssi_whosOnline | `&$return` |
| integrate_ssi_recentPoll | `&$return`, `$topPollInstead` |
| integrate_ssi_showPoll | `&$return` |
| integrate_ssi_news | |
| integrate_ssi_calendar | `&$return`, `$eventOptions` |
| integrate_ssi_boardNews | `&$return` |
| integrate_ssi_recentEvents | `&$return` |
| integrate_ssi_recentAttachments | `&$attachments` |

## Sources/Admin.php

| Хук | Параметры |
|-----|-----------|
| integrate_admin_include | |
| integrate_admin_search | `&$language_files`, `&$include_files`, `&$settings_search` |
| integrate_manage_logs | `&$log_functions` |

## Sources/Attachments.php

| Хук | Параметры |
|-----|-----------|
| integrate_attachment_upload | |

## Sources/BoardIndex.php

| Хук | Параметры |
|-----|-----------|
| integrate_mark_read_button | |

## Sources/Calendar.php

| Хук | Параметры |
|-----|-----------|
| integrate_calendar_buttons | |

## Sources/Display.php

| Хук | Параметры |
|-----|-----------|
| [integrate_display_topic](/hooks/integrate-display-topic) | `&$topic_selects`, `&$topic_tables`, `&$topic_parameters` |
| integrate_poll_buttons | |
| integrate_display_message_list | `&$messages`, `&$posters` |
| integrate_query_message | `&$msg_selects`, `&$msg_tables`, `&$msg_parameters` |
| [integrate_display_buttons](/lessons/kak-dobavit-knopku#h-3) | `&$context['normal_buttons']` |
| [integrate_mod_buttons](/lessons/kak-dobavit-knopku#h-3) | `&$context['mod_buttons']` |
| [integrate_prepare_display_context](/hooks/integrate-prepare-display-context) | `&$output`, `&$message`, `$counter` |

## Sources/Errors.php

| Хук | Параметры |
|-----|-----------|
| integrate_error_types | `&$other_error_types`, `&$error_type`, `$error_message`, `$file`, `$line` |
| integrate_output_error | `$message`, `$error_type`, `$error_level`, `$file`, `$line` |

## Sources/Groups.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_groups | `&$subActions` |

## Sources/Help.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_help | `&$subActions` |
| integrate_helpadmin | |

## Sources/Likes.php

| Хук | Параметры |
|-----|-----------|
| integrate_valid_likes | `$this->_type`, `$this->_content`, `$this->_sa`, `$this->_js`, `$this->_extra` |
| integrate_issue_like_before | `&$type`, `&$content`, `&$user`, `&$time` |
| integrate_issue_like | `$this` |
| integrate_likes_json_response | `&$print` |

## Sources/Load.php

| Хук | Параметры |
|-----|-----------|
| integrate_load_average | `$modSettings['load_average']` |
| [integrate_pre_include](/hooks/integrate-pre-include) | |
| [integrate_pre_load](/hooks/integrate-pre-load) | |
| integrate_verify_user | |
| integrate_force_tfasetup | `&$force_tfasetup` |
| integrate_verify_tfa | `$id_member`, `$user_settings` |
| integrate_user_info | |
| integrate_load_min_user_settings_columns | `&$columns_to_load` |
| integrate_load_min_user_settings | `&$user_info_min` |
| integrate_load_board | `&$custom_column_selects`, `&$custom_column_parameters` |
| integrate_board_info | `&$board_info`, `$row` |
| integrate_load_member_data | `&$select_columns`, `&$select_tables`, `&$set` |
| integrate_member_context | `&$memberContext[$user]`, `$user`, `$display_custom_fields` |
| [integrate_pre_load_theme](/hooks/integrate-pre-load-theme) | `&$id_theme` |
| [integrate_simple_actions](/hooks/integrate-simple-actions) | `&$simpleActions`, `&$simpleAreas`, `&$simpleSubActions`, `&$extraParams`, `&$xmlActions` |
| integrate_theme_include | |
| [integrate_load_theme](/hooks/integrate-load-theme) | |
| integrate_word_censor | `&$text` (^2.1.2) |
| pre_cache_quick_get | `&$key`, `&$file`, `&$function`, `&$params`, `&$level` |
| post_cache_quick_get | `&$cache_block` |
| cache_put_data | `&$key`, `&$value`, `&$ttl` |
| cache_get_data | `&$key`, `&$ttl`, `&$value` |
| integrate_clean_cache | |
| integrate_set_avatar_data | `&$image`, `&$data` |

## Sources/Logging.php

| Хук | Параметры |
|-----|-----------|
| integrate_log_types | `&$log_types` |

## Sources/LogInOut.php

| Хук | Параметры |
|-----|-----------|
| integrate_validate_login | `$_POST['user']`, `isset($_POST['passwrd']) ? $_POST['passwrd'] : null`, `$modSettings['cookieTime']`, `true` |
| integrate_other_passwords | `&$other_passwords` |
| integrate_login | `$user_settings['member_name']`, `null`, `$modSettings['cookieTime']` |
| integrate_logout | `$user_settings['member_name']` |

## Sources/ManageAttachments.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_attachments | `&$subActions` |
| integrate_modify_attachment_settings | `&$config_vars` |
| integrate_save_attachment_settings | |
| integrate_modify_avatar_settings | `&$config_vars` |
| integrate_save_avatar_settings | |
| integrate_attachments_browse | `&$listOptions`, `&$titles` |
| integrate_attachment_remove | `&$filesRemoved`, `$attachments` |
| integrate_remove_attachments | `$attach` |
| integrate_repair_attachments_nomsg | `&$ignore_ids`, `$_GET['substep']`, `$_GET['substep'] + 500` |
| integrate_approve_attachments | `$attachments` |

## Sources/ManageBans.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_bans | `&$subActions` |
| integrate_load_addtional_ip_ban | `&$search_list` |

## Sources/ManageBoards.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_boards | `&$subActions` |
| integrate_boards_main | |
| integrate_edit_category | |
| integrate_edit_board | |
| integrate_modify_board_settings | `&$config_vars` |
| integrate_save_board_settings | |

## Sources/ManageCalendar.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_calendar | `&$subActions` |
| integrate_modify_calendar_settings | `&$config_vars` |
| integrate_save_calendar_settings | |

## Sources/ManageLanguages.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_languages | `&$subActions` |
| integrate_language_settings | `&$config_vars` |
| integrate_save_language_settings | `&$config_vars` |
| integrate_modifylanguages | `&$themes`, `&$lang_dirs`, `&$allows_add_remove`, `&$additional_string_types` |
| integrate_language_edit_helptext | `&$special_groups` |

## Sources/ManageMail.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_mail | `&$subActions` |
| integrate_modify_mail_settings | `&$config_vars` |
| integrate_save_mail_settings | |

## Sources/ManageMaintenance.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_maintenance | `&$subActions` |
| integrate_convert_msgbody | `$body_type` |

## Sources/ManageMembergroups.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_membergroups | `&$subActions` |
| integrate_pre_add_membergroup | |
| integrate_add_membergroup | `$id_group`, `$postCountBasedGroup` |
| integrate_save_membergroup | `(int $_REQUEST['group']` |
| integrate_view_membergroup | |
| integrate_modify_membergroup_settings | `&$config_vars` |
| integrate_save_membergroup_settings | |

## Sources/ManageMembers.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_members | `&$subActions` |
| integrate_view_members_params | `&$params` |
| integrate_activate | `$member['username']` |

## Sources/ManageNews.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_news | `&$subActions` |
| integrate_modify_news_settings | `&$config_vars` |
| integrate_save_news_settings | |

## Sources/ManagePaid.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_subscriptions | `&$subActions` |
| integrate_delete_subscription | `$context['sub_id']` |
| integrate_save_subscription | `($context['action_type'] == 'add' ? $id_subscribe : $context['sub_id'])`, `$_POST['name']`, `$_POST['desc']`, `$isActive`, `$span`, `$cost`, `$_POST['prim_group']`, `$addgroups`, `$isRepeatable`, `$allowpartial`, `$emailComplete`, `$reminder` |

## Sources/ManagePermissions.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_permissions | `&$subActions` |
| integrate_modify_permission_settings | `&$config_vars` |
| integrate_save_permission_settings | |
| integrate_load_permission_levels | `&$groupLevels`, `&$boardLevels` |
| [integrate_load_permissions](/hooks/integrate-load-permissions) | `&$permissionGroups`, `&$permissionList`, `&$leftPermissionGroups`, `&$hiddenPermissions`, `&$relabelPermissions` |
| integrate_load_illegal_permissions | |
| integrate_load_illegal_guest_permissions | |
| integrate_post_moderation_mapping | `&$mappings` |

## Sources/ManagePosts.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_posts | `&$subActions` |
| integrate_save_censors | `&$updates` |
| integrate_censors | |
| integrate_modify_post_settings | `&$config_vars` |
| integrate_save_post_settings | |
| integrate_modify_topic_settings | `&$config_vars` |
| integrate_save_topic_settings | |

## Sources/ManageRegistration.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_registrations | `&$subActions` |
| integrate_modify_registration_settings | `&$config_vars` |
| integrate_save_registration_settings | |

## Sources/ManageScheduledTasks.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_scheduled_tasks | `&$subActions` |
| integrate_scheduled_tasks_settings | `&$config_vars` |
| integrate_save_scheduled_tasks_settings | `&$save_vars` |

## Sources/ManageSearch.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_search | `&$subActions` |
| integrate_modify_search_settings | `&$config_vars` |
| integrate_save_search_settings | |
| integrate_modify_search_weights | `&$factors` |
| integrate_save_search_weights | |

## Sources/ManageSearchEngines.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_search_engines | `&$subActions` |
| integrate_modify_search_engine_settings | `&$config_vars` |
| integrate_save_search_engine_settings | |
| integrate_robots_txt_rules | `&$rules` |

## Sources/ManageServer.php

| Хук | Параметры |
|-----|-----------|
| integrate_server_settings | `&$subActions` |
| integrate_general_settings | `&$config_vars` |
| integrate_save_general_settings | |
| integrate_database_settings | `&$config_vars` |
| integrate_save_database_settings | |
| integrate_cookie_settings | `&$config_vars` |
| integrate_save_cookie_settings | |
| integrate_general_security_settings | `&$config_vars` |
| integrate_save_general_security_settings | |
| integrate_modify_cache_settings | `&$config_vars` |
| integrate_save_cache_settings | |
| integrate_loadavg_settings | `&$config_vars` |
| integrate_save_loadavg_settings | |
| integrate_prepare_db_settings | `&$config_vars` |

## Sources/ManageSettings.php

| Хук | Параметры |
|-----|-----------|
| integrate_modify_features | `&$subActions` |
| integrate_modify_modifications | `&$subActions` |
| integrate_modify_basic_settings | `&$config_vars` |
| integrate_save_basic_settings | |
| integrate_modify_bbc_settings | `&$config_vars` |
| integrate_save_bbc_settings | `$bbcTags` |
| integrate_layout_settings | `&$config_vars` |
| integrate_save_layout_settings | |
| integrate_likes_settings | `&$config_vars` |
| integrate_save_likes_settings | |
| integrate_mentions_settings | `&$config_vars` |
| integrate_save_mentions_settings | |
| integrate_warning_settings | `&$config_vars` |
| integrate_save_warning_settings | `&$save_vars` |
| integrate_spam_settings | `&$config_vars` |
| integrate_save_spam_settings | `&$save_vars` |
| integrate_signature_settings | `&$config_vars` |
| integrate_apply_signature_settings | `&$sig`, `$sig_limits`, `$disabledTags` |
| integrate_save_signature_settings | `&$sig_limits`, `&$bbcTags` |
| integrate_prune_settings | `&$config_vars`, `&$prune_toggle`, `false` |
| integrate_prune_settings | `&$savevar`, `&$prune_toggle`, `true` |
| integrate_general_mod_settings | `&$config_vars` |
| integrate_save_general_mod_settings | `&$save_vars` |

## Sources/ManageSmileys.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_smileys | `&$subActions` |
| integrate_modify_smiley_settings | `&$config_vars` |
| integrate_save_smiley_settings | |

## Sources/Memberlist.php

| Хук | Параметры |
|-----|-----------|
| integrate_memberlist_buttons | |

## Sources/Mentions.php

| Хук | Параметры |
|-----|-----------|
| mention_insert_`{тип контента}` | `$content_id`, `&$members` |
| mention_insert_quote | |
| mention_insert_msg | |

## Sources/MessageIndex.php

| Хук | Параметры |
|-----|-----------|
| integrate_pre_messageindex | `&$sort_methods`, `&$sort_methods_table` |
| integrate_message_index | `&$message_index_selects`, `&$message_index_tables`, `&$message_index_parameters`, `&$message_index_wheres`, `&$topic_ids` |
| integrate_quick_mod_actions | |
| [integrate_messageindex_buttons](/lessons/kak-dobavit-knopku#h-1) | `&$context['normal_buttons']` |

## Sources/ModerationCenter.php

| Хук | Параметры |
|-----|-----------|
| integrate_mod_centre_blocks | `&$valid_blocks` |
| integrate_warning_log_actions | `&$subActions` |

## Sources/Modlog.php

| Хук | Параметры |
|-----|-----------|
| integrate_viewModLog | `&$listOptions`, `&$moderation_menu_name` |

## Sources/MoveTopic.php

| Хук | Параметры |
|-----|-----------|
| integrate_movetopic2_end | |

## Sources/News.php

| Хук | Параметры |
|-----|-----------|
| integrate_xmlfeeds | `&$subActions` |
| integrate_xml_data | `&$xml_data`, `&$feed_meta`, `&$namespaces`, `&$extraFeedTags`, `&$forceCdataKeys`, `&$nsKeys`, `$xml_format`, `$_GET['sa']`, `&$doctype` |
| integrate_fix_url | `&$val` |

## Sources/PackageGet.php

| Хук | Параметры |
|-----|-----------|
| integrate_package_get | `&$subActions` |
| integrate_package_download | |
| integrate_package_upload | |

## Sources/Packages.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_packages | `&$subActions` |
| integrate_modification_types | |
| integrate_packages_sort_id | `&$sort_id`, `&$packages` |

## Sources/PersonalMessage.php

| Хук | Параметры |
|-----|-----------|
| integrate_conversation_buttons | |
| integrate_prepare_pm_context | `&$output`, `&$message`, `$counter` |
| integrate_search_pm_context | |
| integrate_pm_post | |
| integrate_pm_error | |

## Sources/Poll.php

| Хук | Параметры |
|-----|-----------|
| integrate_poll_vote | `&$row['id_poll']`, `&$pollOptions` |
| integrate_poll_add_edit | `$bcinfo['id_poll']`, `$isEdit` |
| integrate_poll_remove | `$pollID` |

## Sources/Post.php

| Хук | Параметры |
|-----|-----------|
| integrate_post_start | |
| integrate_preview_post | `&$form_message`, `&$form_subject` |
| integrate_post_errors | `&$post_errors`, `&$minor_errors`, `$form_message`, `$form_subject` |
| [integrate_post_end](/hooks/integrate-post-end) | |
| integrate_post2_start | `&$post_errors` |
| integrate_post2_pre | `&$post_errors` |
| integrate_poll_add_edit | `$id_poll`, `false` |
| integrate_post2_end | |
| integrate_getTopic_previous_post | `&$row` |
| integrate_post_JavascriptModify | `&$post_errors`, `$row` |
| integrate_jsmodify_xml | |

## Sources/PostModeration.php

| Хук | Параметры |
|-----|-----------|
| integrate_post_moderation | `&$subActions` |

## Sources/Profile-Actions.php

| Хук | Параметры |
|-----|-----------|
| integrate_activate | `$user_profile[$memID]['member_name']` |

## Sources/Profile-Modify.php

| Хук | Параметры |
|-----|-----------|
| integrate_reset_pass | `$cur_profile['member_name']`, `$value`, `$_POST['passwrd1']` |
| integrate_load_profile_fields | `&$profile_fields` |
| integrate_setup_profile_context | `&$fields` |
| integrate_save_custom_profile_fields | `&$changes`, `&$log_changes`, `&$errors`, `$returnErrors`, `$memID`, `$area`, `$sanitize`, `&$deletes` |
| integrate_remove_buddy | `$memID` |
| integrate_add_buddies | `$memID`, `&$new_buddies` |
| integrate_view_buddies | `$memID` |
| integrate_theme_options | |
| integrate_alert_types | `&$alert_types`, `&$group_options` |
| integrate_profile_profileSaveGroups | `$value`, `$additional_groups` |
| before_profile_save_avatar | `&$value` |
| after_profile_save_avatar | |

## Sources/Profile-View.php

| Хук | Параметры |
|-----|-----------|
| integrate_fetch_alerts | `&$alerts`, `&$formats` |
| integrate_show_alert | `&$alert`, `&$link` |
| integrate_profile_showPosts | |
| integrate_profile_stats | `$memID`, `&$context['text_stats']` |
| integrate_profile_trackip | `$ip_string`, `$ip_var` |

## Sources/Profile.php

| Хук | Параметры |
|-----|-----------|
| integrate_profile_areas | `&$profile_areas` |
| integrate_pre_profile_areas | `&$profile_areas` (считается устаревшим с 2.1.4, используйте хук выше) |
| integrate_verify_password | `$cur_profile['member_name']`, `$password`, `false`, `true` |
| integrate_profile_save | `&$profile_vars`, `&$post_errors`, `$memID`, `$cur_profile`, `$current_area` |
| integrate_reset_pass | `$cur_profile['member_name']`, `$cur_profile['member_name']`, `$_POST['passwrd2']` |
| integrate_profile_popup | `&$profile_items` |
| integrate_load_custom_profile_fields | `$memID`, `$area` |

## Sources/Recent.php

| Хук | Параметры |
|-----|-----------|
| integrate_recent_RecentPosts | |
| integrate_recent_buttons | |
| integrate_unread_list | |

## Sources/Register.php

| Хук | Параметры |
|-----|-----------|
| integrate_activate | `$regOptions['username']` |
| integrate_activate | `$row['member_name']` |

## Sources/Reminder.php

| Хук | Параметры |
|-----|-----------|
| integrate_reset_pass | `$username`, `$username`, `$_POST['passwrd1']` |
| integrate_reset_pass | `$row['member_name']`, `$row['member_name']`, `$_POST['passwrd1']` |

## Sources/RemoveTopic.php

| Хук | Параметры |
|-----|-----------|
| integrate_remove_topics_before | `$topics`, `$recycle_board` |
| integrate_remove_topics | `$topics` |
| integrate_pre_remove_message | `$message`, `$decreasePostCount`, `$row` |
| integrate_remove_message | `$message` |

## Sources/Reports.php

| Хук | Параметры |
|-----|-----------|
| integrate_report_types | |
| integrate_report_buttons | |
| integrate_reports_boardperm | `&$disabled_permissions` |
| integrate_reports_groupperm | `&$disabled_permissions` |

## Sources/ScheduledTasks.php

| Хук | Параметры |
|-----|-----------|
| integrate_daily_maintenance | |
| integrate_daily_digest_lang | `&$langtxt`, `$lang` |
| integrate_daily_digest_email | `&$email`, `$types`, `$notify_types`, `$langtxt` |
| integrate_weekly_maintenance | |

## Sources/Search.php

| Хук | Параметры |
|-----|-----------|
| integrate_search | |
| integrate_search_weights | `&$weight_factors` |
| integrate_search_sort_columns | `&$sort_columns` |
| integrate_search_params | `&$search_params` |
| integrate_search_blacklisted_words | `&$blacklisted_words` |
| integrate_search_errors | |
| integrate_subject_only_search_query | `&$subject_query`, `&$subject_query_params` |
| integrate_subject_search_query | `&$subject_query` |
| integrate_main_search_query | `&$main_query` |
| integrate_search_message_list | `&$msg_list`, `&$posters` |
| integrate_quick_mod_actions_search | |
| integrate_search_message_context | `&$output`, `&$message`, `$counter` |

## Sources/Security.php

| Хук | Параметры |
|-----|-----------|
| integrate_validateSession | `&$types` |
| integrate_verify_password | `$user_info['username']`, `$_POST[$type . '_pass']`, `false`, `true` |
| integrate_post_ban_permissions | `&$denied_permissions` |
| integrate_warn_permissions | `$permission_change` |
| integrate_allowed_to_general | `&$user_permissions`, `$permission` |
| integrate_allowed_to_board | `&$return`, `$permission`, `$boards`, `$any` |
| integrate_heavy_permissions_session | `&$heavy_permissions` |
| integrate_boards_allowed_to | `&$boards`, `$deny_boards`, `$permissions`, `$check_access`, `$simple` |
| integrate_spam_protection | `&$timeOverrides` |

## Sources/Session.php

| Хук | Параметры |
|-----|-----------|
| [integrate_load_session](/hooks/integrate-load-session) | |
| integrate_session_handlers | |

## Sources/ShowAttachments.php

| Хук | Параметры |
|-----|-----------|
| integrate_pre_download_request | |
| integrate_download_request | `&$attachRequest` |
| integrate_download_headers | |

## Sources/SplitTopics.php

| Хук | Параметры |
|-----|-----------|
| integrate_split_topic | `$split1`, `$split2`, `$new_subject`, `$id_board` |
| integrate_merge_topic | `$merged_topic`, `$updated_topics`, `$deleted_topics`, `$deleted_polls` |

## Sources/Stats.php

| Хук | Параметры |
|-----|-----------|
| integrate_forum_stats | |

## Sources/Subs-Admin.php

| Хук | Параметры |
|-----|-----------|
| integrate_update_settings_file | `&$settings_defs` |

## Sources/Subs-Attachments.php

| Хук | Параметры |
|-----|-----------|
| integrate_attachment_upload | |
| integrate_createAttachment | `&$attachmentOptions`, `&$attachmentInserts` |
| integrate_assign_attachments | `&$attachIDs`, `&$msgID` |
| integrate_pre_parseAttachBBC | `$attachID`, `$msgID` |
| integrate_post_parseAttachBBC | `&$attachContext` |

## Sources/Subs-Auth.php

| Хук | Параметры |
|-----|-----------|
| integrate_cookie_data | `$data`, `&$custom_data` |
| integrate_validateSession | `&$types` |
| integrate_reset_pass | `$old_user`, `$user`, `$newPassword` |
| integrate_validate_username | `$username`, `&$errors` |
| integrate_mod_cache | |
| integrate_cookie | `$name`, `$value`, `$expire`, `$path`, `$domain`, `$secure`, `$httponly` |

## Sources/Subs-BoardIndex.php

| Хук | Параметры |
|-----|-----------|
| integrate_pre_boardindex | `&$board_index_selects`, `&$board_index_parameters` |
| integrate_boardindex_board | `&$this_category`, `$row_board` |
| integrate_getboardtree | `$boardIndexOptions`, `&$categories` |
| integrate_getboardtree | `$boardIndexOptions`, `&$this_category` |

## Sources/Subs-Boards.php

| Хук | Параметры |
|-----|-----------|
| integrate_pre_modify_board | `$id`, `&$boardOptions` |
| integrate_modify_board | `$id`, `$boardOptions`, `&$boardUpdates`, `&$boardUpdateParameters` |
| integrate_create_board | `&$boardOptions`, `&$board_columns`, `&$board_parameters` |
| integrate_delete_board | `$boards_to_remove`, `&$moveChildrenTo` |
| integrate_pre_boardtree | `&$boardColumns`, `&$boardParameters`, `&$boardJoins`, `&$boardWhere`, `&$boardOrder` |
| integrate_boardtree_board | `$row` |

## Sources/Subs-Calendar.php

| Хук | Параметры |
|-----|-----------|
| integrate_create_event | `&$eventOptions`, `&$event_columns`, `&$event_parameters` |
| integrate_modify_event | `$event_id`, `&$eventOptions`, `&$event_columns`, `&$event_parameters` |
| integrate_remove_event | `$event_id` |

## Sources/Subs-Categories.php

| Хук | Параметры |
|-----|-----------|
| integrate_pre_modify_category | `$cat_id`, `&$catOptions` |
| integrate_modify_category | `$cat_id`, `&$catUpdates`, `&$catParameters` |
| integrate_create_category | `&$catOptions`, `&$cat_columns`, `&$cat_parameters` |
| integrate_delete_category | `$categories`, `&$moveBoardsTo` |

## Sources/Subs-Editor.php

| Хук | Параметры |
|-----|-----------|
| integrate_load_message_icons | `&$icons` |
| integrate_bbc_buttons | `&$context['bbc_tags']`, `&$editor_tag_map` |
| integrate_sceditor_options | `&$sce_options` |
| integrate_create_control_verification_pre | `&$verificationOptions`, `$do_test` |
| integrate_create_control_verification_test' | `$thisVerification`, `&$verification_errors` |
| integrate_create_control_verification_refresh' | `$thisVerification` |
| integrate_create_control_verification_post' | `&$verification_errors`, `$do_test` |
| integrate_autosuggest | `&$searchTypes` |

## Sources/Subs-List.php
| Хук | Параметры | Где определяется |
|-----|-----------|------------------|
| integrate\_`{id списка}` | `&$listOptions` | |
| integrate_group_lists | `&$listOptions` | Groups.php |
| integrate_group_request_list | `&$listOptions` | Groups.php |
| integrate_file_list | `&$listOptions` | ManageAttachments.php |
| integrate_attach_paths | `&$listOptions` | ManageAttachments.php |
| integrate_base_paths | `&$listOptions` | ManageAttachments.php |
| integrate_ban_list | `&$listOptions` | ManageBans.php |
| integrate_ban_items | `&$listOptions` | ManageBans.php |
| integrate_ban_trigger_list | `&$listOptions` | ManageBans.php |
| integrate_ban_log | `&$listOptions` | ManageBans.php |
| integrate_holiday_list | `&$listOptions` | ManageCalendar.php |
| integrate_smf_languages | `&$listOptions` | ManageLanguages.php |
| integrate_lang_main_files_list | `&$listOptions` | ManageLanguages.php |
| integrate_language_list | `&$listOptions` | ManageLanguages.php |
| integrate_mail_queue | `&$listOptions` | ManageMail.php |
| integrate_list_integration_hooks | `&$listOptions` | ManageMaintenance.php |
| integrate_regular_membergroups_list | `&$listOptions` | ManageMembergroups.php |
| integrate_post_count_membergroups_list | `&$listOptions` | ManageMembergroups.php |
| integrate_member_list | `&$listOptions` | ManageMembers.php |
| integrate_approve_list | `&$listOptions` | ManageMembers.php |
| integrate_news_lists | `&$listOptions` | ManageNews.php |
| integrate_subscription_list | `&$listOptions` | ManagePaid.php |
| integrate_subscribed_users_list | `&$listOptions` | ManagePaid.php |
| integrate_scheduled_tasks | `&$listOptions` | ManageScheduledTasks.php |
| integrate_task_log | `&$listOptions` | ManageScheduledTasks.php |
| integrate_spider_list | `&$listOptions` | ManageSearchEngines.php |
| integrate_spider_logs | `&$listOptions` | ManageSearchEngines.php |
| integrate_spider_stat_list | `&$listOptions` | ManageSearchEngines.php |
| integrate_standard_profile_fields | `&$listOptions` | ManageSettings.php |
| integrate_custom_profile_fields | `&$listOptions` | ManageSettings.php |
| integrate_smiley_set_list | `&$listOptions` | ManageSmileys.php |
| integrate_smiley_list | `&$listOptions` | ManageSmileys.php |
| integrate_message_icon_list | `&$listOptions` | ManageSmileys.php |
| integrate_watch_user_list | `&$listOptions` | ModerationCenter.php |
| integrate_warning_list | `&$listOptions` | ModerationCenter.php |
| integrate_warning_template_list | `&$listOptions` | ModerationCenter.php |
| integrate_moderation_log_list | `&$listOptions` | Modlog.php |
| integrate_packages_lists_modification | `&$listOptions` | Packages.php |
| integrate_packages_lists_avatar | `&$listOptions` | Packages.php |
| integrate_packages_lists_language | `&$listOptions` | Packages.php |
| integrate_packages_lists_unknown | `&$listOptions` | Packages.php |
| integrate_mc_unapproved_attach | `&$listOptions` | PostModeration.php |
| integrate_view_warnings | `&$listOptions` | Profile-Actions.php |
| integrate_topic_notification_list | `&$listOptions` | Profile-Modify.php |
| integrate_board_notification_list | `&$listOptions` | Profile-Modify.php |
| integrate_attachments | `&$listOptions` | Profile-View.php |
| integrate_unwatched_topics | `&$listOptions` | Profile-View.php |
| integrate_track_user_list | `&$listOptions` | Profile-View.php |
| integrate_track_message_list | `&$listOptions` | Profile-View.php |
| integrate_track_user_list | `&$listOptions` | Profile-View.php |
| integrate_track_logins_list | `&$listOptions` | Profile-View.php |
| integrate_edit_list | `&$listOptions` | Profile-View.php |
| integrate_request_list | `&$listOptions` | Profile-View.php |
| integrate_view_warnings | `&$listOptions` | Profile-View.php |
| integrate_moderation_actions_list | `&$listOptions` | ReportedContent.php |
| integrate_restore_file_permissions | `&$listOptions` | Subs-Package.php |

## Sources/Subs-Membergroups.php

| Хук | Параметры |
|-----|-----------|
| integrate_delete_membergroups | `$groups` |
| integrate_add_members_to_group | `$members`, `$group`, `&$group_names` |

## Sources/Subs-Members.php

| Хук | Параметры |
|-----|-----------|
| integrate_delete_members | `$users` |
| integrate_register_check | `&$regOptions`, `&$reg_errors` |
| integrate_register | `&$regOptions`, `&$theme_vars`, `&$knownInts`, `&$knownFloats` |
| integrate_post_register | `&$regOptions`, `&$theme_vars`, `&$memberID` |
| integrate_register_after | `$regOptions`, `$memberID` |
| integrate_reattribute_posts | `$memID`, `$email`, `$membername`, `$post_count`, `&$updated` |

## Sources/Subs-MembersOnline.php

| Хук | Параметры |
|-----|-----------|
| integrate_online_stats | `&$membersOnlineStats` |

## Sources/Subs-Post.php

| Хук | Параметры |
|-----|-----------|
| integrate_preparsecode | `&$message`, `$previewing` |
| integrate_unpreparsecode | `&$message` |
| integrate_outgoing_email | `&$subject`, `&$message`, `&$headers`, `&$to_array`, `true` |
| integrate_personal_message | `&$recipients`, `&$from`, `&$subject`, `&$message` |
| integrate_personal_message_after | `&$id_pm`, `&$log`, `&$recipients`, `&$from`, `&$subject`, `&$message` |
| integrate_create_post | `&$msgOptions`, `&$topicOptions`, `&$posterOptions`, `&$message_columns`, `&$message_parameters` |
| integrate_after_create_post | `$msgOptions`, `$topicOptions`, `$posterOptions`, `$message_columns`, `$message_parameters` |
| integrate_before_create_topic | `&$msgOptions`, `&$topicOptions`, `&$posterOptions`, `&$topic_columns`, `&$topic_parameters` |
| integrate_create_topic | `&$msgOptions`, `&$topicOptions`, `&$posterOptions` |
| integrate_modify_topic | `&$topics_columns`, `&$update_parameters`, `&$msgOptions`, `&$topicOptions`, `&$posterOptions` |
| integrate_modify_post | `&$messages_columns`, `&$update_parameters`, `&$msgOptions`, `&$topicOptions`, `&$posterOptions`, `&$messageInts` |
| integrate_after_approve_posts | `$approve`, `$msgs`, `$topic_changes`, `$member_post_changes` |

## Sources/Subs-Themes.php

| Хук | Параметры |
|-----|-----------|
| integrate_get_single_theme | `&$themeValues`, `$id` |
| integrate_get_all_themes | `&$themeValues`, `$enable_only` |
| integrate_get_installed_themes | `&$themeValues` |
| integrate_theme_install | `&$context['to_install']`, `$id_theme` |

## Sources/Subs-Timezones.php

| Хук | Параметры |
|-----|-----------|
| integrate_metazones | `&$tzid_metazones`, `$when` |
| integrate_country_timezones | `&$sorted_tzids`, `$country_code`, `$when` |
| integrate_timezone_fallbacks | `&$fallbacks`, `&$missing`, `$tzids`, `$when` |

## Sources/Subs.php

| Хук | Параметры |
|-----|-----------|
| integrate_change_member_data | `$member_names`, `$var`, `&$data[$var]`, `&$knownInts`, `&$knownFloats` |
| integrate_pre_parsebbc | `&$message`, `&$smileys`, `&$cache_id`, `&$parse_tags` |
| integrate_bbc_codes | `&$codes`, `&$no_autolink_tags` |
| integrate_bbc_print | `&$disabled` |
| integrate_post_parsebbc | `&$message`, `&$smileys`, `&$cache_id`, `&$parse_tags` |
| integrate_smileys | `&$smileyPregSearch`, `&$smileyPregReplacements` |
| integrate_proxy | `$url`, `&$proxied_url` |
| integrate_redirect | `&$setLocation`, `&$refresh`, `&$permanent` |
| [integrate_buffer](/hooks/integrate-buffer) | `$buffers` |
| integrate_exit | `$do_footer` |
| [integrate_theme_context](/hooks/integrate-theme-context) | |
| integrate_security_files | `&$securityFiles` |
| integrate_pre_javascript_output | `&$do_deferred` |
| integrate_pre_css_output | |
| [integrate_menu_buttons](/hooks/integrate-menu-buttons) | `&$buttons` |
| [integrate_current_action](/hooks/integrate-current-action) | `&$current_action` |

## Sources/Themes.php

| Хук | Параметры |
|-----|-----------|
| integrate_manage_themes | `&$subActions` |
| integrate_theme_options | |
| integrate_theme_settings | |
| integrate_wrap_action | |

## Sources/ViewQuery.php

| Хук | Параметры |
|-----|-----------|
| integrate_egg_nog | |

## Sources/Who.php

| Хук | Параметры |
|-----|-----------|
| who_allowed | `&$allowedActions` |
| integrate_whos_online | `$actions` |
| whos_online_after | `&$urls`, `&$data` |
| integrate_credits | |

## Sources/Xml.php

| Хук | Параметры |
|-----|-----------|
| integrate_XMLhttpMain_subActions | `&$subActions` |

## Sources/tasks/Likes-Notify.php

| Хук | Параметры |
|-----|-----------|
| integrate_find_like_author | `$this->_details['content_type']`, `$this->_details['content_id']` |

## Themes/default/index.template.php

| Хук | Параметры |
|-----|-----------|
| integrate\_`{класс списка}`\_quickbuttons | `&$list_items` |
| integrate_pm_quickbuttons | `&$list_items` |
| [integrate_post_quickbuttons](/hooks/integrate-post-quickbuttons) | `&$list_items` |
| integrate_profile_alerts_quickbuttons | `&$list_items` |
| integrate_profile_drafts_quickbuttons | `&$list_items` |
| integrate_profile_showposts_quickbuttons | `&$list_items` |
| integrate_recent_quickbuttons | `&$list_items` |
| integrate_reported_members_quickbuttons | `&$list_items` |
| integrate_reported_posts_quickbuttons | `&$list_items` |
| integrate_unapproved_posts_quickbuttons | `&$list_items` |
| integrate_user_watch_post_quickbuttons | `&$list_items` |

## Themes/default/Post.template.php

| Хук | Параметры |
|-----|-----------|
| integrate_upload_template | |

---

Обозначения: `^x.y.z` — поддерживается, начиная с указанной версии
