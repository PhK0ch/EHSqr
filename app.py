import streamlit as st
from PIL import Image

# Imerys Brand Colors (Based on imerys.com, accessibility-adjusted)
IMERYS_BLUE = "#002F6C"  # Primary Blue
IMERYS_LIGHT_BLUE = "#4DBCE9"
IMERYS_GRAY = "#4A4A4A"  # Darker Gray for better contrast
IMERYS_WHITE = "#FFFFFF"
IMERYS_OFF_WHITE = "#F9F9F9"  # Softer background alternative

def main():
    """Streamlit app with Imerys branding and French localization."""

    # --- Page Configuration ---
    st.set_page_config(
        page_title="Bienvenue - Ressources EHS Imerys",
        page_icon=":safety_vest:",  # Or an Imerys logo favicon
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

        /* Improve header contrast */
        [data-testid="stHeader"] {{
            background-color: {IMERYS_BLUE};
            color: {IMERYS_WHITE};
        }}

        /* Improved sidebar contrast */
        [data-testid="stSidebar"] {{
            background-color: {IMERYS_BLUE}; /* Sidebar now Blue */
            color: {IMERYS_WHITE}; /* White text on Blue */
        }}

        /* Style sidebar headings */
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
            color: {IMERYS_WHITE}; /* Sidebar headings are White */
        }}

        /* Style sidebar links */
        [data-testid="stSidebar"] a {{
            color: {IMERYS_LIGHT_BLUE}; /* Light Blue links */
        }}

        [data-testid="stSidebar"] a:hover {{
            color: {IMERYS_WHITE}; /* White on hover for better visibility */
        }}

        /* Active sidebar item */
        [data-testid="stSidebar"] [aria-current="true"] {{
            color: {IMERYS_WHITE};
            background-color: rgba(255, 255, 255, 0.2); /* Slightly transparent white */
        }}


        /* Input elements */
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

        /* Button elements */
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

        /* Header elements */
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
        # --- Header and Logo ---
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                imerys_logo = Image.open("imerys_logo.png")
                st.image(imerys_logo, width=150)  # Increased logo size slightly
            except FileNotFoundError:
                st.warning("Logo Imerys non trouvé. Placez 'imerys_logo.png' dans le même répertoire.")

        with col2:
            st.title("Bienvenue sur les ressources EHS Imerys - Site de Lixhe")
            st.markdown(
                f"<p style='color:{IMERYS_GRAY};'>Votre portail pour les informations essentielles en matière de santé et de sécurité.</p>",
                unsafe_allow_html=True,  # Allows setting text color with HTML
            )
            st.markdown(
                f"<p style='color:{IMERYS_GRAY};'>Veuillez sélectionner une option dans le menu de navigation à gauche.</p>",
                unsafe_allow_html=True,
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
           # --- QR Code Generation logic (place your code here if needed) ---
           st.write("Code QR généré") # Placeholder

    elif page == "Induction de sécurité":
        st.header("Induction de sécurité - Site de Lixhe")

        # --- Safety Induction Content ---
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
                "Conclusion"
            ]
        )

        if induction_section == "Introduction":
            st.subheader("Bienvenue chez Imerys Minéraux Belgique - Site de Lixhe")
            st.write("La santé et la sécurité sont l'une des valeurs essentielles chez Imerys.")
            st.write("Ce livret est destiné à toute personne entrant en fonction au sein d'Imerys Minéraux Belgique et ce peu importe le statut.")
            st.write("Employés Imerys, Etudiants, Sociétés extérieures.")
            st.write("*La sécurité, la santé et le bien-être n'ont pas de statut chez Imerys.*")
            st.write("La direction, Monsieur Dazza CEO, a rédigé une charte santé et sécurité afin de positionner la vision d'Imerys.")

        elif induction_section == "L'accès au site":
            st.subheader("L'accès au site")
            st.write("L'accès au site est strictement réservé aux personnes autorisées :")
            st.write("- Soit en tant qu'employé")
            st.write("- Soit en tant que visiteur (un accompagnement est obligatoire)")
            st.write("- Soit en tant que technicien (un accueil sécurité et environnement est obligatoire)")
            st.write("Aujourd'hui nous avons Cognibox (passeport sécurité)")
            st.write("Tout accès au site aussi bien pour un visiteur qu'un technicien nécessite un enregistrement.")
            st.write("- Cahier de présence aux entrées site (TC, bâtiment usine)")
            st.write("- Il est interdit de fumer dans les installations (Privilégiez les abris fumeurs)")
            try:
                site_access_image = Image.open("site_access_image.png") # Replace with actual image
                st.image(site_access_image, caption="Accès au Site", use_column_width=True)
            except FileNotFoundError:
                st.warning("Image d'accès au site non trouvée (site_access_image.png).")

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
                environment_image = Image.open("environment_image.png") # Replace with actual image
                st.image(environment_image, caption="Environnement", use_column_width=True)
            except FileNotFoundError:
                st.warning("Image d'environnement non trouvée (environment_image.png).")


        elif induction_section == "La Sécurité d'Entreprise":
            st.subheader("La sécurité d'une entreprise est régie par différents organes")
            st.write("Le CPPT: Comités pour la prévention et la protection au travail. Émet des avis et des propositions sur la politique du Bien-être des travailleurs lors de l'exécution de leur travail, sur le plan global de prévention et le plan annuel d'actions.")
            st.write("Le CE : Comité d'entreprise. Émet des avis sur les orientations stratégiques, l'organisation du temps de travail, les besoins en formations, la politique sociale ainsi que les conditions de travail.")
            st.write("Le SIPP: Service Interne pour la Prévention et la Protection au travail. Le service interne a pour mission générale d'assister l'employeur, les membres de la ligne hiérarchique et les travailleurs de l'entreprise dans l'application de la réglementation relative au bien-être des travailleurs mais également dans la réalisation des mesures et activités de prévention.")
            st.write("Le SEPP : Service externe pour la prévention et la protection au travail. Représenté chez Imerys Lixhe par le CESI. Assiste l'entreprise pour des missions pour lesquelles il n'en a pas les compétences en matière de santé et de bien-être. (surveillance santé, hygiène, ergonomie...)")
            try:
                safety_org_image = Image.open("safety_org_image.png") # Replace with actual image
                st.image(safety_org_image, caption="Organes de Sécurité", use_column_width=True)
            except FileNotFoundError:
                st.warning("Image des organes de sécurité non trouvée (safety_org_image.png).")

        elif induction_section == "Les SERIOUS 7":
            st.subheader("Règles primordiales d'Imerys - Les SERIOUS 7")
            st.write("Ce sont des protocoles de sécurité pour lesquels IMERYS à une attention toute particulière suite à un accident très grave ou mortel.")
            st.write("Ils sont tous applicables sur tous les sites IMERYS et d'une manière ou d'une autre au site de Lixhe et sont les exigences minimales à respecter tant par le personnel Imerys que par les sous-traitants.")
            st.write("Les SERIOUS 7:")
            st.write("- S3 Consignation / déconsignation")
            st.write("- S4 Sécurité électrique")
            st.write("- S10 Protection des machines et des convoyeurs")
            st.write("- S11 Équipements mobiles")
            st.write("- S13 Travail en hauteur")
            st.write("- S14 Sécurisation du terrain")
            st.write("- S19 Sécurité des chariots élévateurs")

            serious_7_subsection = st.selectbox("Plus de détails sur les Serious 7:", ["Aucun", "S03 - LOTOTO", "S04 - Sécurité électrique", "S10 - Protection machine", "S11 - Équipement mobile", "S13 - Travail en hauteur", "S14 - Sécurisation terrain", "S19 - Chariots élévateurs"])
            if serious_7_subsection == "S03 - LOTOTO":
                st.subheader("S03 - Lock-out Tag-out Try-out (LOTOTO)")
                st.write("Il s'agit d'une procédure de sécurité planifiée qui consiste à neutraliser les sources d'énergie pendant une opération de maintenance ou de réparation d'une machine.")
                st.write("Différentes sources d'énergie peuvent animer une installation : électrique, mécanique, hydraulique, thermique, chimique.")
                st.write("Principes de base : Notifications et Coupure des énergies, Pose des cadenas, Vérification des effets, Travail, Remise en ordre, Remise des énergies, Test, Remise en service")
            elif serious_7_subsection == "S04 - Sécurité électrique":
                st.subheader("S04 - Sécurité électrique")
                st.write("Seule une personne qualifiée est autorisée à effectuer les tâches électriques. Ils doivent posséder leur habilitation électrique (BA4-BA5) et une autorisation de l'employeur décrivant les tâches.")
                st.write("Exécuter des tâches sur un équipement électrique : Personnel compétent et autorisé (formation BA4 minimum), Port des EPI adaptés, Mise en place des protections collectives, Respect des procédures de consignation.")
            elif serious_7_subsection == "S10 - Protection machine":
                st.subheader("S10 - Protection machine et convoyeurs")
                st.write("Toute partie mobile sur une machine non protégée contre les contacts et risque d'entraînement est une anomalie qui doit être signalée.")
                st.write("Pour intervention sur installation protégée : Consignation, Balisage, Vérification des risques.")
            elif serious_7_subsection == "S11 - Équipement mobile":
                st.subheader("S11 - Équipement mobile")
                st.write("Utilisation d'équipement mobile demande autorisation de compétence de l'Employeur.")
                st.write("Personnel compétent connaît les règles, Vérification avant utilisation, Respect des règles d'utilisation, Respect des règles de circulation.")
            elif serious_7_subsection == "S13 - Travail en hauteur":
                st.subheader("S13 - Travail en hauteur")
                st.write("Travailler à plus de 2 mètres interdit sauf avec sécurisation collective ou EPI anti-chute (décision après évaluation des risques).")
                st.write("Travail sur échelle autorisé sous conditions : Inspection matériel, Bon usage, Règle des trois points, Léger et courte durée.")
            elif serious_7_subsection == "S14 - Sécurisation terrain":
                st.subheader("S14 - Sécurisation du terrain")
                st.write("Protocole non applicable tel quel à Lixhe, mais mesures à appliquer.")
                st.write("Le merlon : levée de matière empêchant machine de déverser. Autres : Pas de stationnement sur tas de marbre, Vérifier sols, Pas de piétons sans autorisation.")
            elif serious_7_subsection == "S19 - Chariots élévateurs":
                st.subheader("S19 - Chariots élévateurs")
                st.write("Utiliser un équipement mobile est autorisé au personnel compétent.")
                st.write("Règles : Personnel compétent, Vérifications, Ceinture, Règles de circulation/manutention, Pas de casque audio.")
                st.write("Attention piétons : personnes vulnérables, contact visuel primordial.")

        elif induction_section == "Produits et Substances Dangereuses":
            st.subheader("Les produits et substances dangereuses")
            st.write("Usage nécessaire dans process de Production, Support Production et Maintenance.")
            st.write("Essentiel de prendre précautions d'usage pour éviter accidents graves.")
            st.write("Produit considéré dangereux si pictogramme sur étiquette.")
            st.subheader("Conseils de base à appliquer")
            st.write("- Prendre connaissance consignes de sécurité sur Fiche DSS et respecter règles.")
            st.write("- Être formé.")
            st.write("- Avoir regard sur moyens de secours avant interventions.")
            st.write("- Ne pas transvaser un produit dans un autre contenant non adapté.")
            st.write("Si question ou doute, stopper activité et contacter Responsable hiérarchique ou Conseiller en prévention.")
            try:
                danger_symbols_image = Image.open("danger_symbols_image.png") # Replace with actual image
                st.image(danger_symbols_image, caption="Pictogrammes de Danger", use_column_width=True)
            except FileNotFoundError:
                st.warning("Image des pictogrammes de danger non trouvée (danger_symbols_image.png).")


        elif induction_section == "Take 5":
            st.subheader("Take 5")
            st.write("Le take 5 est un outil, une façon de faire pour prendre le temps de réfléchir aux actions avant tâche.")
            st.write("Il est demandé au personnel d'Imerys d'en réaliser un / jour.")
            st.write("Ceci n'est pas suffisant. Démarche continue. Réfléchir avant d'agir pour chaque action.")
            st.write("Pas de stress, pas d'inquiétude. Juste prendre le temps de se mettre en bonnes conditions.")
            st.write("Imerys demande à chacun de prendre le temps d'assurer sa sécurité et celle des autres.")
            try:
                take5_image = Image.open("take5_image.png") # Replace with actual image
                st.image(take5_image, caption="Take 5", use_column_width=True)
            except FileNotFoundError:
                st.warning("Image Take 5 non trouvée (take5_image.png).")


        elif induction_section == "Conclusion":
            st.subheader("Conclusion")
            st.write("Nous sommes tous Responsable de notre propre sécurité et de celle des autres.")
            st.write("Soyez toujours interrogatif et observateur.")
            st.write("N'ayez pas peur d'intervenir si quelque chose vous paraît dangereux ou inapproprié.")
            st.write("Bon travail chez Imerys")

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
