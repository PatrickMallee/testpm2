# Copyright 2020 Onestein (<https://www.onestein.nl>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    send_mail_on_transaction_pending = fields.Boolean(default=True)
