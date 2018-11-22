# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    project_id = fields.Many2one(
        string='Project',
        comodel_name='project.project',
)
