from odoo import models, fields, api

class LatihanBarang(models.Model):
    _name = 'ujian.barang'  # <-- Ini nama tabel di database (Ingat ini!)
    _description = 'Model untuk Latihan Barang'

    name = fields.Char(string='Nama Barang', required=True)
    harga = fields.Integer(string='Harga Barang')
    stok = fields.Integer(string='Stok')  # <--- PASTIKAN INI ADA
    keterangan = fields.Text(string='Keterangan')