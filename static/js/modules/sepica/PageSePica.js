define("SePica", ['jquery', 'Constants'], function ($, Constants) {

    var self = this;
    self.names = null;

    var init = function (callback) {
      
    };

    var getRandomName = function () {
        var item = self.names[Math.floor(Math.random() * self.names.length)];
        return item;
    };

    // Public API
    return {
        init: init,
        getRandomName: getRandomName
    };
});
