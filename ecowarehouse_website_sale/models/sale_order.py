# Copyright 2020 Onestein (<https://www.onestein.nl>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _send_order_confirmation_mail(self):
        if self.env.context.get('from_transaction_pending', False):
            orders = self.env['sale.order']
            for order in self:
                send_mail = order.transaction_ids.mapped('acquirer_id').mapped('send_mail_on_transaction_pending')
                tst = all(send_mail)
                if tst:
                    orders |= order
            return super(SaleOrder, orders)._send_order_confirmation_mail()

        else:
            return super(SaleOrder, self)._send_order_confirmation_mail()
