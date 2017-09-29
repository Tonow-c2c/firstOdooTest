# -*- coding: utf-8 -*-
'''
docsting models
'''
from openerp import models, fields, api
from openerp.addons import decimal_precision as dp
from openerp.fields import Date as fDate
from datetime import timedelta as td

class LibraryBook(models.Model):
    '''
    Docstring class
    '''
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'
    name = fields.Char('Title', required=True)
    short_name = fields.Char(string='Short Title',
                             size=100, # For Char only
                             translate=False, # also for Text fields
                            )
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner',
                                  string='Authors')
    category_ids = fields.Many2many('library.book.category',
                                    string='Categorie')
    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State')
    description = fields.Html(string='Description',
                              # optional:
                              sanitize=True,
                              strip_style=False,
                              translate=False,
                             )
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer(string='Number of Pages',
                           default=0,
                           help='Total book page count',
                           groups='base.group_user',
                           states={'cancel': [('readonly', True)]},
                           copy=True,
                           index=False,
                           readonly=False,
                           required=False,
                           company_dependent=False,
                          )
    reader_rating = fields.Float(
        'Reader Average Rating',
        (14, 4), # Optional precision (total, decimals),
    )
    cost_price = fields.Float('Book Cost',
                              dp.get_precision('Book Price'))
    currency_id = fields.Many2one('res.currency',
                                  string='Currency')
    retail_price = fields.Monetary('Retail Price',
                                   # optional: currency_field='currency_id',
                                   currency_field='currency_id',
                                  )
    publisher_id = fields.Many2one(comodel_name='res.partner', string='Publisher',
                                   # optional:
                                   ondelete='set null',
                                   context={},
                                   domain=[],
                                  )
    publisher_city = fields.Char('Publisher City',
                                 related='publisher_id.city'
                                )
    age_days = fields.Float(string='Days Since Release',
                            compute='_compute_age',
                            inverse='_inverse_age',
                            search='_search_age',
                            store=False,
                            compute_sudo=False,
                           )
    _sql_constraints = [('name_uniq',
                         'UNIQUE (name)',
                         'Book title must be unique.')
                       ]

    @api.constrains('date_release')
    def _check_release_date(self):
        for r in self:
            if r.date_release > fields.Date.today():
                raise models.ValidationError(
                    'Release date must be in the past')

    @api.depends('date_release')
    def _compute_age(self):
        today = fDate.from_string(fDate.today())
        for book in self.filtered('date_release'):
            delta = fDate.from_string(book.date_release) - today
            book.age_days = delta.days


    def name_get(self):
        '''
        Docstring
        '''
        result = []
        for record in self:
            result.append(
                (record.id,
                 u"%s (%s)" % (record.name, record.date_release)
                ))
        return result

    def _inverse_age(self):
        today = fDate.from_string(fDate.today())
        for book in self.filtered('date_release'):
            d = td(days=book.age_days) - today
            book.date_release = fDate.to_string(d)

    def _search_age(self, operator, value):
        today = fDate.from_string(fDate.today())
        value_days = td(days=value)
        value_date = fDate.to_string(today - value_days)
        return [('date_release', operator, value_date)]

class ResPartner(models.Model):
    '''
    Docstring
    '''
    _inherit = 'res.partner'
    book_ids = fields.One2many(comodel_name='library.book',
                               inverse_name='publisher_id',
                               string='Published Books')
