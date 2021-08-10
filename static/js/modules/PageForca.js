define(
    ["jquery", "Forca", "ForcaView", "OffCanvas", "popper", "bootstrap"],
    function ($, Forca, ForcaView, OffCanvas) {
        OffCanvas.init();

        ForcaView.init();

        ForcaView.changeToGameCreatedState(null);

        $(".btn-new-game").click(function () {
            Forca.run();
        });

        $(".btn-letter").click(function () {
            Forca.readPlayerMove($(this).attr("value"));
        });
    }
);

