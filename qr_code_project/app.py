import streamlit as st
import qrcode
from PIL import Image
import io

# Function to generate QR Code
def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    return img

# Function to convert image format
def get_image_bytes(img, format):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format=format)
    return img_byte_arr.getvalue()

# Streamlit UI
st.title("🔗 QR Code Generator")

# Input for the URL
link = st.text_input("Enter a link to generate a QR Code:", "")

if link:
    qr_image = generate_qr_code(link)
    
    # Convert QR image to bytes
    qr_image_bytes = get_image_bytes(qr_image, "PNG")  # Convert to bytes

    # Show QR Code
    st.image(qr_image_bytes, caption="Generated QR Code", use_container_width=True)  # Use bytes here

    # Provide download options
    st.write("📥 Download your QR Code:")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.download_button("PNG", data=get_image_bytes(qr_image, "PNG"), file_name="qr_code.png", mime="image/png")
    with col2:
        st.download_button("JPEG", data=get_image_bytes(qr_image, "JPEG"), file_name="qr_code.jpeg", mime="image/jpeg")
    with col3:
        st.download_button("PDF", data=get_image_bytes(qr_image, "PDF"), file_name="qr_code.pdf", mime="application/pdf")
 

st.markdown("---")
st.markdown("💡 Built with Streamlit & Python | Enhance this project with colors, logos & customization!")
