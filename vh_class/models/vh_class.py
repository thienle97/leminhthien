# -*- coding: utf-8 -*-
from odoo import fields , models
class VhClass(models.Model):
    _name= "vh.clas"

    name = fields.Char('Class Name')
    soluong = fields.Integer()
