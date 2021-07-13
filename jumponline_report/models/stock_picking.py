# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    selected_layout = fields.Selection(related='sale_id.selected_layout', readonly=False, store=True)
