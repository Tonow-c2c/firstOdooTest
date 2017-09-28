# -*- coding: utf-8 -*-
'''
docsting models
'''
from openerp import models, fields
from openerp.addons import decimal_precision as dp
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
    publisher_id = fields.Many2one('res.partner', string='Publisher',
                                   # optional:
                                   ondelete='set null',
                                   context={},
                                   domain=[],
                                  )


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


class ResPartner(models.Model):
    '''
    Docstring
    '''
    _inherit = 'res.partner'
    book_ids = fields.One2many('library.book', 'publisher_id',
                               string='Published Books')
