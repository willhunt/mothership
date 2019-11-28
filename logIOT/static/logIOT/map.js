// Test map, no input data required
function initTestMap() {
    // Variables assigned in script in html template
    var map = new google.maps.Map(document.getElementById('map-devices'), {
        zoom: 2,
        center: new google.maps.LatLng(51.48,0),
    });
}


// Map to single device location
function initDeviceMap() {
    // Variables assigned in script in html template
    var location = {lat: lat, lng: lng};
    var map = new google.maps.Map(document.getElementById('map-device'), {
        zoom: 10,
        center: location,
    });
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}

// Map to show multiple device location
function initDevicesMap() {
    var map = new google.maps.Map(document.getElementById('map-devices'), {
        zoom: 2,
        center: {lat: 51.48, lng: 0}
    });

    // Loop through and place markers
    for( i = 0; i < lats.length; i++ ) {
        var position = new google.maps.LatLng(lats[i], lngs[i]);
        marker = new google.maps.Marker({
            position: position,
            map: map,
        });

        var content_string =    '<div class="map-info">'+
                                '<a href="'+
                                links[i]+
                                '">'+
                                names[i]+
                                '</a>'+
                                '</div>';

        var infowindow = new google.maps.InfoWindow({
          content: content_string
        });

        marker.addListener('click', function() {
          infowindow.open(map, marker);
        });
    }
}

