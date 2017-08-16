var mood1=""; var totsecs = 0;
function settime(){
  var text = document.getElementById("songlength").value;
  var res = text.split(":");
  var mins = parseInt(res[0]);
  var secs = parseInt(res[1]);
  totsecs = (mins * 60) + secs;
  var section = totsecs/4;
  var section2 = section + section ;
  var section3 = section2 + section;
  section4 = totsecs - section3;
  Plotly.d3.selectAll("text.xside").remove();

  Plotly.d3.select("g.xaxislayer-above")
    .append("text")
    .attr("class","xside")
    .attr("x", 990)
    .attr("y",320)
    .attr("fill", "#6969D4")
    .attr("font-family", "IBM Plex Sans")
    .style("font-size", "26px")
    .text(text);

  Plotly.d3.select("g.xaxislayer-above")
    .append("text")
    .attr("class","xside")
    .attr("x",235)
    .attr("y",320)
    .attr("fill", "#6969D4")
    .attr("font-family", "IBM Plex Sans")
    .style("font-size", "26px")
    .text(function(){
      var minutes = Math.floor(section/60);
      var seconds = Math.floor((section-minutes));
      return minutes + ":" + seconds;
  });

  Plotly.d3.select("g.xaxislayer-above")
    .append("text")
    .attr("class","xside")
    .attr("x",485)
    .attr("y",320)
    .attr("fill", "#6969D4")
    .attr("font-family", "IBM Plex Sans")
    .style("font-size", "26px")
    .text(function(){
      var minutes = Math.floor(section2/60);
      var seconds = Math.floor((section2-minutes));
      return minutes + ":" + seconds;
  });

  Plotly.d3.select("g.xaxislayer-above")
    .append("text")
    .attr("class","xside")
    .attr("x",745)
    .attr("y",320)
    .attr("fill", "#6969D4")
    .attr("font-family", "IBM Plex Sans")
    .style("font-size", "26px")
    .text(function(){
      var minutes = Math.floor(section3/60);
      var seconds = Math.floor((section3-minutes));
      return minutes + ":" + seconds;
  });


}

function myFunction2(value) {
  mood1 = value;
  console.log(mood1);

}


window.onload = function() {
  Plotly.plot('graph', );

  var myPlot = document.getElementById('graph');
  var data = [{
      x: [1, 2, 3, 4, 5],
      y: [1, 3, 5, 7, 10],
      line: {simplify: false},
      fill: "tonexty",
    }];

  var layout = {
        hovermode:'closest',
        // title:'Customize Your Track',
        titlefont: {
          family: 'HelvNeue Light for IBM',
          size: 47,
          color: 'black'
        },
        yaxis: {
          visible: false,
          showscale: true,
          showline: false,
          fixedrange: true
        },
        xaxis: {
          visible: true,
          showscale: false,
          showline: false,
          fixedrange: true,
        }
     };
  var options = {
       scrollZoom : false,
       displayModeBar: false,
     };
  var selectedInfo = [];

  Plotly.plot(myPlot, data, layout, options);

  Plotly.d3.select("g.yaxislayer-above")
    .append("text")
    .attr("x",-81)
    .attr("y",30)
    .attr("font-family", "IBM Plex Sans")
    .attr("fill", "#5A6872")
    .style("font-size", "14px")
    .text(function(d){return 'High Energy'});


  Plotly.d3.select("g.yaxislayer-above")
    .append("text")
    .attr("x",-81)
    .attr("y",260)
    .attr("font-family", "IBM Plex Sans")
    .attr("fill", "#5A6872")
    .style("font-size", "14px")
    .text(function(d){return 'Low Energy'});

  // Plotly.d3.selectAll("g.xtick")();

  myPlot.on('plotly_hover', function(data){
    selectedInfo = data.points[0];
    console.log("selectedInfo = " + selectedInfo);
    // hoverInfo.innerHTML = infotext.join('');
  })
  .on('plotly_unhover', function(data){
    console.log("unhover");
  });
  var converter = Plotly.d3.scale.quantize()
                         .domain([100, 400])
                        //  .range(["high","medium","low"])
                         .range([10,9,8,7,6,5,4,3,2,1]);

  myPlot.onmousedown = function(data){
    console.log("this " + selectedInfo + " is my point being moved.");

  };
  myPlot.onmouseup = function(e){
    console.log("hi");
    var newy = converter(event.offsetY);
    console.log(newy + " " + event.offsetY);
    data[0].y[selectedInfo.pointNumber]= newy;
    // data.y[selectedInfo.pointnumber]= newy;
    console.log("newy at mouseup = " + data[0].y[selectedInfo.pointnumber]);
    Plotly.animate('graph', {
      data,
      traces: [0],
      layout: {}
    }, {
      transition: {
        duration: 500,
        easing: 'cubic-in-out'
      }
    });
    selectedInfo = [];
    console.log("finished w animation");

  }
  // myPlot.d3.selectAll("g.xtick").remove();

  var watsonmagic = document.getElementById('generate');
  var data2rank = function(num){
    var mydata = data[0].y[num];
    if(mydata<= 4){
      return 'low';
    }else if(mydata > 4 && mydata <= 6){
      return 'medium';
    }else{
      return 'high';
    }
  }
  var setdirection = function(num){
    var cur = data[0].y[num];
    var next = data[0].y[num+1];

    if(cur < next){
      return 'up';
    }else{
      return 'down';
    }
  }

  watsonmagic.onclick = function(){
    totsecs = totsecs *2;
    var secs = Math.floor(totsecs/4);
    var secs4 = totsecs-(3*secs);

    var moodchange = [
      "\r\n",
      "\r\n#composition settings",
      "\r\nnumMovements: 4",
      "\r\n",
      "\r\n#movement settings",
      "\r\nmovementId: 0",
      "\r\nmovementDuration: "+ totsecs,
      "\r\n",
      "\r\n",
      "\r\n#WB Levers",
      "\r\nmood: "+ mood1,
      "\r\nrhythmSpeed: medium",
      "\r\ncomplexity: super_simple",
      "\r\n",
      "\r\n",
      "\r\nsection:  id:0, tse:'4/4', energy:'"+data2rank(0)+"', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: '"+setdirection(0)+"', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:1, tse:'4/4', energy:'"+data2rank(1)+"', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: '"+setdirection(1)+"' mustHaveGroup1: 'rhythm', mustHaveLayer1: 'melody', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:0, tse:'4/4', energy:'"+data2rank(2)+"', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: '"+setdirection(2)+"', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:0, tse:'4/4', energy:'"+data2rank(3)+"', duration: '"+ (secs4 - 3) +" to "+ (secs4 + 3) +" seconds', slope:'gradual or steep', direction: '"+setdirection(3)+"', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\n",
      "\r\n#end movement",
      "\r\n"]
    var blob = new Blob(moodchange, {type: "text/plain;charset=utf-8"});
    saveAs(blob, "moods.ini");

    console.log("made it");
  }




}
