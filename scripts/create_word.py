from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(word, width=1024, height=512, font_size=100):
    # Create a black background image
    image = Image.new("RGB", (width, height), "black")
    
    # Load a font
    font = ImageFont.load_default()
    
    # Adjust font size based on the image size
    while font.getsize(word)[0] < width - 20:
        font_size += 1
        font = ImageFont.truetype("arial.ttf", font_size)
    
    # Get text size and position
    text_width, text_height = font.getsize(word)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    
    # Draw the text on the image
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), word, fill="white", font=font)
    
    return image

# Example usage:
word = "Zoe"
image = create_image_with_text(word)
image.show()  # Display the image
image.save("Zoe.png")  # Save the image



