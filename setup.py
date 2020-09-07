#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import os

exec(open('redirects/metadata.py').read())

github_url = 'https://github.com/fabiocaccamo'
package_name = 'django-redirects'
package_url = '{}/{}'.format(github_url, package_name)
package_path = os.path.abspath(os.path.dirname(__file__))
long_description_file_path = os.path.join(package_path, 'README.md')
long_description_content_type = 'text/markdown'
long_description = ''
try:
    with open(long_description_file_path) as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name=package_name,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author=__author__,
    author_email=__email__,
    url=package_url,
    download_url='{}/archive/{}.tar.gz'.format(package_url, __version__),
    keywords=[
        'django', 'admin', 'redirects', 'redirect', 'permanent', 'temporary',
        '301', '302', '303', '307', '308', 'exact', 'prefix', 'regex',
    ],
    requires=['django(>=1.7)'],
    install_requires=[
        'six >= 1.9.0, < 2.0.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Build Tools',
    ],
    license=__license__,
    test_suite='runtests.runtests'
)
