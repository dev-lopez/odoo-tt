from odoo import api, fields, models
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
                rec.duration = (rec.return_day -rec.launch_date).days
            else:
                continue