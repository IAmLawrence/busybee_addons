odoo.define('busybee_csutom.WebClient', function (require) {

"use strict";

    var AbstractWebClient = require('web.AbstractWebClient');

    AbstractWebClient = AbstractWebClient.include({

        start: function (parent) {

            this.set('title_part', {"zopenerp": "Busybee"});

            this._super(parent);

        },

    });

});