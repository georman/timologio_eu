from __future__ import unicode_literals

app_name = "timologio_eu"
app_title = "Timologio_eu"
app_publisher = "GAM LTD"
app_description = "Timologio Theme"
app_icon = "icon-edit"
app_color = "#5a6778"
app_email = "info@gam.gr"
app_version = "0.0.1"
app_license = "GNU"


website_context = {
	"brand_html": "<img class='navbar-icon' src='/assets/frappe_theme/img/erp-icon.svg' />ERPNext",
	"top_bar_items": [
		{"label": "Pricing", "url": "/pricing", "right":1},
		{"label": "Features", "url": "/features", "right":1},
		{"label": "Docs", "url": "https://manual.erpnext.com", "right":1},
		{"label": "Blog", "url": "https://blog.frappe.io", "right":1},
	],
	"hide_login": 1,
	"favicon": "/assets/frappe_theme/img/favicon.ico"
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
# home_page = "login"

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

