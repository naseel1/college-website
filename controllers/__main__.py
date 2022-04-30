from odoo import http
from odoo.http import request

class about_college(http.controller):
    @http.route('/about-college', auth='public', website='True')
    def index(self):
        return request.render('collage_website.about_college')
