import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Imerys Brand Colors (Adapt to official Imerys chart - Based on imerys.com)
IMERYS_BLUE = "#002F6C"  # Primary Blue (Darker Blue from the Logo and Header)
IMERYS_LIGHT_BLUE = "#4DBCE9" # Light Blue (Used in Highlights and Accents)
IMERYS_GRAY = "#636466"  # Dark Gray (Body text, footer)
IMERYS_WHITE = "#FFFFFF" # White (Backgrounds, Text)


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
    """Streamlit app for QR code generation with Imerys branding."""

    # --- Page Configuration ---
    st.set_page_config(
        page_title="Imerys EHS QR Code Generator",
        page_icon=":barcode:",  # Use a barcode icon or Imerys logo
        layout="centered",
        initial_sidebar_state="collapsed",  # Optionally collapse the sidebar
    )

    # --- Theme Customization ---
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {IMERYS_WHITE}; /* White background for maximum readability */
            color: {IMERYS_GRAY}; /* Default text color is dark gray for good contrast */
        }}
        .stTextInput > label {{
            color: {IMERYS_BLUE}; /* Input label is Imerys Blue */
        }}
        .stTextInput > div > input {{
            border: 2px solid {IMERYS_LIGHT_BLUE}; /* Input border is light blue */
            border-radius: 0.25rem;
            padding: 0.5rem;
            color: {IMERYS_GRAY}; /* Input text is dark gray */
        }}

        .stDownloadButton > button {{
            background-color: {IMERYS_BLUE}; /* Button background is Imerys Blue */
            color: {IMERYS_WHITE}; /* Button text is white for maximum contrast */
            border: none;
            border-radius: 0.25rem;
            padding: 0.5rem 1rem;
            font-weight: bold; /* Make the button text bolder */
        }}
        .stDownloadButton > button:hover {{
            background-color: {IMERYS_LIGHT_BLUE}; /* Hover state uses light blue */
            color: {IMERYS_WHITE};
        }}
        h1 {{
            color: {IMERYS_BLUE}; /* Main heading is Imerys Blue */
        }}
        h2, h3, h4, h5, h6 {{
            color: {IMERYS_BLUE}; /* Subheadings are also Imerys Blue */
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


    # --- Header and Logo ---
    col1, col2 = st.columns([1, 3])  # Adjust column widths as needed
    with col1:
        # Replace "imerys_logo.png" with the actual path to the Imerys logo
        try:
            imerys_logo = Image.open("imerys_logo.png")
            st.image(imerys_logo, width=100) # Adjust width as needed
        except FileNotFoundError:
            st.warning("Imerys logo not found. Place 'imerys_logo.png' in the same directory.")
            pass # Handle the case where the logo file is missing

    with col2:
        st.title("Imerys EHS QR Code Generator")

    # --- App Content ---
    text = st.text_input("Enter text or URL:", "https://www.imerys.com")

    if text:
        qr_image = generate_qr_code(text)

        # Convert PIL Image to bytes for display
        img_buffer = BytesIO()
        qr_image.save(img_buffer, format="PNG")
        img_bytes = img_buffer.getvalue()

        # Display the QR code using bytes data
        st.image(img_bytes, caption="Generated QR Code", use_column_width=True)

        # Add a download button
        img_buffer_download = BytesIO()  # Use a separate buffer for the download to avoid conflicts
        qr_image.save(img_buffer_download, format="PNG")
        img_bytes_download = img_buffer_download.getvalue()

        st.download_button(
            label="Download QR Code",
            data=img_bytes_download,
            file_name="qr_code.png",
            mime="image/png",
        )

    # --- Footer ---
    st.markdown("---")  # Add a visual separator
    st.markdown(
        f"<p style='text-align: center; color: {IMERYS_GRAY}; font-size: small;'>Imerys EHS - Lixhe</p>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
