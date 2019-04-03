# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SixAliveDetail(models.Model):
    detail_id = models.IntegerField(blank=True, null=True)
    p_id = models.IntegerField(blank=True, null=True)
    p_name = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "6alive_detail"


class Ad360ReplaceKeyword(models.Model):
    replace_keyword = models.CharField(max_length=255, blank=True, null=True)
    search_keyword = models.CharField(max_length=255, blank=True, null=True)
    do_percent = models.IntegerField(blank=True, null=True)
    cur_task_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ad360_replace_keyword"


class Ad360ReplaceKeyword2(models.Model):
    replace_keyword = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ad360_replace_keyword2"


class Ad360ReplaceKeywordPercent(models.Model):
    cur_task_id = models.IntegerField(blank=True, null=True)
    do_percent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ad360_replace_keyword_percent"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group_id", "permission_id"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type_id", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user_id", "group_id"),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user_id", "permission_id"),)


class Baidusearch(models.Model):
    keyword = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    search_times = models.PositiveIntegerField(blank=True, null=True)
    had_search_times = models.PositiveIntegerField(blank=True, null=True)
    rank = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    script_name = models.CharField(max_length=256)
    area = models.CharField(max_length=256, blank=True, null=True)
    total_page = models.IntegerField(blank=True, null=True)
    random_event_status = models.IntegerField(blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    onlysearch = models.IntegerField()
    terminal_type = models.IntegerField(blank=True, null=True)
    start_search_page = models.CharField(max_length=60, blank=True, null=True)
    search_rank = models.IntegerField(blank=True, null=True)
    click_rate = models.IntegerField(blank=True, null=True)
    real_url = models.CharField(max_length=255, blank=True, null=True)
    run_mode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baiduSearch"


class Baidusearchidmap(models.Model):
    taskid = models.PositiveIntegerField()
    search_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "baiduSearchIdMap"


class BaidusearchCopy1(models.Model):
    keyword = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    search_times = models.PositiveIntegerField(blank=True, null=True)
    had_search_times = models.PositiveIntegerField(blank=True, null=True)
    rank = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    script_name = models.CharField(max_length=256)
    area = models.CharField(max_length=256, blank=True, null=True)
    total_page = models.IntegerField(blank=True, null=True)
    random_event_status = models.IntegerField(blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    onlysearch = models.IntegerField()
    terminal_type = models.IntegerField(blank=True, null=True)
    start_search_page = models.CharField(max_length=60, blank=True, null=True)
    search_rank = models.IntegerField(blank=True, null=True)
    click_rate = models.IntegerField(blank=True, null=True)
    real_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baiduSearch_copy1"


class BaidusearchCopy2(models.Model):
    keyword = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    search_times = models.PositiveIntegerField(blank=True, null=True)
    had_search_times = models.PositiveIntegerField(blank=True, null=True)
    rank = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    script_name = models.CharField(max_length=256)
    area = models.CharField(max_length=256, blank=True, null=True)
    total_page = models.IntegerField(blank=True, null=True)
    random_event_status = models.IntegerField(blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    onlysearch = models.IntegerField()
    terminal_type = models.IntegerField(blank=True, null=True)
    start_search_page = models.CharField(max_length=60, blank=True, null=True)
    search_rank = models.IntegerField(blank=True, null=True)
    click_rate = models.IntegerField(blank=True, null=True)
    real_url = models.CharField(max_length=255, blank=True, null=True)
    run_mode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baiduSearch_copy2"


class BaidusearchRank(models.Model):
    server_id = models.IntegerField()
    baidusearch_id = models.IntegerField(
        db_column="baiduSearch_id", blank=True, null=True
    )  # Field name made lowercase.
    start_search_page = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baiduSearch_rank"


class BaidusearchRankCopy1(models.Model):
    server_id = models.IntegerField()
    baidusearch_id = models.IntegerField(
        db_column="baiduSearch_id", blank=True, null=True
    )  # Field name made lowercase.
    start_search_page = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baiduSearch_rank_copy1"


class BaidusearchServerStatus(models.Model):
    server_id = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    search_status = models.IntegerField(blank=True, null=True)
    awin_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baiduSearch_server_status"


class BaiduReplaceKeyword(models.Model):
    keyword = models.CharField(max_length=255, blank=True, null=True)
    task_group_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    found_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baidu_replace_keyword"


class BrowserSizeInfo(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    terminate_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = "browser_size_info"


class Cfgnotify(models.Model):
    check_order = models.IntegerField()
    notify_type = models.CharField(max_length=255)
    notify_name = models.CharField(max_length=255)
    notify_number = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cfgnotify"


class ClientUser(models.Model):
    user = models.CharField(max_length=255, blank=True, null=True)
    pwd = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "client_user"


class CmdMapping(models.Model):
    vm_cmd_id = models.IntegerField(unique=True)
    computer_cmd_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cmd_mapping"


class Comment(models.Model):
    content = models.CharField(max_length=255, blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "comment"


class CommentCopy1(models.Model):
    content = models.CharField(max_length=255, blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "comment_copy1"


class DemoChangearea1(models.Model):
    serverid = models.IntegerField()
    dangri = models.CharField(max_length=255, blank=True, null=True)
    shuangri = models.CharField(max_length=255, blank=True, null=True)
    now = models.CharField(max_length=255, blank=True, null=True)
    changetime = models.FloatField(blank=True, null=True)
    dangri1 = models.CharField(max_length=255, blank=True, null=True)
    shuangri1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "demo_changearea1"


class DemoServerProxyIp(models.Model):
    demo_server_id = models.IntegerField(blank=True, null=True)
    proxy_ip = models.CharField(max_length=255, blank=True, null=True)
    proxy_port = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "demo_server_proxy_ip"


class DialAreaBhq(models.Model):
    areaindex = models.IntegerField()
    area = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "dial_area_bhq"


class DialAreaFsy(models.Model):
    areaindex = models.IntegerField()
    area = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "dial_area_fsy"


class DialAreaUpptp(models.Model):
    areaindex = models.IntegerField()
    area = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "dial_area_upptp"


class DialAreaVpn(models.Model):
    areaindex = models.IntegerField()
    area = models.CharField(max_length=255)
    vpntype = models.IntegerField()

    class Meta:
        managed = False
        db_table = "dial_area_vpn"


class FirefoxUa(models.Model):
    useragent = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "firefox_ua"


class FirefoxUaCopy(models.Model):
    useragent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "firefox_ua_copy"


class GaySmall(models.Model):
    description = models.CharField(max_length=255)
    platform = models.CharField(max_length=255, blank=True, null=True)
    appname = models.CharField(max_length=255, blank=True, null=True)
    useragent = models.CharField(max_length=255, blank=True, null=True)
    z_id = models.IntegerField(blank=True, null=True)
    pandaweburl = models.CharField(
        db_column="pandaWebUrl", max_length=500, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "gay_small"


class GaySmall1(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    appname = models.CharField(max_length=255, blank=True, null=True)
    useragent = models.CharField(max_length=255, blank=True, null=True)
    z_id = models.IntegerField(blank=True, null=True)
    pandaweburl = models.CharField(
        db_column="pandaWebUrl", max_length=500, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "gay_small1"


class GaySmall2(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    appname = models.CharField(max_length=255, blank=True, null=True)
    useragent = models.CharField(max_length=255, blank=True, null=True)
    z_id = models.IntegerField(blank=True, null=True)
    pandaweburl = models.CharField(
        db_column="pandaWebUrl", max_length=500, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "gay_small2"


class IpArea(models.Model):
    ip_begin = models.CharField(max_length=255, blank=True, null=True)
    ip_end = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ip_area"


class IpServerid(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ip_serverid"


class IqyActivateCode(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "iqy_activate_code"


class IqyReginfo(models.Model):
    mobile_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    activate_code = models.CharField(max_length=255, blank=True, null=True)
    start_run_time = models.DateTimeField(blank=True, null=True)
    end_run_time = models.DateTimeField(blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    reg_time = models.DateTimeField(blank=True, null=True)
    act_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "iqy_reginfo"


class IqyReginfoCopy1(models.Model):
    mobile_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    activate_code = models.CharField(max_length=255, blank=True, null=True)
    start_run_time = models.DateTimeField(blank=True, null=True)
    end_run_time = models.DateTimeField(blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "iqy_reginfo_copy1"


class KeywordLib(models.Model):
    keyword = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    pandaweburl = models.CharField(
        db_column="pandaWebUrl", max_length=500, blank=True, null=True
    )  # Field name made lowercase.
    base_info = models.CharField(max_length=200, blank=True, null=True)
    count = models.CharField(max_length=20, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "keyword_lib"


class KeywordLib0(models.Model):
    keyword = models.CharField(max_length=255, blank=True, null=True)
    search_engine_type = models.CharField(max_length=255, blank=True, null=True)
    terminal_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "keyword_lib_0"


class KillProcess(models.Model):
    process_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "kill_process"


class KillProcessComputer(models.Model):
    process_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "kill_process_computer"


class LogTaskgroupLastid(models.Model):
    task_group_id = models.IntegerField(primary_key=True)
    parralle_times = models.IntegerField(blank=True, null=True)
    last_id = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "log_taskgroup_lastid"


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "phone_number"


class Profiles(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    terminal_type = models.IntegerField(blank=True, null=True)
    shortcut = models.CharField(max_length=255, blank=True, null=True)
    ua = models.CharField(max_length=255, blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    ua_pos = models.CharField(max_length=255, blank=True, null=True)
    ua_type = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "profiles"


class ProxyPing(models.Model):
    ip = models.CharField(max_length=255, blank=True, null=True)
    ping = models.FloatField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "proxy_ping"


class ProxySearchDetialDb(models.Model):
    web_name = models.CharField(max_length=255, blank=True, null=True)
    web_url = models.CharField(max_length=255, blank=True, null=True)
    db_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "proxy_search_detial_db"


class ProxySearchDetialSite(models.Model):
    web_name = models.CharField(max_length=255, blank=True, null=True)
    web_url = models.CharField(max_length=255, blank=True, null=True)
    db_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "proxy_search_detial_site"


class ProxySearchDetialUrl(models.Model):
    web_id = models.IntegerField()
    detail_url = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    task_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "proxy_search_detial_url"


class ProxyServerType(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    proxy_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "proxy_server_type"


class Rank(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    search_rowcount = models.IntegerField(blank=True, null=True)
    perpage_rowcount = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "rank"


class RankRearch1(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    search_rowcount = models.IntegerField(blank=True, null=True)
    perpage_rowcount = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "rank_rearch1"


class RestartProcess(models.Model):
    process_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "restart_process"


class RestartProcessComputer(models.Model):
    process_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "restart_process_computer"


class RouteIp(models.Model):
    ip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "route_ip"


class Search58(models.Model):
    keyword = models.CharField(max_length=255)
    run_times = models.IntegerField()
    ran_times = models.IntegerField()
    terminal_type = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255)
    not_found_times = models.IntegerField()
    not_found_total_times = models.IntegerField()
    area = models.CharField(max_length=255)
    server_id = models.IntegerField()
    vm_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "search58"


class Search58Searchidmap(models.Model):
    taskid = models.IntegerField()
    search_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "search58SearchIdMap"


class Search58Log(models.Model):
    keyword = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    update_time = models.DateTimeField()
    task_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "search58log"


class SiteIncludedCount(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    included_count = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "site_included_count"


class SiteShowTimes(models.Model):
    task_group_id = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    show_times = models.IntegerField(blank=True, null=True)
    click_gap = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "site_show_times"


class TaskIpErrorLog(models.Model):
    vm_cur_task_id = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    vpn_dial_log_id = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    cur_task_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "task_ip_error_log"


class TaskStatusRequest(models.Model):
    task_rid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    local_ip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "task_status_request"


class TaskgroupRuntimesMap(models.Model):
    runtimes_type_id = models.IntegerField(blank=True, null=True)
    task_group_id = models.IntegerField(unique=True, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "taskgroup_runtimes_map"


class TblSystemAuthority(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    route = models.CharField(max_length=150, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tbl_system_authority"


class TblSystemUser(models.Model):
    username = models.CharField(unique=True, max_length=20, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=150, blank=True, null=True)
    is_super = models.IntegerField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=20, blank=True, null=True)
    last_login_time = models.IntegerField(blank=True, null=True)
    curr_login_ip = models.CharField(max_length=20, blank=True, null=True)
    curr_login_time = models.IntegerField(blank=True, null=True)
    login_token = models.CharField(max_length=32, blank=True, null=True)
    create_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tbl_system_user"


class TblSystemUserAuthority(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    authority_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tbl_system_user_authority"


class TblWebConfig(models.Model):
    key = models.CharField(primary_key=True, max_length=30)
    value = models.CharField(max_length=1000, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tbl_web_config"


class Token(models.Model):
    token = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "token"


class UaScreenSize(models.Model):
    pcorwap = models.IntegerField()
    s1 = models.CharField(max_length=255, blank=True, null=True)
    s2 = models.CharField(max_length=255, blank=True, null=True)
    s3 = models.CharField(max_length=255, blank=True, null=True)
    s4 = models.CharField(max_length=255, blank=True, null=True)
    s5 = models.CharField(max_length=255, blank=True, null=True)
    s6 = models.CharField(max_length=255, blank=True, null=True)
    s7 = models.CharField(max_length=255, blank=True, null=True)
    s8 = models.CharField(max_length=255, blank=True, null=True)
    s9 = models.CharField(max_length=255, blank=True, null=True)
    s10 = models.CharField(max_length=255, blank=True, null=True)
    s11 = models.CharField(max_length=255, blank=True, null=True)
    s12 = models.CharField(max_length=255, blank=True, null=True)
    s13 = models.CharField(max_length=255, blank=True, null=True)
    s14 = models.CharField(max_length=255, blank=True, null=True)
    s15 = models.CharField(max_length=255, blank=True, null=True)
    s16 = models.CharField(max_length=255, blank=True, null=True)
    s17 = models.CharField(max_length=255, blank=True, null=True)
    s18 = models.CharField(max_length=255, blank=True, null=True)
    s19 = models.CharField(max_length=255, blank=True, null=True)
    s20 = models.CharField(max_length=255, blank=True, null=True)
    s21 = models.CharField(max_length=255, blank=True, null=True)
    s22 = models.CharField(max_length=255, blank=True, null=True)
    s23 = models.CharField(max_length=255, blank=True, null=True)
    s24 = models.CharField(max_length=255, blank=True, null=True)
    s25 = models.CharField(max_length=255, blank=True, null=True)
    s26 = models.CharField(max_length=255, blank=True, null=True)
    s27 = models.CharField(max_length=255, blank=True, null=True)
    s28 = models.CharField(max_length=255, blank=True, null=True)
    s29 = models.CharField(max_length=255, blank=True, null=True)
    s30 = models.CharField(max_length=255, blank=True, null=True)
    s31 = models.CharField(max_length=255, blank=True, null=True)
    s32 = models.CharField(max_length=255, blank=True, null=True)
    s33 = models.CharField(max_length=255, blank=True, null=True)
    s34 = models.CharField(max_length=255, blank=True, null=True)
    s35 = models.CharField(max_length=255, blank=True, null=True)
    s36 = models.CharField(max_length=255, blank=True, null=True)
    s37 = models.CharField(max_length=255, blank=True, null=True)
    s38 = models.CharField(max_length=255, blank=True, null=True)
    s39 = models.CharField(max_length=255, blank=True, null=True)
    s40 = models.CharField(max_length=255, blank=True, null=True)
    s41 = models.CharField(max_length=255, blank=True, null=True)
    s42 = models.CharField(max_length=255, blank=True, null=True)
    s43 = models.CharField(max_length=255, blank=True, null=True)
    s44 = models.CharField(max_length=255, blank=True, null=True)
    s45 = models.CharField(max_length=255, blank=True, null=True)
    s46 = models.CharField(max_length=255, blank=True, null=True)
    s47 = models.CharField(max_length=255, blank=True, null=True)
    s48 = models.CharField(max_length=255, blank=True, null=True)
    s49 = models.CharField(max_length=255, blank=True, null=True)
    s50 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ua_screen_size"


class UsedIpinfo1(models.Model):
    serverid = models.IntegerField()
    ip = models.TextField(blank=True, null=True)
    usetime = models.DateTimeField(blank=True, null=True)
    pingtime = models.IntegerField(blank=True, null=True)
    vmid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "used_ipinfo1"


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = "user"


class User2(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = "user2"


class UserMac(models.Model):
    mac = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user_mac"


class VerificationCodePlatform(models.Model):
    name = models.CharField(max_length=255)
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "verification_code_platform"


class VmAction(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    script = models.TextField()
    type = models.IntegerField(blank=True, null=True)
    to_continue = models.IntegerField()
    task_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "vm_action"
        unique_together = (("id", "task_id"),)


class VmActionTypeDetail(models.Model):
    type_id = models.IntegerField()
    actionids = models.CharField(max_length=120)
    weight = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_action_type_detail"


class VmActionTypeTimes(models.Model):
    type_id = models.IntegerField()
    set_name = models.CharField(max_length=20, blank=True, null=True)
    start_range = models.SmallIntegerField(blank=True, null=True)
    end_range = models.SmallIntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_action_type_times"


class VmAllotTask(models.Model):
    serverid = models.IntegerField(blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    task_group_id = models.IntegerField(blank=True, null=True)
    cur_task_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_allot_task"


class VmAllotTaskByServergroup(models.Model):
    server_group_id = models.IntegerField()
    task_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "vm_allot_task_by_servergroup"


class VmBrowserVersion(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    prefs_check_time = models.DateTimeField(blank=True, null=True)
    prefs_changed_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_browser_version"


class VmCmd(models.Model):
    id = models.IntegerField(primary_key=True)
    cmd = models.CharField(max_length=255)
    memo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_cmd"


class VmCurTask(models.Model):
    server_id = models.IntegerField()
    vm_id = models.IntegerField()
    # task_group_id = models.IntegerField()
    cur_task_id = models.IntegerField()
    cur_profile_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    ran_minutes = models.IntegerField(blank=True, null=True)
    oprcode = models.IntegerField(blank=True, null=True)
    ff_pids = models.CharField(max_length=255, blank=True, null=True)
    succ_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    terminal_type = models.IntegerField()
    standby_time = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    copy_cookie = models.IntegerField(blank=True, null=True)
    click_mode = models.IntegerField(blank=True, null=True)
    inter_time = models.SmallIntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    # task = models.ForeignKey("VmTask", related_name="task_stat", on_delete="CASSADE")
    task_group = models.ForeignKey(
        "VmTaskGroup", related_name="task_group", on_delete="CASSADE"
    )

    class Meta:
        managed = False
        db_table = "vm_cur_task"
        ordering = ("-start_time",)
        unique_together = (("id", "terminal_type"),)


class VmCurTaskHistory(models.Model):
    server_id = models.IntegerField()
    vm_id = models.IntegerField()
    task_group_id = models.IntegerField(blank=True, null=True)
    cur_task_id = models.IntegerField()
    cur_profile_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    ran_minutes = models.IntegerField(blank=True, null=True)
    oprcode = models.IntegerField(blank=True, null=True)
    sub_flag = models.IntegerField(blank=True, null=True)
    ff_pids = models.CharField(max_length=255, blank=True, null=True)
    succ_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    terminal_type = models.IntegerField()
    standby_time = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    copy_cookie = models.IntegerField(blank=True, null=True)
    click_mode = models.IntegerField(blank=True, null=True)
    inter_time = models.SmallIntegerField(blank=True, null=True)
    begin_ip = models.CharField(max_length=255, blank=True, null=True)
    begin_time = models.DateTimeField(blank=True, null=True)
    hot_ip = models.CharField(max_length=255, blank=True, null=True)
    hot_time = models.DateTimeField(blank=True, null=True)
    refresh_ip = models.CharField(max_length=255, blank=True, null=True)
    refresh_time = models.DateTimeField(blank=True, null=True)
    vpn_update_time = models.DateTimeField(blank=True, null=True)
    last_status_ip = models.CharField(max_length=255, blank=True, null=True)
    last_status_time = models.DateTimeField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    time_log = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.IntegerField(blank=True, null=True)
    mouse_type = models.CharField(max_length=255, blank=True, null=True)
    status2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_cur_task_history"
        unique_together = (("id", "terminal_type"),)


class VmCurTaskHistoryCopy1(models.Model):
    server_id = models.IntegerField()
    vm_id = models.IntegerField()
    task_group_id = models.IntegerField(blank=True, null=True)
    cur_task_id = models.IntegerField()
    cur_profile_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    ran_minutes = models.IntegerField(blank=True, null=True)
    oprcode = models.IntegerField(blank=True, null=True)
    ff_hwnd = models.IntegerField(blank=True, null=True)
    ff_pids = models.CharField(max_length=255, blank=True, null=True)
    succ_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    terminal_type = models.IntegerField()
    standby_time = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    copy_cookie = models.IntegerField(blank=True, null=True)
    click_mode = models.IntegerField(blank=True, null=True)
    inter_time = models.SmallIntegerField(blank=True, null=True)
    begin_ip = models.CharField(max_length=255, blank=True, null=True)
    begin_time = models.DateTimeField(blank=True, null=True)
    hot_ip = models.CharField(max_length=255, blank=True, null=True)
    hot_time = models.DateTimeField(blank=True, null=True)
    refresh_ip = models.CharField(max_length=255, blank=True, null=True)
    refresh_time = models.DateTimeField(blank=True, null=True)
    vpn_update_time = models.DateTimeField(blank=True, null=True)
    last_status_ip = models.CharField(max_length=255, blank=True, null=True)
    last_status_time = models.DateTimeField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    time_log = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_cur_task_history_copy1"
        unique_together = (("id", "terminal_type"),)


class VmCustom(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    tel_phone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.PositiveIntegerField(blank=True, null=True)
    order_times = models.PositiveIntegerField(blank=True, null=True)
    order_total_price = models.PositiveIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    qq = models.PositiveIntegerField(blank=True, null=True)
    wechat = models.CharField(max_length=50, blank=True, null=True)
    from_member_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_custom"


class VmDepartMember(models.Model):
    depart_id = models.PositiveIntegerField(blank=True, null=True)
    member_id = models.PositiveIntegerField(blank=True, null=True)
    position_job = models.PositiveIntegerField(blank=True, null=True)
    percentage = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True
    )
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_depart_member"


class VmDepartment(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    member_count = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_department"


class VmGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    groupname = models.CharField(max_length=45)
    quantity = models.PositiveSmallIntegerField()
    cur_vm_num = models.PositiveSmallIntegerField()
    status = models.IntegerField()
    type = models.IntegerField()
    groupid = models.PositiveIntegerField()
    wakeup_savestate = models.IntegerField(blank=True, null=True)
    savestate_time = models.DateTimeField()
    serverid = models.PositiveSmallIntegerField()
    last_status = models.IntegerField()
    startup_time = models.DateTimeField(blank=True, null=True)
    running_time = models.DateTimeField(blank=True, null=True)
    start_times = models.IntegerField()
    restart_times = models.IntegerField()
    exception_vmid = models.SmallIntegerField(blank=True, null=True)
    running_script = models.IntegerField()
    deprecated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_group"
        unique_together = (("id", "running_script"), ("groupid", "serverid"))


class VmInfo(models.Model):
    server_id = models.IntegerField(primary_key=True)
    vm_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    since_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_info"
        unique_together = (("server_id", "vm_id"),)


class VmIsdial(models.Model):
    vmid = models.IntegerField(blank=True, null=True)
    isdial = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=255)
    serverid = models.IntegerField()
    task_id = models.IntegerField(blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_isdial"


class VmList(models.Model):
    vm_id = models.IntegerField()
    vm_name = models.CharField(max_length=255)
    server_id = models.IntegerField()
    status = models.IntegerField()
    startup_time = models.DateTimeField(blank=True, null=True)
    shutdown_time = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField()
    update_time = models.DateTimeField()
    wssc_version = models.CharField(max_length=255, blank=True, null=True)
    warn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_list"


class VmNoProxyTaskUrl(models.Model):
    cur_task_id = models.IntegerField(blank=True, null=True)
    no_proxies_url = models.CharField(max_length=255, blank=True, null=True)
    open_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_no_proxy_task_url"


class VmOnekeyTask(models.Model):
    server_id = models.IntegerField()
    cmd_id = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_onekey_task"


class VmOprcode(models.Model):
    oprcode = models.AutoField(primary_key=True)
    server_id = models.IntegerField()
    group_id = models.IntegerField()
    task_id = models.IntegerField()
    status = models.CharField(max_length=255)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_oprcode"


class VmOrderDevelop(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    send_time = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    developer = models.IntegerField(blank=True, null=True)
    notice = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    verify_member = models.IntegerField(blank=True, null=True)
    verify_time = models.IntegerField(blank=True, null=True)
    set_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_order_develop"


class VmOrderInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    custom_id = models.PositiveIntegerField(blank=True, null=True)
    target = models.PositiveIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)
    start_time = models.PositiveIntegerField(blank=True, null=True)
    end_time = models.PositiveIntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    promote_id = models.IntegerField(blank=True, null=True)
    negotiation_id = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    attachment_path = models.CharField(max_length=255, blank=True, null=True)
    requires = models.CharField(max_length=255, blank=True, null=True)
    pay_way = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    has_pay = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pay_account = models.CharField(max_length=100, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    name_remark = models.CharField(max_length=1000, blank=True, null=True)
    from_member_id = models.IntegerField(blank=True, null=True)
    is_send = models.IntegerField(blank=True, null=True)
    send_developer = models.IntegerField(blank=True, null=True)
    develop_remark = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_order_info"


class VmOrderReason(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=1000, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    member_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_order_reason"


class VmParallelControl(models.Model):
    task_group_id = models.IntegerField()
    parallel_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = "vm_parallel_control"


class VmParallelControlInfo(models.Model):
    server_id = models.IntegerField(primary_key=True)
    task_group_id = models.IntegerField()
    allocated_num = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_parallel_control_info"
        unique_together = (("server_id", "task_group_id"),)


class VmPriv(models.Model):
    id = models.IntegerField(primary_key=True)
    priv = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_priv"


class VmProfiles(models.Model):
    server_id = models.IntegerField(primary_key=True)
    vm_id = models.IntegerField()
    profile_id = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    area = models.SmallIntegerField()
    iqy_tel_num = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_profiles"
        unique_together = (("server_id", "vm_id", "profile_id"),)


class VmProxyIpPort(models.Model):
    ip = models.CharField(max_length=255, blank=True, null=True)
    port = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    real_ip = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_proxy_ip_port"


class VmProxyIpPortTestArea(models.Model):
    ip = models.CharField(max_length=255, blank=True, null=True)
    port = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    real_ip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_proxy_ip_port_test_area"


class VmProxyServerArea(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_proxy_server_area"


class VmResetInfo(models.Model):
    server_id = models.IntegerField()
    vm_id = models.IntegerField()
    reset_times = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    running_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "vm_reset_info"


class VmResetStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    server_id = models.IntegerField()
    vm_id = models.IntegerField()
    status = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_reset_status"
        unique_together = (("server_id", "vm_id"),)


class VmRuntimesType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    times_one_day = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_runtimes_type"


class VmServerAllotStatus(models.Model):
    server_id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    ran_times = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "vm_server_allot_status"
        unique_together = (("server_id", "task_id", "create_time"),)


class VmServerGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    server_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_server_group"
        unique_together = (("id", "server_id"),)


class VmServerList(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=255)
    update_time = models.DateTimeField()
    name = models.CharField(max_length=255, blank=True, null=True)
    run_as_single = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    proxy_mode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_server_list"


class VmServerPoweroff(models.Model):
    server_id = models.IntegerField(primary_key=True)
    poweroff = models.IntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "vm_server_poweroff"


class VmSysDict(models.Model):
    key = models.CharField(max_length=25)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "vm_sys_dict"


class VmSystemAuthority(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    route = models.CharField(max_length=100, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    is_hidden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_system_authority"


class VmSystemMenu(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    route = models.CharField(max_length=50, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_system_menu"


class VmSystemUser(models.Model):
    username = models.CharField(unique=True, max_length=20, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    created_time = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=150, blank=True, null=True)
    is_super = models.IntegerField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=20, blank=True, null=True)
    last_login_time = models.IntegerField(blank=True, null=True)
    create_by = models.IntegerField(blank=True, null=True)
    login_token = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_system_user"


class VmSystemUserAuthority(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    authority_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_system_user_authority"


class VmTask(models.Model):
    id = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    script_file = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    terminal_type = models.IntegerField()
    user_type = models.SmallIntegerField()
    timeout = models.SmallIntegerField()
    is_ad = models.IntegerField(blank=True, null=True)
    inter_time = models.SmallIntegerField(blank=True, null=True)
    copy_cookie = models.IntegerField()
    rolling_times = models.IntegerField(blank=True, null=True)
    click_mode = models.IntegerField(blank=True, null=True)
    standby_time = models.CharField(max_length=4)
    gen_type = models.IntegerField()
    only_test = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    succ_target = models.IntegerField(blank=True, null=True)
    unpay_count = models.IntegerField(blank=True, null=True)
    should_refresh = models.IntegerField()
    script_time = models.IntegerField(blank=True, null=True)
    price_memo = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    open_timing = models.IntegerField(blank=True, null=True)
    close_timing = models.IntegerField(blank=True, null=True)
    aging = models.IntegerField(blank=True, null=True)
    last_start_time = models.IntegerField(blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    interval_times = models.SmallIntegerField(blank=True, null=True)
    interval_min = models.CharField(max_length=255, blank=True, null=True)
    ip_reuse_days = models.IntegerField(blank=True, null=True)
    is_show_task = models.IntegerField(blank=True, null=True)
    binding_areas = models.CharField(max_length=255, blank=True, null=True)
    is_single_task = models.IntegerField(blank=True, null=True)
    is_mv = models.IntegerField(blank=True, null=True)
    screenshot_type = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "vm_task"


class VmTaskAllotImpl(models.Model):
    id = models.IntegerField()
    task_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    allot_times = models.IntegerField()
    ran_times = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    templ_id = models.IntegerField()
    templ_sub_id = models.IntegerField()
    ran_times_lastday = models.IntegerField(blank=True, null=True)
    order_id = models.AutoField(primary_key=True)
    remedy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_allot_impl"


class VmTaskAllotImplTmp(models.Model):
    id = models.IntegerField()
    task_id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    allot_times = models.IntegerField()
    ran_times = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    templ_id = models.IntegerField()
    templ_sub_id = models.IntegerField()
    ran_times_lastday = models.IntegerField(blank=True, null=True)
    detail_id = models.IntegerField(blank=True, null=True)
    allot_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_allot_impl_tmp"
        unique_together = (("task_id", "id", "templ_id", "templ_sub_id"),)


class VmTaskAllotTempl(models.Model):
    id = models.IntegerField(primary_key=True)
    sub_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    percent = models.IntegerField()
    detail_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_allot_templ"
        unique_together = (("id", "sub_id"),)


class VmTaskAllotTemplDetail(models.Model):
    start_min = models.IntegerField()
    end_min = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    sub_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "vm_task_allot_templ_detail"
        unique_together = (("id", "sub_id"),)


class VmTaskCopy1(models.Model):
    id = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    script_file = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    terminal_type = models.IntegerField()
    user_type = models.SmallIntegerField()
    timeout = models.SmallIntegerField()
    is_ad = models.IntegerField(blank=True, null=True)
    inter_time = models.SmallIntegerField(blank=True, null=True)
    copy_cookie = models.IntegerField()
    rolling_times = models.IntegerField(blank=True, null=True)
    click_mode = models.IntegerField(blank=True, null=True)
    standby_time = models.CharField(max_length=4)
    gen_type = models.IntegerField()
    only_test = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    succ_target = models.IntegerField(blank=True, null=True)
    unpay_count = models.IntegerField(blank=True, null=True)
    should_refresh = models.IntegerField()
    script_time = models.IntegerField(blank=True, null=True)
    price_memo = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    open_timing = models.IntegerField(blank=True, null=True)
    close_timing = models.IntegerField(blank=True, null=True)
    aging = models.IntegerField(blank=True, null=True)
    last_start_time = models.IntegerField(blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    interval_times = models.SmallIntegerField(blank=True, null=True)
    interval_min = models.CharField(max_length=255, blank=True, null=True)
    ip_reuse_days = models.IntegerField(blank=True, null=True)
    is_show_task = models.IntegerField(blank=True, null=True)
    binding_areas = models.CharField(max_length=255, blank=True, null=True)
    is_single_task = models.IntegerField(blank=True, null=True)
    is_mv = models.IntegerField(blank=True, null=True)
    screenshot_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_copy1"


class VmTaskFrequency(models.Model):
    task_group_id = models.IntegerField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_frequency"


class VmTaskGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    # t_id = models.IntegerField()
    task_group_name = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    ran_times = models.IntegerField()
    templ_id = models.IntegerField(blank=True, null=True)
    ran_times_lastday = models.IntegerField(blank=True, null=True)
    times_start_range = models.IntegerField()
    times_end_range = models.IntegerField()
    allot_type = models.IntegerField()
    priority = models.IntegerField()
    task_start_time = models.DateTimeField(blank=True, null=True)
    task_latest_succ_time = models.DateTimeField(blank=True, null=True)
    allot_times = models.IntegerField()
    ranking = models.IntegerField(blank=True, null=True)
    task = models.ForeignKey("VmTask", on_delete="CASSADE")

    class Meta:
        managed = False
        db_table = "vm_task_group"
        # unique_together = (("id", "t_id"),)


class VmTaskGroupCopy1(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    task_group_name = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    ran_times = models.IntegerField()
    templ_id = models.IntegerField(blank=True, null=True)
    ran_times_lastday = models.IntegerField(blank=True, null=True)
    times_start_range = models.SmallIntegerField()
    times_end_range = models.SmallIntegerField()
    allot_type = models.IntegerField()
    priority = models.IntegerField()
    task_start_time = models.DateTimeField(blank=True, null=True)
    task_latest_succ_time = models.DateTimeField(blank=True, null=True)
    allot_times = models.IntegerField()
    ranking = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_group_copy1"
        unique_together = (("id", "task_id"),)


class VmTaskGroupCopy2(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    task_group_name = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    ran_times = models.IntegerField()
    templ_id = models.IntegerField(blank=True, null=True)
    ran_times_lastday = models.IntegerField(blank=True, null=True)
    times_start_range = models.IntegerField()
    times_end_range = models.IntegerField()
    allot_type = models.IntegerField()
    priority = models.IntegerField()
    task_start_time = models.DateTimeField(blank=True, null=True)
    task_latest_succ_time = models.DateTimeField(blank=True, null=True)
    allot_times = models.IntegerField()
    ranking = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_group_copy2"
        unique_together = (("id", "task_id"),)


class VmTaskGroupType(models.Model):
    type_id = models.IntegerField()
    task_group_id = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_group_type"


class VmTaskInterval(models.Model):
    task_id = models.IntegerField(primary_key=True)
    times = models.DateTimeField(blank=True, null=True)
    interval = models.SmallIntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_interval"


class VmTaskIpLog(models.Model):
    task_group_id = models.IntegerField(blank=True, null=True)
    cur_task_id = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    begin_ip = models.CharField(max_length=255, blank=True, null=True)
    hot_ip = models.CharField(max_length=255, blank=True, null=True)
    refresh_ip = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    vpn_update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_ip_log"


class VmTaskIpinfo(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    public_ip = models.CharField(max_length=255, blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_ipinfo"


class VmTaskLog(models.Model):
    oprcode = models.IntegerField(blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    a_time = models.DateTimeField(blank=True, null=True)
    b_time = models.DateTimeField(blank=True, null=True)
    c_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    log_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_log"


class VmTaskProfileLatest(models.Model):
    server_id = models.IntegerField(primary_key=True)
    vm_id = models.IntegerField()
    profile_id = models.IntegerField()
    task_id = models.IntegerField()
    task_type = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    re_enable_days = models.IntegerField(blank=True, null=True)
    oprcode = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    re_enable_hours = models.IntegerField(blank=True, null=True)
    terminal_type = models.IntegerField(blank=True, null=True)
    task_group_id = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_profile_latest"
        unique_together = (("server_id", "vm_id", "profile_id", "task_id"),)


class VmTaskProfileLog(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    task_type = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    log_time = models.DateTimeField(blank=True, null=True)
    re_enable_days = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    oprcode = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    re_enable_hours = models.IntegerField(blank=True, null=True)
    terminal_type = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_profile_log"


class VmTaskReenable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    re_enable_hour_start_range = models.IntegerField(blank=True, null=True)
    re_enable_hour_end_range = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_reenable"


class VmTaskRolling7(models.Model):
    task_id = models.IntegerField(primary_key=True)
    rolling_time = models.IntegerField()
    rolling_used_days = models.TextField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    task_group_id = models.IntegerField(blank=True, null=True)
    done = models.IntegerField()
    used_out_server_ids = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_rolling7"
        unique_together = (("task_id", "rolling_time"),)


class VmTaskRuntimesConfig(models.Model):
    task_group_id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    users_used_amount = models.IntegerField(blank=True, null=True)
    remained = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    allocated_server = models.CharField(max_length=2048, blank=True, null=True)
    allot_succ_times = models.IntegerField(blank=True, null=True)
    used_out_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_runtimes_config"
        unique_together = (("task_group_id", "day"),)


class VmTaskSearchadLog(models.Model):
    task_group_id = models.IntegerField(blank=True, null=True)
    cur_task_id = models.IntegerField(blank=True, null=True)
    tid = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_searchad_log"


class VmTaskStatus(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_status"


class VmTaskType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    re_enable_day_start_range = models.IntegerField(blank=True, null=True)
    re_enable_day_end_range = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_type"


class VmTaskValidcycle(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_task_validcycle"


class VmTimeTempl(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_time_templ"


class VmUpdateTask(models.Model):
    server_id = models.IntegerField()
    vm_id = models.IntegerField()
    cmd_id = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_update_task"


class VmUserDayStat(models.Model):
    day = models.CharField(primary_key=True, max_length=255)
    used = models.CharField(max_length=255)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_user_day_stat"


class VmUserRollingPos(models.Model):
    task_group_id = models.IntegerField(blank=True, null=True)
    cur_used_day = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_user_rolling_pos"


class VmUsers(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    terminal_type = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_access_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    modified = models.IntegerField(blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    mobile_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_users"


class VmUsersCopy(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    terminal_type = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_access_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_users_copy"


class VmWeekdayTimes(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    times_start_range = models.IntegerField(blank=True, null=True)
    times_end_range = models.IntegerField(blank=True, null=True)
    weekday = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vm_weekday_times"
        unique_together = (("task_id", "weekday"),)


class VpnChange2(models.Model):
    serverid = models.IntegerField(primary_key=True)
    want_change2 = models.IntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "vpn_change2"


class VpnDialLog(models.Model):
    area = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    change_2_time = models.DateTimeField(blank=True, null=True)
    change_1_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vpn_dial_log"


class VpnStatus(models.Model):
    serverid = models.SmallIntegerField()
    vmid = models.SmallIntegerField(blank=True, null=True)
    jobstatus = models.IntegerField(blank=True, null=True)
    vpnstatus = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    notify_pause = models.IntegerField()
    proxy_ip = models.CharField(max_length=255, blank=True, null=True)
    proxy_port = models.IntegerField(blank=True, null=True)
    ping = models.IntegerField(blank=True, null=True)
    change_1_time = models.DateTimeField(blank=True, null=True)
    single_gid = models.CharField(max_length=255, blank=True, null=True)
    vm_server_id = models.IntegerField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    province_char = models.CharField(max_length=255, blank=True, null=True)
    city_char = models.CharField(max_length=255, blank=True, null=True)
    notify = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vpn_status"


class VpnStatus58(models.Model):
    serverid = models.SmallIntegerField()
    vmid = models.SmallIntegerField(blank=True, null=True)
    jobstatus = models.IntegerField(blank=True, null=True)
    vpnstatus = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vpn_status_58"


class VpnTimeArea(models.Model):
    server_id = models.IntegerField()
    time_begin = models.FloatField(blank=True, null=True)
    time_end = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    time_id = models.IntegerField(blank=True, null=True)
    ping = models.IntegerField(blank=True, null=True)
    ping_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vpn_time_area"


class VpnUpdateFile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    only_area = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "vpn_update_file"


class ZeroScheduleList(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    vm_id = models.IntegerField(blank=True, null=True)
    terminal_type = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    run_times = models.IntegerField(blank=True, null=True)
    ran_times = models.IntegerField(blank=True, null=True)
    succ_times = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "zero_schedule_list"
