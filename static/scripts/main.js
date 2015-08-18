$(function() {

    // Handle submit-address operation
    $('#address-form').on('submit', function(event){
        event.preventDefault();
        console.log("address has been submitted...")
        submit_address();
    });

 
    function clean_input_fields(){
	$("#map_canvas").html("");
	$('#results').html("");
    };

    // post the address - using user input - and handle the response
    function submit_address() {
        console.log("on submit_address...")
        clean_input_fields();
        $.ajax({
            url : "api/v1/address/", 
            type : "POST",
            data : { country : $('#country-text').val(), city : $('#city-text').val(), street : $('#street-text').val()}, 
            // handle a successful response
            success : function(json) {
		// clean the fields
                $('#country-text').val(''); 
		$('#city-text').val(''); 
		$('#street-text').val(''); 


                console.log(json); 

		initialize_map(json.latitude,json.longitude,json.count);
                
                console.log("success"); 
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: no coordinates were found"+
                    " <a href='#' class='close'>&times;</a></div>"); 
                console.log(xhr.status + ": " + xhr.responseText);
		$("#map_canvas").html("");
            }
        });
    };

    function initialize_map(lat,lng,count){
	var url = 'http://maps.googleapis.com/maps/api/staticmap';
        var center = lat + ',' + lng;
        var marker = 'markers=color:red|label:.|' + center;
        var image_src = "<URL>?center=<CENTER>&size=1400x1400&maptype=roadmap&<MARKER>&zoom=12&sensor=false";
	image_src = image_src.replace('<URL>',url); 
	image_src = image_src.replace('<CENTER>',center);
	image_src = image_src.replace('<MARKER>',marker);
        console.log(image_src);
        $("#map_canvas").prepend("<img src=" + image_src + ">");

        $('#results').html("<div class='alert-box alert radius' data-alert>Number of visits in: ("+lat+"," +lng+") is: "+count+
                           " <a href='#' class='close'>&times;</a></div>"); 
    };


});
