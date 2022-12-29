ymaps.ready(init);
var myMap;

function init () {
    myMap = new ymaps.Map("map", {
        center: [56.010569, 92.852572], // Красноярск
        zoom: 11
    }, {
        balloonMaxWidth: 200,
        searchControlProvider: 'yandex#search'
    });
    myMap.events.add('click', function (e) {
        if (!myMap.balloon.isOpen()) {
            var coords = e.get('coords');
            var lat = coords[0];
            var lon = coords[1];
            document.getElementById('lat').value = lat;
            document.getElementById('lon').value = lon;
        }
        else {
            myMap.balloon.close();
        }
    });
}