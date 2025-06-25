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
        "markdown.extensions.def_list",
        "markdown.extensions.tables",
        "pymdownx.tasklist",
    ],
    "extension_configs": {
    },
    "output_format": "html5",
}

