# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    selected_layout = fields.Selection([('ambiance', 'Ambiance Deco'), ('jump', 'Jump Online')])
