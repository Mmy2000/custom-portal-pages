import frappe

def get_context(context):
    room_name = frappe.form_dict.get("docname")
    room = frappe.get_doc('Room', room_name)

    context.room = room
    context.page_title = room.name
    context.meta_description = room.room_type
    context.related_amenities = frappe.get_all(
        "Amenities",
        filters={"name": ["in", [amenity.amenity_id for amenity in room.amenities]]},
        fields=["title"],
    )
    return context
