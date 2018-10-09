from lxml import etree
from .base import BaseElement


class BuildingSymbolizer(BaseElement):
    fill = None
    fill_opacity = None
    height = None

    def __init__(self, fill=None, fill_opacity=None, height=None):
        self.fill = fill
        self.fill_opacity = fill_opacity
        self.height = height

    def to_xml(self):
        root = etree.Element("BuildingSymbolizer")
        if self.fill:
            root.set('fill', self.fill)
        if self.fill_opacity is not None:
            root.set('fill-opacity', str(self.fill_opacity))
        if self.height is not None:
            root.set('height', str(self.height))
        return root


# TODO add GroupSymbolizer support
class GroupSymbolizer(BaseElement):
    def to_xml(self):
        root = etree.Element("GroupSymbolizer")
        return root


class LineSymbolizer(BaseElement):
    stroke = None
    stroke_width = None
    stroke_opacity = None
    stroke_linejoin = None
    stroke_linecap = None
    stroke_dasharray = None
    comp_op = None
    smooth = None

    def __init__(self, stroke=None, stroke_width=None, stroke_opacity=None,stroke_linejoin=None, stroke_linecap=None,
                 stroke_dasharray=None, comp_op=None, smooth=None):
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.stroke_opacity = stroke_opacity
        self.stroke_linejoin = stroke_linejoin
        self.stroke_linecap = stroke_linecap
        self.stroke_dasharray = stroke_dasharray
        self.comp_op = comp_op
        self.smooth = smooth

    def to_xml(self):
        root = etree.Element("LineSymbolizer")
        if self.stroke:
            root.set('stroke', self.stroke)
        if self.stroke_width is not None:
            root.set('stroke-width', str(self.stroke_width))
        if self.stroke_opacity is not None:
            root.set('stroke-opacity', str(self.stroke_opacity))
        if self.stroke_linejoin:
            root.set('stroke-linejoin', str(self.stroke_linejoin))
        if self.stroke_linecap:
            root.set('stroke-linecap', str(self.stroke_linecap))
        if self.stroke_dasharray:
            root.set('stroke-dasharray', ",".join([str(value) for value in self.stroke_dasharray]))
        if self.comp_op:
            root.set('comp-op', self.comp_op)
        if self.smooth is not None:
            root.set('smooth', str(self.smooth))
        return root


class LinePatternSymbolizer(BaseElement):
    file = None
    base = None
    comp_op = None

    def __init__(self, file=None, base=None, comp_op=None):
        self.file = file
        self.base = base
        self.comp_op = comp_op

    def to_xml(self):
        root = etree.Element("LinePatternSymbolizer")
        if self.base:
            root.set('base', self.base)
        if self.file:
            root.set('file', self.file)
        if self.comp_op:
            root.set('comp-op', self.comp_op)
        return root


class MarkersSymbolizer(BaseElement):
    allow_overlap = None
    spacing = None
    max_error = None
    file = None
    transform = None
    opacity = None
    fill = None
    stroke = None
    stroke_width = None
    stroke_opacity = None
    width = None
    height = None
    placement = None
    ignore_placement = None
    marker_type = None

    def __init__(self, allow_overlap=None, spacing=None, max_error=None, file=None, transform=None, opacity=None,
                 fill=None, stroke=None, stroke_width=None, stroke_opacity=None, width=None, height=None,
                 placement=None, ignore_placement=None, marker_type=None):
        self.allow_overlap = allow_overlap
        self.spacing = spacing
        self.max_error = max_error
        self.file = file
        self.transform = transform
        self.opacity = opacity
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.stroke_opacity = stroke_opacity
        self.width = width
        self.height = height
        self.placement = placement
        self.ignore_placement = ignore_placement
        self.marker_type = marker_type

    def to_xml(self):
        root = etree.Element("MarkersSymbolizer")
        if self.allow_overlap is not None:
            root.set('allow-overlap', str(self.allow_overlap).lower())
        if self.spacing is not None:
            root.set('spacing', str(self.spacing))
        if self.max_error is not None:
            root.set('max-error', str(self.max_error))
        if self.file:
            root.set('file', self.file)
        if self.transform:
            root.set('transform', self.transform)
        if self.opacity is not None:
            root.set('opacity', str(self.opacity))
        if self.fill:
            root.set('fill', self.fill)
        if self.stroke:
            root.set('stroke', self.stroke)
        if self.stroke_width is not None:
            root.set('stroke-with', str(self.stroke_width))
        if self.stroke_opacity is not None:
            root.set('stroke-opacity', str(self.stroke_opacity))
        if self.width is not None:
            root.set('width', str(self.width))
        if self.height is not None:
            root.set('height', str(self.height))
        if self.placement:
            root.set('placement', self.placement)
        if self.ignore_placement is not None:
            root.set('ignore-placement', str(self.ignore_placement).lower())
        if self.marker_type:
            root.set('marker-type', self.marker_type)
        return root


