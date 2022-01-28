# Copyright 2022 Onestein (<https://www.onestein.nl>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleEcowarehouse(WebsiteSale):

    def _get_shop_payment_values(self, order, **kwargs):
        res = super(WebsiteSaleEcowarehouse, self)._get_shop_payment_values(order, **kwargs)
        partner = order.partner_id
        if partner and partner.property_supplier_payment_term_id and partner.property_supplier_payment_term_id.payment_acquirer_ids:
            res['acquirers'] = [acq for acq in res['acquirers'] if acq in acq in partner.property_supplier_payment_term_id.payment_acquirer_ids]
        return res
