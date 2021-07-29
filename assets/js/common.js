requirejs.config({
    baseUrl: "/invoca-piroto/assets/js/modules",
    paths: {
        "jquery": "//code.jquery.com/jquery-3.5.1.min",
        "popper": "//cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min",
        "bootstrap": "//stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.bundle.min",
        "datatables": "//cdn.datatables.net/1.10.21/js/jquery.dataTables.min",
        "datatables.bootstrap": "//cdn.datatables.net/1.10.21/js/dataTables.bootstrap4.min",
        "datatables.responsive": "//cdn.datatables.net/responsive/2.2.5/js/dataTables.responsive.min",
        "p5": "https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/p5.min.js",
        "p5.sound": "https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/addons/p5.sound.min.js",
        "lazy": "../lazy",
        "main": "Main",

    },
    shim: {
        "bootstrap": ["jquery"],
    },
    map: {
        '*': {
            'datatables.net': 'datatables',
        }
    },
});