class PolygonSymbolizer(BaseElement):
    fill = None
    fill_opacity = None
    gamma = None
    comp_op = None

    def __init__(self, fill=None, fill_opacity=None, gamma=None, comp_op=None):
        self.fill = fill
        self.fill_opacity = fill_opacity
        self.gamma = gamma
        self.comp_op = comp_op

    def to_xml(self):
        root = etree.Element("PolygonSymbolizer")
        if self.fill:
            root.set('fill', self.fill)
        if self.fill_opacity is not None:
            root.set('fill-opacity', str(self.fill_opacity))
        if self.gamma is not None:
            root.set('fill-opacity', str(self.gamma))
        if self.comp_op:
            root.set('comp-op', self.comp_op)
        return root


class PolygonPatternSymbolizer(BaseElement):
    file = None
    comp_op = None

    def __init__(self, file=None, comp_op=None):
        self.file = file
        self.comp_op = comp_op

    def to_xml(self):
        root = etree.Element("PolygonPatternSymbolizer")
        if self.file:
            root.set('file', self.file)
        if self.comp_op:
            root.set('comp-op', self.comp_op)
        return root


class PointSymbolizer(BaseElement):
    file = None
    allow_overlap = None
    opacity = None
    transform = None
    ignore_placement = None
    comp_op = None

    def __init__(self, file=None, allow_overlap=None, opacity=None, transform=None, ignore_placement=None,
                 comp_op=None):
        self.file = file
        self.allow_overlap = allow_overlap
        self.opacity = opacity
        self.transform = transform
        self.ignore_placement = ignore_placement
        self.comp_op = comp_op

    def to_xml(self):
        root = etree.Element("PointSymbolizer")
        if self.file:
            root.set('file', self.file)
        if self.allow_overlap is not None:
            root.set('allow-overlap', str(self.allow_overlap).lower())
        if self.opacity is not None:
            root.set('opacity', str(self.opacity))
        if self.transform:
            root.set('transform', self.transform)
        if self.ignore_placement is not None:
            root.set('ignore-placement', str(self.ignore_placement).lower())
        if self.comp_op:
            root.set('comp-op', self.comp_op)
        return root


class RasterSymbolizer(BaseElement):
    opacity = None
    scaling = None
    comp_op = None
    colorizer = None

    def __init__(self, opacity=None, scaling=None, comp_op=None, colorizer=None):
        self.opacity = opacity
        self.scaling = scaling
        self.comp_op = comp_op
        self.colorizer = colorizer

    def to_xml(self):
        root = etree.Element("RasterSymbolizer")
        if self.opacity is not None:
            root.set('opacity', str(self.opacity))
        if self.scaling:
            root.set('scaling', self.scaling)
        if self.comp_op:
            root.set('comp-op', self.comp_op)
        if self.colorizer:
            root.append(self.colorizer.to_xml())
        return root


class RasterColorizer(BaseElement):
    default_mode = None
    default_color = None
    epsilon = None
    stops = []

    def __init__(self, default_mode=None, default_color=None, epsilon=None, stops=[]):
        self.default_mode = default_mode
        self.default_color = default_color
        self.epsilon = epsilon
        self.stops = stops
        
    def to_xml(self):
        root = etree.Element("stop")
        if self.default_mode:
            root.set('default-mode', self.default_mode)
        if self.default_color:
            root.set('default_color', self.default_color)
        if self.epsilon is not None:
            root.set('epsilon', str(self.epsilon))
        for stop in self.stops:
            root.append(stop.to_xml())
        return root


class RasterColorizerStop(BaseElement):
    _color = None
    _value = None
    _mode = None

    def __init__(self, value, color=None, mode=None):
        self._value = value
        self._color = color
        self._mode = mode

    def to_xml(self):
        root = etree.Element("stop")
        if self._color:
            root.set('color', self._color)
        if self._value:
            root.set('value', str(self._value))
        if self._mode:
            root.set('mode', self._mode)
        return root


