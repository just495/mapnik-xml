from lxml import etree
from .base import BaseElement


class Parameter(BaseElement):
    _name = None
    _value = None

    def __init__(self, name, value):
        self._name = name
        self._value = value

    def to_xml(self):
        root = etree.Element("Parameter")
        root.set('name', self._name)
        root.text = str(self._value)
        return root


class BaseDatasource(BaseElement):
    _type = None
    base_name = None
    name = None
    estimate_extent = None
    extent = None

    def __init__(self, base_name=None, name=None, estimate_extent=None, extent=None):
        self.base_name = base_name
        self.name = name
        self.estimate_extent = estimate_extent
        self.extent = extent

    def to_xml(self):
        root = etree.Element("Datasource")
        if self.base_name:
            root.set('base', self.base_name)
        if self.name:
            root.set('name', self.name)
        if self._type:
            root.append(Parameter('type', self._type).to_xml())
        if self.estimate_extent is not None:
            root.append(Parameter('estimate_extent', str(self.estimate_extent).lower()).to_xml())
        if self.extent:
            root.append(Parameter('extent', self.extent).to_xml())
        return root


class BasePostgisDatasource(BaseDatasource):
    host = None
    port = None
    dbname = None
    user = None
    password = None
    table = None
    srid = None
    extent_from_subquery = None
    connect_timeout	= None
    persist_connection = None
    row_limit = None
    cursor_size = None
    initial_size = None
    max_size = None
    max_async_connection = None

    def __init__(self, host=None, port=None, dbname=None, user=None, password=None, table=None, srid=None,
                 extent_from_subquery=None, connect_timeout=None, persist_connection=None, row_limit=None,
                 cursor_size=None, initial_size=None, max_size=None, max_async_connection=None, *args, **kwargs):
        super(BasePostgisDatasource, self).__init__(*args, **kwargs)
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.table = table
        self.srid = srid
        self.extent_from_subquery = extent_from_subquery
        self.connect_timeout = connect_timeout
        self.persist_connection = persist_connection
        self.row_limit = row_limit
        self.cursor_size = cursor_size
        self.initial_size = initial_size
        self.max_size = max_size
        self.max_async_connection = max_async_connection

    def to_xml(self):
        root = super(BasePostgisDatasource, self).to_xml()
        if self.host:
            root.append(Parameter('host', self.host).to_xml())
        if self.port is not None:
            root.append(Parameter('port', self.port).to_xml())
        if self.dbname:
            root.append(Parameter('dbname', self.dbname).to_xml())
        if self.user is not None:
            root.append(Parameter('user', self.user).to_xml())
        if self.password is not None:
            root.append(Parameter('password', self.password).to_xml())
        if self.table is not None:
            root.append(Parameter('table', self.table).to_xml())
        if self.srid is not None:
            root.append(Parameter('srid', self.srid).to_xml())
        if self.extent_from_subquery is not None:
            root.append(Parameter('extent_from_subquery', str(self.extent_from_subquery).lower()).to_xml())
        if self.connect_timeout is not None:
            root.append(Parameter('connect_timeout', self.connect_timeout).to_xml())
        if self.persist_connection is not None:
            root.append(Parameter('persist_connection', str(self.persist_connection).lower()).to_xml())
        if self.row_limit is not None:
            root.append(Parameter('row_limit', self.row_limit).to_xml())
        if self.cursor_size is not None:
            root.append(Parameter('cursor_size', self.cursor_size).to_xml())
        if self.initial_size is not None:
            root.append(Parameter('initial_size', self.initial_size).to_xml())
        if self.max_size is not None:
            root.append(Parameter('max_size', self.max_size).to_xml())
        if self.max_async_connection is not None:
            root.append(Parameter('max_async_connection', self.max_async_connection).to_xml())
        return root


class PostgisDatasource(BasePostgisDatasource):
    _type = 'postgis'
    geometry_field = None
    geometry_table = None
    multiple_geometries = None
    encoding = None
    simplify_geometries = None

    def __init__(self, geometry_field=None, geometry_table=None, multiple_geometries=None, encoding=None,
                 simplify_geometries=None, *args, **kwargs):
        super(PostgisDatasource, self).__init__(*args, **kwargs)
        self.geometry_field = geometry_field
        self.geometry_table = geometry_table
        self.multiple_geometries = multiple_geometries
        self.encoding = encoding
        self.simplify_geometries = simplify_geometries

    def to_xml(self):
        root = super(PostgisDatasource, self).to_xml()
        if self.geometry_field is not None:
            root.append(Parameter('geometry_field', self.geometry_field).to_xml())
        if self.geometry_table is not None:
            root.append(Parameter('geometry_table', self.geometry_table).to_xml())
        if self.multiple_geometries is not None:
            root.append(Parameter('multiple_geometries', str(self.multiple_geometries).lower()).to_xml())
        if self.encoding:
            root.append(Parameter('encoding', self.encoding).to_xml())
        if self.simplify_geometries is not None:
            root.append(Parameter('simplify_geometries', str(self.simplify_geometries).lower()).to_xml())
        return root


