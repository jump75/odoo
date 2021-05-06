# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools, _


class ResCompany(models.Model):
    _inherit = "res.company"

    secondary_layout = fields.Selection([('ambiance', 'Ambiance Deco'), ('jump', 'Jump Online')], default='jump')

    logo_ambiance = fields.Binary(string="Company Logo Ambiance")
    primary_color_ambiance = fields.Char()
    secondary_color_ambiance = fields.Char()
    font_ambiance = fields.Selection(
        [("Lato", "Lato"), ("Roboto", "Roboto"), ("Open_Sans", "Open Sans"), ("Montserrat", "Montserrat"),
         ("Oswald", "Oswald"), ("Raleway", "Raleway")], default="Lato")

    report_header_ambiance = fields.Text(string='Company Tagline Ambiance',
                                         help="Appears by default on the top right corner of your printed documents (report header).")
    report_footer_ambiance = fields.Text(string='Report Footer Ambiance', translate=True,
                                         help="Footer text displayed at the bottom of all reports.")
