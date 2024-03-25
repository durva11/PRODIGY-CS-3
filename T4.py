import cv2
import numpy as np

# Function to encrypt the image
def encrypt_image(image, key):
    encrypted_image = cv2.add(image, key)  # Example: Adding a constant key to each pixel
    return encrypted_image

# Function to decrypt the image
def decrypt_image(encrypted_image, key):
    decrypted_image = cv2.subtract(encrypted_image, key)  # Example: Subtracting the same constant key
    return decrypted_image

# Main function
def main():
    # Load the image
    image = cv2.imread(r'C:\Users\Durva Shelke\Downloads\What Is The Nickname Of Your Soul_.jpg')

    # Choose a key for encryption
    key =70  # Example key value

    # Encrypt the image
    encrypted_image = encrypt_image(image, key)

    # Save the encrypted image
    cv2.imwrite(r'C:\Users\Durva Shelke\Downloads\encrypted_image.jpg', encrypted_image)

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)

    # Save the decrypted image
    cv2.imwrite(r'C:\Users\Durva Shelke\Downloads\decrypted_image.jpg', decrypted_image)

    print("Encryption and decryption completed successfully.")

if __name__ == "__main__":
    main()
