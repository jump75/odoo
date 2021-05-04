# -*- coding: utf-8 -*-
{
    'name': "Jump Online Secondary Report Layout",

    'summary': """
        Jump Online Secondary Report Layout
        """,

    'description': """
        TASK ID - 2516145
    """,

    'author': "Odoo PS",
    'website': "http://www.odoo.com",

    # for the full list
    'category': 'Custom Development',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'sale_management', 'stock'],

    # always loaded
    'data': [
        'views/document_views.xml',
        'views/report_templates_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/stock_picking_views.xml'
    ],
}
