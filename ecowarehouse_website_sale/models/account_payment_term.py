# Copyright 2022 Onestein (<https://www.onestein.nl>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    payment_acquirer_ids = fields.Many2many('payment.acquirer')
