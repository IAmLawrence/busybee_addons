# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

class SalaryAdvance(models.Model):
    _inherit = 'salary.advance'

    @api.model
    def default_get(self, field_list):
        result = super(SalaryAdvance, self).default_get(field_list)
        if result.get('user_id'):
            ts_user_id = result['user_id']
        else:
            ts_user_id = self.env.context.get('user_id', self.env.user.id)
        result['employee_id'] = self.env['hr.employee'].search([('user_id', '=', ts_user_id)], limit=1).id

        self_id = request.session.uid
        user = self.env['res.users'].sudo().search([('id', '=', self_id)], limit=1)
        if user.has_group('hr.group_hr_manager'):
            result['admin_login'] = True
        else:
            result['admin_login'] = False
        return result

    admin_login = fields.Boolean(string="Admin", default=False)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, help="Employee")

