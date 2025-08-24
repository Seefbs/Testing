# -*- coding: utf-8 -*-
from odoo import fields, models

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    x_payment_kind = fields.Selection(
        selection=[('cash', 'Cash'),
                   ('transfer', 'Transfer'),
                   ('cheque', 'Cheque'),
                   ('benefit', 'Benefit')],
        string="Payment Method (Journal)",
        help="Used to display conditional fields/labels on payment receipt."
    )

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_instrument_date = fields.Date(string="Instrument Date")
    x_instrument_number = fields.Char(string="Instrument Number")
    x_cheque_no = fields.Char(string="Cheque No.")
    x_cheque_date = fields.Date(string="Cheque Date")

    x_journal_payment_kind = fields.Selection(
        related='journal_id.x_payment_kind', store=False, readonly=True
    )