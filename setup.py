#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author  : xiaotudou
@time: 2019/07/22 15:23
@File    : setup.py 
'''
from setuptools import setup, find_packages


setup(
    name='blogs',
    version='0.1',
    description='Blog System base on Django',
    author='lihui',
    author_email='15634118755@163.com',
    url='https://www.baidu.com',
    license='MIT',
    packages=find_packages('blogs_sys'),
    package_dir={'': 'blogs_sys'},
    # package_data={'': [  # 方法一： 打包数据文件
    #     'themes/*/*/*/*',    # 需要按目录层级匹配
    # ]},
    include_package_data=True,      # 方法二： 配合MANIFEST.in文件
    install_requires=[
        'django~=2.2.3',
        'gunicorn==19.9.0',
        'supervisor==4.0.2',
        'xadmin==2.0.1',
        'PyMySQL==0.9.3',
        'django-ckeditor==5.4.0',
        'django-rest-framework==0.1.0',
        'django-redis==4.10.0',
        'django-autocomplete-light==3.2.10',
        'mistune==0.8.4',
        'Pillow==6.1.0',
        'coreapi==2.3.3',
        # debug
        'django-debug-toolbar==2.0',
        'django-silk==3.0.2',
    ],
    extras_require={
        'ipython': ['ipython==7.6.1']
    },
    scripts=[
        'blogs_sys/manage.py',
    ],
    entry_points={
        'console_script': [
            'blog_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # 软件成熟度如何？一般有下面几种选项
        #    3  - Alpha
        #    4  - Beta
        #    5  - Production/Stable
        'Development Status :: 3 - Alpha',

        # 指明项目的受众
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # 选择项目的许可证(License)
        'License :: OSI Approved :: MIT License',

        # 指定项目需要的Python版本
        'Programming Language :: Python :: 3.6',
    ],
)