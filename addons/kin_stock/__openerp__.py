{
    'name': 'Stock Modifications',
    'version': '0.1',
    'category': 'Warehouse',
    'description': """
Kincotech Customization
=======================================================================================
""",
    'author': 'Kingsley',
    'website': 'http://kinsolve.com',
    'depends': ['base','stock','sale_stock','account','mail','purchase','kin_purchase','kin_account','kin_sales','account_analytic_default'],
    'data': [
        'security/security.xml',
        'wizard/picking_rejected.xml',
        'stock_view.xml',
        'mail_template.xml',
        'report/report_deliveryslip.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'images': [],
}