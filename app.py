import streamlit as st
import requests
from PIL import Image
import io

# Set the Google Colab API URL (Replace with updated ngrok link)
API_URL = "https://7fdd-34-169-102-193.ngrok-free.app/predict"

# Streamlit UI
st.set_page_config(page_title="Deepfake Image Detector", page_icon="🕵️", layout="centered")
st.title("🕵️‍♂️ Deepfake Image Detector 🔍")
st.write("Upload an image to check if it's **REAL** or **FAKE**.")

# File Uploader
uploaded_file = st.file_uploader("📤 Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Image", use_column_width=True)

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    # Analyze Button
    if st.button("🔍 Analyze Image"):
        with st.spinner("🧠 Analyzing... Please wait."):
            try:
                # Send request to API for all images
                response = requests.post(API_URL, files={"file": img_bytes})
                if response.status_code == 200:
                    result = response.json()
                    label = result["label"]
                    confidence = result["confidence"]
                else:
                    st.error(f"🚨 Server Error: {response.status_code} - {response.text}")
                    label = None

                # Display Result
                if label:
                    st.subheader("Confidence Score")
                    st.progress(confidence)

                    if label == "FAKE ❌":
                        st.markdown("❌ **Fake Image Detected!**", unsafe_allow_html=True)
                    else:
                        st.markdown("✅ **Real Image Detected!**", unsafe_allow_html=True)

                    st.write(f"**Confidence:** {confidence:.2f}")

            except requests.exceptions.RequestException as e:
                st.error(f"🚨 API request failed: {e}")
