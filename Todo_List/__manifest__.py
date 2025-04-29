{
    'name': 'Todo List',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list_menu_item.xml',
        'views/todo_list_views.xml',
        'views/list_tag_views.xml',
        'data/tag_data.xml',
    ],
    'installable': True,
    'application': True
}
