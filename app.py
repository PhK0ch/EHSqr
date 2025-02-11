import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
import smtplib
from email.mime.text import MIMEText

# Imerys Brand Colors (Based on imerys.com, accessibility-adjusted)
IMERYS_BLUE = "#002F6C"
IMERYS_LIGHT_BLUE = "#4DBCE9"
IMERYS_GRAY = "#4A4A4A"
IMERYS_WHITE = "#FFFFFF"
IMERYS_OFF_WHITE = "#F9F9F9"

# --- Quiz Questions and Answers ---
quiz_questions = [
    {
        "question": "L'accès au site est:",
        "options": ["Libre à tous", "Strictement réservé aux personnes autorisées", "Autorisé avec badge uniquement"],
        "answer_index": 1,
    },
    {
        "question": "Est-il permis de fumer partout sur le site?",
        "options": ["Oui", "Non, seulement dans les zones fumeurs", "Non, c'est totalement interdit"],
        "answer_index": 1,
    },
    {
        "question": "Quel est le rôle du CPPT?",
        "options": ["Gérer les finances de l'entreprise", "Donner des avis sur la politique de bien-être des travailleurs", "Organiser les événements sociaux"],
        "answer_index": 1,
    },
    {
        "question": "Les SERIOUS 7 sont:",
        "options": ["7 règles de sécurité non importantes", "7 règles primordiales de sécurité", "7 options de restauration sur le site"],
        "answer_index": 1,
    },
    {
        "question": "Que signifie LOTOTO (S03)?",
        "options": ["Lock-out Tag-out Try-out", "Leave Out, Tag-Out, Turn-Over", "Load Out, Transport, Offload, Test, Operate"],
        "answer_index": 0,
    },
    {
        "question": "Qui est autorisé à effectuer des tâches électriques (S04)?",
        "options": ["Toute personne formée", "Seule une personne qualifiée et habilitée", "Les électriciens uniquement"],
        "answer_index": 1,
    },
    {
        "question": "Concernant les équipements mobiles (S11), qu'est-ce qui est important?",
        "options": ["Avoir son permis de conduire", "Avoir l'autorisation de compétence de l'Employeur", "Avoir des chaussures de sécurité"],
        "answer_index": 1,
    },
    {
        "question": "À partir de quelle hauteur le travail est-il considéré 'en hauteur' (S13)?",
        "options": ["Plus de 1 mètre", "Plus de 2 mètres", "Plus de 3 mètres"],
        "answer_index": 1,
    },
    {
        "question": "Que faire face à un produit ou substance dangereuse?",
        "options": ["Ignorer si l'étiquette est illisible", "Prendre connaissance des consignes de sécurité sur la Fiche DSS", "Utiliser sans protection si on est pressé"],
        "answer_index": 1,
    },
    {
        "question": "Le Take 5 est un outil pour:",
        "options": ["Faire une pause de 5 minutes", "Réfléchir aux actions avant de réaliser une tâche", "Organiser une réunion de 5 personnes"],
        "answer_index": 1,
    }
]


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


def send_email(name, company, email, score, total_questions, recipient_email):
    """Sends an email with quiz results."""
    sender_email = "your_sender_email@example.com"  # Replace with your sender email
    sender_password = "your_sender_password"  # Replace with your sender email password or app password

    message = f"""
    Nom: {name}
    Entreprise: {company}
    Email: {email}
    Score du quiz de sécurité: {score}/{total_questions}
    """

    msg = MIMEText(message)
    msg['Subject'] = "Résultats du Quiz d'Induction de Sécurité - Imerys Lixhe"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Or your SMTP server
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        return True, None  # Success, no error
    except Exception as e:
        return False, str(e)  # Failure, return error message


