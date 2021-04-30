# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"

    secondary_layout = fields.Selection(related='company_id.secondary_layout', readonly=False)

    @api.depends('report_layout_id', 'logo', 'font', 'primary_color', 'secondary_color', 'report_header',
                 'report_footer', 'secondary_layout')
    def _compute_preview(self):
        super(BaseDocumentLayout, self)._compute_preview()
