import os
from PIL import Image, ImageDraw, ImageFont

def generate_certificate(name):
    # Load the certificate template
    template_path = "image.png"  # Your provided certificate
    output_folder = "certificates/"
    certificate = Image.open(template_path)

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define font settings (use your preferred .ttf file)
    font_path = "arialbd.ttf"  # Replace with bold Arial font path or any desired .ttf file
    font_size = 63  # Adjusted for visibility
    font = ImageFont.truetype(font_path, size=font_size)

    # Initialize ImageDraw
    draw = ImageDraw.Draw(certificate)

    # Get text size to center it
    text = name.strip()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate position (centered below "This certificate is presented to:")
    x = (certificate.width - text_width) // 2  # Center horizontally
    y = 580  # Adjust this Y-coordinate based on the position on your template

    # Add the user's name to the certificate
    draw.text((x, y), text, fill="black", font=font)
    # draw.rectangle([(x - 10, y - 10), (x + text_width + 10, y + text_height)], fill="black")

    # Save the generated certificate
    output_path = os.path.join(output_folder, f"{name.replace(' ', '_')}.png")
    certificate.save(output_path)
    print(f"Certificate saved for {name} at {output_path}")

# Example usage
user_name = input("Enter the user's name: ")
generate_certificate(user_name)
