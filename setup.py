#!/usr/bin/env python

import os

from setuptools import setup, find_packages

try:
    # Workaround for http://bugs.python.org/issue15881
    import multiprocessing
except ImportError:
    pass

VERSION = '0.5.0'

if __name__ == '__main__':
    setup(
        name = 'django-tastypie-mongoengine',
        version = VERSION,
        description = "MongoEngine support for django-tastypie.",
        long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
        author = 'wlan slovenija',
        author_email = 'open@wlan-si.net',
        url = 'https://github.com/harvard-hbs/hbso-django-tastypie-mongoengine',
        keywords = "REST RESTful tastypie mongo mongodb mongoengine django",
        license = 'AGPLv3',
        packages = find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
        classifiers = (
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU Affero General Public License v3',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Framework :: Django',
            'Framework :: Django :: 5.0',
            'Framework :: Django :: 5.1',
            'Framework :: Django :: 5.2',
        ),
        zip_safe = False,
        python_requires='>=3.11',
        install_requires = (
            'Django>=5.0,<6.0',
            'django-tastypie>=0.14.0,<0.16.0',
            'mongoengine>=0.28.0',
            'python-dateutil>=2.8.0',
            'lxml>=4.9.0',
            'defusedxml>=0.7.0',
            'PyYAML>=6.0',
            'biplist>=1.0.0',
            'python-mimeparse>=1.6.0',
        ),
        test_suite = 'tests.runtests.runtests',
        tests_require = (
            'Django>=5.0,<6.0',
            'django-tastypie>=0.14.0,<0.16.0',
            'mongoengine>=0.28.0',
            'python-dateutil>=2.8.0',
            'lxml>=4.9.0',
            'defusedxml>=0.7.0',
            'PyYAML>=6.0',
            'biplist>=1.0.0',
            'python-mimeparse>=1.6.0',
            'nose',
        ),
    )
