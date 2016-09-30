    $(document).ready(function(){
      
      $("#dropHomophobie").hide();
      $("#dropBehinderung").hide();
      $("#over_map").hide();

      $.get("/visualization/txt/fluechtlingeFD.txt", function(data) {
                $("#fdFluechtlinge").html(data);
            });

      $(".prefDrop").change(
        function() {
          switch($("#dropLayer").val()) {
            case "fluecht":
              layer = $("#dropLayer").val()+$("#dropNorm").val()+"_"+$("#fluechtDrop").val();
              $("#schlagwoerter").show();
              $(".dropSw").hide();
              $("#dropFluechtlinge").show();
              loadLayerData(layer);
              break;
            case "homo":
              layer = $("#dropLayer").val()+$("#dropNorm").val()+"_"+$("#homoDrop").val();
              $("#schlagwoerter").show();
              $(".dropSw").hide();
              $("#dropHomophobie").show();
              loadLayerData(layer);
              break;
            case "beh":
              layer = $("#dropLayer").val()+$("#dropNorm").val()+"_"+$("#behDrop").val();
              $("#schlagwoerter").show();
              $(".dropSw").hide();
              $("#dropBehinderung").show();
              loadLayerData(layer);
              break;
            default:
              layer = $("#dropLayer").val()+$("#dropNorm").val();
              $("#schlagwoerter").hide();
              loadLayerData(layer);
          }
        });


    });