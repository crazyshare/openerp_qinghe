# -*- coding: utf-8 -*-
from openerp import http

class Qinghe(http.Controller):
    @http.route('/qinghe/qinghe/', auth='public')
    def index(self, **kw):
        return http.request.render('qinghe.index',
                                   {'fruits':['apple','banana','pear','orange']})
    @http.route('/qinghe/xlist/', auth='public')
    def xlist(self, **kw):
        return http.request.render('qinghe.xlist',
                                   {'fruits':['apple','banana','pear','orange','loofah']})
    @http.route('/qinghe/xmodel/', auth='public')
    def xmodel(self, **kw):
         #启用qinghe models到全局变量中
        fruits = http.request.env['qinghe.qinghe']
        return http.request.render('qinghe.xmodel',
                                   {'fruits':fruits.search([])})    
    @http.route('/qinghe/website/', auth='public',website=True)
    def website(self, **kw):
        #启用fruits models到全局变量中
        fruits = http.request.env['qinghe.fruits']
        return http.request.render('qinghe.website',
                                   {'fruits':fruits.search([])})    
  