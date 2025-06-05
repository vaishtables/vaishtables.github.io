from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree
import re
import json

class CitekeyExtension(Extension):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        CITEKEY_RE = r'\[?@(\w+\d{4}(?:;@\w+\d{4})*)\]?'
        md.inlinePatterns.register(CitekeyInlineProcessor(CITEKEY_RE, md), 'citekey', 175)


class CitekeyInlineProcessor(InlineProcessor):
    def __init__(self, pattern, md):
        super().__init__(pattern, md)
        self.citekey_count = 0

    def handleMatch(self, m, data):
        matched_text = m.group(0)
        citekey_str = m.group(1)

        self.citekey_count += 1

        is_bracketed = matched_text.startswith('[') and matched_text.endswith(']')

        citekeys = [ck.strip().lstrip('@') for ck in citekey_str.split(';')]
        citation_id = (
            f"PAR{self.citekey_count}" if is_bracketed
            else f"NAR{self.citekey_count}"
            if len(citekeys) == 1
            else f"MULTI{self.citekey_count}"
        )

        span = etree.Element('span')
        span.set('id', citation_id)
        span.set('data-citationItems', json.dumps(citekeys))

        start, end = m.start(0), m.end(0)
        return span, start, end

def makeExtension(**kwargs):
    return CitekeyExtension(**kwargs)
