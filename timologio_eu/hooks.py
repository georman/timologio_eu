# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "timologio_eu"
app_title = "Timologio_eu"
app_publisher = "GAM LTD"
app_description = "Timologio Theme"
app_icon = "icon-edit"
app_color = "black"
app_email = "info@gam.gr"
app_version = "0.0.1"
app_license = "GNU"
hide_in_installer = True

website_context = {
          "top_bar_items": [
		{"label": "Αρχική", "url": "/", "right":1},
		{"label": "Τιμοκατάλογος", "url": "/pricing", "right":1},
		{"label": "Χαρακτηριστικά", "url": "/features", "right":1},
	],
	"hide_login": 1
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/timologio_eu/css/timologio_eu.css"
# app_include_js = "/assets/timologio_eu/js/timologio_eu.js"

# include js, css files in header of web template
# web_include_css = "/assets/timologio_eu/css/timologio_eu.css"
# web_include_js = "/assets/timologio_eu/js/timologio_eu.js"



# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"


# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "timologio_eu.install.before_install"
# after_install = "timologio_eu.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "timologio_eu.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"timologio_eu.tasks.all"
# 	],
# 	"daily": [
# 		"timologio_eu.tasks.daily"
# 	],
# 	"hourly": [
# 		"timologio_eu.tasks.hourly"
# 	],
# 	"weekly": [
# 		"timologio_eu.tasks.weekly"
# 	]
# 	"monthly": [
# 		"timologio_eu.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "timologio_eu.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "timologio_eu.event.get_events"
# }

