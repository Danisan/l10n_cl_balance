# -*- coding: utf-8 -*-
{
    'name': "Balance de 8 columnas",

    'summary': """
        Tutorial about how to inherit and modify already existing QWeb reports.""",

    'description': """
        In this tutorial you will learn how to inherit and modify existing QWeb reports.
    """,

    'author': "Nueva Gestion",
    'website': "http://nuevagestion.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],
    'active': False,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    'installable': True
}
