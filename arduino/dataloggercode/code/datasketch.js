//processing sketch

function setup() {

    timearray = [];//this will be in minutes
    voltagearray = [];//actual volts
    xarray = [];
    yarray = [];
    graphwidth = 400;
    graphheight = 400;
    for(var index = 0;index < data.length;index++){
        voltagearray.push(data[index].v);
        timearray.push((data[index].timestamp - data[0].timestamp)/60.0);
    }
    vrange = voltagearray[0];
    trange = timearray[timearray.length - 1];
    for(var index = 0;index < data.length;index++){
        xarray.push(graphwidth*timearray[index]/trange);
        yarray.push(graphheight - graphheight*voltagearray[index]/vrange);
    }
    createCanvas(graphwidth,graphheight);
      background(153);
    document.getElementById("textio").value = JSON.stringify(timearray,null,"  ");

    for(var index = 0;index < data.length - 1;index++){
        line(xarray[index], yarray[index], xarray[index + 1], yarray[index + 1]);
    }

}

function draw() {


    
}
