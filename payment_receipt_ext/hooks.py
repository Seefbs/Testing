# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def post_init_add_payment_method_lines(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    Journal = env['account.journal']
    Method = env['account.payment.method']
    Line = env['account.payment.method.line']

    inbound_codes = ['cash_in', 'transfer_in', 'cheque_in', 'benefit_in']
    outbound_codes = ['cash_out', 'transfer_out', 'cheque_out', 'benefit_out']

    inbound_methods = {m.code: m for m in Method.search([('code', 'in', inbound_codes)])}
    outbound_methods = {m.code: m for m in Method.search([('code', 'in', outbound_codes)])}

    journals = Journal.search([('type', 'in', ['bank', 'cash'])])
    for j in journals:
        for code, meth in inbound_methods.items():
            if not meth:
                continue
            if not Line.search_count([('journal_id', '=', j.id),
                                      ('payment_method_id', '=', meth.id),
                                      ('payment_type', '=', 'inbound')]):
                Line.create({
                    'journal_id': j.id,
                    'payment_method_id': meth.id,
                    'payment_type': 'inbound',
                })
        for code, meth in outbound_methods.items():
            if not meth:
                continue
            if not Line.search_count([('journal_id', '=', j.id),
                                      ('payment_method_id', '=', meth.id),
                                      ('payment_type', '=', 'outbound')]):
                Line.create({
                    'journal_id': j.id,
                    'payment_method_id': meth.id,
                    'payment_type': 'outbound',
                })