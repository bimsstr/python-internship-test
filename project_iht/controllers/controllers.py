from odoo import http
from odoo.http import request
import json

class ProjectIhtController(http.Controller):
    
    @http.route('/api/project_data', type='http', auth='public', methods=['GET'], csrf=False)
    def get_project_data(self, **kw):
        projects = request.env['project.project'].sudo().search([])
        
        hasil_data = []
        
        for p in projects:
            hasil_data.append({
                'nama_project': p.name,
                'customer': p.partner_id.name if p.partner_id else "Tidak ada customer",
                'lokasi_proyek': p.lokasi_proyek or "", 
                'source_aplikasi': p.source_aplikasi_pendukung or "",
                'pekerja_remote': p.daftar_pekerja_remote or [],
            })
            
        return request.make_response(
            json.dumps({'status': 200, 'data': hasil_data}, default=str),
            headers=[('Content-Type', 'application/json')]
        )