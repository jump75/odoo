# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    secondary_layout = fields.Selection([('ambiance', 'Ambiance Deco'), ('jump', 'Jump Online')])
