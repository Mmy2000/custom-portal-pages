import frappe


def get_context(context):
    rooms = frappe.get_all("Room", fields=["*"])

    for r in rooms:
        # Load hotel document
        hotel = frappe.get_doc("Hotel", r.hotel)
        r["hotel_image"] = hotel.cover_image

        # Load amenities for each room
        room_doc = frappe.get_doc("Room", r.name)
        r["amenities"] = [
            a.amenity_id for a in room_doc.amenities
        ]  # <-- use correct field name

    context.rooms = rooms
    return context
