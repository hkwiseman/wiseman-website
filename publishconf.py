# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://kylewiseman.com'
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True
PLUGIN_PATHS = ['pelican-plugins']
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"
PLUGINS = ['readtime', 'search', 'neighbors', 'pelican-toc']
THEME = os.curdir + "/pelican-themes/Papyrus"

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
