from odoo import http
from odoo.http import request
import json

class LatihanController(http.Controller):

    # URL ini yang nanti dites di Postman: http://localhost:8069/api/get_barang
    @http.route('/api/get_barang', auth='public', type='json', methods=['GET'])
    def get_semua_barang(self, **kw):
        # Ambil semua data dari model yang kita buat di Langkah 2
        barang_rec = request.env['latihan.barang'].sudo().search([])
        
        hasil = []
        for b in barang_rec:
            hasil.append({
                'nama': b.name,
                'harga': b.harga
            })
            
        return {'status': 200, 'data': hasil, 'message': 'Sukses ambil data!'}