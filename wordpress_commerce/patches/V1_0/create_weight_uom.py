# Copyright (c) 2024, Mohammed Awadh and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from wordpress_commerce.after_install import create_weight_uom

def execute():
	create_weight_uom()
