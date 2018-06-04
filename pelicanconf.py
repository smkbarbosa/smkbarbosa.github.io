#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from decouple import config

AUTHOR = u'Samuel Barbosa'
SITENAME = u'Samuel Barbosa'
SITEURL = ''
SITEDESCRIPTION = u'Notes about python, django and others technologys'
SITESUBTITLE = u'Notes about python, django and others technologys'

PATH = 'content'

TIMEZONE = 'America/Araguaina'

DEFAULT_LANG = u'en'
# LOCALE = ['en_US']

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Samuel Barbosa (Blog pt-br)', 'http://smkbarbosa.eti.br/'),
         ('sempreUpdate', 'https://sempreupdate.com.br/'),
         )

# Social widget
SOCIAL = (('github', 'https://github.com/smkbarbosa'),
          ('twitter', 'https://twitter.com/smk_barbosa'),
          ('linkedin', 'https://www.linkedin.com/in/samuel-barbosa-2968802b/'),
          ('xing', 'https://t.me/smk_barbosa'),)

DEFAULT_PAGINATION = 10

ADDTHIS_PUBID = config('ADDTHIS')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/medius'
#THEME_COLOR = "red"
SIDEBAR_DISPLAY = ['recents', 'tags', 'social']
COPYRIGHT = "Samuel Barbosa"
DISQUS_SITENAME = "smkbarbosa"

MEDIUS_AUTHORS = {
    'Samuel Barbosa': {
        'description': """
            I work as an IT support at UFT and I study Internet Systems at IFTO.
            The free hours are to study guitar and act as a reviewer in the portal SempreUpdate
         """,
        'cover': 'https://lh3.googleusercontent.com/-IMSro0eSmDk/WByW5hsdGcI/AAAAAAAAGXk/FUUtI_VGI6UPK6evtZc4Gy6djyS1JKwVgCJkCGAYYCw/w970-h546-n-rw-no/Samuel.png',
        'image': 'https://s.gravatar.com/avatar/232a2ae269520f21c1fa9a7e1896b737?s=80',
        'links': (('github', 'https://github.com/smkbarbosa'),
                  ('twitter-square', 'https://twitter.com/smk_barbosa'),
                  ('envelope-square', 'mailto:contato@smkbarbosa.eti.br'),
                  ('paper-plane', 'https://t.me/smkbarbosa')),
    }
}

MEDIUS_CATEGORIES = {
    'Article': {
        'description': 'Some interesting texts for personal development.',
        'logo': '/images/key.jpg',
        'thumbnail': '/images/blog.jpg'
    }
}
