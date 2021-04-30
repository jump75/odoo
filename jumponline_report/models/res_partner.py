# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    report_layout_id = fields.Many2one('report.layout')
    second_layout = fields.Selection(related='company_id.secondary_layout', store=True, readonly=False,
                                     default=lambda self: self.env.company.secondary_layout)

    @api.onchange('second_layout')
    def _onchange_report_layout_id(self):
        self.ensure_one()
        company_id = self.env.user.company_id
        company_id.secondary_layout = self.second_layout
