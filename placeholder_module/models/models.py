from odoo import api, fields, models


class PlaceholderModule(models.Model):
    _name = "placeholder_module.placeholder_module"
    _description = "placeholder_module.placeholder_module"

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends("value")
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
