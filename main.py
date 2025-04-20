import streamlit as st
from cryptography.fernet import Fernet

# Set page config
st.set_page_config(page_title="Encryption & Decryption App", page_icon="🔐", layout="centered")

# App title
st.title("🔐 Encryption & Decryption App")

# Generate key if not in session
if "key" not in st.session_state:
    st.session_state.key = Fernet.generate_key().decode()

# Sidebar
st.sidebar.title("🔑 Encryption Key")
generate_key = st.sidebar.button("Generate New Key")
if generate_key:
    st.session_state.key = Fernet.generate_key().decode()

st.sidebar.code(st.session_state.key)
key_input = st.sidebar.text_input("Or Paste Your Own Key", value=st.session_state.key)

# Select action
option = st.selectbox("🔄 Select Action", ["Encrypt", "Decrypt"])

# User input
user_input = st.text_area("📝 Enter Your Text")

# Encryption/Decryption Logic
def encrypt_message(message, key):
    f = Fernet(key.encode())
    return f.encrypt(message.encode()).decode()

def decrypt_message(token, key):
    try:
        f = Fernet(key.encode())
        return f.decrypt(token.encode()).decode()
    except Exception as e:
        return f"❌ Error: {e}"

# Output
if st.button("🚀 Submit"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        if option == "Encrypt":
            encrypted = encrypt_message(user_input, key_input)
            st.success("🔒 Encrypted Text:")
            st.code(encrypted)
        elif option == "Decrypt":
            decrypted = decrypt_message(user_input, key_input)
            st.success("🔓 Decrypted Text:")
            st.code(decrypted)
