from unittest import TestCase
from mapnik_xml import Map, Style, Rule, BuildingSymbolizer, LinePatternSymbolizer, LineSymbolizer, MarkersSymbolizer,\
    TextSymbolizer, PointSymbolizer, PolygonPatternSymbolizer, PolygonSymbolizer, RasterSymbolizer, ShieldSymbolizer,\
    GroupSymbolizer, DebugSymbolizer, Layer, PostgisDatasource, PgRasterDatasource, GdalDatasource, OgrDatasource,\
    OsmPluginDatasource, ShapeFileDatasource
from mapnik_xml.datasources import BasePostgisDatasource


class MapTestCase(TestCase):
    def setUp(self):
        self.map = Map()
        self.map.layers = []
        self.map.style = []

    def test_map_empty(self):
        self.assertEqual(self.map.to_string(), '<Map/>')

    def test_map_buffer_size(self):
        buffer_size = 256
        self.map.buffer_size = buffer_size
        self.assertEqual(self.map.to_string(), '<Map buffer-size="256"/>')

    def test_map_background_color(self):
        self.map.background_color = '#FFFFFF'
        self.assertEqual(self.map.to_string(), '<Map background-color="#FFFFFF"/>')

    def test_map_background_image(self):
        self.map.background_image = 'pattern.png'
        self.assertEqual(self.map.to_string(), '<Map background-image="pattern.png"/>')

    def test_map_font_directory(self):
        self.map.font_directory = '/usr/lib/fonts'
        self.assertEqual(self.map.to_string(), '<Map font-directory="/usr/lib/fonts"/>')

    def test_map_minimum_version(self):
        self.map.minimum_version = '0.6.1'
        self.assertEqual(self.map.to_string(), '<Map minimum-version="0.6.1"/>')

    def test_map_maximum_extent(self):
        self.map.maximum_extent = '-180,-90,180,90'
        self.assertEqual(self.map.to_string(), '<Map maximum-extent="-180,-90,180,90"/>')

    def test_map_srs(self):
        srs = '+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-100000 ' \
              '+ellps=airy +towgs84=446.448,-125.157,542.06,0.1502,0.247,0.8421,-20.4894 +units=m +no_defs'
        self.map.srs = srs
        self.assertEqual(self.map.to_string(), '<Map srs="{:s}"/>'.format(srs))

    def test_map_style(self):
        style = Style()
        self.map.styles.append(style)
        self.assertEqual(self.map.to_string(), '<Map><Style/></Map>')

    def test_map_layer(self):
        layer = Layer()
        self.map.layers.append(layer)
        self.assertEqual(self.map.to_string(), '<Map><Layer/></Map>')


class LayerTestCase(TestCase):
    def setUp(self):
        self.layer = Layer()

    def test_layer_empty(self):
        self.assertEqual(self.layer.to_string(), '<Layer/>')

    def test_layer_style(self):
        self.layer.styles = [Style(name='test')]
        self.assertEqual(self.layer.to_string(), '<Layer>'
                                                 '<StyleName>test</StyleName>'
                                                 '</Layer>')

    def test_layer_style_str(self):
        self.layer.styles = ['test']
        self.assertEqual(self.layer.to_string(), '<Layer>'
                                                 '<StyleName>test</StyleName>'
                                                 '</Layer>')

    def test_layer_abstract(self):
        self.layer.abstract = 'abstract'
        self.assertEqual(self.layer.to_string(), '<Layer abstract="abstract"/>')

    def test_layer_cache_features_on(self):
        self.layer.cache_features = True
        self.assertEqual(self.layer.to_string(), '<Layer cache-features="on"/>')

    def test_layer_cache_features_off(self):
        self.layer.cache_features = False
        self.assertEqual(self.layer.to_string(), '<Layer cache-features="off"/>')

    def test_layer_clear_label_cache_on(self):
        self.layer.clear_label_cache = True
        self.assertEqual(self.layer.to_string(), '<Layer clear-label-cache="on"/>')

    def test_layer_clear_label_cache_off(self):
        self.layer.clear_label_cache = False
        self.assertEqual(self.layer.to_string(), '<Layer clear-label-cache="off"/>')

    def test_layer_minzoom(self):
        self.layer.minzoom = 0
        self.assertEqual(self.layer.to_string(), '<Layer minzoom="0"/>')

    def test_layer_maxzoom(self):
        self.layer.maxzoom = 10000
        self.assertEqual(self.layer.to_string(), '<Layer maxzoom="10000"/>')

    def test_layer_name(self):
        self.layer.name = 'layer name'
        self.assertEqual(self.layer.to_string(), '<Layer name="layer name"/>')

    def test_layer_title(self):
        self.layer.title = 'layer title'
        self.assertEqual(self.layer.to_string(), '<Layer title="layer title"/>')

    def test_layer_srs(self):
        self.layer.srs = 'srs'
        self.assertEqual(self.layer.to_string(), '<Layer srs="srs"/>')

    def test_layer_status_on(self):
        self.layer.status = True
        self.assertEqual(self.layer.to_string(), '<Layer status="on"/>')

    def test_layer_status_off(self):
        self.layer.status = False
        self.assertEqual(self.layer.to_string(), '<Layer status="off"/>')

    def test_layer_queryable_true(self):
        self.layer.queryable = True
        self.assertEqual(self.layer.to_string(), '<Layer queryable="true"/>')

    def test_layer_queryable_false(self):
        self.layer.queryable = False
        self.assertEqual(self.layer.to_string(), '<Layer queryable="false"/>')

    def test_layer_datasource(self):
        self.layer.datasource = PostgisDatasource()
        self.assertEqual(self.layer.to_string(), '<Layer>'
                                                 '<Datasource>'
                                                 '<Parameter name="type">postgis</Parameter>'
                                                 '</Datasource>'
                                                 '</Layer>')


