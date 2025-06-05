from pelican import signals

def add_zid_map(generator):
    zid_map = {}

    for article in generator.articles:
        # Get from metadata
        zid = article.metadata.get('zid')
        if zid:
            article.ZID = zid  # promote to attribute
            zid_map[zid] = article

    generator.context['zid_map'] = zid_map

def register():
    signals.article_generator_finalized.connect(add_zid_map)
