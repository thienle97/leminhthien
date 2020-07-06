from odoo import fields , models
class VhClass(models.Model):
    _name = "vh.cars"

    name = odoo.Char('Cars Name')
    color = odoo.Char('Color')
