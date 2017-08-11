var section = 0; var section4= 0; var mood1=""; var mood2 = ""; var mood3 = ""; var mood4 = "";
function settime(){
  var text = document.getElementById("songlength").value;
  var res = text.split(":");
  var mins = parseInt(res[0]);
  var secs = parseInt(res[1]);
  var totsecs = (mins * 60) + secs;
  section = totsecs/4;
  var section2 = section + section ;
  var section3 = section2 + section;
  section4 = totsecs - section3;
  Plotly.d3.selectAll("text.xside").remove();

  Plotly.d3.select("g.xaxislayer-above")
    .append("text")
    .attr("class","xside")
    .attr("x",1420)
    .attr("y",280)
    .style("font-size", "12px")
    .text(text);
  Plotly.d3.select("g.xaxislayer-above")
    .append("text")
    .attr("class","xside")
    .attr("x",400)
    .attr("y",280)
    .style("font-size", "12px")
    .text(function(){
      var minutes = Math.floor(section/60);
      var seconds = Math.floor((section-minutes));
      return minutes + ":" + seconds;
  });

  Plotly.d3.select("g.xaxislayer-above")
    .append("text")
    .attr("class","xside")
    .attr("x",750)
    .attr("y",280)
    .style("font-size", "12px")
    .text(function(){
      var minutes = Math.floor(section2/60);
      var seconds = Math.floor((section2-minutes));
      return minutes + ":" + seconds;
  });

  Plotly.d3.select("g.xaxislayer-above")
    .append("text")
    .attr("class","xside")
    .attr("x",1080)
    .attr("y",280)
    .style("font-size", "12px")
    .text(function(){
      var minutes = Math.floor(section3/60);
      var seconds = Math.floor((section3-minutes));
      return minutes + ":" + seconds;
  });


}

function myFunction(selected) {
  mood1 = selected.options[selected.selectedIndex].value;
  console.log(mood1);
    // document.getElementById("myDropdown").classList.toggle("show");
    // document.getElementById("myDropdown").firstChild.data =

}

function myFunction2(selected) {
  mood2 = selected.options[selected.selectedIndex].value;
  console.log(mood2);
    // document.getElementById("myDropdown2").classList.toggle("show");

}
function myFunction3(selected) {
  mood3 = selected.options[selected.selectedIndex].value;
  console.log(mood3);
    // document.getElementById("myDropdown3").classList.toggle("show");

}
function myFunction4(selected) {
  mood4 = selected.options[selected.selectedIndex].value;
  console.log(mood4);
    // document.getElementById("myDropdown4").classList.toggle("show");

}

window.onload = function() {
  Plotly.plot('graph', );

  var myPlot = document.getElementById('graph');
  var data = [{
      x: [1, 2, 3, 4, 5],
      y: [1, 3, 5, 7, 10],
      // y: ["low", "medium", "high", "low", "medium"],
      line: {simplify: false},
      // fill: "tonexty",
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
    .attr("x",-20)
    .attr("y",30)
    .style("font-size", "12px")
    .text(function(d){return 'High Energy'});

  Plotly.d3.select("g.yaxislayer-above")
    .append("text")
    .attr("x",-25)
    .attr("y",150)
    .style("font-size", "12px")
    .text(function(d){return 'Medium Energy'});

  Plotly.d3.select("g.yaxislayer-above")
    .append("text")
    .attr("x",-20)
    .attr("y",280)
    .style("font-size", "12px")
    .text(function(d){return 'Low Energy'});

  Plotly.d3.selectAll("g.xtick").remove();

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

    var moodchange = [
      "\r\n",
      "#composition settings",
      "\r\nnumMovements: 4",
      "\r\n",
      "\r\n#movement settings",
      "\r\nmovementId: 0",
      "\r\nmovementDuration: "+ section,
      "\r\n",
      "\r\n",
      "\r\n#WB Levers",
      "\r\nmood: "+ mood1,
      "\r\nrhythmSpeed: medium",
      "\r\ncomplexity: super_simple",
      "\r\n",
      "\r\n",
      "\r\nsection:  id:0, tse:'4/4', energy:'"+data2rank(0)+"', durationInMeasures:'4', slope:'gradual or steep', direction: '"+setdirection(0)+"', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:1, tse:'4/4', energy:'"+data2rank(1)+"', durationInMeasures: '8 or 12', slope:'gradual or steep', direction: '"+setdirection(1)+"' mustHaveGroup1: 'rhythm', mustHaveLayer1: 'melody', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\n",
      "\r\n#end movement",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n#movement settings",
      "\r\nmovementId: 1",
      "\r\nmovementDuration: "+ section,
      "\r\n",
      "\r\n",
      "\r\n#WB Levers",
      "\r\nmood: "+ mood2,
      "\r\nrhythmSpeed: medium",
      "\r\ncomplexity: super_simple",
      "\r\n",
      "\r\n",
      "\r\nsection:  id:0, tse:'4/4', energy:'"+data2rank(1)+"', durationInMeasures:'4', slope:'gradual or steep', direction: '"+setdirection(1)+"', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:1, tse:'4/4', energy:'"+data2rank(2)+"', durationInMeasures: '8 or 12', slope:'gradual or steep', direction: '"+setdirection(2)+"' mustHaveGroup1: 'rhythm', mustHaveLayer1: 'melody', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\n",
      "\r\n#end movement",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n#movement settings",
      "\r\nmovementId: 2",
      "\r\nmovementDuration: "+ section,
      "\r\n",
      "\r\n",
      "\r\n#WB Levers",
      "\r\nmood: "+ mood3,
      "\r\nrhythmSpeed: medium",
      "\r\ncomplexity: super_simple",
      "\r\n",
      "\r\n",
      "\r\nsection:  id:0, tse:'4/4', energy:'"+data2rank(2)+"', durationInMeasures:'4', slope:'gradual or steep', direction: '"+setdirection(2)+"', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:1, tse:'4/4', energy:'"+data2rank(3)+"', durationInMeasures: '8 or 12', slope:'gradual or steep', direction: '"+setdirection(3)+"' mustHaveGroup1: 'rhythm', mustHaveLayer1: 'melody', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\n",
      "\r\n#end movement",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n#movement settings",
      "\r\nmovementId: 3",
      "\r\nmovementDuration: "+ section4,
      "\r\n",
      "\r\n",
      "\r\n#WB Levers",
      "\r\nmood: "+ mood4,
      "\r\nrhythmSpeed: medium",
      "\r\ncomplexity: super_simple",
      "\r\n",
      "\r\n",
      "\r\nsection:  id:0, tse:'4/4', energy:'"+data2rank(3)+"', durationInMeasures:'4', slope:'gradual or steep', direction: '"+setdirection(3)+"', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:1, tse:'4/4', energy:'"+data2rank(4)+"', durationInMeasures: '8 or 12', slope:'gradual or steep', direction: '"+setdirection(4)+"' mustHaveGroup1: 'rhythm', mustHaveLayer1: 'melody', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\n",
      "\r\n#end movement",
      "\r\n",
      "\r\n",
      "\r\n"]
    var blob = new Blob(moodchange, {type: "text/plain;charset=utf-8"});
    saveAs(blob, "moods.ini");

    console.log("made it");
  }




}
