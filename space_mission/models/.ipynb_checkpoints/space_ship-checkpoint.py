from odoo import api, fields, models


class SpaceShip(models.Model):
    _name = 'space.ship'
    _description = 'Odoo new space ship'

    name = fields.Char(string='Name')
    active = fields.Boolean(default=True)

    type = fields.Selection(selection=[('tourism', 'Tourism'),
                                      ('transport', 'Transport'),
                                      ('millitary', 'Millitary'),
                                      ('fighter', 'Fighter'),
                                      ('explorer', 'Explorer')],
                            string='Ship Class',)
    model = fields.Char(string='Model', required = True)
    captain = fields.Char(string='Captain', required = True)
    crew_size = fields.Integer(string= "Required Crew",
                                        help="Minimum number of crewmembers needed to operate the Vessel.",)
    length = fields.Float(string='Length', help="Length of the Ship",)
    width = fields.Float(string='Width', help="Width of the Ship",)
    height = fields.Float(string='Height', help="Height of the Ship",)
    fuel_type = fields.Selection(selection=[('solid_fuel','Solid Fuel'),
                                            ('liquid_fuel', 'Liquid Fuel')],
                                 string='Fuel Type',)