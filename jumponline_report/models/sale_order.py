# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    selected_layout = fields.Selection(related='company_id.secondary_layout', store=True, readonly=False)

    @api.onchange('partner_id')
    def set_default_selected_layout(self):
        if self.partner_id:
            self.selected_layout = self.partner_id.second_layout
