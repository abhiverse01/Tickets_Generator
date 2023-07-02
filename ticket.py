from PIL import Image, ImageDraw, ImageFont, ImageOps


def generate_ticket(ticket_id, location, date):
    try:
        # Create an image with a light blue background
        img = Image.new('RGB', (600, 400), color=(135, 206, 250))

        # Add a border
        border = ImageOps.expand(img, border=20, fill='black')
        d = ImageDraw.Draw(border)

        # Load the default font
        fnt = ImageFont.load_default()

        # Add some padding and arrange the ticket details on the ticket
        padding = 50
        d.text((padding, padding), f"Ticket ID: {ticket_id}", font=fnt, fill=(0, 0, 0))
        d.text((padding, padding + 50), f"Location: {location}", font=fnt, fill=(0, 0, 0))
        d.text((padding, padding + 100), f"Date: {date}", font=fnt, fill=(0, 0, 0))

        # Save the image
        image_path = f"{ticket_id}.jpg"
        border.save(image_path)

        return image_path
    except Exception as e:
        print(f"An error occurred while generating the ticket: {e}")
        return None
