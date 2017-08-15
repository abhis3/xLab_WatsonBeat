/*
 Copyright 2017 IBM Corp.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */
 //

const express = require("express");
const session = require("express-session");
const log4js = require("log4js");
const passport = require("passport");
const WebAppStrategy = require("./../lib/appid-sdk").WebAppStrategy;
const helmet = require("helmet");
const bodyParser = require("body-parser"); // get information from html forms
const flash = require("connect-flash");
const app = express();
const logger = log4js.getLogger("testApp");
const userAttributeManager = require("bluemix-appid").UserAttributeManager;
const exphbs = require('express-handlebars');
const path = require('path');
var FormData = require('form-data');
var fs = require('fs');
var request = require('request');
var _ = require('underscore');

////
var http = require('http');
var https = require('https');
////
   
var config = require('../config');

// Below URLs will be used for App ID OAuth flows
const LANDING_PAGE_URL = "/home";
const LOGIN_URL = "/login";
const LOGIN_ANON_URL = "/ibm/bluemix/appid/loginanon";
const CALLBACK_URL = "/ibm/bluemix/appid/callback";
const LOGOUT_URL = "/ibm/bluemix/appid/logout";
const ROP_LOGIN_PAGE_URL = "/ibm/bluemix/appid/rop/login";

app.use(helmet());
app.use(flash());
app.set('views', path.join(__dirname, "/../views"));
app.set('view engine', 'handlebars');
//app.engine('.html', require('handlebars'));
app.engine('handlebars', exphbs({defaultLayout: 'main'}));

// Setup express application to use express-session middleware
// Must be configured with proper session storage for production
// environments. See https://github.com/expressjs/session for
// additional documentation
app.use(session({
    secret: "123456",
    resave: true,
    saveUninitialized: true
})); 

// Use static resources from /samples directory
app.use(express.static(__dirname + "/../public"));
app.use(express.static(__dirname + "/../node_modules/carbon-components/css")); 

// Configure express application to use passportjs
app.use(passport.initialize());
app.use(passport.session()); 

userAttributeManager.init({"profilesUrl": 'https://appid-profiles.ng.bluemix.net'});

// Configure passportjs to use WebAppStrategy
passport.use(new WebAppStrategy({
    tenantId: config['tenantId'],
    clientId: config['clientId'],
    secret: config['secret'],
    oauthServerUrl: config['oauthServerUrl'],
    redirectUri: config['appURL'] + CALLBACK_URL
}));

// Configure passportjs with user serialization/deserialization. This is required
// for authenticated session persistence accross HTTP requests. See passportjs docs
// for additional information http://passportjs.org/docs
passport.serializeUser(function(user, cb) {
    cb(null, user);
});

passport.deserializeUser(function(obj, cb) {
    cb(null, obj);
});

app.get("/", (req, res) => {
    res.render('mainPage');
});

app.get("/authed/main", (req, res) => {
    res.render('test2');
})

app.get("/popup", (req, res) => {
    console.log("Dis good stuff boi");
})
 
// app.get("/test", (req, res) => {
//  res.send("TESTTTTT");
// });

// Explicit login endpoint. Will always redirect browser to login widget due to {forceLogin: true}.
// If forceLogin is set to false redirect to login widget will not occur of already authenticated users.
app.get(LOGIN_URL, passport.authenticate(WebAppStrategy.STRATEGY_NAME, {
    successRedirect: "/dashboard",
    // successRedirect: "/test",
    forceLogin: true
}));
 
// Explicit anonymous login endpoint. Will always redirect browser for anonymous login due to forceLogin: true
app.get(LOGIN_ANON_URL, passport.authenticate(WebAppStrategy.STRATEGY_NAME, {
    successRedirect: LANDING_PAGE_URL,
    allowAnonymousLogin: true,
    allowCreateNewAnonymousUser: true
}));

// Callback to finish the authorization process. Will retrieve access and identity tokens/
// from App ID service and redirect to either (in below order)
// 1. the original URL of the request that triggered authentication, as persisted in HTTP session under WebAppStrategy.ORIGINAL_URL key.
// 2. successRedirect as specified in passport.authenticate(name, {successRedirect: "...."}) invocation
// 3. application root ("/")
app.get(CALLBACK_URL, passport.authenticate(WebAppStrategy.STRATEGY_NAME));

