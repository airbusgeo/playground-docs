# OneAtlas Data

OneAtlas Playground access OneAtlas Data. This is a streaming service that allows access to the imagery through an API. The large satellite images are cut into tiles of 256 px by 256 px according to the XYZ format (a simpler version of the [WMTS](https://en.wikipedia.org/wiki/Web_Map_Tile_Service) format). Each tile is provided in JPEG or PNG format and only contains the RGB channels (i.e. the Infrared channel has been removed). 

A specific processing has been applied to the images correct for atmospheric transparency. Please note that this prevents scientific usage of the images but still enable machine learning usage. The native projection is GEOGRAPHIC (EPSG:4326) but for ease of display on mobile device and browsers, the images are also available in WebMercator (EPSG:3857) and tiled according to the format used by [GoogleMaps and many other](http://www.maptiler.org/google-maps-coordinates-tile-bounds-projection/) web mapping services.

For Pleiades images, resolution levels are provided from L1 to L17 in GEOG and toL18 in WebMercator.
For SPOT images, resolution levels are provided from L1 to L18 in GEOG and to L19 in WebMercator.

For more information on OneAtlas Data access API, please refer to [the GEO API Website](http://www.geoapi-airbusds.com/)
