from odoo import fields, models


class TransmitMethod(models.Model):
    _name = "transmit.method"
    _description = "Transmit Method"
    _order = "sequence, id"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    sequence = fields.Integer(default=10)
    customer_ok = fields.Boolean(
        string="For Customers",
        help="Allow using this transmit method on customer invoices.",
        default=True,
    )
    supplier_ok = fields.Boolean(
        string="For Vendors",
        help="Allow using this transmit method on vendor invoices.",
        default=False,
    )
