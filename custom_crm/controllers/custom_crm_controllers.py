from odoo import http
from odoo.http import Response
import json

# class VisitController(http.Controller):

#     @http.route('/api/visits', auth='public', method=['GET'], csrf=False)
#     def get_visits(self, **kw):
#         try:
#             visits = http.request.env['custom_crm.visits'].sudo().search_read([],['id','name','customer','done'])
#             res = json.dumps(visits, ensure_ascii=False).enconde('utf-8')
#             return Response(res, content_type='application/json;charset=utf-8', status=200)
#         except Exception as e:
#             return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)


class VisitController(http.Controller):

    @http.route('/api/', auth='public', website=True, sitemap=True)
    def index(self, **kw):
        return 'At least this went well'

    @http.route('/api/visits', auth='public', method=['GET'], csrf=False)
    def get_visits(self, **kw):
        try:
            visits = http.request.env['custom_crm.visit'].sudo().search_read([], ['id', 'name', 'customer', 'done'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)