# -*- coding: utf-8 -*-
from odoo import fields, models

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    x_instrument_date = fields.Date(string="Instrument Date")
    x_instrument_number = fields.Char(string="Instrument Number")
    x_cheque_no = fields.Char(string="Cheque No.")
    x_cheque_date = fields.Date(string="Cheque Date")