// Logout endpoint. Clears authentication information from session
app.get(LOGOUT_URL, function(req, res){
    WebAppStrategy.logout(req);
    res.redirect(LANDING_PAGE_URL);
});

// Protected area. If current user is not authenticated - redirect to the login widget will be returned.
// In case user is authenticated - a page with current user information will be returned.
app.get("/dashboard", passport.authenticate(WebAppStrategy.STRATEGY_NAME), function(req, res){
    var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;
  
    //console.log('user protection BRUHHHHHH');

    userAttributeManager.getAllAttributes(accessToken).then(function (attributes) {
        givePointsAndRenderPage(req, res);
    });
});

app.post("/rop/login/submit", bodyParser.urlencoded({extended: false}), passport.authenticate(WebAppStrategy.STRATEGY_NAME, {
    successRedirect: LANDING_PAGE_URL,
    failureRedirect: ROP_LOGIN_PAGE_URL,
    failureFlash : true // allow flash messages
}));

app.get(ROP_LOGIN_PAGE_URL, function(req, res) {
    // render the page and pass in any flash data if it exists
    res.render("login.ejs", { message: req.flash('error') });
});


/////////
function givePointsAndRenderPage(req, res) {
    //return the protected page with user info
    var email = req.user.email;
    if(req.user.email !== undefined && req.user.email.indexOf('@') != -1)
           email = req.user.email.substr(0,req.user.email.indexOf('@'));
    var renderOptions = {
        name: req.user.name || email || "Guest",
    };
    //console.log(req.user.name);

    //console.log();
    //res.render('protected', { locals: { data : renderOptions } });
    res.render('dashboard', renderOptions);

}

const onGetMixcloudSuccess = function (res, token, filepath) {
    // Do whatever you need to if the token exists.
    //redirect
    var url = "https://api.mixcloud.com/upload/?access_token=";
    url = url.concat(token);


    var formData = {
        mp3: fs.createReadStream(filepath),
        name: path.basename(filepath, path.extname(filepath))
        //my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
    }

    var req = request.post({ 'url': url, 'formData': formData }, function (err, resp, body) {
      if (resp.statusCode == 403) {
        console.log(resp.statusCode);
        res.redirect("/mixcloud/failure");
      } else {
        console.log(resp.statusCode);
        console.log("Did mixCloud finally")
        res.redirect('/dashboard');
      }
    });

    

    /*
    var formData = {
        mp3: filepath,
        name: 'API Upload',
        my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
    };

    request.post({url:url, formData: formData}, function(err, httpResponse, body) {
        if (err) {
            return console.error('upload failed:', err);
        }
        console.log('Upload successful!  Server responded with:', body);
    });
    */





    //res.redirect('test2');

    //var form = new FormData();

    //form.append('file', fs.createReadStream(filepath));

};
const onGetMixcloudFailure = function (error) {
    // Do any error handling if the token is not found.
    res.redirect("/mixcloud/login");
};


