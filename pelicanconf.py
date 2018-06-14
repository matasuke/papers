#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kosuke Futamata'
AUTHOR_REAL = 'Kosuke'
SITENAME = 'Paper Survey'
SITEURL = ''

DEFAULT_DATE = 'fs'

DISPLAY_PAGES_ON_MENU = True

#AUTHOR_IMAGE = 'yoshi.png'
AUTHOR_IMAGE = 'kosuke.jpg'

#to github io
MOREABOUTMEURL = 'http://matasukef.github.io'

PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
THEME = 'uikit'
STYLE = "almost-flat"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/matasuke_f'),
          ('github', 'https://github.com/matasukef'),
          ('facebook', 'https://www.facebook.com/matasukef'),
          ('linkedin', ''))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 0
DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 0



LICENSE = {
    'cc_name':"by-sa",
    'hosted':False,
    'compact':True,
    'brief':False
    }
