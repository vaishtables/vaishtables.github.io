from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.inlinepatterns import SubstituteTagInlineProcessor
import xml.etree.ElementTree as etree
import re
import markdown


import re
import xml.etree.ElementTree as etree
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

class SupSubProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        full = m.group(0)

        if full.startswith('^') and full.endswith('^'):
            tag = 'sup'
            text = full[1:-1]
        elif full.startswith(',') and full.endswith(','):
            tag = 'sub'
            text = full[1:-1]
        else:
            return None, None, None  # Should not happen

        el = etree.Element(tag)
        el.text = text
        return el, m.start(0), m.end(0)

class SupSubExtension(Extension):
    def extendMarkdown(self, md):
        sup_pattern = r'\^\w+\^'
        md.inlinePatterns.register(SupSubProcessor(sup_pattern, md), 'sup_marker', 175)

        # Match .text.
        sub_pattern = r'\,\w+\,'
        md.inlinePatterns.register(SupSubProcessor(sub_pattern, md), 'sub_marker', 174)




class ThemeMarkProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        symbol = m.group(1)
        el = etree.Element("small")
        el.text = symbol + ':'
        return el, m.start(0), m.end(0)


class ThemeMarkExtension(Extension):
    def extendMarkdown(self, md):
        pattern = (
            r'(?:#)?('
            r'(?:[↔∴∵↑↓⭫⇣§≺≻⤒⤓→⇢∆∝~⥁♀⁎×≔≠∀⚤⏳]︎?'
            r'|\U0001F9E0|\U0001F9EC|\U0001F449)'
            r'):'
        )
        md.inlinePatterns.register(ThemeMarkProcessor(pattern, md), 'thememark_colon', 5)



with open("C://Users/vaish/Desktop/Notes//2025062240.md", "r", encoding="utf-8") as f:
    md_text = f.read()

html = markdown.markdown(md_text, extensions=["def_list", "tables", SupSubExtension(), ThemeMarkExtension()])

print(html)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)
