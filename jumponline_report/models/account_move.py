# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    selected_layout = fields.Selection([('ambiance', 'Ambiance Deco'), ('jump', 'Jump Online')])

    @api.onchange('partner_id')
    def set_default_selected_layout(self):
        self.ensure_one()
        if self.partner_id:
            self.selected_layout = self.partner_id.second_layout
