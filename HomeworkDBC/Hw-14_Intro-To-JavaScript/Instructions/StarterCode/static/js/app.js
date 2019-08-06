// from data.js
var tableData = data;

// set up table
var tbody = d3.select("tbody");

// function to loop through data and create table
function createTable(data) {
  // empty table so new data can be filled in
  tbody.html("");
  data.forEach((dataRow) => {
    var row = tbody.append("tr");
    Object.values(dataRow).forEach((val) => {
    var cell = row.append("td");
    cell.text(val);
    }
    );
  });
};

// function for date interactivity
function handleClick() {
  d3.event.preventDefault();
  var date = d3.select("#datetime").property("value");
  let filteredData = tableData;
  if (date) {
    filteredData = filteredData.filter(row => row.datetime === date);
  }
  createTable(filteredData);
};

// Attach an event to listen for the form button
d3.selectAll("#filter-btn").on("click", handleClick);

// Build the table when the page loads
createTable(tableData);
