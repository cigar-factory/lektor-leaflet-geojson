import json

from jinja2 import Markup, Template
from lektor.pluginsystem import Plugin

CSS_JS = Template(
    """
<link rel="stylesheet" href="https://unpkg.com/leaflet@{{ version }}/dist/leaflet.css" crossorigin=""/>
<script src="https://unpkg.com/leaflet@{{ version }}/dist/leaflet.js" crossorigin=""></script>
"""
)

MAP_HTML = Template(
    """
<div id="map-{{ id }}" style="{{ div_style }}"></div>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    var geoj = {{ geojson | tojson }};

    var map = L.map("map-{{ id }}", {
      layers: [
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
          detectRetina: true,
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        }),
      ],
    });

    var layer = L.geoJSON(geoj);
    layer.addTo(map);
    map.fitBounds(layer.getBounds(), {
      maxZoom: 14,
    });
  });
</script>
"""
)


def _map(geojson, div_style):
    id_ = hash(json.dumps(geojson))
    if type(geojson) == str:
        try:
            gj_dict = json.loads(geojson)
        except json.decoder.JSONDecodeError:
            return geojson
    elif type(geojson) == dict:
        gj_dict = geojson
    else:
        return geojson

    if (
        "geometries" not in gj_dict
        and "geometry" not in gj_dict
        and "features" not in gj_dict
        and "bbox" not in gj_dict
    ):
        return geojson

    return Markup(MAP_HTML.render(geojson=gj_dict, id=id_, div_style=div_style))


def _import_leaflet(version=None):
    if not version:
        return Markup(CSS_JS.render(version="latest"))
    return Markup(CSS_JS.render(version=version))


class LeafletGeoJsonPlugin(Plugin):
    name = "lektor-leaflet-geojson"

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters["map"] = _map
        self.env.jinja_env.globals["import_leaflet"] = _import_leaflet
