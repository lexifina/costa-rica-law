"""SINALEVI full text (the `html` of _CargarTextoCompleto) -> one file per article, one paragraph per line.

The page is a header (titles, version navigation) followed by one Word-HTML document per article, each closed by a
"Ficha Articulo <label>" link (handleArticuloClick(n, ficha, version, idArticulo)). Text before an article's link
belongs to that article, including Title and Chapter headings printed above it.
"""
import html as htmllib
import re
from html.parser import HTMLParser

MARK = re.compile(r'<div class="pb-5 pt-2">\s*<a class="enlaceFicha"[^>]*?handleArticuloClick\(\s*(\d+)\s*,\s*(\d+)\s*,'
                  r'\s*(\d+)\s*,\s*(\d+)\s*\)[^>]*>\s*(.*?)\s*</a>\s*</div>', re.S)
HEAD_END = re.compile(r'<h2 class="h2-Size title-center pb-4">\s*Versi\u00f3n de la Norma:[^<]*</h2>.*?</div>\s*</div>', re.S)
BLOCK = {'p', 'div', 'li', 'ul', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'tr', 'blockquote', 'dl', 'dt',
         'dd', 'thead', 'tbody', 'section', 'center', 'pre', 'title'}
SKIP = {'style', 'script', 'head', 'title', 'xml'}
WS = re.compile(r'[\s\u00a0\u2000-\u200a\u202f\u205f\u3000]+')
INVISIBLE = re.compile(r'[\u00ad\u200b-\u200d\u2060\ufeff]')


def norm(s: str) -> str:
    return WS.sub(' ', INVISIBLE.sub('', s)).strip()


class Lines(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.cur: list[str] = []
        self.skip = 0
        self.cells = 0

    def flush(self):
        t = norm(''.join(self.cur))
        if t:
            self.lines.append(t)
        self.cur = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == 'br':
            if self.cells:
                self.cur.append(' ')
            else:
                self.flush()
        elif tag in ('td', 'th'):
            if self.cells:
                self.cur.append(' | ')
            self.cells += 1
        elif tag == 'tr':
            self.flush()
            self.cells = 0
        elif tag == 'img':
            self.cur.append(' [imagen] ')
        elif tag in BLOCK and not self.cells:
            self.flush()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag.lower() in SKIP:
            self.skip -= 1

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == 'tr':
            self.flush()
            self.cells = 0
        elif tag in BLOCK and not self.cells:
            self.flush()

    def handle_data(self, data):
        if not self.skip:
            self.cur.append(data)

    def handle_comment(self, data):
        pass

    def close(self):
        super().close()
        self.flush()


def to_lines(h: str) -> list[str]:
    # Word conditional comments and <![if ...]> blocks hide nothing we print; drop them with the comments
    h = re.sub(r'<!\[(?:if|endif)[^\]]*\]>', '', h)
    p = Lines()
    p.feed(h)
    p.close()
    return p.lines


def label_slug(label: str) -> str:
    s = norm(htmllib.unescape(label))
    s = re.sub(r'^Ficha\s+', '', s, flags=re.I)
    s = s.lower()
    s = s.replace('\u00e1', 'a').replace('\u00e9', 'e').replace('\u00ed', 'i').replace('\u00f3', 'o').replace('\u00fa', 'u')
    s = s.replace('\u00f1', 'n').replace('\u00fc', 'u').replace('\u00ba', '').replace('\u00b0', '')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:80].rstrip('-') or 'articulo'


def parse(page: str) -> list[tuple[str, str, list[str]]]:
    """[(slug, label, lines)] in document order. A text with no article links is one unit, `texto`."""
    m = HEAD_END.search(page)
    start = m.end() if m else 0
    body = page[start:]
    units: list[tuple[str, str, list[str]]] = []
    pos = 0
    used: dict[str, int] = {}
    for mk in MARK.finditer(body):
        seg = body[pos:mk.start()]
        pos = mk.end()
        label = norm(htmllib.unescape(mk.group(5)))
        slug = label_slug(label)
        used[slug] = used.get(slug, 0) + 1
        if used[slug] > 1:
            slug = f'{slug}~{used[slug]}'
        units.append((slug, label, to_lines(seg)))
    tail = to_lines(body[pos:])
    if not units:
        return [('texto', 'Texto', tail)] if tail else []
    if tail:
        # text after the last article link (closing formula, signatures): its own file
        units.append(('final', 'Final', tail))
    return units
