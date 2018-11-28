"""The setup.py file for Tron CLI."""

import sys


from setuptools import setup, find_packages

def cat(files, join_str=''):
    """Concatenate `files` content with `join_str` between them."""
    files_content = (open(f).read() for f in files)
    return join_str.join(files_content)


PKG_NAME = 'troncli'
PKG_AUTHOR = ', '.join(['Weiyu X'])
PKG_SCRIPTS = ['tron-cli']
PKG_VERSION = '0.1.3'
PKG_REQUIRES = [
    'cbox==0.5.0',
    'certifi==2018.10.15',
    'chardet==3.0.4',
    'idna==2.7',
    'psutil==5.4.7',
    'requests==2.20.0',
    'six==1.11.0',
    'urllib3==1.24'
]

PKG_DESC = 'A command line tool to monitor and manage tron nodes.'
PKG_LONG_DESC = cat(['README.md', 'CHANGELOG.md'], u'\n\n')

setup(
    name=PKG_NAME,
    version=PKG_VERSION,
    author=PKG_AUTHOR,
    author_email='weiyu@tron.network',
    description=PKG_DESC,
    long_description=PKG_LONG_DESC,
    long_description_content_type='text/markdown',
    url='https://github.com/tronprotocol/tron-cli',
    packages=find_packages(),
    zip_safe=False,
    scripts=PKG_SCRIPTS,
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=PKG_REQUIRES,
)