def main():
    """Streamlit app with Imerys branding and French localization."""

    # --- Page Configuration ---
    st.set_page_config(
        page_title="Bienvenue - Ressources EHS Imerys",
        page_icon=":safety_vest:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # --- Theme Customization ---
    st.markdown(
        f"""
        <style>
        /* General app background and text */
        .stApp {{
            background-color: {IMERYS_OFF_WHITE};
            color: {IMERYS_GRAY};
        }}
        [data-testid="stHeader"] {{
            background-color: {IMERYS_BLUE};
            color: {IMERYS_WHITE};
        }}
        [data-testid="stSidebar"] {{
            background-color: {IMERYS_BLUE};
            color: {IMERYS_WHITE};
        }}
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
            color: {IMERYS_WHITE};
        }}
        [data-testid="stSidebar"] a {{
            color: {IMERYS_LIGHT_BLUE};
        }}
        [data-testid="stSidebar"] a:hover {{
            color: {IMERYS_WHITE};
        }}
        [data-testid="stSidebar"] [aria-current="true"] {{
            color: {IMERYS_WHITE};
            background-color: rgba(255, 255, 255, 0.2);
        }}
        .stTextInput > label {{
            color: {IMERYS_BLUE};
        }}
        .stTextInput > div > input {{
            border: 2px solid {IMERYS_LIGHT_BLUE};
            border-radius: 0.25rem;
            padding: 0.5rem;
            color: {IMERYS_GRAY};
            background-color: {IMERYS_WHITE};
        }}
        .stNumberInput > label {{
            color: {IMERYS_BLUE};
        }}
       .stNumberInput > div > input {{
            border: 2px solid {IMERYS_LIGHT_BLUE};
            border-radius: 0.25rem;
            padding: 0.5rem;
            color: {IMERYS_GRAY};
            background-color: {IMERYS_WHITE};
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
        # --- Welcome Page ---
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                imerys_logo = Image.open("imerys_logo.png")
                st.image(imerys_logo, width=150)
            except FileNotFoundError:
                st.warning("Logo Imerys non trouvé. Placez 'imerys_logo.png' dans le même répertoire.")

        with col2:
            st.title("Bienvenue sur les ressources EHS Imerys - Site de Lixhe")
            st.markdown(f"<p style='color:{IMERYS_GRAY};'>Votre portail pour les informations essentielles en matière de santé et de sécurité.</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:{IMERYS_GRAY};'>Veuillez sélectionner une option dans le menu de navigation à gauche.</p>", unsafe_allow_html=True)

        try:
            site_image = Image.open("imerys_lixhe.jpg")
            st.image(site_image, caption="Site de Lixhe", use_column_width=True)
        except FileNotFoundError:
            st.warning("Image du site non trouvée. Placez 'imerys_lixhe.jpg' dans le même répertoire.")

    elif page == "Générateur de code QR":
        # --- QR Code Generator Page ---
        st.header("Générateur de code QR")
        text = st.text_input("Entrez le texte ou l'URL:", "https://www.imerys.com")
        if text:
            qr_image = generate_qr_code(text)

            # Convert PIL Image to bytes for display
            img_buffer = BytesIO()
            qr_image.save(img_buffer, format="PNG")
            img_bytes = img_buffer.getvalue()

            # Display the QR code using bytes data
            st.image(img_bytes, caption="Code QR généré", use_column_width=True)

            # Add a download button
            img_buffer_download = BytesIO()  # Use a separate buffer for the download to avoid conflicts
            qr_image.save(img_buffer_download, format="PNG")
            img_bytes_download = img_buffer_download.getvalue()

            st.download_button(
                label="Télécharger le code QR",
                data=img_bytes_download,
                file_name="qr_code.png",
                mime="image/png",
            )

    elif page == "Induction de sécurité":
        # --- Safety Induction Page ---
        st.header("Induction de sécurité - Site de Lixhe")
        st.subheader("Induction de Sécurité Interactive")
        st.write("Veuillez remplir le formulaire ci-dessous, suivre les sections d'induction, et compléter le quiz à la fin.")

        # --- User Information Form (FIRST STEP) ---
        with st.form("user_info_form"):
            st.subheader("Informations Personnelles")
            name = st.text_input("Nom *", key="name_input")  # Added key for state persistence
            company = st.text_input("Entreprise *", key="company_input")  # Added key for state persistence
            email = st.text_input("Adresse e-mail *", key="email_input")  # Added key for state persistence
            user_info_submitted = st.form_submit_button("Valider les informations personnelles")

        if user_info_submitted:  # Only proceed if user info is submitted
            if not name or not company or not email:
                st.error("Veuillez remplir tous les champs obligatoires.")
            else:
                st.session_state['user_info_submitted'] = True  # Track form submission in session state
        elif 'user_info_submitted' not in st.session_state:
            st.session_state['user_info_submitted'] = False  # Initialize session state

        if st.session_state['user_info_submitted']:  # Show induction content and quiz only after form submission

            progress_bar = st.progress(0)  # Progress bar initialization
            total_sections = 9  # Number of induction sections + Quiz
            section_percentage = 100 / total_sections
            progress_value = 0

            induction_section = st.radio(
                "Choisissez une section de l'induction :",
                [
                    "Introduction",
                    "L'accès au site",
                    "L'Environnement",
                    "La Sécurité d'Entreprise",
                    "Les SERIOUS 7",
                    "Produits et Substances Dangereuses",
                    "Take 5",
                    "Conclusion",
                    "Quiz de compréhension"  # Quiz is now a section
                ], index=0
            )

            if induction_section == "Introduction":
                st.subheader("Introduction")
                st.write("La santé et la sécurité sont l'une des valeurs essentielles chez Imerys.")
                st.write("Ce livret est destiné à toute personne entrant en fonction au sein d'Imerys Minéraux Belgique et ce peu importe le statut.")
                st.write("Employés Imerys, Etudiants, Sociétés extérieures.")
                st.write("*La sécurité, la santé et le bien-être n'ont pas de statut chez Imerys.*")
                st.write("La direction, Monsieur Dazza CEO, a rédigé une charte santé et sécurité afin de positionner la vision d'Imerys.")
                progress_value = section_percentage * 1
            elif induction_section == "L'accès au site":
                st.subheader("L'accès au site")
                st.write("L'accès au site est strictement réservé aux personnes autorisées :")
                st.write("- Soit en tant que qu'employé")
                st.write("- Soit en tant que visiteur (un accompagnement est obligatoire)")
                st.write("- Soit en tant que technicien (un accueil sécurité et environnement est obligatoire)")
                st.write("Aujourd'hui nous avons Cognibox (passeport sécurité)")
                st.write("Tout accès au site aussi bien pour un visiteur qu'un technicien nécessite un enregistrement.")
                st.write("- Cahier de présence aux entrées site (TC, bâtiment usine)")
                st.write("- Il est interdit de fumer dans les installations (Privilégiez les abris fumeurs)")
                try:
                    site_access_image = Image.open("site_access_image.png")  # Replace with actual image
                    st.image(site_access_image, caption="Accès au Site", use_column_width=True)
                except FileNotFoundError:
                    st.warning("Image d'accès au site non trouvée (site_access_image.png).")
                progress_value = section_percentage * 2
            elif induction_section == "L'Environnement":
                st.subheader("L'environnement")
                st.write("Depuis 2018, Imerys applique le tri sélectif de ses déchets afin de garantir au maximum leurs bonnes valorisations.")
                st.write("Il est demandé à chacun d'entre nous de s'impliquer en bon père de famille.")
                st.write("- Je place les déchets au bon endroits")
                st.write("- Je ne laisse pas des déchets traîner et ramasse ce qui traine (par oubli ou perte)")
                st.write("- Je nettoie mon emplacement lorsque je le quitte")
                st.subheader("La gestion des énergies")
                st.write("Par << Energie >>, il est sous-entendu toute consommation d'une ressource ayant une incidence sur l'Environnement lorsqu'elle est utilisée.")
                st.write("Chaque action, tâche qui nécessite/utilise de l'énergie donne lieu à un aspect environnemental qui peut avoir un impact sur l'Environnement Relation de cause à effet.")
                st.write("Exemples :")
                st.write("- Ne pas faire fonctionner la climatisation les fenêtres ouvertes")
                st.write("- Couper les moteurs d'une machine qui ne fonctionne pas")
                st.write("- Éteindre les lumières lorsqu'elles ne sont pas utilisées")
                st.write("- Signaler toute fuite d'eau")
                st.write("- Couper son chauffage en quittant son lieu de travail")
                try:
                    environment_image = Image.open("environment_image.png")  # Replace with actual image
                    st.image(environment_image, caption="Environnement", use_column_width=True)
                except FileNotFoundError:
                    st.warning("Image d'environnement non trouvée (environment_image.png).")
                progress_value = section_percentage * 3
            elif induction_section == "La Sécurité d'Entreprise":
                st.subheader("La sécurité d'une entreprise est régie par différents organes")
                st.write("Le CPPT: Comités pour la prévention et la protection au travail. Émet des avis et des propositions sur la politique du Bien-être des travailleurs lors de l'exécution de leur travail, sur le plan global de prévention et le plan annuel d'actions.")
                st.write("Le CE : Comité d'entreprise. Émet des avis sur les orientations stratégiques, l'organisation du temps de travail, les besoins en formations, la politique sociale ainsi que les conditions de travail.")
                st.write("Le SIPP: Service Interne pour la Prévention et la Protection au travail. Le service interne a pour mission générale d'assister l'employeur, les membres de la ligne hiérarchique et les travailleurs de l'entreprise dans l'application de la réglementation relative au bien-être des travailleurs mais également dans la réalisation des mesures et activités de prévention.")
                st.write("Le SEPP : Service externe pour la prévention et la protection au travail. Représenté chez Imerys Lixhe par le CESI. Assiste l'entreprise pour des missions pour lesquelles il n'en a pas les compétences en matière de santé et de bien-être. (surveillance santé, hygiène, ergonomie...)")
                try:
                    safety_org_image = Image.open("safety_org_image.png")  # Replace with actual image
                    st.image(safety_org_image, caption="Organes de Sécurité", use_column_width=True)
                except FileNotFoundError:
                    st.warning("Image des organes de sécurité non trouvée (safety_org_image.png).")
                progress_value = section_percentage * 4
            elif induction_section == "Les SERIOUS 7":
                st.subheader("Règles primordiales d'Imerys - Les SERIOUS 7")
                # --- (SERIOUS 7 content - unchanged) ---
                serious_7_subsection = st.selectbox("Plus de détails sur les Serious 7:", ["Aucun", "S03 - LOTOTO", "S04 - Sécurité électrique", "S10 - Protection machine", "S11 - Équipement mobile", "S13 - Travail en hauteur", "S14 - Sécurisation terrain", "S19 - Chariots élévateurs"])
                if serious_7_subsection == "S03 - LOTOTO":
                    st.subheader("S03 - Lock-out Tag-out Try-out (LOTOTO)")
                    # --- (LOTOTO content - unchanged) ---
                # --- (rest of SERIOUS 7 subsections - unchanged) ---
                progress_value = section_percentage * 5

            elif induction_section == "Produits et Substances Dangereuses":
                st.subheader("Les produits et substances dangereuses")
                # --- (Produits et Substances Dangereuses content - unchanged) ---
                try:
                    danger_symbols_image = Image.open("danger_symbols_image.png")  # Replace with actual image
                    st.image(danger_symbols_image, caption="Pictogrammes de Danger", use_column_width=True)
                except FileNotFoundError:
                    st.warning("Image des pictogrammes de danger non trouvée (danger_symbols_image.png).")
                progress_value = section_percentage * 6

            elif induction_section == "Take 5":
                st.subheader("Take 5")
                # --- (Take 5 content - unchanged) ---
                try:
                    take5_image = Image.open("take5_image.png")  # Replace with actual image
                    st.image(take5_image, caption="Take 5", use_column_width=True)
                except FileNotFoundError:
                    st.warning("Image Take 5 non trouvée (take5_image.png).")
                progress_value = section_percentage * 7

            elif induction_section == "Conclusion":
                st.subheader("Conclusion")
                # --- (Conclusion content - unchanged) ---
                progress_value = section_percentage * 8

            elif induction_section == "Quiz de compréhension": # Quiz section
                progress_value = section_percentage * 9
                st.markdown("---")
                st.subheader("Quiz de compréhension")
                st.write("Répondez aux questions suivantes pour tester vos connaissances.")

                quiz_score = 0
                user_answers = []

                for i, question_data in enumerate(quiz_questions):
                    question_number = i + 1
                    st.markdown(f"**Question {question_number}:** {question_data['question']}")
                    user_answer_index = st.radio(f" ", question_data["options"], index=None, key=f"q{i}")  # Unique key for each radio
                    user_answers.append(user_answer_index)  # Store answer index

                if any(answer is not None for answer in user_answers):  # Check if any question has been answered
                    for i, question_data in enumerate(quiz_questions):
                        if user_answers[i] == question_data["answer_index"]:
                            quiz_score += 1

                    st.markdown("---")
                    st.subheader("Résultats du Quiz")
                    st.write(f"Votre score: **{quiz_score}/{len(quiz_questions)}**")

                    if quiz_score == len(quiz_questions):
                        st.success("Félicitations ! Vous avez réussi le quiz.")
                    elif quiz_score >= len(quiz_questions) * 0.7:  # Example passing score (70%)
                        st.warning("Vous avez presque réussi. Veuillez revoir les sections pour améliorer votre score.")
                    else:
                        st.error("Vous n'avez pas réussi le quiz. Veuillez revoir attentivement l'induction de sécurité.")

                    if st.button("Envoyer les résultats par email", key="send_email_button", disabled=False):  # Button to send email, enabled after quiz
                        recipient_email = email  # Use email from the form
                        success, error_message = send_email(name, company, email, quiz_score, len(quiz_questions), recipient_email)
                        if success:
                            st.success("Résultats envoyés par email avec succès!")
                        else:
                            st.error(f"Erreur lors de l'envoi de l'email: {error_message}")
                            st.error("Veuillez vérifier votre connexion internet et les informations de messagerie.")

                        # Security Warning - VERY IMPORTANT (remains unchanged)
                        st.warning("⚠️ **Important: Les informations d'identification de l'email (sender_email, sender_password) sont actuellement codées en dur dans le code.**  Pour une application réelle, il est **crucial** de stocker ces informations de manière sécurisée (variables d'environnement, gestion des secrets) et d'utiliser un service d'envoi d'emails robuste et sécurisé.  **Ne jamais coder en dur des informations sensibles dans une application de production.**")

            progress_bar.progress(int(progress_value))  # Update progress bar


    elif page == "Générateur de permis de travail":
        # --- Work Permit Generator Page (Placeholder - remains unchanged) ---
        st.header("Générateur de permis de travail")
        st.write("Section en construction. Veuillez revenir plus tard.")

    # --- Footer (remains unchanged) ---
    st.markdown("---")
    st.markdown(
        f"<p style='text-align: center; color: {IMERYS_GRAY}; font-size: small;'>Imerys EHS - Lixhe</p>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
