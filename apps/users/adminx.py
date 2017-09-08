# _*_ coding:utf-8 _*_


import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "暮雪网后台管理系统"
    site_footer = "暮雪在线网"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']  # 后台自定义显示列 显示字段
    search_fields = ['title', 'image', 'url', 'index']  # 定义后台搜索 搜索功能
    list_filter = ['title', 'image', 'url', 'index', 'add_time']  # 过滤器 通过时间搜索


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
