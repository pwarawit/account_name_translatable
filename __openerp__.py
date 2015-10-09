# -*- encoding: utf-8 -*-
##############################################################################
#
#    Account Name Translatable module for Odoo 8
#    Copyright (C) 2015 InfoMobius (http://infomobius.com)
#    @author PanaEk Warawit <p.warawit@infomobius.com>
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


{
    'name': 'Account Name Translatable',
    'version': '0.1',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': 'This module modify base name field of account.account to be translatable',
    'description': """
This module sets the translatable fields of the account name (name field) of acccount.account model 
to be translatable fields. (It was non-translatable by default).
    """,
    'author': 'InfoMobius',
    'website': 'http://infomobius.com',
    'depends': ['account'],
}
