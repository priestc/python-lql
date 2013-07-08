from setuptools import setup

import sys

if sys.version_info < (3 , 0):
    REQUIRES = ['pyparsing<=2.0.0']
else:
    REQUIRES = ['pyparsing>=2.0.0']


setup(
    name='python-lql',
    version='1.0.0',
    description='Parsing utility for Library Query Language.',
    long_description=open('README.rst').read(),
    author='Chris Priest',
    author_email='cp368202@ohiou.edu',
    url='https://github.com/priestc/python-lql',
    packages=['LQL'],
    include_package_data=True,
    license='LICENSE',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=REQUIRES,
)