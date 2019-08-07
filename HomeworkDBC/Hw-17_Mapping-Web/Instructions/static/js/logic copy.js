console.log('logic.js read in')
------------------

// get geojsondata
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  createFeatures(data.features);
)};
function createFeatures(earthquakeData) {
// create function for market radius based on earthquate magnitude to define markers
  function magSize(mag){
    if(feature.properties.mag < 2){ radius: 1}
      else if(feature.properties.mag >2 <4){radius:3}
      else if(feature.properties.mag >4.1 <6){radius:5}
      else if(feature.properties.mag >6.1 <8){radius:7}
      else(feature.properties.mag >8.1 ){radius:9}
      return magSize
    }

  function magColor(mag){
    if(feature.properties.mag < 2){color: "white"}
      else if(feature.properties.mag >2 <4){color: "yellow"}
      else if(feature.properties.mag >4.1 <6){color: "orange"}
      else if(feature.properties.mag >6.1 <8){color: "red"}
      else(feature.properties.mag >8.1 ){color: "darkred"}
      return magSize
    }
}
var MagMarker = [];

for (var i = 0; i < features.length; i++) {
  mMagMarker.push(
    L.circle(feature.coordinates){
      color: magColor
      radius: magSize
    });

    .bindPopup("<h3>" + feature.properties.place + "</h3><hr><p>" + new Date(feature.properties.time) + "</p>" + "</br>Magnitude: " + feature.properties.mag )
    .addTo(myMap)  
  
  )};
  
  


// Once we get a response, send the data.features object to the createFeatures function
createFeatures(data.features);


-----------



 // Create our map, giving it the streetmap and earthquakes layers to display on load
 var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5,
  layers: [streetmap, darkmap, overlayMap]
});

// create streetmap and darkmap layers
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

  //create earthquake layer
  var overlayMap = {
    earthquakeData: earthquakeLayer
  };
--------------------------------------



// Store our API endpoint inside queryUrl


function createFeatures(earthquakeData) {
  function onEachFeature(feature, layer)

}


---------------

var icons = {
  white: L.circle({
    color: "white"
    fillColor: "white",
    minOpacity: 0.2,
    radius: 1
    
  }),
  yellow: L.circle({
    color: "white"
    fillColor: "white",
    minOpacity: 0.2,
    radius: 1
  }),
  orange: L.circle({
    color: "white"
    fillColor: "white",
    minOpacity: 0.2,
    radius: 1
  }),
  red: L.circle({
    color: "white"
    fillColor: "white",
    minOpacity: 0.2,
    radius: 1
  }),
  darkred: L.circle({
    color: "white"
    fillColor: "white",
    minOpacity: 0.2,
    radius: 1
  })
};








 
 });



function createFeatures(earthquakeData) {
  for (var i = 0; i < features.length; i++) {
    var feature = features[i];
    L.circle(feature.coordinates)
      .bindPopup("<h3>" + feature.properties.place + "</h3><hr><p>" + new Date(feature.properties.time) + "</p>" + "</br>Magnitude: " + feature.properties.mag )
      .addTo(myMap)  
  }


  }

  // Create a GeoJSON layer containing the features array on the earthquakeData object
  // Run the onEachFeature function once for each piece of data in the array
  var earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: onEachFeature
    
  });

  // Sending our earthquakes layer to the createMap function
  createMap(earthquakes);
}

 {



  // Define a baseMaps object to hold our base layers
  var baseMaps = {
    "Street Map": streetmap,
    "Dark Map": darkmap
  };

  // Create overlay object to hold our overlay layer
  var overlayMaps = {
    Earthquakes: earthquakes
  };

 

  // Create a layer control
  // Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

  var info = L.control({
    position: "bottomright"
  });
  
  // When the layer control is added, insert a div with the class of "legend"
  info.onAdd = function() {
    var div = L.DomUtil.create("div", "legend");
    return div;
  };
  // Add the info legend to the map
  info.addTo(map);
}
