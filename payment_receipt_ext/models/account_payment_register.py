# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    x_instrument_date = fields.Date(string="Instrument Date")
    x_instrument_number = fields.Char(string="Instrument Number")
    x_cheque_no = fields.Char(string="Cheque No.")
    x_cheque_date = fields.Date(string="Cheque Date")

    x_show_instrument = fields.Boolean(compute='_compute_x_show_flags')
    x_show_cheque = fields.Boolean(compute='_compute_x_show_flags')

    @api.depends('journal_id.type', 'payment_method_line_id.name')
    def _compute_x_show_flags(self):
        for rec in self:
            is_bank_cash = rec.journal_id and rec.journal_id.type in ('bank', 'cash')
            name = (rec.payment_method_line_id.name or '').strip().lower()
            is_cheque = name.startswith('cheque')
            rec.x_show_instrument = bool(is_bank_cash)
            rec.x_show_cheque = bool(is_bank_cash and is_cheque)

    def _create_payments(self):
        payments = super()._create_payments()
        vals = {}
        if self.x_instrument_date:
            vals['x_instrument_date'] = self.x_instrument_date
        if self.x_instrument_number:
            vals['x_instrument_number'] = self.x_instrument_number
        if self.x_cheque_no:
            vals['x_cheque_no'] = self.x_cheque_no
        if self.x_cheque_date:
            vals['x_cheque_date'] = self.x_cheque_date
        if vals:
            payments.write(vals)
        return payments