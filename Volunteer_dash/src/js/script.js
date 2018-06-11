import db from './Fb'

mapPromise.then(() => {
    navigator.geolocation.getCurrentPosition(function (position) {
        const {coords}=position;
        const rname=`${coords.latitude}${coords.longitude}`;
        db.collection("volunteers").doc(rname).set({
            lat:coords.latitude,
            lon:coords.longitude
        }).then(function () {
            let map = new google.maps.Map(
                document.getElementById('map'), {zoom: 18, center: {lat: coords.latitude, lng: coords.longitude}, style:[ { "stylers": [ { "hue": "#16a085" } ] }, { "featureType": "administrative.country", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.business", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.government", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.medical", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.place_of_worship", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.school", "stylers": [ { "visibility": "off" } ] }, { "featureType": "poi.sports_complex", "stylers": [ { "visibility": "off" } ] }, { "featureType": "road", "elementType": "geometry", "stylers": [ { "lightness": 100 }, { "visibility": "simplified" } ] }, { "featureType": "road", "elementType": "labels", "stylers": [ { "visibility": "off" } ] }, { "featureType": "road.highway.controlled_access", "stylers": [ { "visibility": "off" } ] } ]});
            let quadMarkers=[],quadHexMarkers=[],peopleMarkers=[],volunteerMarkers=[];
            /**
             * @description A function to remove marker points in the map
             * @param markerArray - Array of markers to be removed
             */
            function removeMarker(markerArray){
                for(let i=0;i<markerArray.length;i++){
                    let marker=markerArray.pop();
                    marker.setMap(null);
                }
            }
            /**
             * @description A function to plot drone marker points in the map
             */
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
            /**
             * @description A function to plot hexagon marker points in the map
             */
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
            /**
             * @description A function to initiate the plots and the unsubscribe refs
             */
            let unSubPeople=plotPeople();
            let unSubVolunteers=plotVolunteers();
        })
    });

});
console.log(db);