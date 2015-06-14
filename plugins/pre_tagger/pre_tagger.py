from pelican import signals
import re

def pre_tagger(html):
    if html._content:
        page_content = html._content
    else:
        return

    pre_elements = re.findall('<pre>', page_content)
    if len(pre_elements) > 0:
        updated_content = page_content.replace('<pre>', '<pre class=highlight>')
        html._content = updated_content

def register():
    signals.content_object_init.connect(pre_tagger)
