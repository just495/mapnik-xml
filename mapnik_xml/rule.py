from lxml import etree
from .base import BaseElement
from .scale_denominators import MinScaleDenominator, MaxScaleDenominator
from .filters import Filter, ElseFilter


class Rule(BaseElement):
    name = None
    title = None
    min_scale = None
    max_scale = None
    filter = None
    else_filter = False
    items = []

    def __init__(self, name=None, title=None, min_scale=None, max_scale=None, filter=None, else_filter=False, items=[]):
        self.name = name
        self.title = title
        self.min_scale = min_scale
        self.max_scale = max_scale
        self.filter = filter
        self.else_filter = else_filter
        self.items = items

    def to_xml(self):
        root = etree.Element("Rule")
        if self.name:
            root.set('name', self.name)
        if self.title:
            root.set('title', self.title)
        if self.min_scale is not None:
            root.append(MinScaleDenominator(self.min_scale).to_xml())
        if self.max_scale is not None:
            root.append(MaxScaleDenominator(self.max_scale).to_xml())
        if self.filter:
            root.append(Filter(self.filter).to_xml())
        if not self.filter and self.else_filter:
            root.append(ElseFilter().to_xml())
        for item in self.items:
            root.append(item.to_xml())
        return root
