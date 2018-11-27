# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Build It',
    'version': '1.0',
    'category': 'Purchases',
    'author':'hka@novway.com',
    'description': """
Use Purchase Request module for requesting product.
    """,
    'summary': 'Manage construction sites',
    'website': 'https://www.build-it.co',
    'images': ['static/description/icon.jpg'],
    'depends': ['mail'],
    'data': [
        'data/build_it_data.xml',
        'security/build_it_security.xml',
        'security/ir.model.access.csv',
        'views/build_it_view.xml',
        'views/project_project_views.xml',
        'views/purchase_order_views.xml'
    ],
    'depends': [
        'base',
        'purchase',
        'project',
        'stock',
        'hr',
        ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 105,
    'license': 'AGPL-3',
}
