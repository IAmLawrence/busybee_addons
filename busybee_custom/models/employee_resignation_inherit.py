# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EmployeeResignation(models.Model):
    _inherit = 'hr.resignation'

    emp_contract = fields.Many2one('hr.contract', related='employee_id.contract_id', string='Employee Contract')

