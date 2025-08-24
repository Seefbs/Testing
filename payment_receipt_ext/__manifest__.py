# -*- coding: utf-8 -*-
{
    "name": "Payment Receipt Extensions",
    "summary": "Extra fields & formatted Payment Receipt/Voucher for Odoo 18",
    "version": "18.0.1.0.8",
    "author": "Seef Business Solutions",
    "website": "https://www.seefbs.com",
    "license": "LGPL-3",
    "category": "Accounting/Accounting",
    "depends": ["account"],
    "data": [
        "views/payment_views.xml",
        "report/payment_receipt_report.xml"
    ],
    "installable": True,
    "application": False
}