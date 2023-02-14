from odoo import _, api, fields, models
import datetime

class CustomCrm(models.Model):
    _name = 'custom_crm.visit'
    _description = 'Gestion de visitas'

    name = fields.Char('Descripcion')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime('Fecha')
    type = fields.Selection(selection=[('p','Presencial'),('w','WhatsApp'),('t','Telefono')], string='Tipo de visita',required=True)
    done = fields.Boolean(string='Realizado', readonly=True)
    image = fields.Binary('Imagen')


    def toggle_state(self):
        self.done = not self.done


    def f_create(self):
        visit = {
            'name': 'Test',
            'customer': 1,
            'date': str(datetime.date(2023,6,16)),
            'type':'w',
            'done': False
        }
        self.env['custom_crm.visit'].create(visit)

    def f_search_update(self):
        visit = self.env['custom_crm.visit'].search([('name','=','Test')])
        visit.write({
            'name': 'ORM Test'
        })

    
    def f_delete(self):
        visit = self.env['custom_crm.visit'].browse([1])
        visit.unlink()



class VisitReport(models.AbstractModel):
    # _name = 'report.custom_crm.report_visit_document'


    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     report_obj = self.env['ir.actions.report']
    #     report = report_obj._get_report_from_name('custom_crm.report_visit_document')
    #     return {
    #         'doc_ids': docids,
    #         'doc_model': self.env['custom_crm.visit'],
    #         'docs': self.env['custom_crm.visit'].browse(docids)
    #     }


    _name='report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['custom_crm.visit'],
            'docs': self.env['custom_crm.visit'].browse(docids)
        }



class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    zone = fields.Selection(selection=[('n','Norte'),('s','Sur'),('e','Este'),('o','Oeste'),('c','Centro')], string='Zona Comercial')
    
        
    
    
