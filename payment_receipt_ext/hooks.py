
# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def post_init_add_payment_method_lines(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    Journal = env['account.journal']
    Method = env['account.payment.method']
    Line = env['account.payment.method.line']

    # Use built-in manual methods
    try:
        manual_in = env.ref('account.account_payment_method_manual_in')
    except Exception:
        manual_in = Method.search([('payment_type','=','inbound')], limit=1)
    try:
        manual_out = env.ref('account.account_payment_method_manual_out')
    except Exception:
        manual_out = Method.search([('payment_type','=','outbound')], limit=1)

    journals = Journal.search([('type', 'in', ['bank', 'cash'])])
    kinds = [
        ('Cash', 'cash'),
        ('Transfer', 'transfer'),
        ('Cheque', 'cheque'),
        ('Benefit', 'benefit'),
    ]

    for j in journals:
        # inbound lines
        if manual_in:
            for name, kind in kinds:
                if not Line.search_count([('journal_id','=',j.id),
                                          ('payment_type','=','inbound'),
                                          ('name','=',name)]):
                    Line.create({
                        'journal_id': j.id,
                        'payment_type': 'inbound',
                        'payment_method_id': manual_in.id,
                        'name': name,
                        'x_line_kind': kind,
                    })
        # outbound lines
        if manual_out:
            for name, kind in kinds:
                if not Line.search_count([('journal_id','=',j.id),
                                          ('payment_type','=','outbound'),
                                          ('name','=',name)]):
                    Line.create({
                        'journal_id': j.id,
                        'payment_type': 'outbound',
                        'payment_method_id': manual_out.id,
                        'name': name,
                        'x_line_kind': kind,
                    })
