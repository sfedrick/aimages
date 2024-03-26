from PIL import Image

def upscale_image(input_path, output_path, target_width, target_height):
    # Open the input image
    with Image.open(input_path) as img:
        # Upscale the image
        upscaled_img = img.resize((target_width, target_height), Image.LANCZOS)
        
        # Save the upscaled image
        upscaled_img.save(output_path)
        print(f"Image upscaled and saved to {output_path}")

# Example usage:
input_image_path = "aimage_5_1.png"
output_image_path = "upscaled_image_zoe_phone.png"
target_width = 1080  # Desired width in pixels
target_height = 2340  # Desired height in pixels

upscale_image(input_image_path, output_image_path, target_width, target_height)
