{
    'name': 'Custom Theme Banner',
    'description': 'A module that displays a "Hello World" banner at the top of the homepage.',
    'version': '1.0',
    'author': 'Shah Alam Sumon',
    'category': 'Website',
    'depends': ['website'],
    'sequence': 100,
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_theme_banner/static/**/*',
        ],
    },
    'installable': True,
    'application': True,
}
