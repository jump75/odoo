# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"

    secondary_layout = fields.Selection(related='company_id.secondary_layout', readonly=False)
    logo_ambiance = fields.Binary(related='company_id.logo_ambiance', store=True, readonly=False)
    preview_logo_ambiance = fields.Binary(related='logo_ambiance', string="Preview logo Ambiance")
    primary_color_ambiance = fields.Char(related='company_id.primary_color_ambiance', readonly=False)
    secondary_color_ambiance = fields.Char(related='company_id.secondary_color_ambiance', readonly=False)
    report_header_ambiance = fields.Text(related='company_id.report_header_ambiance', readonly=False)
    report_footer_ambiance = fields.Text(related='company_id.report_footer_ambiance', readonly=False)
    preview_ambiance = fields.Html(compute='_compute_preview_ambiance',
                                   sanitize=False,
                                   sanitize_tags=False,
                                   sanitize_attributes=False,
                                   sanitize_style=False,
                                   sanitize_form=False,
                                   strip_style=False,
                                   strip_classes=False)

    @api.depends('report_layout_id', 'logo_ambiance', 'secondary_layout', 'report_header_ambiance',
                 'report_footer_ambiance', 'primary_color_ambiance', 'secondary_color_ambiance')
    def _compute_preview_ambiance(self):
        """ compute a qweb based preview to display on the wizard """
        styles = self._get_asset_style()
        for wizard in self:
            if wizard.report_layout_id:
                preview_css = self._get_css_for_preview(styles, wizard.id)
                wizard.preview_ambiance = self.env['ir.ui.view']._render_template('web.report_invoice_wizard_preview',
                                                                      {'company': wizard, 'preview_css': preview_css})
            else:
                wizard.preview_ambiance = False

    @api.depends('report_layout_id', 'logo', 'font', 'primary_color', 'secondary_color', 'report_header',
                 'report_footer', 'secondary_layout')
    def _compute_preview(self):
        super(BaseDocumentLayout, self)._compute_preview()
