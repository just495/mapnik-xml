from lxml import etree
from .base import BaseElement


class Style(BaseElement):
    name = None
    opacity = None
    filter_mode = None
    rules = []

    def __init__(self, name=None, opacity=None, filter_mode=None, rules=None):
        if name:
            self.name = name
        if opacity is not None:
            self.opacity = opacity
        if filter_mode:
            self.filter_mode = filter_mode
        if rules:
            self.rules = rules

    def to_xml(self):
        root = etree.Element("Style")
        if self.name:
            root.set('name', self.name)
        if self.opacity is not None:
            root.set('opacity', str(self.opacity))
        if self.filter_mode:
            root.set('filter-mode', self.filter_mode)
        for rule in self.rules:
            root.append(rule.to_xml())
        return root
