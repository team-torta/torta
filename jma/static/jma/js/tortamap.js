import Feature from 'ol/Feature.js';
import Map from 'ol/Map.js';
import View from 'ol/View.js';
import Point from 'ol/geom/Point.js';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer.js';
import {fromLonLat} from 'ol/proj.js';
import VectorSource from 'ol/source/Vector.js';
import {Icon, Style} from 'ol/style.js';

var rome = new Feature({
 geometry: new Point(fromLonLat([139.63, 35.51]))
});

rome.setStyle(new Style({
 image: new Icon(/** @type {module:ol/style/Icon~Options} */ ({
   color: '#8959A8',
   crossOrigin: 'anonymous',
   src: 'data/dot.png'
 }))
}));

var osmSource = new ol.source.OSM();

var vectorSource = new VectorSource({
 features: [rome]
});
// var vectorLayer = new VectorLayer({
//  source: vectorSource
// });

var map = new ol.Map({
  layers: [
    new ol.layer.Tile({
      source: osmSource
    }),
    new VectorLayer({
     source: vectorSource
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
