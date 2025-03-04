# re means regular expression, we can give numbers, small & capital letters & characters in password.
import re
import streamlit as st

# Page styling
st.set_page_config(
    page_title="🔐 Password Strength Checker", 
    page_icon="🔑", 
    layout="centered"
)

# Custom CSS for better UI
st.markdown(""" 
<style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a1a, #444);
        color: white;
        font-family: 'Arial', sans-serif;
    }

    /* Center aligning main content */
    .main { text-align: center; }

    /* Text input styling */
    .stTextInput {
        width: 60% !important;
        margin: auto;
        border-radius: 10px;
        border: 2px solid #ffcc00;
    }

    /* Button Styling */
    .stButton button {
        width: 50%;
        background-color: #007BFF;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px;
        transition: 0.3s ease-in-out;
    }

    .stButton button:hover {
        background-color: #ff4500;
        color: white;
        transform: scale(1.1);
    }

    /* Expander styling */
    .st-expander {
        background: #222;
        border-left: 5px solid #ffcc00;
        border-radius: 10px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Page Title and Description with Icons
st.title("🔐 Password Strength Generator")
st.write("🛡️ **Please Enter your password below to check its security level.**")

# Function to check password strength.
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ **Password should be at least 8 characters long.**")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔠 **Include both uppercase (A-Z) & lowercase (a-z) letters.**")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 **Include at least one number (0-9).**")

    if re.search(r"[!@*^#%$&_]", password):
        score += 1
    else:
        feedback.append("🔣 **Include at least one special character (!@*^#%$&_).**")

    # Display password strength result with icons
    if score == 4:
        st.success("✅ **Strong Password** - 🎉 Congratulations! Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback section
    if feedback:
        with st.expander("💡 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Password input field with icon
password = st.text_input("🔑 Please Enter Your Password", type="password", help="🔍 Ensure your password is strong.")

# Button Functionality
if st.button("🔍 Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ **Please enter a password first!**")
