import streamlit as st

def vigenere_encrypt(plaintext, key):
    """Encrypts the plaintext using the Vigenère cipher."""
    ciphertext = ""
    key = key.lower()
    key_length = len(key)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Decrypts the ciphertext using the Vigenère cipher."""
    plaintext = ""
    key = key.lower()
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext

# Streamlit UI
st.title("Vigenère Cipher App")

st.sidebar.header("Choose Operation")
operation = st.sidebar.radio("Select an operation:", ("Encrypt", "Decrypt"))

st.sidebar.header("Input Text and Key")
input_text = st.sidebar.text_area("Enter the text:", "")
key = st.sidebar.text_input("Enter the key:", "")

if st.sidebar.button("Perform Operation"):
    if not input_text or not key:
        st.error("Both text and key are required!")
    else:
        if operation == "Encrypt":
            result = vigenere_encrypt(input_text, key)
            st.success("Text encrypted successfully!")
            st.write("### Encrypted Text:")
            st.code(result, language="")
        elif operation == "Decrypt":
            result = vigenere_decrypt(input_text, key)
            st.success("Text decrypted successfully!")
            st.write("### Decrypted Text:")
            st.code(result, language="")

# Styling the UI
st.markdown(
    """
    <style>
    .stSidebar {
        background-color: #f7f7f9;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
