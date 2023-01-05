from odoo import api, fields, models, _
from datetime import timedelta


class MissionInfo(models.Model):
    _name = 'mission.info'
    _description = 'Information about the space mission'

    name = fields.Char(string="Mission's Name")
    active = fields.Boolean(default=True)
    destiny = fields.Char(string="Destination Location")
    spaceship_id = fields.Many2one('space.ship', string='Spaceship')
    crew_id = fields.Many2one('res.partner', string="Crew Member")
    captain_id = fields.Char(related='spaceship_id.captain', string="Spaceship Captain")
    launch_date = fields.Datetime(string='Launch Date', default=fields.Date.today)
    duration = fields.Float(string='Mission duration', default='1')
    return_date = fields.Datetime(string='Return Date', compute='_compute_return_date', inverse='_inverse_return_date')

    
    fuel_needed = fields.Integer(string='Fuel needed', default='0')
    engine_count = fields.Integer(string='Engine Count', default='1')
    security_engines = fields.Boolean(default=False, string='Engines')
    security_shields = fields.Boolean(default=False, string='Shields')
    security_power = fields.Boolean(default=False, string='Power')
    security_thrusters = fields.Boolean(default=False, string='Thrusters')
    security_weapons = fields.Boolean(default=False, string='Weapons')
    security_crew = fields.Boolean(default=False, string='Crew')
    security_confirmed = fields.Boolean(default=False, compute='_get_security_checked', store=True, string='Security Checked', readonly=True)
    
    project_ids = fields.One2many(comodel_name='project.project', inverse_name='mission_id')
    captain_ids = fields.One2many(comodel_name='project.project', inverse_name='captain_id')

    @api.depends('launch_date','duration')
    def _compute_return_date(self):
        for rec in self:
            if not (rec.launch_date and rec.duration):
                rec.return_date = rec.launch_date
            else:
                duration = timedelta(days=rec.duration)
                rec.return_date = rec.launch_date + duration

    def _inverse_return_date(self):
        for rec in self:
            if rec.launch_date and rec.return_date:
                rec.duration = (rec.return_date -rec.launch_date).days
            else:
                continue
                
    @api.depends('security_engines','security_shields','security_power','security_thrusters','security_weapons','security_crew')
    def _get_security_checked(self):
        for rec in self:
            if rec.security_engines and rec.security_shields and rec.security_power and rec.security_thrusters and rec.security_weapons and rec.security_crew:
                rec.security_confirmed = True
            else:
                rec.security_confirmed = False
    