////////
app.get("/scUpload", passport.authenticate(WebAppStrategy.STRATEGY_NAME), function(req, res){
    //var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;

    // // //userAttributeManager.getAllAttributes(accessToken).then(function (attributes) { //WORKS
    // userAttributeManager.getAttribute(accessToken, "access_token_mc").then(function (attributes) { //WORKS
 // //        //console.log(attributes.user.name);
 // //        //testPostHelper(req, res);
 // //        //console.log(req);
 // //        //console.log(attributes)
 // //        //console.log(req.user.name) //WORKS
 // //        // console.log(`all attributes ${attributes.holder}`);
 //            var temp = attributes["access_token_mc"];
 //          console.log(`single attribute: ${JSON.stringify(attributes)}`); //WORKS
 //          console.log(`single attribute: ${JSON.stringify(temp)}`); //<--- Use this
 // //        //console.log(`all attributes: ${JSON.stringify(attributes)}`); //WORKS
 //         //res.end();
 // //        //req.end();
 //     });
 // //    //req.end();
    
    //var key = "access_token_mc";
    //getAtt(function(req, res, key) {access_token_mc = attributes});


    // getAtt(req, res, "access_token_mcs", (token) => {
    //     console.log(`got em: ${token}`);
    //     // res.send(token);
    // });
    var filepath = '/Users/asundaresan/Desktop/BeatUpload/Vivaldi-Winter.mp3';
    scUpload(req, res, "access_token_mc", filepath ,onGetMixcloudSuccess, onGetMixcloudFailure);


    //  isValidAtt(req, res, "access_token_mc", (err, data) => {
    //     if err:
    //         //redirect
    //     else:

    //         access_token_mc = getAtt(req, res, "access_token_mc", (token) => {
    //             console.log(`got em: ${token}`);
    //             // res.send(token);
    //         });


    //     console.log(`got em: ${flag}`);
    // });

    //isValidAtt(req, res, "key", function (foundAttribute) { res.redirect("succesPage"); }, function (errorWhileFindingAtt) { res.redirect("failurePage"); });
});


const scUpload = function (req, res, key, filepath, onSuccess, onFailure) {
    var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;

    //userAttributeManager.getAllAttributes(accessToken).then(function (attributes) { //WORKS
    userAttributeManager.getAttribute(accessToken, key).then(function (attributes) { //WORKS
        console.log(`single attribute: ${JSON.stringify(attributes)}`);

        if (onSuccess && typeof onSuccess === 'function') {
            onSuccess(res, attributes[key], filepath);
        }
    }).catch((error) => {
        //redirect
        //console.log("Caught error from getAtt():");
        //console.log(error);
        //onFailure(error);
        res.redirect("/mixcloud/login");
    });
    //req.end();
};


// function isValidAtt(req, res, att, onSuccess, onFailure) {
//     var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;

//     userAttributeManager.getAllAttributes(accessToken).then(function (attributes) { //WORKS
//     //userAttributeManager.getAttribute(accessToken, key).then(function (attributes) { //WORKS
//         console.log(`single attribute: ${JSON.stringify(attributes)}`);
//         var flag = false

//         // Checks to see if attribute is in key set of JSON. Is so, flag = true
//         for(var k in attributes) {
//             if (k == att) {
//                 flag = true;
//             }
//         }

//         // if (!flag) { onFailure({message: "Could not fi"}); }
//         if (!flag) { callback({message: "could not find attribute"}, null); }



//         if (callback && typeof callback === 'function') {

//             callback(null, attributes[key]); 
//         }
//     });
//     //req.end();
// };




app.get("/testWriteAtt", passport.authenticate(WebAppStrategy.STRATEGY_NAME), function(req, res){
    var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;

    userAttributeManager.setAttribute(accessToken, "holder2", "456").then(function (attributes) {
        console.log(`stored attributes after call: ${JSON.stringify(attributes)}`);
        //res.end();
    });
});


function writeAtt(req, res, key, value) {
    var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;

    userAttributeManager.setAttribute(accessToken, key, value).then(function (attributes) {
        console.log(`stored attributes after call: ${JSON.stringify(attributes)}`);
    });
};



app.get("/mixcloud/login", (req, res) => {
    //res.render('mixCloudLogin');
    res.redirect("https://www.mixcloud.com/oauth/authorize?client_id=E4XqsKQQHnsmYhqXTY&redirect_uri=http%3A%2F%2Flocalhost%3A1234%2Fmixcloud%2Fauth");
})


