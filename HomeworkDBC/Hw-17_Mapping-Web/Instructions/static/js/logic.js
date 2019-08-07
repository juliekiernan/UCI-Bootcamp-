console.log('logic.js read in')

// add streetmap and darkmap tile layers
var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
});

var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.dark",
  accessToken: API_KEY
});

// create earthquake map layer 1. get geojson data, 2. create functions to define color/size marker based on magnitude
// get geojsondata 3. create legend
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

d3.json(queryUrl, function(data) {
  function magColorSize(feature) {
    return{
      color:"#000000",
      fillColor: magColor(feature.properties.mag),
      radius: magSize(feature.properties.mag),
      minOpacity: 0.2, 
    };
  }
  function magColor(magnitude) {
    switch (true) {
      case magnitude > 8: return "#ff0000";
      case magnitude > 6: return "#ffa500";
      case magnitude > 4: return "#eecc00";
      case magnitude > 2: return "#ffff00";
      default: return "#ccffcc";
    }
  }
  function magSize(magnitude) {
    if (magnitude === 0) {return 1;}
      return magnitude * 5;
  };
// add GeoJSON layer, add markers
  L.geoJson(data, {
    pointToLayer: function(feature, latlng) {
      return L.circleMarker(latlng);
    },
    style: magColorSize,
    // popup for each marker to display earthquake info
    onEachFeature: function(feature, layer) {
      layer.bindPopup("<h3>" + feature.properties.place + "</h3><hr><p>" + new Date(feature.properties.time) + "</p>" + "</br>Magnitude: " + feature.properties.mag )
      }
  }).addTo(map);

// create legend
  legend.onAdd = function() {
  var div = L.DomUtil.create("div", "info legend");

  var grades = [0, 2, 4, 6, 8];
  var colors = [
     "#ff0000",
     "#ffa500",
    "#eecc00",
     "#ffff00",
    "#ccffcc",
  ];
  // Loop through intervals to create label with color.
      for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
          "<i style='background: " + colors[i] + "'></i> " +
          grades[i] + (grades[i + 1] ? "&ndash;" + grades[i + 1] + "<br>" : "+");
      }
      return div;
    };
  //show one layer at a time
var baseMaps = {
  Light: streetmap,
  Dark: darkmap
};
//  map complilation from above 
// initialize myMap
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5,
  layers: [streetmap, darkmap]
});
});