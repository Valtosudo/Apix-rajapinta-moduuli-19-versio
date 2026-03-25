from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    transmit_method_id = fields.Many2one(
        comodel_name="transmit.method",
        string="Sending Method",
        ondelete="restrict",
        tracking=True,
    )
    transmit_method_code = fields.Char(
        related="transmit_method_id.code",
        string="Sending Method Code",
        store=True,
    )
