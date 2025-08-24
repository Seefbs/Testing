# -*- coding: utf-8 -*-
from odoo import fields, models

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    x_instrument_date = fields.Date(string="Instrument Date")
    x_instrument_number = fields.Char(string="Instrument Number")
    x_cheque_no = fields.Char(string="Cheque No.")
    x_cheque_date = fields.Date(string="Cheque Date")

    def _create_payments(self):
        moves = super()._create_payments()
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
            moves.write(vals)
        return moves