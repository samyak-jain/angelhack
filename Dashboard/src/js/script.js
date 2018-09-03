import db from './Fb'
import $ from 'jquery'
mapPromise.then(()=>{
    let map = new google.maps.Map(
        document.getElementById('map'), {zoom: 18, center: {lat: 12.99498846, lng: 77.66104998}, style:[ { "stylers": [ { "hue": "#16a085" } ] }, { "featureType": "administrative.country", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.business", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.government", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.medical", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.place_of_worship", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.school", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.sports_complex", "stylers": [ { "visibility": "off" } ] }, { "featureType": "road", "elementType": "geometry", "stylers": [ { "lightness": 100 }, { "visibility": "simplified" } ] }, { "featureType": "road", "elementType": "labels", "stylers": [ { "visibility": "off" } ] }, { "featureType": "road.highway.controlled_access", "stylers": [ { "visibility": "off" } ] } ]});
    let quadMarkers=[],quadHexMarkers=[],peopleMarkers=[],volunteerMarkers=[];
    function removeMarker(markerArray){
        for(let i=0;i<markerArray.length;i++){
            let marker=markerArray.pop();
            marker.setMap(null);
        }
    }
    function plotQuads(){
        return db.collection("quads").onSnapshot(function(querySnapshot) {
            removeMarker(quadMarkers);
            querySnapshot.forEach(function(doc) {
                // doc.data() is never undefined for query doc snapshots
                console.log("plotQuads");
                let id =doc.id;
                let data = doc.data();
                quadMarkers.push(new google.maps.Marker({position:{lat:+data.lat,lng:+data.lon} , map: map, icon: '../img/drone-bee.png'}));
            });
        });
    }
    function plotHex(){
        return db.collection("position").onSnapshot(function(querySnapshot) {
            removeMarker(quadHexMarkers);
            querySnapshot.forEach(function(doc) {
                // doc.data() is never undefined for query doc snapshots
                console.log("plot Hex");
                let id =doc.id;
                let data = doc.data();
                quadHexMarkers.push(new google.maps.Marker({position:{lat:+data.lat,lng:+data.lon} , map: map,icon: {
                        path: google.maps.SymbolPath.CIRCLE,
                        scale: 15.5,
                        fillColor: "#ff9c0a",
                        fillOpacity: 1.0,
                        strokeWeight: 0.4
                    },}));
            });
        });
    }
    function plotPeople(){
        return db.collection("help").onSnapshot(function(querySnapshot) {
            removeMarker(peopleMarkers);
            querySnapshot.forEach(function(doc) {
                // doc.data() is never undefined for query doc snapshots
                console.log("plotPeople");
                let id =doc.id;
                let data = doc.data();
                peopleMarkers.push(new google.maps.Marker({position:{lat:+data.lat,lng:+data.lon} , map: map,icon: {
                        path: google.maps.SymbolPath.CIRCLE,
                        scale: 15.5,
                        fillColor: "#ff0e00",
                        fillOpacity: 1.0,
                        strokeWeight: 0.4
                    },}));
            });
        });
    }
    function plotVolunteers(){
        return db.collection("volunteers").onSnapshot(function(querySnapshot) {
            removeMarker(volunteerMarkers);
            querySnapshot.forEach(function(doc) {
                // doc.data() is never undefined for query doc snapshots
                console.log("plotVolunteers");
                let id =doc.id;
                let data = doc.data();
                volunteerMarkers.push(new google.maps.Marker({position:{lat:+data.lat,lng:+data.lon} , map: map,icon: {
                        path: google.maps.SymbolPath.CIRCLE,
                        scale: 15.5,
                        fillColor: "#0004ff",
                        fillOpacity: 1.0,
                        strokeWeight: 0.4
                    },}));
            });
        });
    }
    let unSubQuad=plotQuads();
    let unSubHex=plotHex();
    let unSubPeople=plotPeople();
    let unSubVolunteers=plotVolunteers();
    /*
    function filterHandle (){
        $( "#Quad" ).is(':checked')?plotQuads():(()=>{unSubQuad();removeMarker(quadMarkers);})();
        $( "#Hex" ).is(':checked')?plotHex():(()=>{removeMarker(quadHexMarkers);})();
        $( "#People").is(':checked')?plotHex():(()=>{unSubPeople();removeMarker(peopleMarkers);})();
        $( "#Volunteers" ).is(':checked')?plotVolunteers():(()=>{unSubVolunteers();removeMarker(volunteerMarkers);})();
    }
    filterHandle();

    $( "input[type=checkbox]" ).on( "click",filterHandle) ;*/
});
console.log(db);