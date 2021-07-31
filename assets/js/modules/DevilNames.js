define("DevilNames", ['jquery', 'Constants'], function ($, Constants) {

    var self = this;

    var getRandomName = function (callback) {

        $.get("/api/random", function (data) {
            if (callback != null) {
                callback(data);
            }
        });
    };

    // Public API
    return {
        getRandomName: getRandomName,
    };
});
