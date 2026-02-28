import streamlit as st
import pandas as pd
import os
import base64
import sqlite3
import matplotlib.pyplot as plt

# -------------------------------------------------
# CONFIGURATION PAGE
# -------------------------------------------------

st.set_page_config(
    page_title="Animal Scraping App",
    page_icon="🐾",
    layout="wide"
)

# -------------------------------------------------
# STYLES CSS
# -------------------------------------------------

def appliquer_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

        h1 { text-align: center; font-size: 42px !important; font-weight: 700 !important; margin-bottom: 10px; }
        h2 { font-size: 30px !important; font-weight: 500 !important; margin-top: 30px; }
        p  { font-size: 18px !important; }

        /* Sidebar */
        section[data-testid="stSidebar"] { background-color: #1F618D !important; }
        section[data-testid="stSidebar"] div[role="button"]:hover { background-color: #154360 !important; border-radius: 8px; }
        section[data-testid="stSidebar"] .stSelectbox label {
            color: white !important;
            text-align: center !important;
            width: 100% !important;
            display: block !important;
            margin-bottom: 10px !important;
        }
        div[data-baseweb="popover"] li { color: #1B2631 !important; }
        div[data-baseweb="select"] [aria-selected="true"] { color: #1F618D !important; }

        div.stButton > button,
        div.stDownloadButton > button,
        div.stLinkButton > a {
            background-color: #1F618D !important;
            color: white !important;
            font-size: 18px;
            font-weight: bold !important;
            padding: 12px 25px;
            border-radius: 12px;
            border: none;
            transition: 0.3s ease;
        }
                
        div.stButton > button:hover,
        div.stDownloadButton > button:hover { background-color: #154360 !important; }
        div.stButton > button:active { transform: scale(0.98); }

        /* Selectbox */
        div[data-baseweb="select"] > div { background-color: #EAF2F8 !important; border-radius: 8px !important; font-size: 16px; }
        div[data-baseweb="select"]:hover > div { background-color: #D4E6F1 !important; }
        div[data-baseweb="select"] span { color: #1F618D !important; }

        .block-container { padding-top: 2rem; }
        </style>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# FONCTIONS UTILITAIRES
# -------------------------------------------------

def add_banner(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <div style="text-align:center; margin-bottom:2px;">
            <img src="data:image/jpg;base64,{encoded}"
                 style="width:100%; height:250px; object-fit:contain; border-radius:15px;">
        </div>
    """, unsafe_allow_html=True)

def titre_section(texte):
    st.markdown(f"<h2 style='text-align: center;'>{texte}</h2>", unsafe_allow_html=True)

def charger_csv(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    st.error("Fichier introuvable.")
    return None

def charger_sqlite():
    """Charge les données nettoyées depuis SQLite."""
    conn = sqlite3.connect("animals.db")
    df = pd.read_sql_query("SELECT * FROM data_clean", conn)
    conn.close()
    return df

def bouton_telechargement_centre(df, nom_fichier):
    _, col_centre, _ = st.columns([1, 2, 1])
    with col_centre:
        st.download_button(
            label="Télécharger les données",
            data=df.to_csv(index=False),
            file_name=nom_fichier,
            mime="text/csv"
        )

def carte_metrique(col, couleur, titre, valeur):
    col.markdown(f"""
        <div style="background-color:{couleur}; padding:15px; border-radius:10px; text-align:center;">
            <p style="color:white; font-size:14px; font-weight:bold; margin:0;">{titre}</p>
            <p style="color:white; font-size:28px; font-weight:bold; margin:0;">{valeur}</p>
        </div>""", unsafe_allow_html=True)

def graphique_bar(titre, valeurs, couleur):
    st.subheader(titre)
    fig, ax = plt.subplots()
    ax.bar(valeurs.index, valeurs.values, color=couleur, edgecolor="white")
    plt.xticks(rotation=45, ha='right', fontsize=8)
    st.pyplot(fig)

# -------------------------------------------------
# EN-TÊTE
# -------------------------------------------------

appliquer_styles()
add_banner("banner.jpg")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
    <h1 style="text-align:center; font-size:25px; font-weight:600; white-space:nowrap;">
        <span style="color:#1F618D;">🐾 Animal Scraping Application</span>
    </h1>
""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Application de collecte, visualisation et évaluation des données animales</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
# -------------------------------------------------
# NAVIGATION SIDEBAR
# -------------------------------------------------

st.sidebar.markdown("""
    <div style="text-align:center; margin-bottom:20px;">
        <p style="color:white; font-size:28px; margin:0;">🐾</p>
        <p style="color:white; font-size:16px; font-weight:bold; margin:0;">Animal Scraping App</p>
        <hr style="border-color:rgba(255,255,255,0.3); margin:10px 0;">
    </div>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Navigation",
    ["Scraping avec BeautifulSoup", "Téléchargement", "Tableau de bord", "Formulaire d'évaluation"]
)

st.sidebar.markdown("""
    <div style="position:fixed; bottom:30px; width:200px;">
        <hr style="border-color:rgba(255,255,255,0.3);">
        <p style="color:white; font-size:10px; text-align:center; margin:0;">🌍 Source : https://sn.coinafrique.com</p>
    </div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# DICTIONNAIRE DES FICHIERS
# -------------------------------------------------

# Fichiers BeautifulSoup (section Scraping)
fichiers_BS = {
    "Chiens":                "data/data_chien_BS.csv",
    "Moutons":               "data/data_mouton_BS.csv",
    "Poules/Lapins/Pigeons": "data/data_poule_BS.csv",
    "Autres animaux":        "data/data_autres_BS.csv",
}

# Fichiers Web Scraper bruts (section Téléchargement)
fichiers_WS = {
    "Chiens":                "data/data_chien_WS.csv",
    "Moutons":               "data/data_mouton_WS.csv",
    "Poules/Lapins/Pigeons": "data/data_poule_WS.csv",
    "Autres animaux":        "data/data_autres_WS.csv",
}

# -------------------------------------------------
# SECTION 1 : SCRAPING (données BeautifulSoup)
# -------------------------------------------------

if menu == "Scraping avec BeautifulSoup":
    #titre_section("Scraping des données")

    st.markdown("""
        <div style="background-color:#1F618D; color:white; padding:20px;
                    border-radius:12px; margin-bottom:35px; font-size:18px;">
            <b>🎯 Objectif :</b> Extraire automatiquement les annonces d'animaux sur plusieurs pages du site source.<br><br>
            <b> 📊 : </b> 4 catégories disponibles
        </div>
    """, unsafe_allow_html=True)

    # Nombre de pages par catégorie
    pages_par_categorie = {
        "Chiens":                list(range(1, 12)),
        "Moutons":               list(range(1, 17)),
        "Poules/Lapins/Pigeons": list(range(1, 11)),
        "Autres animaux":        list(range(1, 7)),
    }

    categorie = st.selectbox("Choisir une catégorie", list(fichiers_BS.keys()))
    nb_pages  = st.selectbox("Nombre de pages à afficher", pages_par_categorie[categorie])

    _, col_centre, _ = st.columns([1, 2, 1])
    with col_centre:
        lancer = st.button("Lancer le scraping")

    if lancer:
        df = charger_csv(fichiers_BS[categorie])
        if df is not None:
            # Simuler le nombre de pages (environ 12 annonces par page)
            df = df.head(nb_pages * 12)
            st.success("Scraping effectué avec succès !")
            st.write(f"**Dimension :** {df.shape[0]} lignes × {df.shape[1]} colonnes")
            st.dataframe(df)
            bouton_telechargement_centre(df, f"{categorie}_BS.csv")

# -------------------------------------------------
# SECTION 2 : TÉLÉCHARGEMENT (données brutes Web Scraper)
# -------------------------------------------------

elif menu == "Téléchargement":
    titre_section("Téléchargement des bases existantes")

    st.markdown("""
        <div style="background-color:#EAF2F8; padding:15px; border-radius:10px; margin-bottom:20px;">
            <p style="color:#1F618D; font-size:15px; margin:0;">
            📂 Ces données sont les données <b>brutes</b> collectées via <b>Web Scraper</b> (non nettoyées).
            </p>
        </div>
    """, unsafe_allow_html=True)

    for categorie, file_path in fichiers_WS.items():
        st.markdown(f"<h3 style='color:#1F618D; font-weight:bold;'>🐾 {categorie}</h3>", unsafe_allow_html=True)
        df = charger_csv(file_path)
        if df is not None:
            st.markdown(f"""
                <div style="background-color:#EAF2F8; padding:15px; border-radius:10px; text-align:center; margin-bottom:10px;">
                    <p style="color:#1F618D; font-size:16px; font-weight:bold; margin:0;">Données brutes Web Scraper</p>
                    <p style="color:#555; font-size:13px; margin:5px 0;">{df.shape[0]} lignes · {df.shape[1]} colonnes</p>
                </div>""", unsafe_allow_html=True)
            _, col_centre, _ = st.columns([1, 2, 1])
            with col_centre:
                st.download_button(
                    label=f"⬇️ Télécharger {categorie}",
                    data=df.to_csv(index=False),
                    file_name=f"{categorie}_WS_brut.csv",
                    mime="text/csv"
                )
        st.markdown("---")

# -------------------------------------------------
# SECTION 3 : TABLEAU DE BORD (données nettoyées SQLite)
# -------------------------------------------------

elif menu == "Tableau de bord":
    titre_section("Tableau de bord analytique")

    df = charger_sqlite()

    if df is not None and not df.empty:

        # Nettoyage colonne price
        df["price"] = df["price"].astype(str).str.replace(" ", "").str.replace("CFA", "").str.replace("Prixsurdemande", "")
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

        # Métriques
        col1, col2, col3, col4 = st.columns(4)
        carte_metrique(col1, "#1F618D", "Total annonces", len(df))
        carte_metrique(col2, "#28B463", "Prix moyen",     round(df["price"].mean(), 2))
        carte_metrique(col3, "#E67E22", "Prix minimum",   df["price"].min())
        carte_metrique(col4, "#8E44AD", "Prix maximum",   df["price"].max())

        st.markdown("---")

        # ==============================
        # FILTRE PAR FOURCHETTE DE PRIX
        # ==============================
        st.markdown("<h3 style='color:#1F618D; font-weight:bold;'>🔍 Rechercher par budget</h3>", unsafe_allow_html=True)

        prix_min = int(df["price"].min())
        prix_max = int(df["price"].max())

        fourchette = st.slider(
            "Sélectionner une fourchette de prix (CFA)",
            min_value=prix_min,
            max_value=prix_max,
            value=(prix_min, prix_max)
        )
    

        # ==============================
        # FILTRE PAR VILLE
        # ==============================
        villes = ["Toutes"] + sorted(df["adress"].dropna().unique().tolist())
        ville_choisie = st.selectbox("📍 Filtrer par ville", villes)

        # Appliquer les filtres
        df_filtre = df[
            (df["price"] >= fourchette[0]) &
            (df["price"] <= fourchette[1])
        ]
        if ville_choisie != "Toutes":
            df_filtre = df_filtre[df_filtre["adress"] == ville_choisie]

        st.write(f"**{len(df_filtre)} annonces trouvées**")

        st.markdown("---")

        # ==============================
        # TOP 5 ANNONCES LES MOINS CHÈRES
        # ==============================
        st.markdown("<h3 style='color:#28B463; font-weight:bold;'>💰 Top 5 des annonces les moins chères</h3>", unsafe_allow_html=True)

        top5 = df_filtre.dropna(subset=["price"]).nsmallest(5, "price")[["name", "price", "adress", "url_image"]]

        for _, row in top5.iterrows():
            col_img, col_info = st.columns([1, 3])
            with col_img:
                try:
                    st.image(row["url_image"], width=120)
                except:
                    st.write("📷 Pas d'image")
            with col_info:
                st.markdown(f"""
                    <div style="background-color:#EAF2F8; padding:12px; border-radius:10px;">
                        <p style="color:#1F618D; font-size:16px; font-weight:bold; margin:0;">{row['name']}</p>
                        <p style="color:#28B463; font-size:15px; font-weight:bold; margin:5px 0;">💵 {int(row['price'])} CFA</p>
                        <p style="color:#555; font-size:13px; margin:0;">📍 {row['adress']}</p>
                    </div>""", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("---")

        # ==============================
        # TABLEAU INTERACTIF
        # ==============================
        st.markdown("<h3 style='color:#8E44AD; font-weight:bold;'>📋 Toutes les annonces filtrées</h3>", unsafe_allow_html=True)
        st.dataframe(df_filtre[["name", "price", "adress"]].reset_index(drop=True))

    else:
        st.warning("⚠️ Aucune donnée disponible dans la base de données.")

# -------------------------------------------------
# SECTION 4 : FORMULAIRE D'ÉVALUATION
# -------------------------------------------------

elif menu == "Formulaire d'évaluation":
    titre_section("Formulaire d'évaluation")
    st.write("Merci d'avoir testé l'application. Votre retour nous aide à améliorer la qualité du service.")

    choix = st.radio("Choisir le formulaire", ["KoboToolbox", "Google Forms"])

    _, col_centre, _ = st.columns([1, 2, 1])
    with col_centre:
        if choix == "KoboToolbox":
            st.link_button("Remplir le formulaire Kobo", "https://ee.kobotoolbox.org/x/BCGiZdWE")
        else:
            st.link_button("Remplir le formulaire Forms", "https://forms.gle/RUqv9iHApj6HyLK67")