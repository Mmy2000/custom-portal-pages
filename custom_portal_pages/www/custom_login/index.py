import frappe


def get_context(context):
    context.is_logged_in = frappe.session.user != "Guest"
    context.title = "Custom Login"
    context.message = "Welcome to the login page"
    return context
