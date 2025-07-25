from PIL import Image

# Open JFIF image
img = Image.open('spot_image.jfif')

# Save as standard JPEG
img.save('converted_image.jpg', 'JPEG')