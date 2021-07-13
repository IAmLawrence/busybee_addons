# -*- coding: utf-8 -*-
# from odoo import http


# class BusybeeCustom(http.Controller):
#     @http.route('/busybee_custom/busybee_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/busybee_custom/busybee_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('busybee_custom.listing', {
#             'root': '/busybee_custom/busybee_custom',
#             'objects': http.request.env['busybee_custom.busybee_custom'].search([]),
#         })

#     @http.route('/busybee_custom/busybee_custom/objects/<model("busybee_custom.busybee_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('busybee_custom.object', {
#             'object': obj
#         })
