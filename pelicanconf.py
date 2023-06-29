#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'KholdFuzion'
SITENAME = u'Fuzion Labs'
SITEURL = 'kholdfuzion.net'
THEME = "themes/blueidea"
PATH = 'content'

STATIC_PATHS = ['images', 'icons', 'feeds']

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

LINKS = (
        ('Github', 'http://github.com/kholdfuzion'),
        ('Gitlab', 'http://gitlab.com/kholdfuzion'),
	('ipfs', 'http://ipfs.io'),
	('Trade-N-Games', 'http://www.tradengames.com/store/pc/home.asp')
)

