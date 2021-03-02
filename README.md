# lektor-leaflet-geojson

[![Run tests](https://github.com/cigar-factory/lektor-leaflet-geojson/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/cigar-factory/lektor-leaflet-geojson/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cigar-factory/lektor-leaflet-geojson/branch/main/graph/badge.svg?token=cL2LogCTnu)](https://codecov.io/gh/cigar-factory/lektor-leaflet-geojson)
[![PyPI Version](https://img.shields.io/pypi/v/lektor-leaflet-geojson.svg)](https://pypi.org/project/lektor-leaflet-geojson/)
![License](https://img.shields.io/pypi/l/lektor-leaflet-geojson.svg)
![Python Compatibility](https://img.shields.io/badge/dynamic/json?query=info.requires_python&label=python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Flektor-leaflet-geojson%2Fjson)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

Lektor template filter to convert geojson objects to Leaflet maps

## Installation

```
pip install lektor-leaflet-geojson
```

## Usage

Import the leaflet JS and CSS. You can skip this step if you are managing Leaflet yourself (e.g: with NPM)

```
{{ import_leaflet('1.7.1') }} {# using a specified version #}
```

```
{{ import_leaflet() }} {# default to "latest" #}
```

The `|map()` filter can be used to render a GeoJSON feature on a map. Pass some inline CSS to style the map div.

```
{{
  '{"type": "Feature", "geometry": {"type": "Point", "coordinates": [125.6, 10.1]}}' | map("height: 300px; width: 300px;")
}}
```
