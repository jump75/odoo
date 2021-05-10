# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    report_layout_id = fields.Many2one('report.layout')
    selected_layout = fields.Selection([('ambiance', 'Ambiance Deco'), ('jump', 'Jump Online')],
                                     default=lambda self: self.env.company.secondary_layout)