class TextSymbolizer(BaseElement):
    spacing = None
    label_position_tolerance = None
    force_odd_labels = None
    max_char_angle_delta = None
    halo_rasterizer = None
    displacement = None
    avoid_edges = None
    margin = None
    repeat_distance = None
    allow_overlap = None
    placement = None
    opacity = None
    minimum_padding = None
    minimum_path_length = None
    placement_type = None
    placements = None
    upright = None
    clip = None
    largest_bbox_only = None
    comp_op = None
    # Text layout options
    dx = None
    dy = None
    vertical_alignment = None
    horizontal_alignment = None
    justify_alignment = None
    text_ratio = None
    wrap_width = None
    wrap_before = None
    orientation = None
    rotate_displacement = None
    # Character formatting options
    face_name = None
    fontset_name = None
    size = None
    fill = None
    halo_fill = None
    halo_radius = None
    halo_comp_op = None
    character_spacing = None
    line_spacing = None
    wrap_character = None
    text_transform = None
    # Deprecated options
    name = None
    minimum_distance = None

    def __init__(self, spacing=None, label_position_tolerance=None, force_odd_labels=None, max_char_angle_delta=None,
                 halo_rasterizer=None, displacement=None, avoid_edges=None, margin=None, repeat_distance=None,
                 allow_overlap=None, placement=None, opacity=None, minimum_padding=None, minimum_path_length=None,
                 placement_type=None, placements=None, upright=None, clip=None, largest_bbox_only=None, comp_op=None,
                 dx=None, dy=None, vertical_alignment=None, horizontal_alignment=None, justify_alignment=None,
                 text_ratio=None, wrap_width=None, wrap_before=None, orientation=None, rotate_displacement=None,
                 face_name=None, fontset_name=None, size=None, fill=None, halo_fill=None, halo_radius=None,
                 halo_comp_op=None, character_spacing=None, line_spacing=None, wrap_character=None,
                 text_transform=None, name=None, minimum_distance=None):
        self.spacing = spacing
        self.label_position_tolerance = label_position_tolerance
        self.force_odd_labels = force_odd_labels
        self.max_char_angle_delta = max_char_angle_delta
        self.halo_rasterizer = halo_rasterizer
        self.displacement = displacement
        self.avoid_edges = avoid_edges
        self.margin = margin
        self.repeat_distance = repeat_distance
        self.allow_overlap = allow_overlap
        self.placement = placement
        self.opacity = opacity
        self.minimum_padding = minimum_padding
        self.minimum_path_length = minimum_path_length
        self.placement_type = placement_type
        self.placements = placements
        self.upright = upright
        self.clip = clip
        self.largest_bbox_only = largest_bbox_only
        self.comp_op = comp_op
        self.dx = dx
        self.dy = dy
        self.vertical_alignment = vertical_alignment
        self.horizontal_alignment = horizontal_alignment
        self.justify_alignment = justify_alignment
        self.text_ratio = text_ratio
        self.wrap_width = wrap_width
        self.wrap_before = wrap_before
        self.orientation = orientation
        self.rotate_displacement = rotate_displacement
        self.face_name = face_name
        self.fontset_name = fontset_name
        self.size = size
        self.fill = fill
        self.halo_fill = halo_fill
        self.halo_radius = halo_radius
        self.halo_comp_op = halo_comp_op
        self.character_spacing = character_spacing
        self.line_spacing = line_spacing
        self.wrap_character = wrap_character
        self.text_transform = text_transform
        self.name = name
        self.minimum_distance = minimum_distance

    def to_xml(self):
        root = etree.Element("TextSymbolizer")
        if self.name:
            root.text = self.name
        if self.spacing is not None:
            root.set('spacing', str(self.spacing))
        if self.label_position_tolerance is not None:
            root.set('label-position-tolerance', str(self.label_position_tolerance))
        if self.force_odd_labels is not None:
            root.set('force-odd-labels', str(self.force_odd_labels).lower())
        if self.max_char_angle_delta is not None:
            root.set('max-char-angle-delta', str(self.max_char_angle_delta))
        if self.halo_rasterizer:
            root.set('halo_rasterizer', self.halo_rasterizer)
        if self.displacement:
            root.set('displacement', str(self.displacement))
        if self.avoid_edges is not None:
            root.set('avoid-edges', str(self.avoid_edges).lower())
        if self.margin is not None:
            root.set('margin', str(self.margin))
        if self.repeat_distance is not None:
            root.set('repeat-distance', str(self.repeat_distance))
        if self.allow_overlap is not None:
            root.set('allow-overlap', str(self.allow_overlap).lower())
        if self.placement:
            root.set('placement', self.placement)
        if self.opacity is not None:
            root.set('opacity', str(self.opacity))
        if self.minimum_padding is not None:
            root.set('minimum-padding', str(self.minimum_padding))
        if self.minimum_path_length is not None:
            root.set('minimum-path-length', str(self.minimum_path_length))
        if self.placement_type:
            root.set('placement-type', self.placement_type)
        if self.placements:
            root.set('placements', self.placements)
        if self.upright:
            root.set('upright', self.upright)
        if self.clip is not None:
            root.set('clip', str(self.clip).lower())
        if self.largest_bbox_only is not None:
            root.set('largest-bbox-only', str(self.largest_bbox_only).lower())
        if self.comp_op:
            root.set('comp-op', self.comp_op)
        if self.dx is not None:
            root.set('dx', str(self.dx))
        if self.dy is not None:
            root.set('dy', str(self.dy))
        if self.vertical_alignment:
            root.set('vertical-alignment', self.vertical_alignment)
        if self.horizontal_alignment:
            root.set('horizontal-alignment', self.horizontal_alignment)
        if self.justify_alignment:
            root.set('justify-alignment', self.justify_alignment)
        if self.text_ratio is not None:
            root.set('text-ratio', str(self.text_ratio))
        if self.wrap_width is not None:
            root.set('wrap-width', str(self.wrap_width))
        if self.wrap_before is not None:
            root.set('wrap-before', str(self.wrap_before).lower())
        if self.orientation is not None:
            root.set('orientation', str(self.orientation))
        if self.rotate_displacement is not None:
            root.set('rotate-displacement', self.rotate_displacement)
        if self.face_name:
            root.set('face-name', self.face_name)
        if self.fontset_name:
            root.set('fontset-name', self.fontset_name)
        if self.size is not None:
            root.set('size', str(self.size))
        if self.fill:
            root.set('fill', self.fill)
        if self.halo_fill:
            root.set('halo-fill', self.halo_fill)
        if self.halo_radius is not None:
            root.set('halo-radius', str(self.halo_radius))
        if self.halo_comp_op:
            root.set('halo-comp-op', self.halo_comp_op)
        if self.character_spacing is not None:
            root.set('character-spacing', str(self.character_spacing))
        if self.line_spacing is not None:
            root.set('line-spacing', str(self.line_spacing))
        if self.wrap_character:
            root.set('wrap-character', self.wrap_character)
        if self.text_transform:
            root.set('text-transform', self.text_transform)
        if self.minimum_distance is not None:
            root.set('minimum-distance', str(self.minimum_distance))
        return root