app.get("/mixcloud/auth", function (req, res) {
    //emitter.setMaxListeners(11);
    const code = req.query.code;

    console.log(`query code: ${code}`);
    // var paths = '/oauth/authorize?client_id=E4XqsKQQHnsmYhqXTY&redirect_uri=http%3A%2F%2Flocalhost%3A1234%2Fmixcloud%2Fauth&client_secret='.concat(config['secret']);
    // paths = paths.concat('&code=');
    // paths = paths.concat(code);

    //console.log(paths);
    //console.log(config["mixCloudSecret"]);

    var paths = "https://www.mixcloud.com/oauth/access_token?client_id=E4XqsKQQHnsmYhqXTY&redirect_uri=http%3A%2F%2Flocalhost%3A1234%2Fmixcloud%2Fauth&client_secret=";
    paths = paths.concat(config["mixCloudSecret"]);
    paths = paths.concat("&code=");
    paths = paths.concat(code);

    const finalPath = paths;

    var options = {
        host: 'mixcloud.com',
        path: finalPath,
        method: 'GET'
    };

    //console.log(options);

    var mcRequest = https.request(options, function(mcResponse) {

        mcResponse.on('data', function(chunk) {
            //var access_token = (chunk.toString('utf8'));
            var access_token_mc = (JSON.parse(chunk.toString('utf8')))["access_token"];
            //console.log(`access_token: ${access_token_mc}`); //WORKS

            writeAtt(req, res, "access_token_mc", access_token_mc);



            //console.log(access_token["access_token"]);
            // var holder = (access_token["access_token"]);
            // console.log(holder);

            
            ////////////
            //TODO: Check if access_token undefined
            ////////////

            //onsole.log("IN DATA STREAM");
        });
        //console.log("WTF IS HAPPENING");

        // res.on('end', function(res) {
        //     console.log("IN END STREAM");
        //     //res.render('test2');
        // });

        // req.on('error', function(err) {
        //     res.send('error: ' + err.message);
        // });
    });
    mcRequest.end();
    //console.log("121212121212121212");
    //console.log(`access_token: ${access_token}`);
    //res.render('test2');
    res.redirect("/dashboard");

    //res.redirect("https://www.mixcloud.com/oauth/access_token?client_id=E4XqsKQQHnsmYhqXTY&redirect_uri=http%3A%2F%2Flocalhost%3A1234%2Fauthed%2Fmain&client_secret=6wf3ckQF2LHKfJW8n8hxSFKr4q27wXtE&code=gEMQsfQAd7");



    //https://www.mixcloud.com/oauth/access_token?client_id=E4XqsKQQHnsmYhqXTY&redirect_uri=http%3A%2F%2Flocalhost%3A1234%2Fauthed%2Fmain&client_secret=6wf3ckQF2LHKfJW8n8hxSFKr4q27wXtE&code=gEMQsfQAd7

});





//<INPUT type="button" id="button-id" value="Save" onclick="this.disabled=true;load_page('form-id');return false;" />


function testPostHelper(req, res) {
    //return the protected page with user info
    var email = req.user.email;
    if(req.user.email !== undefined && req.user.email.indexOf('@') != -1)
           email = req.user.email.substr(0,req.user.email.indexOf('@'));
    var renderOptions = {
        name: req.user.name || email || "Guest",
    };
    console.log(req.user.name);
    res.end();

    //console.log();
    //res.render('protected', { locals: { data : renderOptions } });
    //res.render('index', renderOptions);

}




/////////////////////////////////////////////////////////////////////
app.get("/track/", (req, res) => {
    res.render('track');
})

app.get("/track/cognitive/", (req, res) => {
    res.render('cognitive');
})

app.get("/track/cognitive/play", (req, res) => {
    res.render('cognitive-play');
})


app.get("/track/custom/", (req, res) => {
    res.render('custom');
})

app.get("/track/custom/play", (req, res) => {
    res.render('custom-play');
})

app.get("/mixcloud/failure", (req, res) => {
    res.render('mcFailure');
})




//TODO
app.get("/mixcloud/upload", (req, res) => {
    res.render('test2');
})





app.get("/scUploadFinal", passport.authenticate(WebAppStrategy.STRATEGY_NAME), function(req, res){
    getRecentMP3(req, res, "/Users/watsonbeat1/Repo/xLabWatsonBeat/ReaperProjects/", scUpload);
    console.log("GOT HERE");
   //console.log(fullpath);
});



