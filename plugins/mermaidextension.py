from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re
import html

class FencedExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(FencedPreprocessor(md), 'fenced_block', 25)

class FencedPreprocessor(Preprocessor):
    FENCED_BLOCK_RE = re.compile(
        r'(?P<fence>^`{3,})(?P<lang>\w+)?[ \t]*\n(?P<code>.*?)(?<=\n)(?P=fence)[ \t]*$',
        re.DOTALL | re.MULTILINE
    )

    RAW_LANGS = {'mermaid', 'math', 'latex'}

    def run(self, lines):
        text = "\n".join(lines)
        new_text = []
        last_end = 0

        for match in self.FENCED_BLOCK_RE.finditer(text):
            # Add text before the match
            new_text.append(text[last_end:match.start()])

            lang = (match.group('lang') or '').strip()
            code = match.group('code').rstrip()

            if lang.lower() in self.RAW_LANGS:
                html_block = f'<pre class="{html.escape(lang)}">\n{code}\n</pre>'
            else:
                safe_code = html.escape(code)
                html_block = f'<pre class="{html.escape(lang)}"><code>{safe_code}</code></pre>'

            new_text.append(html_block)
            last_end = match.end()

        # Add remaining text
        new_text.append(text[last_end:])
        return ''.join(new_text).splitlines()

def makeExtension(**kwargs):
    return FencedExtension(**kwargs)
