from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path, 'r')
    pixels = image.load()
    width, height = image.size

    for py in range(height):
        for px in range(width):
            pixels[px, py] = pixels[px, py] ^ key

    image.save("encrypted_image.png")
    image.show()

def decrypt_image(image_path, key):
    image = Image.open(image_path, 'r')
    pixels = image.load()
    width, height = image.size

    for py in range(height):
        for px in range(width):
            pixels[px, py] = pixels[px, py] ^ key

    image.save("decrypted_image.png")
    image.show()

if __name__ == "__main__":
    image_path = input("Enter path of image: ")
    key = int(input("Enter encryption key: "))

    encrypt_image(image_path, key=None)
    decrypt_image("encrypted_image.png", key=None)