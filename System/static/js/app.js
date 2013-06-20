$(document).ready(function(){

    $("#logout").click(function(){

        $("div#contenido").append('<div id="mensaje" title="Dialogo"> </div>');
        $("div#mensaje").html("Logout");
        $( "#mensaje" ).dialog({ buttons: { "Ok": function() { $(this).dialog("close"); } } });

        var jsoon = $.JSON.encode(datos);
        $.ajax({
            url: "/logout", 
            type: "POST",
            dataType: "json",
            complete: function (data) {
                var info = $.parseJSON(data.responseText).toString().split(","); 
                if (info[0] == "TRUE") {
                    $("#vacations").attr("checked","checked")
                    $("#vacations").val("1");
                } else {
                    $("#vacations").val("0");
                    $("#autorespuesta").attr("disabled","disabled");
                }

                $("#autorespuesta").val(info[1]);
            }
        });

    });
});
