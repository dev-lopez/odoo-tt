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
    'licence': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/space_mission_groups.xml',
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menu.xml',
    ],
    'demo': [
        'demo/space_mission_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}