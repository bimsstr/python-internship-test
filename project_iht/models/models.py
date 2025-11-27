from odoo import models, fields, api


class project_iht(models.Model):
    _inherit = 'project.project'

    lokasi_proyek=fields.Text(String='Lokasi Proyek')
    source_aplikasi_pendukung=fields.Char(String='Source Aplikasi Pendukung')
    daftar_pekerja_remote=fields.Char(String='Daftar Pekerja Remote')


