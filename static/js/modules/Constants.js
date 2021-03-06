define("Constants",
    [],
    function () {

    var BASEURL = "/";

    var AppConstants = {
        BASEURL: BASEURL,

        HANGED: [
            BASEURL + 'static/images/forca/enforcado0.jpg',
            BASEURL + 'static/images/forca/enforcado1.jpg',
            BASEURL + 'static/images/forca/enforcado2.jpg',
            BASEURL + 'static/images/forca/enforcado3.jpg',
            BASEURL + 'static/images/forca/enforcado4.jpg',
            BASEURL + 'static/images/forca/enforcado5.jpg',
            BASEURL + 'static/images/forca/enforcado6.jpg',
            BASEURL + 'static/images/forca/enforcado7.jpg',
        ],

        EVENTS: {
            GAME_CREATED_EVENT: 'game-created-event',
            GAME_STARTED_EVENT: 'game-started-event',
            GAME_RUNNING_EVENT: 'game-running-event',
            GAME_LOST_EVENT: 'game-lost-event',
            GAME_WON_EVENT: 'game-won-event',
        }
    };

    // Public API
    return AppConstants;
});
