import re
from pelican import signals

# Updated regex to capture optional link text after a pipe
ZID_PATTERN = re.compile(r"\[\[([0-9]{10})(\|([^\]]+))?\]\]")

def replace_zid_references(generators):
    # Find the context and zid_map from the ArticlesGenerator
    for generator in generators:
        context = getattr(generator, 'context', None)
        zid_map = context.get('zid_map') if context else None
        articles = context.get('articles') if context else None

        if zid_map and articles:
            break
    else:
        return  # Nothing to do

    # Replace ZID references in article content
    for article in articles:
        content = getattr(article, '_content', None)
        if not content:
            continue

        def replace(match):
            zid = match.group(1)
            custom_text = match.group(3)
            target_article = zid_map.get(zid)
            if not target_article:
                return match.group(0)  # leave unchanged

            link_text = custom_text if custom_text else target_article.title
            return f'<a href="{target_article.url}">{link_text}</a>'

        article._content = ZID_PATTERN.sub(replace, content)

def register():
    signals.all_generators_finalized.connect(replace_zid_references)
