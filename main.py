import base64
from PIL import Image

def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read())
    return encoded_image

def decode_image(encoded_image, output_path):
    decoded_image = base64.b64decode(encoded_image)
    with open(output_path, "wb") as img_file:
        img_file.write(decoded_image)

def save_encoded_string(encoded_image, output_file):
    with open(output_file, "w") as f:
        f.write(encoded_image.decode())

def load_encoded_string(input_file):
    with open(input_file, "r") as f:
        encoded_image = f.read().encode()
    return encoded_image

def main():
    while True:
        print("Choose an option:")
        print("1. Encode image")
        print("2. Decode image")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            image_path = input("Enter the path of the image to encode: ")
            encoded_image = encode_image(image_path)
            print("Encoded image:")
            print(encoded_image)
            output_file = input("Enter the name of the file to save the encoded string: ")
            save_encoded_string(encoded_image, output_file)
            print(f"Encoded string saved to {output_file}")

        elif choice == "2":
            input_file = input("Enter the path of the file containing the encoded string: ")
            encoded_image = load_encoded_string(input_file)
            output_path = input("Enter the path to save the decoded image (including the extension): ")
            decode_image(encoded_image, f"{output_path}.jpg")
            print(f"Decoded image saved to {output_path}.jpg")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
