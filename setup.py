# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = 0.3

setup(name='kealm',
    version=VERSION,
    description='a cli tool set by junmei',
    long_description='enjoy it!',
    classifiers=[],
    keywords='python cli terminal',
    author='junmei',
    author_email='ahumeijun@live.com',
    url='https://github.com/ahumeijun/kealm-cli',
    license='MIT',
    packages=find_packages(),
    include_packages_data=True,
    zip_safe=True,
    install_requires=[
    ],
    entry_points={
        'console_scripts':[
            'bs64=kealm.kealm:base64_encode',
            'url=kealm.kealm:url_encode',
            'roll=kealm.kealm:roll',
            'xcsmb=kealm.symbolic:symbolic'
        ]
    }
)