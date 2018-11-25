function gridData() {
    var data = new Array();
    var xpos = 1; //starting xpos and ypos at 1 so the stroke will show when we make the grid below
    var ypos = 1;
    var width = 25;
    var height = 25;
    var click = 0;
    

    // iterate for rows    
    for (var row = 0; row < 20; row++) {
       data.push( new Array() );
       
       // iterate for cells/columns inside rows
       for (var column = 0; column < 20; column++) {
         index = (row * 20) + column

         data[row].push({
          x: xpos,
          y: ypos,
          width: width,
          height: height,
          click: click,
          index: index
         })
         // increment the x position. I.e. move it over by 50 (width variable)
         xpos += width;
       }
       // reset the x position after a row is complete
       xpos = 1;
       // increment the y position for the next row. Move it down 50 (height variable)
       ypos += height;   
    }
    return data;
}


function drawGrid(flip_counts) {
    var counts = Object.values(flip_counts);
    var min = Math.min.apply( null, counts );
    var max = Math.max.apply( null, counts );

    var color = d3.scaleOrdinal(d3['schemeCategory20c']);
    // console.log(d3['schemeDark2']);
       // .domain([min,max])
       // .range(["red","blue"]);

    var grid = d3.select("#grid")
       .append("svg")
       .attr("width","510px")
       .attr("height","510px");
       
    var row = grid.selectAll(".row")
       .data(gridData)
       .enter().append("g")
       .attr("class", "row");
       
    var column = row.selectAll(".square")
       .data(function(d) { return d; })
       .enter().append("rect")
       .attr("class","square")
       .attr("x", function(d) { return d.x; })
       .attr("y", function(d) { return d.y; })
       .attr("width", function(d) { return d.width; })
       .attr("height", function(d) { return d.height; })
       .style("fill", function(d) { return color(flip_counts[d.index]);})
       .style("stroke", "#222")
       .on('click', function(d) {
           console.log(flip_counts[d.index])
        })
}


    