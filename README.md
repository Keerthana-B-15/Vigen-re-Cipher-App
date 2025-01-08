# Vigenère Cipher App

A modern web application to encrypt and decrypt text using the **Vigenère Cipher**, built with Python and Streamlit.

![image](https://github.com/user-attachments/assets/b2b69298-4c21-44a1-8c0b-4bf8412ffe3c)
![image](https://github.com/user-attachments/assets/8fe2de78-083e-4487-8ea5-d84c981f08ec)





## 🚀 Features
- **Encrypt Text**: Securely encrypt any text using the Vigenère cipher.
- **Decrypt Text**: Decrypt previously encrypted text to reveal the original message.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.


## 🛠️ How It Works
The Vigenère cipher is a method of encrypting text using a series of Caesar ciphers based on the letters of a keyword. Each letter in the plaintext is shifted by a number of places determined by the corresponding letter in the key.

### Example
#### Encryption:
- Plaintext: `HELLO`
- Key: `KEY`
- Encrypted Text: `RIJVS`

#### Decryption:
- Ciphertext: `RIJVS`
- Key: `KEY`
- Original Text: `HELLO`


## 🖥️ Built With
- **Python**: Core logic for encryption and decryption.
- **Streamlit**: For building an interactive user interface.


## 📂 File Structure
```plaintext
.
├── app.py                 # Main application file
├── requirements.txt       # Dependencies for the app
└── README.md              # Project documentation
```

## 🚀 Deployment
1. Clone the repository:
   ```bash
   [git clone https://github.com/yourusername/vigenere-cipher-app.git](https://github.com/Keerthana-B-15/Vigen-re-Cipher-App)
   cd vigenere-cipher-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   streamlit run app.py
   ```

4. Deploy on [Streamlit Community Cloud](https://share.streamlit.io/):
   - Push your code to GitHub.
   - Deploy the app by connecting your GitHub repository to Streamlit.

## 💡 Why This Was Built
The Vigenère cipher is a classic cryptographic technique often introduced in cryptography courses. This app provides an interactive way to explore how the cipher works and understand its limitations, such as susceptibility to frequency analysis attacks when the key length is short.

The project was designed to:
- Simplify understanding of the Vigenère cipher.
- Provide a hands-on tool for students and cryptography enthusiasts.
- Demonstrate how modern UI tools like Streamlit can be used for educational purposes.

## 🎓 Concept Overview
### Vigenère Cipher
- **Encryption**: Shifts each letter of the plaintext by a number of positions defined by the corresponding letter in the key.
- **Decryption**: Reverses the process to retrieve the original text.

**Key Points**:
1. Letters wrap around the alphabet (e.g., `Z` shifted by 1 becomes `A`).
2. Non-alphabetic characters remain unchanged.
3. Case sensitivity is preserved.

## 🤝 Contributing
Contributions are welcome! If you'd like to enhance the app, feel free to:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.


### 🛠 Future Enhancements
- Add support for advanced cryptographic techniques.
- Include historical context and applications of the Vigenère cipher.
- Add more styling and themes to the UI.


Give it a try and explore the beauty of cryptography! 🔐✨

### Why This Was Built
1. **Educational Tool**: To help users understand how the Vigenère cipher works by providing an interactive platform.
2. **Modern Technology Showcase**: Demonstrates how Streamlit can simplify building web apps with minimal effort.
3. **Fun with Cryptography**: Encourages experimentation with encryption and decryption, making cryptography accessible to all.
