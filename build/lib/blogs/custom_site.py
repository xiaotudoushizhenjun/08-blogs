#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author  : xiaotudou
@time: 2019/07/17 14:06
@File    : custom_site.py 
'''
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = '博客'
    site_title = 'Blog 管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')