require.config({
    shim: {
        'underscore': {
            exports: '_'
        },
        'backbone': {
            deps: [
                'underscore',
                'jquery'
            ],
            exports: 'Backbone'
        },
        'jquery': {
            exports: '$'
        },
        'bootstrap': {
            deps: [
                'jquery'
            ]
        }
    },
    paths: {
        jquery: 'libs/jquery-2.1.4.min',
        underscore: 'libs/underscore-min',
        backbone: 'libs/backbone-min',
        bootstrap: 'libs/bootstrap.min'
    }
});