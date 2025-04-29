from odoo import models, fields

class Program(models.Model):
    _name = 'todo.program'
    _description = 'Todo Program'

    name = fields.Char(string='name', required=True)
    description = fields.Text(string='Description')
    is_completed = fields.Boolean(string='Is Complete', default=False)
    todo_list_id = fields.Many2one(
        'todo.lists',
        string='Todo List',
    )