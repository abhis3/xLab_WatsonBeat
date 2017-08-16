var mood1=""; var totsecs = 0;
var setCogSongLength = function(secs){
  totsecs = secs * 2;
  console.log(totsecs);
}

var setMood = function(mood){
  mood1 = mood;
  console.log(mood1);
}

  var cogthingshappen1 =  function(){
    console.log('cogthingshappen1')
    console.log(mood1);
    console.log(totsecs);
    var secs = Math.floor(totsecs/4);
    var secs4 = totsecs-(3*secs);
    var moodchange = [
      "\r\n",
      "#composition settings",
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
      "\r\nsection:  id:0, tse:'4/4', energy:'low', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: 'up', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:1, tse:'4/4', energy:'high', duration: '"+ (secs*2 - 3) +" to "+ (secs*2 + 3) +" seconds', slope:'gradual or steep', direction: 'down' mustHaveGroup1: 'rhythm', mustHaveLayer1: 'melody', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:2, tse:'4/4', energy:'low', duration: '"+ (secs4 - 3) +" to "+ (secs4 + 3) +" seconds', slope:'gradual or steep', direction: 'up', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\n",
      "\r\n#end movement",
      "\r\n"];
    var blob = new Blob(moodchange, {type: "text/plain;charset=utf-8"});
    saveAs(blob, "moods.ini");

    console.log("made it");
  }

  var cogthingshappen2 =  function(){
    console.log('cogthingshappen2');
    console.log(mood1);
    console.log(totsecs);
    var secs = Math.floor(totsecs/4);
    var secs4 = totsecs-(3*secs);
    var mymood = [
      "\r\n",
      "#composition settings",
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
      "\r\nsection:  id:0, tse:'4/4', energy:'medium', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: 'down', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:1, tse:'4/4', energy:'low', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: 'up' mustHaveGroup1: 'rhythm', mustHaveLayer1: 'melody', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:0, tse:'4/4', energy:'medium', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: 'down', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:0, tse:'4/4', energy:'low', duration: '"+ (secs4 - 3) +" to "+ (secs4 + 3) +" seconds', slope:'gradual or steep', direction: 'up', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\n",
      "\r\n#end movement",
      "\r\n"];
      var blob = new Blob(mymood, {type: "text/plain;charset=utf-8"});
      saveAs(blob, "moods.ini");

      console.log("made it");
  }
  var cogthingshappen3 =  function(){
    console.log('cogthingshappen3')
    console.log(mood1);
    console.log(totsecs);
    var secs = Math.floor(totsecs/4);
    var secs4 = totsecs-(3*secs);

    var mymood = [
      "\r\n",
      "#composition settings",
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
      "\r\nsection:  id:0, tse:'4/4', energy:'high', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: 'down', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:1, tse:'4/4', energy:'low', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: 'up' mustHaveGroup1: 'rhythm', mustHaveLayer1: 'melody', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:0, tse:'4/4', energy:'high', duration: '"+ (secs - 3) +" to "+ (secs + 3) +" seconds', slope:'gradual or steep', direction: 'down', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\nsection:  id:0, tse:'4/4', energy:'low', duration: '"+ (secs4 - 3) +" to "+ (secs4 + 3) +" seconds', slope:'gradual or steep', direction: 'up', mustHaveLayer2: 'bass3', mustHaveLayer3: 'drumsKit'",
      "\r\n",
      "\r\n#end movement",
      "\r\n"];


      var blob = new Blob(mymood, {type: "text/plain;charset=utf-8"});
      saveAs(blob, "moods.ini");

      console.log("made it");
  }
