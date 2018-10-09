from lxml import etree


class BaseElement:
    def to_xml(self):
        raise NotImplementedError()

    def to_string(self):
        return str(etree.tostring(self.to_xml()), encoding='utf-8')
