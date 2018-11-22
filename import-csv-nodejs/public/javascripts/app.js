
$(function(){

    $("#tableaudit").hide();
    $("#a1").hide();
    $("#invsel").hide();
    $("#audit").hide();
    $("#reset1").hide();
    $("#drop").hide();
    $("#a6").hide();
    $("#a3").hide();
    $("#audittext").hide();
    $("#fromdate").hide()
    $("#todate").hide()
    $("#search").hide()
    $("#a10").hide()
    
    var id="Bangalore";
    
    $("#search").on('click', function(){

        $.get( "/fetchdata", function( data ) {
            

            var products = data['data'];
            var t = $("#audittext").val("");
            console.log(t);
            var dateFrom = $('#fromdate').val();

            var dateTo = $('#todate').val();
            $('#fromdate').val("");
            
            $('#todate').val("");
            // var dateCheck = "02/07/2013";

            var d1 = dateFrom.split("-");
            var d2 = dateTo.split("-");
            // var c = dateCheck.split("-");

            var from = new Date(d1[2], parseInt(d1[1])-1, d1[0]);  // -1 because months are from 0 to 11
            var to   = new Date(d2[2], parseInt(d2[1])-1, d2[0]);
            

            $("#trdata").html('');
            

            var string = '';
            var p = products;
            for(var i=1;i<p.length;i++){
                var dateCheck = p[i]['date_recieved'];
                    var c = dateCheck.split("-");
                    var check = new Date(c[2], parseInt(c[1])-1, c[0]);
                    console.log(check)
                
                if(p[i]["itemid"]!=""&&p[i]["itemid"]!=""&&p[i]["item_category"]!=""&&p[i]["company"]!=""&&p[i]["no_items_recieved"]!=""&&p[i]["date_recieved"]!=""&&p[i]["no_of_days"]!=""){
                if(p[i]["inventory_location"]==id&&p[i]["currently_in_inventory"]=="1"){
                    if(check > from && check < to){
                var neww = '<tr><a href="www.google.com"><td>'+p[i]["inventory_id"]+'</td><td>'+p[i]["itemid"]+'</td><td>'+p[i]["item_category"]+'</td><td>'+p[i]["company"]+'</td><td>'+p[i]["no_items_recieved"]+'</td><td>'+p[i]["date_recieved"]+'</td><td>'+p[i]["no_of_days"]+'</td></a></tr>';
                neww.link("www.google.com");
                string += neww
                console.log(p[i]);
                }
            }
            }
            }
            $("#trdata").html(string);

        });
    });

    $("#invsel").change(function(){

        $.get( "/fetchdata", function( data ) {

            var products = data['data'];
            id = $("#invsel").val();
            $('#fromdate').val("");
            
            $('#todate').val("");
            
            $("#drop").val("None");
            var a=0;
            var b=0;
            
            console.log(a+","+b);
            $("#trdata").html('');

            $("#message").hide();

            var string = '';
            var p = products;
            for(var i=1;i<p.length;i++){
                if(p[i]["itemid"]!=""&&p[i]["itemid"]!=""&&p[i]["item_category"]!=""&&p[i]["company"]!=""&&p[i]["no_items_recieved"]!=""&&p[i]["date_recieved"]!=""&&p[i]["no_of_days"]!=""){
                if(p[i]["inventory_location"]==id&&p[i]["currently_in_inventory"]=="1"){
                    
                    var neww = '<tr><a href="www.google.com"><td>'+p[i]["inventory_id"]+'</td><td>'+p[i]["itemid"]+'</td><td>'+p[i]["item_category"]+'</td><td>'+p[i]["company"]+'</td><td>'+p[i]["no_items_recieved"]+'</td><td>'+p[i]["date_recieved"]+'</td><td>'+p[i]["no_of_days"]+'</td></a></tr>';
                    neww.link("www.google.com");
                    string += neww
                    console.log(p[i]);
                }
            }
            }

            $("#trdata").html(string);

        });
    });
    
    /** Click on Fetch data and display in HTML table **/
    $("#drop").change(function(){

        $.get( "/fetchdata", function( data ) {

            var products = data['data'];
            var t = $("#drop").val();
            console.log(t);
            var a=0;
            var b=0;
            if(t=="None"){
                a = 0;
                b= 600;
            }
            else if(t=="Less than 90 days"){
                a=0;
                b=90;
            }
            else if(t=="Between 90 and 110 days"){
                a=90;
                b=110;
            }
            else if(t=="More than 110 days"){
                a=110;
                b=600;
            }
            console.log(a+","+b);
            $("#trdata").html('');

            $("#message").hide();

            var string = '';
            var p = products;
            for(var i=1;i<p.length;i++){
                if(p[i]["itemid"]!=""&&p[i]["itemid"]!=""&&p[i]["item_category"]!=""&&p[i]["company"]!=""&&p[i]["no_items_recieved"]!=""&&p[i]["date_recieved"]!=""&&p[i]["no_of_days"]!=""){
                if(p[i]["inventory_location"]==id&&parseInt(p[i]["no_of_days"])>a&&parseInt(p[i]["no_of_days"])<b&&p[i]["currently_in_inventory"]=="1"){
                    console.log(a+","+b);
                    var neww = '<tr><a href="www.google.com"><td>'+p[i]["inventory_id"]+'</td><td>'+p[i]["itemid"]+'</td><td>'+p[i]["item_category"]+'</td><td>'+p[i]["company"]+'</td><td>'+p[i]["no_items_recieved"]+'</td><td>'+p[i]["date_recieved"]+'</td><td>'+p[i]["no_of_days"]+'</td></a></tr>';
                    neww.link("www.google.com");
                    string += neww
                    console.log(p[i]);
                }
            }
            }

            $("#trdata").html(string);

        });
    });
    
    $("#reset1").on('click', function(){

        $.get( "/fetchdata", function( data ) {

            var products = data['data'];
            var t = $("#audittext").val("");
            $('#fromdate').val("");
            
            $('#todate').val("");
            console.log(t);

            $("#trdata").html('');
            $("#drop").val("None");
            $("#message").hide();
            $("#tablenormal").show();
            $("#tableaudit").hide();

            var string = '';
            var p = products;
            for(var i=1;i<p.length;i++){
                if(p[i]["itemid"]!=""&&p[i]["itemid"]!=""&&p[i]["item_category"]!=""&&p[i]["company"]!=""&&p[i]["no_items_recieved"]!=""&&p[i]["date_recieved"]!=""&&p[i]["no_of_days"]!=""){
                if(p[i]["inventory_location"]==id&&p[i]["currently_in_inventory"]=="1"){
                var neww = '<tr><a href="www.google.com"><td>'+p[i]["inventory_id"]+'</td><td>'+p[i]["itemid"]+'</td><td>'+p[i]["item_category"]+'</td><td>'+p[i]["company"]+'</td><td>'+p[i]["no_items_recieved"]+'</td><td>'+p[i]["date_recieved"]+'</td><td>'+p[i]["no_of_days"]+'</td></a></tr>';
                neww.link("www.google.com");
                string += neww
                console.log(p[i]);
                }
            }
            }

            $("#trdata").html(string);

        });
    });

    $("#audit").on('click', function(){

        $.get( "/fetchdata", function( data ) {

            var products = data['data'];
            var t = $("#audittext").val();
            console.log(t);
            $('#fromdate').val("");
            
            $('#todate').val("");

            $("#trdataaudit").html('');

            $("#message").hide();
            $("#tablenormal").hide();
            $("#tableaudit").show();

            var string = '';
            var p = products;
            for(var i=1;i<p.length;i++){
                if(p[i]["itemid"]!=""&&p[i]["itemid"]!=""&&p[i]["item_category"]!=""&&p[i]["company"]!=""&&p[i]["no_items_recieved"]!=""&&p[i]["date_recieved"]!=""&&p[i]["no_of_days"]!=""){
                if(p[i]["itemid"]==t){
                var neww = '<tr><a href="www.google.com"><td>'+p[i]["inventory_id"]+'</td><td>'+p[i]["itemid"]+'</td><td>'+p[i]["inventory_location"]+'</td><td>'+p[i]["item_category"]+'</td><td>'+p[i]["company"]+'</td><td>'+p[i]["no_items_recieved"]+'</td><td>'+p[i]["no_items_remaining"]+'</td><td>'+p[i]["date_recieved"]+'</td><td>'+p[i]["no_of_days"]+'</td><td>'+p[i]["date_sent"]+'</td><td>'+p[i]["inventory_sent"]+'</td></a></tr>';
                neww.link("www.google.com");
                string += neww
                console.log(p[i]);
                }
            }
            }

            $("#trdataaudit").html(string);

        });
    });
    $("#fetchdata").on('click', function(){

        $.get( "/import", function( data ) {

        });

        $.get( "/fetchdata", function( data ) {

            

            var products = data['data'];

            $("#trdata").html('');

            $("#message").hide();
            $("#a1").show();
            $("#invsel").show();
            $("#audit").show();
            $("#reset1").show();
            $("#drop").show();
            $("#a6").show();
            $("#a3").show();
            $("#audittext").show();
            $("#fromdate").show()
            $("#todate").show()
            $("#search").show()
            $("#a10").show()


            var string = '';
            var p = products;
            for(var i=1;i<p.length;i++){
                if(p[i]["itemid"]!=""&&p[i]["itemid"]!=""&&p[i]["item_category"]!=""&&p[i]["company"]!=""&&p[i]["no_items_recieved"]!=""&&p[i]["date_recieved"]!=""&&p[i]["no_of_days"]!=""){
                if(p[i]["inventory_location"]==id&&p[i]["currently_in_inventory"]=="1"){
                var neww = '<tr><a href="www.google.com"><td>'+p[i]["inventory_id"]+'</td><td>'+p[i]["itemid"]+'</td><td>'+p[i]["item_category"]+'</td><td>'+p[i]["company"]+'</td><td>'+p[i]["no_items_recieved"]+'</td><td>'+p[i]["date_recieved"]+'</td><td>'+p[i]["no_of_days"]+'</td></a></tr>';
                neww.link("www.google.com");
                string += neww
                console.log(p[i]);
                }
            }
            }

            $("#trdata").html(string);

        });
    });
 
    /** Import data after click on a button */



});
