# -*- coding: utf-8 -*-

from openerp import models, fields, api

class qinghe(models.Model):
    _name = 'qinghe.qinghe'

    name = fields.Char()
    

class fruits(models.Model):
    _name='qinghe.fruits'
    
    name = fields.Char()