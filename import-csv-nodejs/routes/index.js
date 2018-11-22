var express = require('express');

var csv = require("fast-csv");

var router = express.Router();

var fs = require('fs');

var mongoose = require('mongoose');

var Product  = mongoose.model('Products');

var csvfile = __dirname + "/../public/files/maindb.csv";


var stream = fs.createReadStream(csvfile);

router.get('/', function(req, res, next) {

    res.render('index', { title: 'Import CSV file using NodeJS' });

}).get('/import', function(req, res, next) {

    var  products  = []
    
var csvStream = csv()
        .on("data", function(data){
         
         var item = new Product({
            inventory_id: data[0],

            inventory_location: data[1],

            itemid: data[2],

            item_category: data[3],

            company: data[4],

            no_items_recieved: data[6],

            no_items_remaining: data[7],

            date_recieved:data[8], 

            no_of_days : data[13],

            currently_in_inventory : data[14],

            date_sent : data[15],

            inventory_sent : data[16]

         });
         
          item.save(function(error){

            console.log(item);

              if(error){

                   throw error;

              }

          }); 

    }).on("end", function(){
          console.log(" End of file import");
    });
  
    stream.pipe(csvStream);

    res.json({success : "Data imported successfully.", status : 200});
     
  }).get('/fetchdata', function(req, res, next) {
    
    Product.find({}, function(err, docs) {

        if (!err){ 

            res.json({success : "Updated Successfully", status : 200, data: docs});

        } else { 

            throw err;

        }

    });
  
});
module.exports = router;