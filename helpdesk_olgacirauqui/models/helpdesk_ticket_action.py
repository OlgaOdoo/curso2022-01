from odoo import fields,models

class HelpdeskTicketAction(models.Model):
    _name = "helpdesk.ticket.action"
    _description = "Helpdesk Ticket Action"
    _order = "sequence"

    sequence = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()
    duration =fields.Float()
    action_ids = fields
    ticket_id=fields.Many2one(
        comodel_name="helpdesk.ticket"
    )
    def review(self):
        for record in self: 
            record.description = '%s\n%s' %(record.description, 'OK')