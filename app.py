import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

def generate_qr_code(text):
  """Generates a QR code image from the given text."""
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr.add_data(text)
  qr.make(fit=True)

  img = qr.make_image(fill_color="black", back_color="white")
  return img

def main():
  """Streamlit app for QR code generation."""
  st.title("Simple QR Code Generator")

  text = st.text_input("Enter text or URL:", "https://www.streamlit.io")

  if text:
    qr_image = generate_qr_code(text)

    # Display the QR code
    st.image(qr_image, caption="Generated QR Code", use_column_width=True)

    # Add a download button
    img_buffer = BytesIO()
    qr_image.save(img_buffer, format="PNG")  # Save the PIL image to the buffer
    img_bytes = img_buffer.getvalue()

    st.download_button(
        label="Download QR Code",
        data=img_bytes,
        file_name="qr_code.png",
        mime="image/png",
    )

if __name__ == "__main__":
  main()