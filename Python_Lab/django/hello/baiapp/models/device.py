# from django.utils import timezone
# from field_history.tracker import FieldHistoryTracker
# from django.db import models
# from django.contrib.postgres.fields import JSONField


# class Device(models.Model):
#     EVENT_CHOICES = (
#         ("normal", "正常"),
#         ("offline", "掉线"),
#         ("black_screen", "黑屏"),
#         ("shelter", "遮挡"),
#         ("stuck", "卡机"),
#         ("feign_death", "假死"),
#     )
#     STATE_CHOICES = (("online", "在线"), ("offline", "离线"))
#     DENSE_CHOICES = (("one_level", "秘密"), ("two_level", "机密"), ("three_level", "绝密"))
#     POINT_CHOICES = (
#         ("one_point", "一类视频监控点"),
#         ("two_point", "二类视频监控点"),
#         ("three_point", "三类视频监控点"),
#     )
#     DISCOVER_CHOICES = (("new", "新发现"), ("update", "更新"))
#     DEVICE_TYPE_CHOICES = (
#         ("one_point", "一类视频监控点"),
#         ("two_point", "二类视频监控点"),
#         ("three_point", "三类视频监控点"),
#     )
#     CONTROL_CHOICES = (
#         ("uncontrol", "未纳管"),
#         ("controlling", "纳管中"),
#         ("controlled", "已纳管"),
#         ("control_fail", "纳管失败"),
#     )
#     LIST_CHOICES = (
#         ("access_list", "接入名单"),
#         ("white_list", "白名单"),
#         ("black_list", "黑名单"),
#     )
#     BLOCK_CHOICES = (("blocked", "阻断"), ("unblocked", "未阻断"))

#     # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     # 基础信息
#     mac = models.CharField("Mac地址", max_length=22, null=True, blank=True)
#     name = models.CharField("设备名称", max_length=120, null=True, blank=True)
#     os = models.CharField("操作系统", max_length=64, null=True, blank=True)
#     system_version = models.CharField("系统版本", max_length=64, null=True, blank=True)
#     web_version = models.CharField("Web版本", max_length=64, null=True, blank=True)
#     serial_number = models.CharField("序列号", max_length=100, null=True, blank=True)
#     model = models.CharField("型号", max_length=64, null=True, blank=True)
#     manufacturer = models.CharField("厂商", max_length=64, null=True, blank=True)
#     vendor_in_chinese = models.CharField("厂商中文", max_length=64, null=True, blank=True)
#     control = models.CharField(
#         choices=CONTROL_CHOICES, verbose_name="纳管状态", max_length=20, default="uncontrol"
#     )
#     belong_list = models.CharField(
#         choices=LIST_CHOICES, max_length=40, default="access_list"
#     )
#     block_state = models.CharField(
#         choices=BLOCK_CHOICES, max_length=40, default="unblocked"
#     )
#     # hardware info
#     cpu_model = models.CharField("CPU", max_length=64, null=True, blank=True)
#     memory = models.CharField("内存", max_length=16, null=True, blank=True)
#     storage = models.CharField("存储", max_length=16, null=True, blank=True)

#     # 关联信息
#     devicetype = models.ForeignKey(
#         "DeviceType", on_delete=models.SET_NULL, null=True, blank=True
#     )
#     ipasset = models.ForeignKey(
#         "IpAssets", on_delete=models.SET_NULL, null=True, blank=True
#     )
#     detachment = models.ForeignKey(
#         "Detachment", null=True, blank=True, on_delete=models.SET_NULL
#     )
#     plat_id = models.CharField("平台", max_length=120, null=True, blank=True)

#     # 位置
#     Lat = models.FloatField("经度", null=True, blank=True)
#     Lng = models.FloatField("纬度", null=True, blank=True)
#     address = models.CharField("省/市/区", blank=True, max_length=100)
#     location = models.CharField("详细地址", blank=True, max_length=100)

#     update_time = models.DateTimeField("更新时间", blank=True, null=True)
#     created_time = models.DateTimeField("创建时间", auto_now_add=True)
#     device_source = models.CharField("设备来源", max_length=200, null=True, blank=True)
#     number_manage = models.BooleanField("账号管理", default=True)
#     field_mate = models.BooleanField("一机一档", default=True)

#     dense = models.CharField(
#         "密集", max_length=20, choices=DENSE_CHOICES, default="one_level", blank=True
#     )
#     point_type = models.CharField(
#         "监控点位类型", max_length=100, choices=POINT_CHOICES, default="one_point", blank=True
#     )
#     state_info = models.CharField(
#         "状态",
#         max_length=16,
#         choices=STATE_CHOICES,
#         blank=True,
#         null=True,
#         default="offline",
#     )
#     access_time = models.DateTimeField("入网时间", default=timezone.now)
#     discover_state = models.CharField(
#         "发现状态", choices=DISCOVER_CHOICES, default="new", max_length=20
#     )
#     field_history = FieldHistoryTracker(["state_info", "belong_list"])
#     safe_info = JSONField(null=True, blank=True)
#     hardware_info = JSONField(null=True, blank=True)
#     software_info = JSONField(null=True, blank=True)
#     probe_group = models.CharField("探针组", max_length=40, null=True, blank=True)
#     user_name = models.CharField("用户名", max_length=40, null=True, blank=True)
#     probe_id = models.CharField("探针ID", max_length=40, null=True, blank=True)
#     is_manual = models.BooleanField("是否手动添加", default=False)

#     class Meta:
#         ordering = ("-update_time",)



