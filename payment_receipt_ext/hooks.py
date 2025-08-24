# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def post_init_add_payment_method_lines(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    Journal = env['account.journal']
    Method = env['account.payment.method']
    Line = env['account.payment.method.line']

    codes = ['cash', 'transfer', 'cheque', 'benefit']
    methods = {m.code: m for m in Method.search([('code', 'in', codes)])}
    # Try to use XMLIDs if search missed any (due to noupdate)
    for code in codes:
        if code not in methods:
            try:
                methods[code] = env.ref(f'payment_receipt_ext.account_payment_method_{code}')
            except Exception:
                pass

    journals = Journal.search([('type', 'in', ['bank', 'cash'])])
    for j in journals:
        for code, meth in methods.items():
            if not meth:
                continue
            # inbound line
            if not Line.search_count([('journal_id', '=', j.id),
                                      ('payment_method_id', '=', meth.id),
                                      ('payment_type', '=', 'inbound')]):
                Line.create({
                    'journal_id': j.id,
                    'payment_method_id': meth.id,
                    'payment_type': 'inbound',
                })
            # outbound line
            if not Line.search_count([('journal_id', '=', j.id),
                                      ('payment_method_id', '=', meth.id),
                                      ('payment_type', '=', 'outbound')]):
                Line.create({
                    'journal_id': j.id,
                    'payment_method_id': meth.id,
                    'payment_type': 'outbound',
                })