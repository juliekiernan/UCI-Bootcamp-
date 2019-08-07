


function buildMetadata(sample) {
  // @TODO: Complete the following function that builds the metadata panel
  var defaultURL = "/bellybutton.sqlite";

  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`
  

    // Use `.html("") to clear any existing metadata
    tbody.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    function getData(route) {
      console.log(route);
      d3.json(`/${route}`).then(function(data) {
        console.log("newdata", data);
        updatePlotly(data);
      });
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots

    // @TODO: Build a Bubble Chart using the sample data

    var trace1 = {
      x: [1, 2, 3, 4],
      y: [10, 11, 12, 13],
      mode: 'markers',
      marker: {
        color: ['hsl(0,100,40)', 'hsl(33,100,40)', 'hsl(66,100,40)', 'hsl(99,100,40)'],
        size: [12, 22, 32, 42],
        opacity: [0.6, 0.7, 0.8, 0.9]
      },
      type: 'scatter'
    };
    
    var trace2 = {
      x: [1, 2, 3, 4],
      y: [11, 12, 13, 14],
      mode: 'markers',
      marker: {
        color: 'rgb(31, 119, 180)',
        size: 18,
        symbol: ['circle', 'square', 'diamond', 'cross']
      },
      type: 'scatter'
    };
    var trace3 = {
      x: [1, 2, 3, 4],
      y: [12, 13, 14, 15],
      mode: 'markers',
      marker: {
        size: 18,
        line: {
          color: ['rgb(120,120,120)', 'rgb(120,120,120)', 'red', 'rgb(120,120,120)'],
          width: [2, 2, 6, 2]
        }
      },
      type: 'scatter'
    };
    
    var data = [trace1, trace2, trace3];
    var layout = {showlegend: false};
    Plotly.newPlot('myDiv', data, layout);

    // @TODO: Build a Pie Chart
    const data = [];
    const left = data.slice(0,10);
    var layout = {
      title: "Pie Chart"
    };
    Plotly.newPlot("plot", data, layout);
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