function getRecentMP3(req, res, dir, callback) {
    // var files = fs.readdirSync(dir);

    // // use underscore for max()
    // return _.max(files, function (f) {
    //     var fullpath = path.join(dir, f);

    //     // ctime = creation time is used
    //     // replace with mtime for modification time
    //     if (path.extname(fullpath) === '.mp3') {
    //         console.log(fullpath);
    //     }
    //     // console.log("---------");
    //     // console.log(fullpath);
    //     // console.log(path.extname(fullpath));
    //     // console.log("---------");
    //     // //console.log(fs.statSync(fullpath).ctime);

    //     return fs.statSync(fullpath).ctime;
    // });
    var finalPath = "";
    var finalTime = "";

    fs.readdir(dir,function(err, list){
        list.forEach(function(file){
            var fullpath = path.join(dir, file);
                if (path.extname(fullpath) === '.mp3') {
                    if (finalPath === "") {
                        finalPath = fullpath;
                        finalTime = fs.statSync(fullpath).ctime;
                    }    

                    if ((fs.statSync(fullpath).ctime) > finalTime) {
                        finalPath = fullpath;
                        finalTime = fs.statSync(fullpath).ctime;
                    }


                    // console.log("------------");
                    // console.log(fullpath);
                    // stats = fs.statSync(fullpath);
                    // //console.log(stats.mtime);
                    // console.log(stats.ctime);
                    // console.log("------------");
                }
        })
        return callback(req, res, "access_token_mc", finalPath, onGetMixcloudSuccess, onGetMixcloudFailure);
    })

};




app.get("/track/custom/generate", function(req, res){
    getINIandTrack(req, res, "/Users/watsonbeat1/Repo/xLabWatsonBeat/MIDI", "/Users/watsonbeat1/Repo/xLabWatsonBeat/INI", getTrack, connectToWatsonBeat, callReaper);
    console.log("GOT HERE");
   //console.log(fullpath);
});



function getINIandTrack(req, res, dirTrack, dirINI, trackCallback, watsonCallback, reaperCallback) {

    var finalPathINI = "";
    var finalTime = "";

    fs.readdir(dirINI,function(err, list){
        list.forEach(function(file){
            var fullpath = path.join(dirINI, file);
                if (path.extname(fullpath) === '.ini') {
                    if (finalPathINI === "") {
                        finalPathINI = fullpath;
                        finalTime = fs.statSync(fullpath).ctime;
                    }    

                    if ((fs.statSync(fullpath).ctime) > finalTime) {
                        finalPathINI = fullpath;
                        finalTime = fs.statSync(fullpath).ctime;
                    }


                    // console.log("------------");
                    // console.log(finalPathINI);
                    // // stats = fs.statSync(fullpath);
                    // // //console.log(stats.mtime);
                    // // console.log(stats.ctime);
                    // // console.log("------------");
                }
        })
        return trackCallback(req, res, dirTrack, finalPathINI, watsonCallback, reaperCallback);
    })

};



const getTrack = function(req, res, dirTrack, pathINI, watsonCallback, reaperCallback) {

    var finalPathTrack = "";
    var finalTime = "";
    //Pick a random MIDI .txt file of the 8 available for the demo
    var random = Math.floor(Math.random() * (9));
    var count = 0;

    fs.readdir(dirTrack,function(err, list){
        list.forEach(function(file){
            var fullpath = path.join(dirTrack, file);
                if (path.extname(fullpath) === '.txt') {
                    if (finalPathTrack === "") {
                        finalPathTrack = fullpath;
                        finalTime = fs.statSync(fullpath).ctime;
                    }    

                    if (count === random) {
                        finalPathTrack = fullpath;
                        finalTime = fs.statSync(fullpath).ctime;
                    } 


                    count = count + 1;
                    // console.log("------------");
                    // console.log(finalPathTrack);
                    // // stats = fs.statSync(fullpath);
                    // // //console.log(stats.mtime);
                    // // console.log(stats.ctime);
                    // console.log("------------");
                }
        })
        return watsonCallback(req, res, finalPathTrack, pathINI, reaperCallback);
    })

};


