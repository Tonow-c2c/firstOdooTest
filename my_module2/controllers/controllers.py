# -*- coding: utf-8 -*-
from openerp import http

# class MyModule2(http.Controller):
#     @http.route('/my_module2/my_module2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module2/my_module2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module2.listing', {
#             'root': '/my_module2/my_module2',
#             'objects': http.request.env['my_module2.my_module2'].search([]),
#         })

#     @http.route('/my_module2/my_module2/objects/<model("my_module2.my_module2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module2.object', {
#             'object': obj
#         })