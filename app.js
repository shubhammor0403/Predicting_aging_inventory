
var session = require('express-session');

var flash = require('connect-flash');

var mongoose = require('mongoose');

mongoose.Promise = global.Promise;

mongoose.connect('mongodb://localhost/dbproducts', { useMongoClient: true });

// require("./models/Product");
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(session({ cookie: { maxAge: 60000 }, 

                  secret: 'secret',

                  resave: false, 

                  saveUninitialized: false}));
app.set('view engine', 'ejs');

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/",function(req,res){
    res.render("dell1.ejs");
});
// app.get("/import-csv-nodejs/",function(req,res){
//     res.render("http://localhost:3000");
// })
app.listen(2000,function(){
    console.log("server initiated........");
});