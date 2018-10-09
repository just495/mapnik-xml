from lxml import etree
from .base import BaseElement


class Map(BaseElement):
    buffer_size = None
    srs = None
    background_color = None
    font_directory = None
    minimum_version = None
    background_image = None
    maximum_extent = None
    paths_from_xml = None
    styles = []
    layers = []

    def __init__(self, buffer_size=None, srs=None, background_color=None, font_directory=None, minimum_version=None,
                 background_image=None, maximum_extent=None, styles=[], layers=[]):
        self.buffer_size = buffer_size
        self.srs = srs
        self.background_color = background_color
        self.font_directory = font_directory
        self.minimum_version = minimum_version
        self.background_image = background_image
        self.maximum_extent = maximum_extent
        self.styles = styles
        self.layers = layers

    def to_xml(self):
        root = etree.Element("Map")
        if self.buffer_size:
            root.set('buffer-size', str(self.buffer_size))
        if self.srs:
            root.set('srs', self.srs)
        if self.background_color:
            root.set('background-color', self.background_color)
        if self.background_image:
            root.set('background-image', self.background_image)
        if self.font_directory:
            root.set('font-directory', self.font_directory)
        if self.minimum_version:
            root.set('minimum-version', self.minimum_version)
        if self.maximum_extent:
            root.set('maximum-extent', self.maximum_extent)
        for style in self.styles:
            root.append(style.to_xml())
        for layer in self.layers:
            root.append(layer.to_xml())
        return root
