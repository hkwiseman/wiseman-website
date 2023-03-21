AUTHOR = 'Kyle Wiseman'
SITENAME = 'Kyle Wiseman'
SITEURL = 'https://kylewiseman.com'
TIMEZONE = 'America/Detroit'
DEFAULT_LANG = 'en'

SUBTITLE = 'Introduction'
SUBTEXT = '''Welcome! I am a full-stack software engineer based in North Carolina. 
This website serves as a public hub of my software portfolio, 
posts chronicling my learning journey in technology,
 and the occasional analysis on current events 
within the industry.

<br><br>For a more complete look at my background check out my <a href="https://kylewiseman.com/pages/about.html">bio</a> or <a href="https://kylewiseman.com/pages/resume.html">resume</a>
<br>
<br>Feel free to contact me through LinkedIn or by email at: kyle@kylewiseman.com
'''
COPYRIGHT = '©2023'
PATH = 'content'
THEME = 'pelican-themes/Papyrus'
THEME_STATIC_PATHS = ['static']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors', 'pelican-toc']
STATIC_PATHS = [
    'images',
    'images/favicon.ico',
    'extra/robots.txt',
    ]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    }
DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (('index', 'search',))
PAGINATED_TEMPLATES = {'index':None}

# Site search plugin
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"
# Table of Content Plugin
TOC = {
    'TOC_HEADERS'       : '^h[1-3]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression
    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True

# Social widgets
SOCIAL = (
    ('github', 'https://github.com/hkwiseman'),
    ('linkedin', 'https://www.linkedin.com/in/hkylewiseman/'),
    ('reddit', 'https://www.reddit.com/user/hkwiseman')
)

# Article share widgets
SHARE = (
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("reddit", "https://reddit.com/submit?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''