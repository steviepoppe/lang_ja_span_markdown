# -*- coding: utf-8 -*-
"""
============================================
lang="ja" span extension for Markdown-Python
============================================
A small Python-Markdown extension for embedding Japanese content in multilingual markdown files 
into stylizable span tags using {{}} brackets as span tags with a `lang="ja"` attribute.

Example:
    {{読書クラブ}}
Will output:
    <span lang="ja">読書クラブ</span>

:website: https://steviepoppe.net/
:copyright: Copyright 2016 Stevie Poppe
:license: MIT license, see LICENSE for details.
"""

from __future__ import absolute_import
from __future__ import unicode_literals
import markdown
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.inlinepatterns import Pattern

SPANJP_RE = r"(\{\{)(.+?)(\}\})"

def makeExtension(*args, **kwargs):
    return SpanJPExtension(*args, **kwargs)

class SpanJPExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('span_jp', SpanJPPattern(SPANJP_RE, 'sub'),
'<not_strong')

class SpanJPPattern(Pattern):

    def handleMatch(self, matched):
        elem = markdown.util.etree.Element("span")
        elem.set("lang", "ja")
        elem.text = matched.group(3)
        return elem

