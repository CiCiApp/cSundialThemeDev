define([
    'require',
    'jquery',
    'backbone'
], function (require, $, Backbone) {
    "use strict";

    var FileItem = Backbone.Model.extend({

    });

    var FileList = Backbone.Collection.extend({

    });

    return Backbone.View.extend({
        el: $('#content'),

        initialize: function () {
            var self = this;
            $.get(this.dirListingJsonUrl(), function (data) {
                var files = data.files;
                files.map(function(f) {
                    $(self.el).append('<tr><td>' + f.name + '</td></tr>');
                })
            });
        },

        dirListingJsonUrl: function () {
            return location.pathname + '?type=json&static_token=' + $('#static-token').val();
        }
    });
});