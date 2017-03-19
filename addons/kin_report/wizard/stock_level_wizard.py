from openerp import models, fields, api


class StockLevelWizard(models.TransientModel):
    _name = 'stock.level.wizard'

    #     def pdf_report(self, cr, uid, ids, context=None):
    #         context = context or {}
    #         datas = {'name':'PFS Report','ids': context.get('active_ids', [])} # use ids for pdf report otherwise there will be error
    #
    #         return {'type': 'ir.actions.report.xml',
    #                     'report_name': 'pfa.form.pdf.webkit',
    #                     'datas':datas,
    #                     }

    @api.multi
    def stock_excel_report(self):
        context = self.env.context or {}
        datas = {'name': 'Current Stock Level Report', 'active_ids': context.get('active_ids', [])}

        if context.get('xls_export'):
            return {
                     'name':'Excel Stock Level Report',
                     'type': 'ir.actions.report.xml',
                    'report_name': 'kin_report.report_stock_level',
                    'datas': datas,
                    }
        return True


    name = fields.Char(string='Name'),
    stock_location_ids = fields.Many2many('stock.location', 'stock_wizard_rel', 'stockwizard_id', 'stockloc_id', string='Stock Locations', required=True)
    category_ids = fields.Many2many('product.category', 'prod_category_rel', 'stockwizard_id', 'stockloc_id', string='Product Categories')
    is_include_zero_qty = fields.Boolean('Include Zero Qty. Stock')




