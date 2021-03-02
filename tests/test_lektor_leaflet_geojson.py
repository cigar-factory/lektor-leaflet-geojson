import json

from lektor_leaflet_geojson import _import_leaflet, _map

FEATURE = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [125.6, 10.1]},
}


def test_import_leaflet_with_version():
    assert "leaflet@1.7.1" in _import_leaflet("1.7.1")


def test_import_leaflet_without_version():
    assert "leaflet@latest" in _import_leaflet()


def test_map_string():
    html = _map(json.dumps(FEATURE, indent=2), "height:200px; width: 200px;")
    assert f"var geoj = {json.dumps(FEATURE, sort_keys=True)};" in html
    assert 'style="height:200px; width: 200px;"' in html


def test_map_dict():
    html = _map(FEATURE, "height:200px; width: 200px;")
    assert f"var geoj = {json.dumps(FEATURE, sort_keys=True)};" in html
    assert 'style="height:200px; width: 200px;"' in html


def test_map_not_geojson():
    assert "foobar" == _map("foobar", "height:200px; width: 200px;")


def test_map_invalid():
    assert 3 == _map(3, "height:200px; width: 200px;")
