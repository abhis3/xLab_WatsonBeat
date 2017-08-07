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
// 	res.send("TESTTTTT");
// });

// Explicit login endpoint. Will always redirect browser to login widget due to {forceLogin: true}.
// If forceLogin is set to false redirect to login widget will not occur of already authenticated users.
app.get(LOGIN_URL, passport.authenticate(WebAppStrategy.STRATEGY_NAME, {
	successRedirect: "/mixcloud/login",
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


////////
app.get("/testGet", passport.authenticate(WebAppStrategy.STRATEGY_NAME), function(req, res){
	var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;

	userAttributeManager.getAllAttributes(accessToken).then(function (attributes) {
	//userAttributeManager.getAttribute(accessToken, "holder2").then(function (attributes) {
        //console.log(attributes.user.name);
        //testPostHelper(req, res);
        //console.log(req);
        //console.log(attributes)
        //console.log(req.user.name) //WORKS
        // console.log(`all attributes ${attributes.holder}`);
         //console.log(`single attribute[${JSON.stringify(attributes)}]`); //WORKS
        console.log(`all attributes: ${JSON.stringify(attributes)}`); //WORKS
        //res.end();
    });
});


app.get("/testWriteAtt", passport.authenticate(WebAppStrategy.STRATEGY_NAME), function(req, res){
	var accessToken = req.session[WebAppStrategy.AUTH_CONTEXT].accessToken;

	userAttributeManager.setAttribute(accessToken, "holder2", "456").then(function (attributes) {
		console.log(`stored attributes after call: ${JSON.stringify(attributes)}`);
		//res.end();
    });
});



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

    var req = https.request(options, function(res) {

        res.on('data', function(chunk) {
            //var access_token = (chunk.toString('utf8'));
            var access_token = (JSON.parse(chunk.toString('utf8')))["access_token"];
            console.log(`access_token: ${access_token}`);
            //console.log(access_token["access_token"]);
            // var holder = (access_token["access_token"]);
            // console.log(holder);

            
            ////////////
            //TODO: Check if access_token undefined
            ////////////

            //onsole.log("IN DATA STREAM");
        });

        // res.on('end', function(res) {
        //     console.log("IN END STREAM");
        //     //res.render('test2');
        // });

        // req.on('error', function(err) {
        //     res.send('error: ' + err.message);
        // });
    });
    req.end();
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





//TODO
app.get("/mixcloud/upload", (req, res) => {
    res.render('test2');
})








var port = process.env.PORT || 1234;
app.listen(port, function(){
	logger.info("Listening on http://localhost:" + port + "/web-app-sample.html");
});
