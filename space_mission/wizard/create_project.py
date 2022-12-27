from odoo import api, fields, models


class CreateProject(models.TransientModel):
    _name = 'space.mission.create.project'
    _description = 'Create Project Wizard for your Mission'


    def _default_mission(self):
        return self.env['mission.info'].browse(self._context.get('active_id'))
    def _default_name(self):
        return self.env['mission.info'].browse(self._context.get('active_id')).name
    def _default_destiny(self):
        return self.env['mission.info'].browse(self._context.get('active_id')).destiny
    def _default_captain(self):
        return self.env['mission.info'].browse(self._context.get('active_id')).captain_id
    def _default_launch(self):
        return self.env['mission.info'].browse(self._context.get('active_id')).launch_date
    def _default_return(self):
        return self.env['mission.info'].browse(self._context.get('active_id')).return_date



    name = fields.Char(string='Mission Name', default=_default_name)
    mission_id = fields.Many2one('mission.info', string='Related Mission', default=_default_mission)
    captain_id = fields.Char(related='mission_id.captain_id', string='Captain of the Mission')
    destiny_id = fields.Many2one('mission.info', string='Destination', default=_default_destiny)
    launch_date = fields.Datetime(string='Launch Date', default=_default_launch)
    return_date = fields.Datetime(string='Return Date', default=_default_return)


    def create_project(self):
        project_id = self.env['project.project'].create({
            'name':self.name,
            'mission_id':self.mission_id.id,
            'captain_id':self.captain_id,
        })