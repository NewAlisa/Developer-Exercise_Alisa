from odoo import models, fields, api

class TodoLists(models.Model):
    _name = 'todo.lists'
    _description = 'Todo Lists'
    _rec_name = 'title'


    def progress(self):
        for record in self:
            record.status = 'in_progress'
            
    def done(self):
        for record in self:
            record.status = 'complete'
    
    @api.onchange('progarm_id.is_completed')
    def all_progams_completed(self):
        for record in self:
            if all(program.is_completed for program in record.progarm_ids):
                record.check_completed = True
            else:
                record.check_completed = False
 
    
    title = fields.Char(string='Title', required=True)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    status = fields.Selection([
        ('draft', 'DRAFT'),
        ('in_progress', 'IN PROGRESS'),
        ('complete', 'COMPLETE')
    ], string='Status', default='draft')
    tag_ids = fields.Many2many(
        'lists.tag',
        string="Tags",
    )
    progarm_ids = fields.One2many(
        'todo.program',
        'todo_list_id',
        string="Program",
    )
    user_id = fields.Many2many('res.users', string="Attendee")
    check_completed = fields.Boolean(string='Is Complete',compute='all_progams_completed')