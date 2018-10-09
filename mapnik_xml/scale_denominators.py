from lxml import etree
from .base import BaseElement


class MinScaleDenominator(BaseElement):
    _value = None

    def __init__(self, value):
        self._value = value

    def to_xml(self):
        root = etree.Element("MinScaleDenominator")
        root.text = str(self._value)
        return root


class MaxScaleDenominator(BaseElement):
    _value = None

    def __init__(self, value):
        self._value = value

    def to_xml(self):
        root = etree.Element("MaxScaleDenominator")
        root.text = str(self._value)
        return root