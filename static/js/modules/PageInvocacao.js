define(
    ["jquery", "DevilNames", "OffCanvas", "popper", "bootstrap"],
    function ( $, DevilNames, OffCanvas ) {
        OffCanvas.init();

        setRandomName = function(data){
            document.getElementById("devil-name").innerHTML = data.name;
        }

        if(document.getElementById("devil-name")) {
            DevilNames.getRandomName(setRandomName);
        }

        $("#button-random-name").click(function () {
            DevilNames.getRandomName(setRandomName);
        });

    }
);