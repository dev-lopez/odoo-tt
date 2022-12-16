from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'


    mission_id = fields.Many2one('mission.info', string='Related Mission')
    captain_id = fields.Char(related='mission_id.captain_id', string="Spaceship Captain")