# -*- coding: utf-8 -*-
{
    'name': "qinghe",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "上海善之农生物科技有限公司",
    'website': "http://www.caimaimai.com.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base'],
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'qh_list.xml',
        'xmodel.xml',
        'demo.xml',
        'website.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo.xml',
    #],
}