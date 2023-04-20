from PIL import Image

# Load the two images
img1 = Image.open('file1.png')
img2 = Image.open('file2.png')

# Get the RGB pixel data for each image
pixels1 = img1.load()
pixels2 = img2.load()

# Create a new image to store the XOR result
xored_image = Image.new(img1.mode, img1.size)

# Get the pixel data for the XOR image
xored_pixels = xored_image.load()

# Iterate over each pixel in the images and XOR the RGB values
for x in range(img1.width):
    for y in range(img1.height):
        r1, g1, b1 = pixels1[x, y]
        r2, g2, b2 = pixels2[x, y]
        xored_pixels[x, y] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)
        
# Save the XOR image to a new file
xored_image.save('xored.png')