class StyleTestCase(TestCase):

    def setUp(self):
        self.style = Style()

    def test_style_empty(self):
        self.assertEqual(self.style.to_string(), '<Style/>')

    def test_style_name(self):
        self.style.name = 'style name'
        self.assertEqual(self.style.to_string(), '<Style name="style name"/>')

    def test_style_opacity(self):
        self.style.opacity = 0.5
        self.assertEqual(self.style.to_string(), '<Style opacity="0.5"/>')

    def test_style_filter_mode(self):
        self.style.filter_mode = 'default'
        self.assertEqual(self.style.to_string(), '<Style filter-mode="default"/>')

    def test_style_rule(self):
        rule = Rule()
        self.style.rules.append(rule)
        self.assertEqual(self.style.to_string(), '<Style><Rule/></Style>')


class RuleTestCase(TestCase):

    def setUp(self):
        self.rule = Rule()

    def test_rule_empty(self):
        self.assertEqual(self.rule.to_string(), '<Rule/>')

    def test_rule_name(self):
        self.rule.name = 'rule name'
        self.assertEqual(self.rule.to_string(), '<Rule name="rule name"/>')

    def test_rule_title(self):
        self.rule.title = 'rule title'
        self.assertEqual(self.rule.to_string(), '<Rule title="rule title"/>')

    def test_rule_min_scale(self):
        self.rule.min_scale = 0
        self.assertEqual(self.rule.to_string(), '<Rule>'
                                                '<MinScaleDenominator>0</MinScaleDenominator>'
                                                '</Rule>')

    def test_rule_max_scale(self):
        self.rule.max_scale = 0
        self.assertEqual(self.rule.to_string(), '<Rule>'
                                                '<MaxScaleDenominator>0</MaxScaleDenominator>'
                                                '</Rule>')

    def test_rule_filter(self):
        self.rule.filter = '[major] = 1'
        self.assertEqual(self.rule.to_string(), '<Rule>'
                                                '<Filter>[major] = 1</Filter>'
                                                '</Rule>')

    def test_rule_else_filter(self):
        self.rule.else_filter = True
        self.assertEqual(self.rule.to_string(), '<Rule><ElseFilter/></Rule>')


class BuildingSymbolizerTestCase(TestCase):
    def setUp(self):
        self.symb = BuildingSymbolizer()

    def test_building_symbolizer_empty(self):
        self.assertEqual(self.symb.to_string(), '<BuildingSymbolizer/>')

    def test_building_symbolizer_fill(self):
        self.symb.fill = '#FFFFFF'
        self.assertEqual(self.symb.to_string(), '<BuildingSymbolizer fill="#FFFFFF"/>')

    def test_building_symbolizer_fill_opacity(self):
        self.symb.fill_opacity = .5
        self.assertEqual(self.symb.to_string(), '<BuildingSymbolizer fill-opacity="0.5"/>')

    def test_building_symbolizer_fill_opacity(self):
        self.symb.height = '[height]'
        self.assertEqual(self.symb.to_string(), '<BuildingSymbolizer height="[height]"/>')

    def test_building_symbolizer_fill_opacity(self):
        self.symb.height = .5
        self.assertEqual(self.symb.to_string(), '<BuildingSymbolizer height="0.5"/>')


# TODO write tests for LinePatternSymbolizer
class LinePatternSymbolizerTestCase(TestCase):
    pass


