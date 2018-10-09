from lxml import etree
from .base import BaseElement
from .style import Style


class StyleName(BaseElement):
    _style = None

    def __init__(self, style):
        self._style = style

    def to_xml(self):
        root = etree.Element('StyleName')
        root.text = self._style.name if isinstance(self._style, Style) else self._style
        return root


class Layer(BaseElement):
    abstract = None
    cache_features = None
    clear_label_cache = None
    minzoom = None
    maxzoom = None
    name = None
    srs = None
    status = None
    title = None
    queryable = None
    styles = []
    datasource = None

    def __init__(self, abstract=None, cache_features=None, clear_label_cache=None, minzoom=None, maxzoom=None,
                 name=None, srs=None, status=None, title=None, queryable=None, styles=[], datasource=None):
        self.abstract = abstract
        self.cache_features = cache_features
        self.clear_label_cache = clear_label_cache
        self.minzoom = minzoom
        self.maxzoom = maxzoom
        self.name = name
        self.srs = srs
        self.status = status
        self.title = title
        self.queryable = queryable
        self.styles = styles
        self.datasource = datasource

    def to_xml(self):
        root = etree.Element("Layer")
        if self.abstract:
            root.set('abstract', self.abstract)
        if self.cache_features is not None:
            root.set('cache-features', 'on' if self.cache_features else 'off')
        if self.clear_label_cache is not None:
            root.set('clear-label-cache', 'on' if self.clear_label_cache else 'off')
        if self.minzoom is not None:
            root.set('minzoom', str(self.minzoom))
        if self.maxzoom is not None:
            root.set('maxzoom', str(self.maxzoom))
        if self.name:
            root.set('name', self.name)
        if self.srs:
            root.set('srs', self.srs)
        if self.status is not None:
            root.set('status', 'on' if self.status else 'off')
        if self.title:
            root.set('title', self.title)
        if self.queryable is not None:
            root.set('queryable', str(self.queryable).lower())
        if self.datasource:
            root.append(self.datasource.to_xml())
        for style in self.styles:
            root.append(StyleName(style).to_xml())
        return root