const callReaper = function (res, fname ) {
  console.log("Zip file name:", fname)

  var mp3 = fname.replace ( ".zip", ".mp3")

  var pythonScript = path.join(__dirname, "/../pyscripts/runReaper.py")
  // + mood + " " + __dirname+"/mp3/"
  var args = [ fname, path.join(__dirname, "/../zip"), path.join(__dirname, "/../ReaperProjects") ]
  console.log ("pythonscript:", pythonScript, args)
  var spawn = require('child_process').spawn;
  var process1 = spawn('python',[pythonScript, fname, path.join(__dirname, "/../zip"), path.join(__dirname, "/../ReaperProjects")]);

  process1.stdout.pipe(process.stdout);

  var mp3File = path.join(__dirname, "/../ReaperProjects/WatsonBeat-" + fname.replace ( ".zip", ".mp3"))

  process1.stdout.on('data', function(data) {
    console.log ( "stdout on:", data.toString())
    //var done = data.toString()
    var done1 = data
    //alert ( done1 )
    if ( done1 == 100 ) {
      //energyMapSection.displayAudioElementsAndPlay(mp3File)
      console.log("FINISHED 100");
      res.redirect("/track/custom/play");
      //alert ( done1 )
    }
  })
  process1.on('error', function(data){
    console.log ( "error:", data.toString())
  })
  process1.on('close', function(data){
    console.log("Close", data.toString())
    //alert(mp3File)
    console.log("FINISHED SUCCESS WATSON");
    //res.redirect("/track/custom/play");
    //res.render("test2");
    //moodSection.displayAudioElementsAndPlay(mp3File)
  })

}


const connectToWatsonBeat = function(req, res, pathTrack, pathINI, reaperCallback) {

    // console.log("------------");
    // console.log(pathTrack);
    // console.log(pathINI);
    // console.log("------------");

    //var url = 'http://127.0.0.1:3000/'
    var url = 'http://arlab053.austin.ibm.com:1025/'

    var formData = {
        myFile: fs.createReadStream(pathTrack),
        iniFile: fs.createReadStream(pathINI)
    }

    // var header = {
    //   'User-Agent':'Electron',
    //   'range':'bytes=100-',
    // }


    var fileNum = 0
    var pythonScript = __dirname + "/pyscripts/getMp3FileId.py"
    // + mood + " " + __dirname+"/mp3/"
    var args = [ "WatsonBeat", __dirname + "/../zip/", "zip" ]
    console.log ("pythonscript:", pythonScript, args)
    var spawn = require('child_process').spawn;
    var process1 = spawn('python',[pythonScript, "WatsonBeat", __dirname+"/../zip/", "zip"]);


    process1.stdout.on('data', function(data) {
        console.log("python data:", data.toString())
        fileNum = parseInt(data.toString()) + 1
        //console.log ( "fileNum for new Mp3", fileNum)
        console.log ( "fileNum for new Zip", fileNum)
    })
    process1.on('error', function(data){
        console.log("Error getting mp3 file Id:", data.toString())
    })
    process1.on('close', function(data){
        console.log("Close", data.toString())

        console.log ( "fileNum for new Zip file", fileNum)

        var mp3 = __dirname + "/../mp3/" + "WatsonBeat" + "-" + fileNum.toString() + ".mp3"
        //var ws = fs.createWriteStream(mp3);

        var fname = "WatsonBeat" + "-" + fileNum.toString() + ".zip"
        var zip = __dirname + "/../zip/" + "WatsonBeat" + "-" + fileNum.toString() + ".zip"
        var ws = fs.createWriteStream(zip);

        console.log(formData)
        console.log ( "New Zip file: ", zip)

        var header = {
            'User-Agent':'Electron',
            'range':'bytes=100-',
        }

        var respStream = request.post({url:url, headers:header, formData: formData})
        respStream.on('error', function(err) {
            console.log("Error: cannot connect to server: ", err)
            alert("Error: cannot connect to server")
            // go back to home page
            //document.getElementById("homePage").click()
            res.redirect("/track/");
        })
        respStream.on('response', function(response) {
            respStream.pipe(ws)
            console.log("I am here")
        })
        respStream.on('end', function () {
            console.log("piping done")
            //moodSection.displayAudioElementsAndPlay(mp3,true)
            return reaperCallback(res, fname)
        })
    })






    // var fileNum = 0
    // var pythonScript = __dirname + "/pyscripts/getMp3FileId.py"
    // // + mood + " " + __dirname+"/mp3/"
    // var args = [ mood, __dirname + "/zip/", "zip" ]
    // console.log ("pythonscript:", pythonScript, args)
    // var spawn = require('child_process').spawn;
    // var process1 = spawn('python',[pythonScript, mood, __dirname+"/zip/", "zip"]);


    // process1.stdout.on('data', function(data) {
    //     console.log("python data:", data.toString())
    //     fileNum = parseInt(data.toString()) + 1
    //     //console.log ( "fileNum for new Mp3", fileNum)
    //     console.log ( "fileNum for new Zip", fileNum)
    // })

    // process1.on('error', function(data){
    //     console.log("Error getting mp3 file Id:", data.toString())
    // })
    // process1.on('close', function(data){
    // console.log("Close", data.toString())

    // console.log ( "fileNum for new Zip file", fileNum)

    // var mp3 = __dirname + "/mp3/" + mood + "-" + fileNum.toString() + ".mp3"
    // //var ws = fs.createWriteStream(mp3);

    // var fname = mood + "-" + fileNum.toString() + ".zip"
    // var zip = __dirname + "/zip/" + mood + "-" + fileNum.toString() + ".zip"
    // var ws = fs.createWriteStream(zip);

    // console.log(formData)
    // console.log ( "New Zip file: ", zip)









    // var respStream = request.post({url:url, headers:header, formData: formData})


    // respStream.on('error', function(err) {
    //     console.log("Error: cannot connect to server: ", err)
    //     alert("Error: cannot connect to server")
    //     // go back to home page
    //     res.redirect("/track/");
    // })

    // respStream.on('response', function(response) {
    //     respStream.pipe(ws)
    //     console.log("I am here")
    // })
    
    // respStream.on('end', function () {
    //     console.log("piping done....");
    //     console.log(".mp3 is saved????");
    //     //moodSection.displayAudioElementsAndPlay(mp3,true)
    //     callReaper()
    //     //res.redirect("/track/custom/play");
    // })



    console.log("------------");
    console.log(pathTrack);
    console.log(pathINI);
    console.log("------------");
    //res.render("test2");
}


    // var req = request.post({ 'url': url, 'formData': formData }, function (err, resp, body) {
    //   if (resp.statusCode == 403) {
    //     console.log(resp.statusCode);
    //     res.redirect("/mixcloud/failure");
    //   } else {
    //     console.log(resp.statusCode);
    //     res.render('test2');
    //   }
    // });










