# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountPaymentMethodLine(models.Model):
    _inherit = 'account.payment.method.line'

    x_line_kind = fields.Selection([
        ('cash', 'Cash'),
        ('transfer', 'Transfer'),
        ('cheque', 'Cheque'),
        ('benefit', 'Benefit'),
    ], string="Kind")

    @api.onchange('x_line_kind')
    def _onchange_x_line_kind(self):
        for rec in self:
            if rec.x_line_kind and (not rec.name or rec.name in ('New', '')):
                rec.name = dict(self._fields['x_line_kind'].selection).get(rec.x_line_kind)