class LineSymbolizerTestCase(TestCase):
    def setUp(self):
        self.symb = LineSymbolizer()

    def test_line_symbolizer_empty(self):
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer/>')

    def test_line_symbolizer_stroke(self):
        self.symb.stroke = 'black'
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer stroke="black"/>')

    def test_line_symbolizer_stroke_width(self):
        self.symb.stroke_width = .5
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer stroke-width="0.5"/>')

    def test_line_symbolizer_stroke_opacity(self):
        self.symb.stroke_opacity = .5
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer stroke-opacity="0.5"/>')

    def test_line_symbolizer_stroke_linejoin(self):
        self.symb.stroke_linejoin = 'miter'
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer stroke-linejoin="miter"/>')

    def test_line_symbolizer_stroke_linecap(self):
        self.symb.stroke_linecap = 'butt'
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer stroke-linecap="butt"/>')

    def test_line_symbolizer_stroke_dasharray(self):
        self.symb.stroke_dasharray = (22.5, 0)
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer stroke-dasharray="22.5,0"/>')

    def test_line_symbolizer_comp_op(self):
        self.symb.comp_op = 'multiply'
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer comp-op="multiply"/>')

    def test_line_symbolizer_smooth(self):
        self.symb.smooth = 0
        self.assertEqual(self.symb.to_string(), '<LineSymbolizer smooth="0"/>')


# TODO write tests for MarkersSymbolizer
class MarkersSymbolizerTestCase(TestCase):
    pass


# TODO write tests for TextSymbolizer
class TextSymbolizerTestCase(TestCase):
    pass


# TODO write tests for PointSymbolizer
class PointSymbolizerTestCase(TestCase):
    pass


# TODO write tests for PolygonPatternSymbolizer
class PolygonPatternSymbolizerTestCase(TestCase):
    pass


# TODO write tests for PolygonSymbolizer
class PolygonSymbolizerTestCase(TestCase):
    pass


# TODO write tests for RasterSymbolizer
class RasterSymbolizerTestCase(TestCase):
    pass


# TODO write tests for ShieldSymbolizer
class ShieldSymbolizerTestCase(TestCase):
    def setUp(self):
        self.symb = ShieldSymbolizer()

    def test_shield_symbolizer_empty(self):
        self.assertEqual(self.symb.to_string(), '<ShieldSymbolizer/>')


# TODO write tests for GroupSymbolizer
class GroupSymbolizerTestCase(TestCase):
    pass


class DebugSymbolizerTestCase(TestCase):
    def setUp(self):
        self.symb = DebugSymbolizer()

    def test_debug_symbolizer_empty(self):
        self.assertEqual(self.symb.to_string(), '<DebugSymbolizer/>')


class BasePostgisDatasourceTestCase(TestCase):
    def setUp(self):
        self.datasource = BasePostgisDatasource()
        self.datasource._type = 'postgis'

    def test_datasource_empty(self):
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_host(self):
        self.datasource.host = '127.0.0.1'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="host">127.0.0.1</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_port(self):
        self.datasource.port = 5432
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="port">5432</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_dbname(self):
        self.datasource.dbname = 'data'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="dbname">data</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_user(self):
        self.datasource.user = 'postgres'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="user">postgres</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_password(self):
        self.datasource.password = 'postgres'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="password">postgres</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_table(self):
        self.datasource.table = 'public.table'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="table">public.table</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_srid(self):
        self.datasource.srid = 4326
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="srid">4326</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_extent_from_subquery_true(self):
        self.datasource.extent_from_subquery = True
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="extent_from_subquery">true</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_extent_from_subquery_false(self):
        self.datasource.extent_from_subquery = False
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="extent_from_subquery">false</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_connect_timeout(self):
        self.datasource.connect_timeout = 10
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="connect_timeout">10</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_persist_connection_true(self):
        self.datasource.persist_connection = True
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="persist_connection">true</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_persist_connection_false(self):
        self.datasource.persist_connection = False
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="persist_connection">false</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_row_limit(self):
        self.datasource.row_limit = 10
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="row_limit">10</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_cursor_size(self):
        self.datasource.cursor_size = 10
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="cursor_size">10</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_initial_size(self):
        self.datasource.initial_size = 10
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="initial_size">10</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_max_size(self):
        self.datasource.max_size = 10
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="max_size">10</Parameter>'
                                                      '</Datasource>' % self.datasource._type)


    def test_datasource_max_async_connection(self):
        self.datasource.max_async_connection = 1
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="max_async_connection">1</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_estimate_extent_true(self):
        self.datasource.estimate_extent = True
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="estimate_extent">true</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_estimate_extent_false(self):
        self.datasource.estimate_extent = False
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="estimate_extent">false</Parameter>'
                                                      '</Datasource>' % self.datasource._type)

    def test_datasource_extent(self):
        self.datasource.extent = '-180,-90,180,90'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">%s</Parameter>'
                                                      '<Parameter name="extent">-180,-90,180,90</Parameter>'
                                                      '</Datasource>' % self.datasource._type)


