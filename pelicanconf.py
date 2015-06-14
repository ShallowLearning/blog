#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Joshua D. Loyal'
SITENAME = u'Shallow Learning'
SITEURL = u'https://joshloyal.github.io/shallow-learning'

TIMEZONE = 'America/New_York'

#from utils import filters
#JINJA_FILTERS = { 'sidebar' : filters.sidebar, 'pretty_data': filters.pretty_date }

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

MENUITEMS = (('About', 'https://joshloyal.github.io'),)
#             ('Resume', 'https://joshloyal.github.io/docs/resume.pdf'),)
#
## Social widget
#SOCIAL = (('github', 'https://github.com/joshloyal'),
#          ('linkedin', 'https://linkedin.com/in/joshloyal'),)

# Pages to show on homepage
DEFAULT_PAGINATION = 3
POST_LIMIT = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%m-%d-%Y')
DEFAULT_CATEGORY = 'misc'

# Formatting for urls
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = True

# Specify theme
THEME = "./templates/pure"

PROFILE_IMG_URL = "images/profile_image.jpg"
COVER_IMG_URL = "images/coverimage.jpg"
#TAGLINE = ""

PLUGIN_PATHS = ["./plugins"]
PLUGINS = ['render_math', 'gravatar']

# liquid tag plugins
PLUGINS += ['liquid_tags.img', 'liquid_tags.video', 'liquid_tags.notebook']

# some configuration if running with livebuild (dumb hack really...)
cwd = os.getcwd().split('/')[-1]

if cwd == 'shallow-learning':
    print('Adding _nb_header.html to theme...')
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
    NOTEBOOK_DIR = './content/notebooks'
elif cwd == 'output':
    print('Adding ../_nb_header.html to theme...')
    EXTRA_HEADER = open('../_nb_header.html').read().decode('utf-8')
    NOTEBOOK_DIR = '../content/notebooks'

PATH = "content"
STATIC_PATHS = ['images']

TYPOGRIFY = True
