# from odoo import http


# class PlaceholderModule(http.Controller):
#     @http.route('/placeholder_module/placeholder_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/placeholder_module/placeholder_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('placeholder_module.listing', {
#             'root': '/placeholder_module/placeholder_module',
#             'objects': http.request.env['placeholder_module.placeholder_module'].search([]),
#         })

#     @http.route('/placeholder_module/placeholder_module/objects/<model("placeholder_module.placeholder_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('placeholder_module.object', {
#             'object': obj
#         })

