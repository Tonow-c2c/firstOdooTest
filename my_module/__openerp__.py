# -*- coding: utf-8 -*-
{
    'name': "Library Books",
    'summary': "Manage your books",
    'depends': ['base', 'decimal_precision'],
    'data': [
        'views/library_book.xml',
        'views/library_member.xml',
        'views/test_backend_views.xml',
    ],
    'test': ['tests/test_books.yml'],
}


#{
#    'name': "Title",
#    'summary': "Short subtitle phrase",
#    'description': """Long description""",
#    'author': "Your name",
#    'license': "AGPL-3",
#    'website': "http://www.example.com",
#    'category': 'Uncategorized',
#    'version': '9.0.1.0.0',
#    'depends': ['base'],
#    'data': ['views.xml'],
#    'demo': ['demo.xml'],
#}
