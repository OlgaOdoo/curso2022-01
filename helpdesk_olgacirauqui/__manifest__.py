# -*- coding: utf-8 -*-


{
   'name': 'Helpdek Olga Cirauqui',
    'summary': 'Manage helpdesk tickets',
    'version': '15.0.1.0.0',
    'author': 'Olga Cirauqui',
    'depends': ['base', 'mail'],
    'license': 'AGPL-3',
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_tag_views.xml',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_ticket_actions_views.xml'
    ],
    'demo':[
        'demo/account_demo.xml'
    ],
}