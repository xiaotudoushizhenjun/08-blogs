#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author  : xiaotudou
@time: 2019/07/22 7:47
@File    : serializers.py 
'''
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'category', 'desc', 'content_html', 'created_time']