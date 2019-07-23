#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author  : xiaotudou
@time: 2019/07/19 22:28
@File    : comment_block.py 
'''
from django import template

from comment.forms import CommentForm
from comment.models import Comment


register = template.Library()


@register.inclusion_tag('comment/block.html')
def comment_block(target):
    return {
        'target': target,
        'comment_form': CommentForm(),
        'comment_list': Comment.get_by_target(target),
    }