class PgRasterDatasource(BasePostgisDatasource):
    _type = 'pgraster'
    raster_field = None
    raster_table = None
    prescale_rasters = None
    use_overviews = None
    clip_rasters = None
    band = None

    def __init__(self, raster_field=None, raster_table=None, prescale_rasters=None, use_overviews=None,
                 clip_rasters=None, band=None, *args, **kwargs):
        super(PgRasterDatasource, self).__init__(*args, **kwargs)
        self.raster_field = raster_field
        self.raster_table = raster_table
        self.prescale_rasters = prescale_rasters
        self.use_overviews = use_overviews
        self.clip_rasters = clip_rasters
        self.band = band

    def to_xml(self):
        root = super(PgRasterDatasource, self).to_xml()
        if self.raster_field is not None:
            root.append(Parameter('raster_field', self.raster_field).to_xml())
        if self.raster_table is not None:
            root.append(Parameter('raster_table', self.raster_table).to_xml())
        if self.prescale_rasters is not None:
            root.append(Parameter('prescale_rasters', str(self.prescale_rasters).lower()).to_xml())
        if self.use_overviews is not None:
            root.append(Parameter('use_overviews', str(self.use_overviews).lower()).to_xml())
        if self.clip_rasters is not None:
            root.append(Parameter('clip_rasters', str(self.clip_rasters).lower()).to_xml())
        if self.band is not None:
            root.append(Parameter('band', self.band).to_xml())
        return root


class ShapeFileDatasource(BaseDatasource):
    _type = 'shape'
    encoding = None
    file = None

    def __init__(self, encoding=None, file=None, *args, **kwargs):
        super(ShapeFileDatasource, self).__init__(*args, **kwargs)
        self.encoding = encoding
        self.file = file

    def to_xml(self):
        root = super(ShapeFileDatasource, self).to_xml()
        if self.encoding:
            root.append(Parameter('encoding', self.encoding).to_xml())
        if self.file:
            root.append(Parameter('file', self.file).to_xml())
        return root


class GdalDatasource(BaseDatasource):
    _type = 'gdal'
    base = None
    file = None
    nodata = None
    shared = None

    def __init__(self, base=None, file=None, nodata=None, shared=None, *args, **kwargs):
        super(GdalDatasource, self).__init__(*args, **kwargs)
        self.base = base
        self.file = file
        self.nodata = nodata
        self.shared = shared

    def to_xml(self):
        root = super(GdalDatasource, self).to_xml()
        if self.base:
            root.append(Parameter('base', self.base).to_xml())
        if self.file:
            root.append(Parameter('file', self.file).to_xml())
        if self.nodata is not None:
            root.append(Parameter('nodata', self.nodata).to_xml())
        if self.shared is not None:
            root.append(Parameter('shared', str(self.shared).lower()).to_xml())
        return root


class OgrDatasource(BaseDatasource):
    _type = 'ogr'
    file = None
    base = None
    layer = None
    layer_by_index = None
    layer_by_sql = None
    multiple_geometries = None
    encoding = None
    string = None

    def __init__(self, file=None, base=None, layer=None, layer_by_index=None, layer_by_sql=None,
                 multiple_geometries=None, encoding=None, string=None, *args, **kwargs):
        super(OgrDatasource, self).__init__(*args, **kwargs)
        self.file = file
        self.base = base
        self.layer = layer
        self.layer_by_index = layer_by_index
        self.layer_by_sql = layer_by_sql
        self.multiple_geometries = multiple_geometries
        self.encoding = encoding
        self.string = string

    def to_xml(self):
        root = super(OgrDatasource, self).to_xml()
        if self.file:
            root.append(Parameter('file', self.file).to_xml())
        if self.base:
            root.append(Parameter('base', self.base).to_xml())
        if self.layer:
            root.append(Parameter('layer', self.layer).to_xml())
        if self.layer_by_index is not None:
            root.append(Parameter('layer_by_index', self.layer_by_index).to_xml())
        if self.layer_by_sql:
            root.append(Parameter('layer_by_sql', self.layer_by_sql).to_xml())
        if self.multiple_geometries:
            root.append(Parameter('multiple_geometries', str(self.multiple_geometries).lower()).to_xml())
        if self.encoding:
            root.append(Parameter('encoding', self.encoding).to_xml())
        if self.string:
            root.append(Parameter('string', self.string).to_xml())
        return root


class OsmPluginDatasource(BaseDatasource):
    _type = 'osm'
    file = None
    bbox = None
    filter_factor = None

    def __init__(self, file=None, bbox=None, filter_factor=None, *args, **kwargs):
        super(OsmPluginDatasource, self).__init__(*args, **kwargs)
        self.file = file
        self.bbox = bbox
        self.filter_factor = filter_factor

    def to_xml(self):
        root = super(OsmPluginDatasource, self).to_xml()
        if self.file:
            root.append(Parameter('file', self.file).to_xml())
        if self.base:
            root.append(Parameter('bbox', self.bbox).to_xml())
        if self.filter_factor is not None:
            root.append(Parameter('filter_factor', self.filter_factor).to_xml())
        return root
