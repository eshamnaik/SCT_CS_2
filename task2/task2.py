from PIL import Image
import random

def swap_pixels(image):
    pixels = list(image.getdata())
    width, height = image.size

    # Randomly swap a few pixels
    for _ in range(min(100, len(pixels) // 2)):
        idx1 = random.randint(0, len(pixels) - 1)
        idx2 = random.randint(0, len(pixels) - 1)
        pixels[idx1], pixels[idx2] = pixels[idx2], pixels[idx1]

    new_image = Image.new(image.mode, image.size)
    new_image.putdata(pixels)
    return new_image

def apply_math_operation(image, operation, value):
    pixels = list(image.getdata())
    new_pixels = []

    for pixel in pixels:
        if operation == 'add':
            new_pixel = tuple(min(255, max(0, p + value)) for p in pixel)
        elif operation == 'subtract':
            new_pixel = tuple(min(255, max(0, p - value)) for p in pixel)
        else:
            raise ValueError("Invalid operation. Use 'add' or 'subtract'.")
        
        new_pixels.append(new_pixel)

    new_image = Image.new(image.mode, image.size)
    new_image.putdata(new_pixels)
    return new_image

def main():
    print("Welcome to the Image Encryption Tool!")
    input_image_path = input("Enter the path to the image: ")
    
    # Open the image
    try:
        image = Image.open(input_image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    print("Choose an operation:")
    print("1. Swap pixels")
    print("2. Add value to each pixel")
    print("3. Subtract value from each pixel")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        encrypted_image = swap_pixels(image)
        encrypted_image.show()
        encrypted_image.save("encrypted_swapped.png")
        print("Encrypted image with swapped pixels saved as 'encrypted_swapped.png'.")

    elif choice in ['2', '3']:
        value = int(input("Enter the value to add/subtract (0-255): "))
        operation = 'add' if choice == '2' else 'subtract'
        encrypted_image = apply_math_operation(image, operation, value)
        encrypted_image.show()
        encrypted_image.save(f"encrypted_math_{operation}.png")
        print(f"Encrypted image with {operation} operation saved as 'encrypted_math_{operation}.png'.")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
