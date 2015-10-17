/**
 * Created by Tom on 15/10/2015.
 */



var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var parseDate = d3.time.format("%d-%b-%y").parse;

var x = d3.time.scale()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var area = d3.svg.area()
    .x(function(d) { return x(d.time); })
    .y0(height)
    .y1(function(d) { return y(d.y); });

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.json("test_data.json", function(error, data) {
  if (error) throw error;
  //console.log(data);
    convData = d3.entries(data);
   // console.log(d3.entries(data));

    parsedData = [];

    for(prop in convData){
     //    console.log(convData[prop] + 'kkk');
         var nest = convData[prop];
         for (prop2 in nest){
            // console.log(nest[prop2])
            for(prop3 in nest[prop2]){
                              parsedData = (nest[prop2])

             }
         }
    }

    console.log(parsedData);
  parsedData.forEach(function(d){
  //  console.log(console.log(JSON.stringify(d)) + 'ggg');
   //   console.log(d3.keys(d))
   //   console.log(d3.values(d))

   console.log(d.time + ' : '+ d.y);
   // d.date =+ parseDate(d.date);
   // d.close = + d.close;
  });

  // x.domain(d3.extent(data, function(d) { console.log('pop'); return (d.time); }));
  x.domain([0, d3.max(data, function(d) { return d.time; })]);
    y.domain([0, d3.max(data, function(d) { return d.y; })]);

  svg.append("path")
      .datum(data)
      .attr("class", "area")
      .attr("d", area);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Price ($)");
});