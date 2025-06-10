import pymdownx


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
    "extensions": [
        "plugins.citekeyx",
        "plugins.fencedx",
        "markdown.extensions.attr_list",
        "markdown.extensions.def_list",
        "pymdownx.tasklist",
        "pymdownx.progressbar",
    ],
    "extension_configs": {
    },
    "output_format": "html5",
}

