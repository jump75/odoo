# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    selected_layout = fields.Selection(related='company_id.secondary_layout', store=True, readonly=False)

    @api.onchange('partner_id')
    def set_default_selected_layout(self):
        if self.partner_id:
            self.selected_layout = self.partner_id.second_layout
