#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Elizabeth Camp'

copy_date ='2018'
SITENAME = 'Elizabeth H. Camp'
SITESUBTITLE = 'data'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

STATIC_PATHS = ['images', 'pdfs','pages']

#SITELOGO = 'images/logo.png'
#SITELOGO_SIZE = 32
#FAVICON = 'images/favicon.png'

# Top menus
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = [('CV', '/pdfs/Camp_CV_7_2018.pdf')]
ARCHIVES_SAVE_AS = 'archives.html'
DISPLAY_ARCHIVE_ON_MENU = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['plugins']#['D:/WebsitePelican/source/plugins']
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'render_math',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    ]

# for Tique Search Plugin
#DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives')

IGNORE_FILES = ['.ipynb_checkpoints']
#'ipynb.markup'
#liquid_tags.notebook',
#    'liquid_tags.include_code',
# 'ipynb.liquid',

THEME = "D:/WebsitePelican/staticsitesource/themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'flatly2'
#BANNER = "/images/banner.png"
#BANNER_ALL_PAGES = False

JINJA_ENVIRONMENT = {
    "extensions": ['jinja2.ext.i18n'],
}

#MARKUP = ('md', 'ipynb')

IPYNB_USE_METACELL = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/betsyhcamp/'),
          ('github', 'https://github.com/betsyhcamp'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



