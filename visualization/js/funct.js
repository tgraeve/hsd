/*burger menu test*/
    $(document).ready(function(){
      /* Hier der jQuery-Code */
      // $( ".cross" ).hide();
      // $( ".menu" ).hide();
      // $(".schlagwoerter").hide();
      $("#dropHomophobie").hide();
      $("#dropBehinderung").hide();
      $("#over_map").hide();

      // $( ".hamburger" ).click(
      //   function() {
      //     $( ".menu" ).slideToggle( "slow", function() {
      //       $( ".hamburger" ).hide();
      //       $( ".cross" ).show();
      //     });
      // });

      // $( ".cross" ).click(
      //   function() {
      //     $( ".menu" ).slideToggle( "slow", function() {
      //       $( ".cross" ).hide();
      //       $( ".hamburger" ).show();
      //     });
      // });

      // $(".menu").click(
      //   function() {
      //     $( ".menu" ).slideToggle( "slow", function() {
      //       $( ".cross" ).hide();
      //       $( ".hamburger" ).show();
      //     });
      // });

      var actLayer = "Flüchtlinge";

      // $("#bAll").click(loadAll);
      // $("#bAll").click(function() {
      //     $("#layername").html("Twitteraktivität");
      //     $("#schlagwoerter").hide();
      //     $(".schlagwoerter").hide();
      //     actLayer = "Twitteraktivität";
      // });
        

      // $("#bFluecht").click(loadFluechtlinge);
      // $("#bFluecht").click(
      //   function() {
      //     $("#layername").html("Flüchtlinge");
      //     $("#over_map").show();
      //     $(".schlagwoerter").hide();
      //     $("#schlagwoerter").show();
      //     $("#swFluechtlinge").show();
      //     $("#flAll").attr("checked", "checked");
      //     actLayer = "Flüchtlinge"
      //   });

      // $("#bHomo").click(loadHomophobie);
      // $("#bHomo").click(
      //   function() {
      //     $("#layername").html("Homophobie");
      //     $("#over_map").show();
      //     $("#schwuchtel").attr("checked", "checked");
      //     $(".schlagwoerter").hide();
      //     $("#schlagwoerter").show();
      //     $("#swHomophobie").show();
      //     actLayer = "Homophobie";
      // });

      // $("#bBeh").click(
      //   function() {
      //     $("#layername").html("Behinderung");
      //     alert("Bisher noch keine Daten hinterlegt!")
      //     $("#over_map").show();
      //     $("#krüppel").attr("checked", "checked");
      //     $(".schlagwoerter").hide();
      //     $("#schlagwoerter").show();
      //     $("#swBehinderung").show();
      //     actLayer = "Behinderung";
      // });

      $.get("/visualization/txt/fluechtlingeFD.txt", function(data) {
                // #echo_file = id from div
                $("#fdFluechtlinge").html(data);
            });

      $("#dropLayer").change( 
        function() {
          switch ($("#dropLayer").val()) {
            case "Twitteraktivität":
              loadAll();
              $("#schlagwoerter").hide();
              break;
            case "Flüchtlinge":
              loadFluechtlinge();
              $("#schlagwoerter").show();
              $(".dropSw").hide();
              $("#dropFluechtlinge").show();
              break;
            case "Homophobie":
              loadHomophobie();
              $("#schlagwoerter").show();
              $(".dropSw").hide();
              $("#dropHomophobie").show();
              break;
            case "Behinderung":
              alert("Bisher leider keine Daten hinterlegt!")
              $("#schlagwoerter").show();
              $(".dropSw").hide();
              $("#dropBehinderung").show();
              break;
          }
        });

      $("#dropNorm").change( 
        function() {
          switch ($("#dropLayer").val()) {
            case "Twitteraktivität":
              switch ($("dropNorm").val()) {
                case "keine (reine Anzahl)":
                  loadAll();
                  break;
                case "über Einwohner":
                  loadAllPN();
                  break;
              }
              break;
            case "Flüchtlinge":
              switch ($("#dropNorm").val()) {
                case "keine (reine Anzahl)":
                  loadFluechtlinge();
                  break;
                case "über Einwohner":
                  loadFluechtlingePN();
                  break;
                case "über Twitteraktivität":
                  loadFluechtlingeTN();
                  break;
                }
              break;
            case "Homophobie":
              switch ($("#dropNorm").val()) {
                case "keine (reine Anzahl)":
                  loadHomophobie();
                  break;
                case "über Einwohner":
                  loadHomophobiePN();
                  break;
                case "über Twitteraktivität":
                  loadHomophobieTN();
                  break;
                }
              break;
            case "Behinderung":
              switch ($("#dropNorm").val()) {
                case "keine (reine Anzahl)":
                  loadBehinderung();
                  break;
                case "über Einwohner":
                  loadBehinderungPN();
                  break;
                case "über Twitteraktivität":
                  loadBehinderungTN();
                  break;
                }
              break;
          }
        });

      // $("#om_tab1").click(
      //   function() {
      //     $("#fdFluechtlinge").hide();
      //     $(".normalisierung").show();
      //     switch (actLayer) {
      //       case "Twitteraktivität":
      //         break;
      //       case "Flüchtlinge":
      //         $("#schlagwoerter").show();
      //         $("#swFluechtlinge").show();
      //         break;
      //       case "Homophobie":
      //         $("#schlagwoerter").show();
      //         $("#swHomophobie").show();
      //         break;
      //       case "Behinderung":
      //         $("#schlagwoerter").show();
      //         $("#swBehinderung").show();
      //     };
          
      //     $("#om_tab2").css({ "border-top":"rgba(30,36,38,0.5)",
      //                         "border-right":"rgba(30,36,38,0.5)",
      //                         "border-bottom":"white 1px solid",
      //                         "color":"#BDBDBD",
      //                         "background-color":"rgba(30,36,38,0.5)",
      //                         "left":"50%"
      //     });
      //     $("#om_tab1").css({ "border-top":"white 1px solid",
      //                         "border-left":"white 1px solid",
      //                         "border-bottom":"rgba(30,36,38,0.9)",
      //                         "color":"white",
      //                         "background-color":"rgba(30,36,38,0.9)",
      //     });
      // });

      // $("#om_tab2").click(function() {
      //   $(".normalisierung").hide();
      //   $(".schlagwoerter").hide();
      //   $("#fdFluechtlinge").show();
      //   $("#om_tab1").css({ "border-top":"rgba(30,36,38,0.5)",
      //                       "border-left":"rgba(30,36,38,0.5)",
      //                       "border-bottom":"white 1px solid",
      //                       "color":"#BDBDBD",
      //                       "background-color":"rgba(30,36,38,0.5)",
      //   });
      //   $("#om_tab2").css({ "border-top":"white 1px solid",
      //                       "border-right":"white 1px solid",
      //                       "border-bottom":"rgba(30,36,38,0.9)",
      //                       "color":"white",
      //                       "background-color":"rgba(30,36,38,0.9)",
      //                       "left":"49.6%"
      //   });
      // });

      // $(".radio").click(
      //   function(){
      //     if (actLayer == "Twitteraktivität") {
      //         switch ($("input[name='norm']:checked").val()) {
      //           case "keine":
      //             loadAll();
      //             break;
      //           case "einwohner":
      //             loadAllPN();
      //         }
      //     }
      //     else if (actLayer == "Flüchtlinge") {
      //       switch ($("input[name='swFluechtlinge']:checked").val()) {
      //         case "flAll":
      //           switch ($("input[name='norm']:checked").val()) {
      //             case "keine":
      //               loadFluechtlinge();
      //               break;
      //             case "einwohner":
      //               loadFluechtlingePN();
      //               break;
      //             case "twitter":
      //               loadFluechtlingeTN();
      //           }
      //       }
      //     }
      //     else if (actLayer == "Homophobie") {
      //       switch ($("input[name='swHomophobie']:checked").val()) {
      //         case "schwuchtel":
      //           switch ($("input[name='norm']:checked").val()) {
      //             case "keine":
      //               loadHomophobie();
      //               break;
      //             case "einwohner":
      //               loadHomophobiePN();
      //               break;
      //             case "twitter":
      //               loadHomophobieTN();
      //           }
      //       }
      //     }
      // });
    });