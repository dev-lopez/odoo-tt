{
    'name': 'custom_crm',
    'version': '1.0',
    'description': """
        descripcion larga
    """,
    'summary': """
        Modulo CRM para la gestion de visitas
    """,
    'author': 'Alexis Lopez',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base',
        'sale_management'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_crm_menu_views.xml',
        'views/custom_crm_view.xml',
        'views/sales_order_inherit.xml',
        'reports/custom_crm_report.xml'
    ],
    'demo': [
        'demo/demo.xml'
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        
    }
}