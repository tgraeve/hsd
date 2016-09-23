var map;
  var heatmap;

  function initLayer() {
    heatmap.setMap(null);
    heatmap = new google.maps.visualization.HeatmapLayer({
      data: getPoints(),
      map: map
    });
    heatmap.set('radius', heatmap.get('radius') ? null : 60);
    heatmap.set('opacity', heatmap.get('opacity') ? null : 0.9);

  }

  function initialize() {

    var styleArray = [
      { featureType: 'road',
        elementType: 'geometry',
        stylers: [
          { visibility: 'off' }
        ]
      },
      { featureType: 'road',
        elementType: 'labels',
        stylers: [
          { visibility: 'off' }
        ]
      },
      { featureType: 'transit',
        stylers: [
          { visibility: 'off' }
        ]
      },
      { featureType: 'landscape',
        elementType: 'geometry.fill', 
        stylers: [
          { color: '#343f43' }
        ] 
      },
      { elementType: 'labels.text',
        stylers: [
          { invert_lightness: true }
        ]
      },
      { featureType: 'poi',
        elementType: 'geometry.fill',
        stylers: [
          { color: '#343f43' }
        ]
      }
    ];

    var mapOptions = {
      zoom: 6,
      center: {lat: 50.5, lng: 10.0},
      mapTypeId: google.maps.MapTypeId.TERRAIN,
      styles: styleArray,
      mapTypeControl:false
    };

    map = new google.maps.Map(document.getElementById('map'), mapOptions);

    var center;
    function calculateCenter() {
      center = map.getCenter();
    }

    google.maps.event.addDomListener(map, 'idle', function() {
      calculateCenter();
    });

    google.maps.event.addDomListener(window, 'resize', function() {
      map.setCenter(center);
    });

    heatmap = new google.maps.visualization.HeatmapLayer({
      data: getPoints(),
      map: map
    });
    heatmap.set('radius', heatmap.get('radius') ? null : 60);
    heatmap.set('opacity', heatmap.get('opacity') ? null : 0.9);

  }

    var latLonArray;
    var arrLength;

    function loadFluechtlinge() {
      var oFrame = document.getElementById("fluechtCoords");
      var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
      while (strRawContents.indexOf("\r") >= 0)
          strRawContents = strRawContents.replace("\r", "");
      var arrLines = strRawContents.split("\n");
      //alert("File " + oFrame.src + " has " + arrLines.length + " lines");
      latLonArray = new Array(arrLines.length);
      arrLength = arrLines.length;
      for (var i = 0; i < arrLines.length; i++) {
        var curLine = arrLines[i];
        //alert("Line #" + (i + 1) + " is: '" + curLine + "'");
        var curString = curLine.toString();
        var curArr = curString.split(",");
        //alert(curArr[1]);
        latLonArray[i] = new Array(3);
        latLonArray[i][0] = parseFloat(curArr[0]);
        latLonArray[i][1] = parseFloat(curArr[1]);
        latLonArray[i][2] = parseFloat(curArr[2]);
        //alert((i+1) + ", 1: " + latLonWeightArray[i][0]);
        //alert((i+1) + ", 2: " + latLonWeightArray[i][1]);
        //alert((i+1) + ", 3: " + latLonWeightArray[i][2]);
      }
      initLayer();
    }

    function loadFluechtlingePN() {
      var oFrame = document.getElementById("fluechtCoordsPN");
            var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
      while (strRawContents.indexOf("\r") >= 0)
          strRawContents = strRawContents.replace("\r", "");
      var arrLines = strRawContents.split("\n");
      //alert("File " + oFrame.src + " has " + arrLines.length + " lines");
      latLonArray = new Array(arrLines.length);
      arrLength = arrLines.length;
      for (var i = 0; i < arrLines.length; i++) {
        var curLine = arrLines[i];
        //alert("Line #" + (i + 1) + " is: '" + curLine + "'");
        var curString = curLine.toString();
        var curArr = curString.split(",");
        //alert(curArr[1]);
        latLonArray[i] = new Array(3);
        latLonArray[i][0] = parseFloat(curArr[0]);
        latLonArray[i][1] = parseFloat(curArr[1]);
        latLonArray[i][2] = parseFloat(curArr[2]);
        //alert((i+1) + ", 1: " + latLonWeightArray[i][0]);
        //alert((i+1) + ", 2: " + latLonWeightArray[i][1]);
        //alert((i+1) + ", 3: " + latLonWeightArray[i][2]);
      }
      initLayer();
    }

    function loadFluechtlingeTN() {
      var oFrame = document.getElementById("fluechtCoordsTN");
            var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
      while (strRawContents.indexOf("\r") >= 0)
          strRawContents = strRawContents.replace("\r", "");
      var arrLines = strRawContents.split("\n");
      //alert("File " + oFrame.src + " has " + arrLines.length + " lines");
      latLonArray = new Array(arrLines.length);
      arrLength = arrLines.length;
      for (var i = 0; i < arrLines.length; i++) {
        var curLine = arrLines[i];
        //alert("Line #" + (i + 1) + " is: '" + curLine + "'");
        var curString = curLine.toString();
        var curArr = curString.split(",");
        //alert(curArr[1]);
        latLonArray[i] = new Array(3);
        latLonArray[i][0] = parseFloat(curArr[0]);
        latLonArray[i][1] = parseFloat(curArr[1]);
        latLonArray[i][2] = parseFloat(curArr[2]);
        //alert((i+1) + ", 1: " + latLonWeightArray[i][0]);
        //alert((i+1) + ", 2: " + latLonWeightArray[i][1]);
        //alert((i+1) + ", 3: " + latLonWeightArray[i][2]);
      }
      initLayer();
    }

    function loadAll() {
      var oFrame = document.getElementById("allCoords");
            var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
      while (strRawContents.indexOf("\r") >= 0)
          strRawContents = strRawContents.replace("\r", "");
      var arrLines = strRawContents.split("\n");
      //alert("File " + oFrame.src + " has " + arrLines.length + " lines");
      latLonArray = new Array(arrLines.length);
      arrLength = arrLines.length;
      for (var i = 0; i < arrLines.length; i++) {
        var curLine = arrLines[i];
        //alert("Line #" + (i + 1) + " is: '" + curLine + "'");
        var curString = curLine.toString();
        var curArr = curString.split(",");
        //alert(curArr[1]);
        latLonArray[i] = new Array(3);
        latLonArray[i][0] = parseFloat(curArr[0]);
        latLonArray[i][1] = parseFloat(curArr[1]);
        latLonArray[i][2] = parseFloat(curArr[2]);
        //alert((i+1) + ", 1: " + latLonWeightArray[i][0]);
        //alert((i+1) + ", 2: " + latLonWeightArray[i][1]);
        //alert((i+1) + ", 3: " + latLonWeightArray[i][2]);
      }
      initLayer();
    }

    function loadAllPN() {
      var oFrame = document.getElementById("allCoordsPN");
            var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
      while (strRawContents.indexOf("\r") >= 0)
          strRawContents = strRawContents.replace("\r", "");
      var arrLines = strRawContents.split("\n");
      //alert("File " + oFrame.src + " has " + arrLines.length + " lines");
      latLonArray = new Array(arrLines.length);
      arrLength = arrLines.length;
      for (var i = 0; i < arrLines.length; i++) {
        var curLine = arrLines[i];
        //alert("Line #" + (i + 1) + " is: '" + curLine + "'");
        var curString = curLine.toString();
        var curArr = curString.split(",");
        //alert(curArr[1]);
        latLonArray[i] = new Array(3);
        latLonArray[i][0] = parseFloat(curArr[0]);
        latLonArray[i][1] = parseFloat(curArr[1]);
        latLonArray[i][2] = parseFloat(curArr[2]);
        //alert((i+1) + ", 1: " + latLonWeightArray[i][0]);
        //alert((i+1) + ", 2: " + latLonWeightArray[i][1]);
        //alert((i+1) + ", 3: " + latLonWeightArray[i][2]);
      }
      initLayer();
    }

    function loadHomophobie() {
      var oFrame = document.getElementById("homophCoords");
      var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
      while (strRawContents.indexOf("\r") >= 0)
          strRawContents = strRawContents.replace("\r", "");
      var arrLines = strRawContents.split("\n");
      //alert("File " + oFrame.src + " has " + arrLines.length + " lines");
      latLonArray = new Array(arrLines.length);
      arrLength = arrLines.length;
      for (var i = 0; i < arrLines.length; i++) {
        var curLine = arrLines[i];
        //alert("Line #" + (i + 1) + " is: '" + curLine + "'");
        var curString = curLine.toString();
        var curArr = curString.split(",");
        //alert(curArr[1]);
        latLonArray[i] = new Array(3);
        latLonArray[i][0] = parseFloat(curArr[0]);
        latLonArray[i][1] = parseFloat(curArr[1]);
        latLonArray[i][2] = parseFloat(curArr[2]);
        //alert((i+1) + ", 1: " + latLonWeightArray[i][0]);
        //alert((i+1) + ", 2: " + latLonWeightArray[i][1]);
        //alert((i+1) + ", 3: " + latLonWeightArray[i][2]);
      }
      initLayer();
    }

    function loadHomophobiePN() {
      var oFrame = document.getElementById("homophCoordsPN");
      var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
      while (strRawContents.indexOf("\r") >= 0)
          strRawContents = strRawContents.replace("\r", "");
      var arrLines = strRawContents.split("\n");
      //alert("File " + oFrame.src + " has " + arrLines.length + " lines");
      latLonArray = new Array(arrLines.length);
      arrLength = arrLines.length;
      for (var i = 0; i < arrLines.length; i++) {
        var curLine = arrLines[i];
        //alert("Line #" + (i + 1) + " is: '" + curLine + "'");
        var curString = curLine.toString();
        var curArr = curString.split(",");
        //alert(curArr[1]);
        latLonArray[i] = new Array(3);
        latLonArray[i][0] = parseFloat(curArr[0]);
        latLonArray[i][1] = parseFloat(curArr[1]);
        latLonArray[i][2] = parseFloat(curArr[2]);
        //alert((i+1) + ", 1: " + latLonWeightArray[i][0]);
        //alert((i+1) + ", 2: " + latLonWeightArray[i][1]);
        //alert((i+1) + ", 3: " + latLonWeightArray[i][2]);
      }
      initLayer();
    }

    function loadHomophobieTN() {
      var oFrame = document.getElementById("homophCoordsTN");
      var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML;
      while (strRawContents.indexOf("\r") >= 0)
          strRawContents = strRawContents.replace("\r", "");
      var arrLines = strRawContents.split("\n");
      //alert("File " + oFrame.src + " has " + arrLines.length + " lines");
      latLonArray = new Array(arrLines.length);
      arrLength = arrLines.length;
      for (var i = 0; i < arrLines.length; i++) {
        var curLine = arrLines[i];
        //alert("Line #" + (i + 1) + " is: '" + curLine + "'");
        var curString = curLine.toString();
        var curArr = curString.split(",");
        //alert(curArr[1]);
        latLonArray[i] = new Array(3);
        latLonArray[i][0] = parseFloat(curArr[0]);
        latLonArray[i][1] = parseFloat(curArr[1]);
        latLonArray[i][2] = parseFloat(curArr[2]);
        //alert((i+1) + ", 1: " + latLonWeightArray[i][0]);
        //alert((i+1) + ", 2: " + latLonWeightArray[i][1]);
        //alert((i+1) + ", 3: " + latLonWeightArray[i][2]);
      }
      initLayer();
    }

  function toggleHeatmap() {
    heatmap.setMap(heatmap.getMap() ? null : map);
  }

  function changeGradient() {
    var gradient = [
      // 'rgba(0, 255, 255, 0)',
      'rgba(0, 255, 255, 1)',
      'rgba(0, 191, 255, 1)',
      'rgba(0, 127, 255, 1)',
      // 'rgba(0, 63, 255, 1)',
      'rgba(0, 0, 255, 1)',
      'rgba(0, 0, 223, 1)',
      // 'rgba(0, 0, 191, 1)',
      'rgba(0, 0, 159, 1)',
      'rgba(0, 0, 127, 1)',
      'rgba(63, 0, 91, 1)',
      'rgba(127, 0, 63, 1)',
      // 'rgba(191, 0, 31, 1)',
      'rgba(255, 0, 0, 1)'
    ]
    heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
  }

  // Heatmap data
  function getPoints() {
    var googleArray = new Array(arrLength);
      for (var i = 0; i < arrLength; i++){
          googleArray[i] = {location: new google.maps.LatLng(latLonArray[i][0], latLonArray[i][1]), weight: latLonArray[i][2]};
      }
      return googleArray
      //Daten zum Testen des Heatmap-Layers
     //return [new google.maps.LatLng(52.21231, 11.254687)]    
  }

    google.maps.event.addDomListener(window, 'load', initialize);