class ShieldSymbolizer(TextSymbolizer):
    base = None
    file = None
    opacity = None
    text_opacity = None
    unlock_image = None
    shield_dx = None
    shield_dy = None
    transform = None

    def __init__(self, base=None, file=None, opacity=None, text_opacity=None, unlock_image=None, shield_dx=None,
                 shield_dy=None, transform=None, *args, **kwargs):
        super(ShieldSymbolizer, self).__init__(*args, **kwargs)
        self.base = base
        self.file = file
        self.opacity = opacity
        self.text_opacity = text_opacity
        self.unlock_image = unlock_image
        self.shield_dx = shield_dx
        self.shield_dy = shield_dy
        self.transform = transform

    def to_xml(self):
        root = super(ShieldSymbolizer, self).to_xml()
        root.tag = 'ShieldSymbolizer'
        if self.base:
            root.set('base', self.base)
        if self.file:
            root.set('file', self.file)
        if self.opacity is not None:
            root.set('opacity', str(self.opacity))
        if self.text_opacity is not None:
            root.set('text-opacity', str(self.text_opacity))
        if self.unlock_image:
            root.set('unlock-image', self.unlock_image)
        if self.shield_dx is not None:
            root.set('shield-dz', self.shield_dx)
        if self.shield_dy is not None:
            root.set('shield-dy', self.shield_dy)
        if self.transform:
            root.set('transform', self.transform)
        return root


class DebugSymbolizer(BaseElement):
    def to_xml(self):
        root = etree.Element("DebugSymbolizer")
        return root
