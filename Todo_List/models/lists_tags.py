from odoo import models, fields

class ListsTag(models.Model):
    _name = 'lists.tag'
    _description = 'Lists Tag'

    name = fields.Char(string='Tag Name', required=True)
