var osmSource = new ol.source.OSM();
var map = new ol.Map({
  layers: [
    new ol.layer.Tile({
      source: osmSource
    })
  ],
  target: 'map',
  controls: ol.control.defaults({
    attributionOptions: {
      collapsible: false
    }
  }),
  view: new ol.View({
    center: ol.proj.fromLonLat([139.63, 35.51]),
    zoom: 10
  })
});
