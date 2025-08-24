# -*- coding: utf-8 -*-
{
    "name": "Payment Receipt Extensions",
    "summary": "Extra fields & formatted Payment Receipt/Voucher for Odoo 18",
    "version": "18.0.1.0.4",
    "author": "Seef Business Solutions",
    "website": "https://www.seefbs.com",
    "license": "LGPL-3",
    "category": "Accounting/Accounting",
    "depends": ["account"],
    "data": [
        "data/payment_methods.xml",
        "views/payment_views.xml",
        "report/payment_receipt_report.xml"
    ],
    "post_init_hook": "post_init_add_payment_method_lines",
    "installable": True,
    "application": False
}