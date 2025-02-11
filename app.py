import streamlit as st
from PIL import Image

# Imerys Brand Colors (Based on imerys.com)
IMERYS_BLUE = "#002F6C"
IMERYS_LIGHT_BLUE = "#4DBCE9"
IMERYS_GRAY = "#636466"
IMERYS_WHITE = "#FFFFFF"

def main():
    """Streamlit app with Imerys branding and French localization."""

    # --- Page Configuration ---
    st.set_page_config(
        page_title="Bienvenue - Ressources EHS Imerys",
        page_icon=":safety_vest:", # Or an Imerys logo favicon
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # --- Theme Customization ---
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {IMERYS_WHITE};
            color: {IMERYS_GRAY};
        }}
        .stTextInput > label {{
            color: {IMERYS_BLUE};
        }}
        .stTextInput > div > input {{
            border: 2px solid {IMERYS_LIGHT_BLUE};
            border-radius: 0.25rem;
            padding: 0.5rem;
            color: {IMERYS_GRAY};
        }}
        .stDownloadButton > button {{
            background-color: {IMERYS_BLUE};
            color: {IMERYS_WHITE};
            border: none;
            border-radius: 0.25rem;
            padding: 0.5rem 1rem;
            font-weight: bold;
        }}
        .stDownloadButton > button:hover {{
            background-color: {IMERYS_LIGHT_BLUE};
            color: {IMERYS_WHITE};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {IMERYS_BLUE};
        }}
         /* Style the sidebar */
        [data-testid="stSidebar"] {{
            background-color: {IMERYS_WHITE};
            color: {IMERYS_GRAY};
        }}

        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
            color: {IMERYS_BLUE};
        }}

        [data-testid="stSidebar"] a {{ /* Links in sidebar */
            color: {IMERYS_GRAY};
        }}

        [data-testid="stSidebar"] a:hover {{
            color: {IMERYS_BLUE};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Sidebar Navigation ---
    st.sidebar.header("Navigation")
    page = st.sidebar.radio(
        "Choisissez une page :",
        [
            "Bienvenue",
            "Générateur de code QR",
            "Induction de sécurité",
            "Générateur de permis de travail",
        ],
    )


    # --- Page Content ---
    if page == "Bienvenue":
        # --- Header and Logo ---
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                imerys_logo = Image.open("imerys_logo.png")
                st.image(imerys_logo, width=150) # Increased logo size slightly
            except FileNotFoundError:
                st.warning("Logo Imerys non trouvé. Placez 'imerys_logo.png' dans le même répertoire.")

        with col2:
            st.title("Bienvenue sur les ressources EHS Imerys - Site de Lixhe")
            st.markdown(
            f"<p style='color:{IMERYS_GRAY};'>Votre portail pour les informations essentielles en matière de santé et de sécurité.</p>",
            unsafe_allow_html=True, # Allows setting text color with HTML
            )
            st.markdown(
            f"<p style='color:{IMERYS_GRAY};'>Veuillez sélectionner une option dans le menu de navigation à gauche.</p>",
            unsafe_allow_html=True
            )

        # Add a relevant image, perhaps of the Lixhe site:
        try:
            site_image = Image.open("imerys_lixhe.jpg")  # Replace with the correct filename
            st.image(site_image, caption="Site de Lixhe", use_column_width=True)
        except FileNotFoundError:
            st.warning("Image du site de Lixhe non trouvée. Placez 'imerys_lixhe.jpg' dans le même répertoire.")



    elif page == "Générateur de code QR":
       st.header("Générateur de code QR")

       # ---App Content ---
       text = st.text_input("Entrez le texte ou l'URL:", "https://www.imerys.com")

       if text:
           #--- Code that generates the QR COde removed to prevent exceeding token limit ---
           st.write("Code QR généré") # Placeholder

    elif page == "Induction de sécurité":
        st.header("Induction de sécurité (Site de Lixhe)")
        st.write("Cette section présentera une induction de sécurité dynamique basée sur les directives d'Imerys Lixhe.")

    elif page == "Générateur de permis de travail":
        st.header("Générateur de permis de travail")
        st.write("Cette section vous permettra de générer un permis de travail pour le site de Lixhe.")


    # --- Footer ---
    st.markdown("---")
    st.markdown(
        f"<p style='text-align: center; color: {IMERYS_GRAY}; font-size: small;'>Imerys EHS - Lixhe</p>",
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
