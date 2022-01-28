# Copyright 2020 Onestein (<https://www.onestein.nl>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _set_transaction_pending(self):
        return super(PaymentTransaction, self.with_context(from_transaction_pending=True))._set_transaction_pending()