class PostgisDatasourceTestCase(BasePostgisDatasourceTestCase):
    def setUp(self):
        self.datasource = PostgisDatasource()

    def test_datasource_geometry_field(self):
        self.datasource.geometry_field = 'geom'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">postgis</Parameter>'
                                                      '<Parameter name="geometry_field">geom</Parameter>'
                                                      '</Datasource>')

    def test_datasource_geometry_table(self):
        self.datasource.geometry_table = 'table'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">postgis</Parameter>'
                                                      '<Parameter name="geometry_table">table</Parameter>'
                                                      '</Datasource>')

    def test_datasource_multiple_geometries_true(self):
        self.datasource.multiple_geometries = True
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">postgis</Parameter>'
                                                      '<Parameter name="multiple_geometries">true</Parameter>'
                                                      '</Datasource>')

    def test_datasource_multiple_geometries_false(self):
        self.datasource.multiple_geometries = False
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">postgis</Parameter>'
                                                      '<Parameter name="multiple_geometries">false</Parameter>'
                                                      '</Datasource>')

    def test_datasource_encoding(self):
        self.datasource.encoding = 'CP1251'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">postgis</Parameter>'
                                                      '<Parameter name="encoding">CP1251</Parameter>'
                                                      '</Datasource>')

    def test_datasource_simplify_geometries_true(self):
        self.datasource.simplify_geometries = True
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">postgis</Parameter>'
                                                      '<Parameter name="simplify_geometries">true</Parameter>'
                                                      '</Datasource>')

    def test_datasource_simplify_geometries_false(self):
        self.datasource.simplify_geometries = False
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">postgis</Parameter>'
                                                      '<Parameter name="simplify_geometries">false</Parameter>'
                                                      '</Datasource>')


class PgRasterDatasourceTestCase(BasePostgisDatasourceTestCase):
    def setUp(self):
        self.datasource = PgRasterDatasource()

    def test_datasource_raster_field(self):
        self.datasource.raster_field = 'raster'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="raster_field">raster</Parameter>'
                                                      '</Datasource>')

    def test_datasource_raster_table(self):
        self.datasource.raster_table = 'table'
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="raster_table">table</Parameter>'
                                                      '</Datasource>')

    def test_datasource_prescale_rasters_true(self):
        self.datasource.prescale_rasters = True
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="prescale_rasters">true</Parameter>'
                                                      '</Datasource>')

    def test_datasource_prescale_rasters_false(self):
        self.datasource.prescale_rasters = False
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="prescale_rasters">false</Parameter>'
                                                      '</Datasource>')

    def test_datasource_use_overviews_true(self):
        self.datasource.use_overviews = True
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="use_overviews">true</Parameter>'
                                                      '</Datasource>')

    def test_datasource_use_overviews_false(self):
        self.datasource.use_overviews = False
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="use_overviews">false</Parameter>'
                                                      '</Datasource>')

    def test_datasource_clip_rasters_true(self):
        self.datasource.clip_rasters = True
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="clip_rasters">true</Parameter>'
                                                      '</Datasource>')

    def test_datasource_clip_rasters_false(self):
        self.datasource.clip_rasters = False
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="clip_rasters">false</Parameter>'
                                                      '</Datasource>')

    def test_datasource_band(self):
        self.datasource.band = 0
        self.assertEqual(self.datasource.to_string(), '<Datasource>'
                                                      '<Parameter name="type">pgraster</Parameter>'
                                                      '<Parameter name="band">0</Parameter>'
                                                      '</Datasource>')


# TODO write tests for ShapeFileDatasource
class ShapeFileDatasourceTestCase(TestCase):
    def setUp(self):
        self.datasource = ShapeFileDatasource()


# TODO write tests for GdalDatasource
class GdalDatasourceTestCase(TestCase):
    def setUp(self):
        self.datasource = GdalDatasource()


# TODO write tests for OgrDatasource
class OgrDatasourceTestCase(TestCase):
    def setUp(self):
        self.datasource = OgrDatasource()


# TODO write tests for OsmPluginDatasource
class OsmPluginDatasourceTestCase(TestCase):
    def setUp(self):
        self.datasource = OsmPluginDatasource()
