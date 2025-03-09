import streamlit as st
import re
import time
import random
from streamlit_extras.stylable_container import stylable_container

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")
    
    # Upper and lowercase check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("🟠 Use both uppercase and lowercase letters.")
    
    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("🟡 Include at least one digit.")
    
    # Special character check
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("🟢 Include at least one special character (@, $, !, %, *, ?, &).")
    
    # Strength classification
    if strength >= 4:
        return "🔥 Strong", "green", feedback, 100
    elif strength >= 2:
        return "⚠️ Moderate", "orange", feedback, 60
    else:
        return "❌ Weak", "red", feedback, 30

# Streamlit UI
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")
st.title("🔐 Innovative Password Strength Checker")
st.markdown("### Check your password's strength with real-time feedback!")

password = st.text_input("Enter your password:", type="password")

# Suggest a strong password below input field
st.markdown("**Suggested Strong Password:** `P@ssw0rd123!` (Customize it!)")

if st.button("Check Password Strength"):
    if password:
        with st.spinner("Analyzing password strength..."):
            time.sleep(1.5)
        
        strength, color, feedback, progress = check_password_strength(password)
        
        st.markdown(f"<h3 style='color:{color}; text-align:center'>{strength}</h3>", unsafe_allow_html=True)
        
        # Progress bar animation
        st.progress(progress)
        
        # Confetti effect for strong passwords
        if strength == "🔥 Strong":
            with stylable_container("confetti", css_styles="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999; pointer-events: none;"):
                for _ in range(10):
                    x_pos = random.randint(10, 90)
                    y_pos = random.randint(10, 90)
                    st.markdown(f'<div style="position:absolute; top:{y_pos}%; left:{x_pos}%; font-size:24px;">🎉</div>', unsafe_allow_html=True)
        
        if feedback:
            st.write("### Suggestions:")
            for tip in feedback:
                st.markdown(f"- {tip}")
    else:
        st.warning("Please enter a password to check its strength.")
