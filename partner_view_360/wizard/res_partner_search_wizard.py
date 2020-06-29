# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2019 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api, _
import logging
from datetime import date
_logger = logging.getLogger(__name__)
from odoo.exceptions import Warning
from odoo.tools.safe_eval import safe_eval


# class ResPartnerEmployerSearchWizard(models.TransientModel):
#     _name = "res.partner.employer.search.wizard"

    #gdpr_id = fields.Many2one('gdpr') #some gdpr object
    # search_reason = fields.Selection(string="Search reason" ,selection=[('reason','Reason')])#
    # search_domain = fields.Char(string="Search Filter", default=[('company_registry', '=', '')])
    
    # @api.multi
    # def search_employer(self):
    #     raise Warning("Inte implementerat än")
    #     something = True #byt ut mot en check efter om det är ett eller många resultat
    #     view_type = "tree"
    #     view_id = "view_partner_employer_kanban"
    #     partner_id = self.env['res.partner'].search([('company_registry', '=', self.company_registry)]).mapped('id')
    #     if len(partner_id) > 0:
    #         partner_id = partner_id[0]
    #     else:
    #         raise Warning(_("No id found"))
    #     if something:
    #         view_type = "form"
    #         view_id = "view_partner_employer_form"
    #     return{
    #         'name': _('Employers'), #vad gör den?
    #         'domain':[('id', '=', partner_id)],
    #         'view_type': view_type,
    #         'res_model': 'res.partner',
    #         'view_id':  view_id,
    #         'view_mode': 'form',
    #         'type': 'ir.actions.act_window',
    #     }

class ResPartnerJobseekerSearchWizard(models.TransientModel):
    _name = "res.partner.jobseeker.search.wizard"

    #gdpr_id = fields.Many2one('gdpr.inventory') 
    #gdpr_reasons = fields.Many2one(related="gdpr_id.reasons?")
    reason_or_id = fields.Selection(string="Access by reason or identification?", selection=[('reason', 'Reason'), ('id', 'Identification')])
    search_reason = fields.Selection(string="Search reason",selection=[('record incoming documents','Record incoming documents'), ("follow-up of job seekers' planning","Follow-up of job seekers' planning"), ('directory Assistance','Directory Assistance'), ('matching','Matching'), ('decisions for other officer','Decisions for other officer'),('administration of recruitment meeting/group activity/project','Administration of recruitment meeting/group activity/project'),('investigation','Investigation'),('callback','Callback'),('other reason','Other reason')])#
    identification = fields.Selection(string="Identification",selection=[('id document','ID document'), ('Digital ID','Digital ID'), ('id document-card/residence permit card','ID document-card/Residence permit card'), ('known (previously identified)','Known (previously identified)'), ('identified by certifier','Identified by certifier')])#
    search_domain = fields.Char(string="Search Filter", default=[('social_sec_nr', '=', '')] )
    other_reason = fields.Char(string="Other reason")

    @api.multi
    def search_jobseeker(self):
        # ~ raise Warning("Inte implementerat än")
        if ("social_sec_nr" in self.search_domain or "company_registry" in self.search_domain) and "=" not in self.search_domain:
            raise Warning(_("Social security number has to be searched in full"))
        if self.search_reason == False and self.identification == False:
            raise Warning(_("Search reason or identification must be set before searching"))
        elif self.search_reason == "other reason" and self.other_reason == False:
            raise Warning(_("Other reason selected but other reason field is not filled in"))
        
        partner_ids = self.env['res.partner'].search(safe_eval(self.search_domain)).mapped('id')
        if len(partner_ids) < 1:
            raise Warning(_("No id found"))       
            
        action = {
            'name': _('Jobseekers'),
            'domain': [('id', '=', partner_ids), ('is_jobseeker', '=', True)],
            #'view_type': 'tree',
            'res_model': 'res.partner',
            'view_ids':  [self.env.ref("partner_view_360.view_jobseeker_kanban").id, self.env.ref("partner_view_360.view_jobseeker_form").id, self.env.ref("partner_view_360.view_jobseeker_tree").id], 
            'view_mode': 'kanban,tree,form',
            'type': 'ir.actions.act_window',
        }
        if len(partner_ids) == 1:
            action['view_id'] = self.env.ref("partner_view_360.view_jobseeker_form").id
            action['res_id'] = partner_ids[0]
            action['view_mode'] = 'form'

        return action