// const scUpload = function (req, res, key, filepath, onSuccess, onFailure) {
//     var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;

//     //userAttributeManager.getAllAttributes(accessToken).then(function (attributes) { //WORKS
//     userAttributeManager.getAttribute(accessToken, key).then(function (attributes) { //WORKS
//         console.log(`single attribute: ${JSON.stringify(attributes)}`);

//         if (onSuccess && typeof onSuccess === 'function') {
//             onSuccess(res, attributes[key], filepath);
//         }
//     }).catch((error) => {
//         //redirect
//         //console.log("Caught error from getAtt():");
//         //console.log(error);
//         //onFailure(error);
//         res.redirect("/mixcloud/login");
//     });
//     //req.end();
// };


// const onGetMixcloudSuccess = function (res, token, filepath) {
//     // Do whatever you need to if the token exists.
//     //redirect
//     var url = "https://api.mixcloud.com/upload/?access_token=";
//     url = url.concat(token);


//     var formData = {
//         mp3: fs.createReadStream(filepath),
//         name: path.basename(filepath, path.extname(filepath))
//         //my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
//     }

//     var req = request.post({ 'url': url, 'formData': formData }, function (err, resp, body) {
//       if (resp.statusCode == 403) {
//         console.log(resp.statusCode);
//         res.redirect("/mixcloud/failure");
//       } else {
//         console.log(resp.statusCode);
//         res.render('test2');
//       }
//     });

// };
// const onGetMixcloudFailure = function (error) {
//     // Do any error handling if the token is not found.
//     res.redirect("/mixcloud/login");
// };








var port = process.env.PORT || 1234;
app.listen(port, function(){
    logger.info("Listening on http://localhost:" + port + "/web-app-sample.html");
});
