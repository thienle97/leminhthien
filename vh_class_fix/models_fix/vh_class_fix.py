from odoo import models_fix, fields_fix


class VhClassFix(models_fix.Model):
    _name= 'vh.class.fix'

    name = fields.Char('CLass Name')
    soluong = fields.Integer()
