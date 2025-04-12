# 🔒 Encrypter / Decrypter

Encrypter is a simple Python GUI application that encrypts and decrypts files (images, PDFs, etc.) using an XOR-based algorithm. Built with Tkinter, it offers an easy-to-use interface where users input a key, select a file, and instantly encrypt or decrypt it. Whether you're looking to secure sensitive images or simply learn about basic encryption techniques, Encrypter is for you!

---

## Table of Contents

- [Features](#features-)
- [Requirements](#requirements-)
- [Installation](#installation-)
- [Usage](#usage-)
- [How It Works](#how-it-works-)
- [Customization](#customization-)

---

## Features ✨

- **Simple GUI:** A colorful and minimalistic design using Tkinter.
- **Easy Encryption/Decryption:** Toggle file security with a single key (XOR method).
- **Multi-format Support:** Works with common file types like JPEG, PNG, PDF, etc.
- **Lightweight & Fast:** Built in Python, perfect for quick encrypt/decrypt tasks.

---

## Requirements 🛠

- **Python 3.x**: Make sure you have Python 3 installed.
- **Tkinter:** Typically included with standard Python distributions.
  
No external libraries are required, making it easy and portable!

---

## Installation 💾

1. **Clone or Download the Repository**

   ```bash
   git clone https://github.com/yourusername/encrypter.git
   cd encrypter
   ```

2. **Run the Application**

   Simply execute the script:

   ```bash
   python encrypter.py
   ```

---

## Usage 🚀

1. **Launch the App:**  
   Run the `encrypter.py` file to open the GUI window.

2. **Enter the Encryption Key:**  
   Type your desired numeric key in the provided text box.  
   _Example Key: `123`_

3. **Select a File:**  
   Click on the "Enter Key" button. A file dialog will appear to choose your file.  
   Supported file types: JPEG, PNG, PDF, etc.

4. **Encryption/Decryption Process:**  
   The script will read the file, perform XOR encryption using your key, and then save the updated file automatically in place.  
   ➡️ You can run the process again with the same key to decrypt the file.

5. **Success Message:**  
   Once complete, if there's any error with the key or process, an error message with emojis will alert you. Enjoy your encrypted/decrypted file!

---

## How It Works 🔍

- **Key Input:**  
  Users must enter a numeric key which is used to perform an XOR operation on every byte of the selected file.

- **XOR Operation:**  
  The core encryption/decryption method is based on the XOR bitwise operator. This method provides a simple toggle where the same key is used to encrypt and decrypt.

- **File Handling:**  
  The file is read in binary mode, processed byte by byte, and then overwritten with the new bytearray which represents the encrypted or decrypted content.

---

## Customization 🎨

Feel free to modify the interface or the encryption logic to add more functionalities:
- **Interface Design:**  
  Customize the GUI elements (colors, fonts, window dimensions) as per your style.
- **Advanced Encryption:**  
  Extend the XOR algorithm or integrate other encryption methods for enhanced security.
- **Error Handling:**  
  Implement additional error messages or warnings for different file types and key validations.

---

Enjoy using the Encrypter! If you have any suggestions or contributions, feel free to create an issue or a pull request on GitHub. Happy encrypting! 🔐
