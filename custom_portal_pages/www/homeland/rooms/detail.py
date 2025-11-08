import frappe

def get_context(context):
    room_name = frappe.form_dict.get("docname")
    room = frappe.get_doc('Room', room_name)

    context.room = room
    context.page_title = room.name
    context.meta_description = room.room_type

    return context
