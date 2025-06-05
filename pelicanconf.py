AUTHOR = 'Vaish'
SITENAME = 'Fragments'
SITEURL = "."
THEME = "theme"
PATH = "content"
USE_FOLDER_AS_CATEGORY = False
TIMEZONE = 'Canada/Eastern'
DEFAULT_LANG = 'en'
RELATIVE_URLS = True 
PLUGIN_PATHS = ['plugins']
PLUGINS = ['zid_mapper','zid_linker']
ARTICLE_EXCLUDES = ['Fleeting']

MARKDOWN = {
    'extension_configs': {
        'plugins.citekeyx': {},
        'plugins.fencedx' : {}
    },
    'output_format': 'html5',
}
