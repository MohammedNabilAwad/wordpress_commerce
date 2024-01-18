# Copyright (c) 2024, Mohammed Awadh and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def create_weight_uom():
	for unit in ['g', 'kg', 'lbs', 'oz']:
		if not frappe.db.get_value("UOM", unit.title(), "name"):
			uom = frappe.new_doc("UOM")
			uom.uom_name = unit.title()
			uom.insert(ignore_permissions=True)