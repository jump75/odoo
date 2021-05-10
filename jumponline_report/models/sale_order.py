# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    selected_layout = fields.Selection([('ambiance', 'Ambiance Deco'), ('jump', 'Jump Online')])

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        if self.selected_layout:
            invoice_vals['selected_layout'] = self.selected_layout
        return invoice_vals

    @api.onchange('partner_id')
    def onchange_partner_select_layout(self):
        self.ensure_one()
        if self.partner_id:
            self.selected_layout = self.partner_id.selected_layout
