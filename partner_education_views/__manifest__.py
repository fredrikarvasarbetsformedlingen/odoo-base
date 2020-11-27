# -*- coding: UTF-8 -*-

################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2019 N-Development (<https://n-development.com>).
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
################################################################################

{
    'name': 'Partner Education',
    'version': '12.0.0.0.1',
    'category': 'Mail',
    'description': """Partner Education Level""",

    'author': "N-development",
    'license': 'AGPL-3',
    'website': 'https://www.n-development.com',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/res.drivers_license.csv',
        'data/res.partner.education_level.csv',
        'data/res.sun.csv',
        'views/res_sun_view.xml',
        'views/education_level_view.xml',
        'views/res_drivers_license_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'images': [
        'static/description/img.png'
    ],
}
