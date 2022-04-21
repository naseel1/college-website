from odoo import http
from odoo.http import request

class about_college(http.controller):
    @http.route('/about-college', auth='public', website='True')
    def index(self):
        return request.render('sample_theme.about_college')
