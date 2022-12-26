{
    'name': 'Space Mission',
    'description': '''
        Helps organice and manage Odoo's Moon travel. It manages:
        - Space Crew
        - Space Ship
    ''',
    'summary': 'Odoo Inc module to manage the travel to the Moon',
    'author': 'Alexis Lopez',
    'category': 'Traveling',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'depends': ['base',
               'project',],
    'data': [
        'security/space_mission_groups.xml',
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menu.xml',
        'views/space_ship_view.xml',
        'views/mission_info.xml',
        'views/project_views_inherit.xml',
    ],
    'demo': [ ],
    'installable': True,
    'application': True,
    'auto_install': False,
}