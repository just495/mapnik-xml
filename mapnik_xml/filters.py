from lxml import etree
from .base import BaseElement


class Filter(BaseElement):
    _value = None

    def __init__(self, value):
        self._value = value

    def to_xml(self):
        root = etree.Element("Filter")
        root.text = self._value
        return root


class ElseFilter(BaseElement):

    def to_xml(self):
        root = etree.Element("ElseFilter")
        return root
