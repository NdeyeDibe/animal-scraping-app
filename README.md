# 🐾 Animal Scraping App

> Application web interactive de collecte, stockage et visualisation des annonces d'animaux sur [CoinAfrique Sénégal](https://sn.coinafrique.com).

---

## 🔗 Liens

| Ressource | Lien |
|-----------|------|
| 🚀 Application Streamlit | [https://animals1235.streamlit.app/](https://animals1235.streamlit.app/) |
| 📋 Formulaire KoboToolbox | [https://ee.kobotoolbox.org/x/BCGiZdWE](https://ee.kobotoolbox.org/x/BCGiZdWE) |
| 📋 Formulaire Google Forms | [https://forms.gle/RUqv9iHApj6HyLK67](https://forms.gle/RUqv9iHApj6HyLK67) |

---

## 📌 Description du projet

**Animal Scraping App** est une application Streamlit complète permettant de collecter, stocker et visualiser les annonces d'animaux publiées sur **CoinAfrique Sénégal**. Les données sont collectées via deux outils complémentaires avec des pipelines distincts.

---

## 🐶🐑🐓🦎 Catégories couvertes

| Catégorie | URL CoinAfrique | Variables collectées |
|-----------|----------------|----------------------|
| Chiens | [/categorie/chiens](https://sn.coinafrique.com/categorie/chiens) | Nom, Prix, Adresse, Image |
| Moutons | [/categorie/moutons](https://sn.coinafrique.com/categorie/moutons) | Nom, Prix, Adresse, Image |
| Poules / Lapins / Pigeons | [/categorie/poules-lapins-et-pigeons](https://sn.coinafrique.com/categorie/poules-lapins-et-pigeons) | Détails, Prix, Adresse, Image |
| Autres animaux | [/categorie/autres-animaux](https://sn.coinafrique.com/categorie/autres-animaux) | Nom, Prix, Adresse, Image |

---

## 🔄 Pipeline de collecte des données

| Outil | Nettoyage | Format de stockage | Fichiers |
|-------|-----------|--------------------|----------|
| **BeautifulSoup** | ❌ Non nettoyées | 📄 CSV | `data_chien_BS.csv`, `data_mouton_BS.csv`, `data_poule_BS.csv`, `data_autres_BS.csv` |
| **Web Scraper** | ❌ Brutes | 📄 CSV | `data_chien_WS.csv`, `data_mouton_WS.csv`, `data_poule_WS.csv`, `data_autres_WS.csv` |
| **Web Scraper** | ✅ Nettoyées | 🗄️ SQLite (`animals.db`) | Table `data_clean` |

---

## 🚀 Fonctionnalités de l'application

### 1. 🔍 Scraping avec BeautifulSoup
- Sélection de la catégorie et du nombre de pages à afficher
- Chargement des données collectées via BeautifulSoup (non nettoyées, stockées en CSV)
- Affichage du tableau et téléchargement en CSV

### 2. 📥 Téléchargement
- Téléchargement des données **brutes** collectées via **Web Scraper** (CSV)
- Disponible pour les 4 catégories d'animaux

### 3. 📊 Tableau de bord analytique
- Données **nettoyées** issues de **Web Scraper**, chargées depuis la base **SQLite** (`animals.db`)
- Métriques clés : total annonces, prix moyen, prix min/max
- Filtre par fourchette de prix (slider)
- Filtre par ville
- Top 5 des annonces les moins chères (avec images)
- Tableau interactif des annonces filtrées

### 4. 📋 Formulaire d'évaluation
- Choix entre **KoboToolbox** et **Google Forms**
- Lien direct vers le formulaire depuis l'interface

---

## 📁 Structure du projet

```
animal-scraping-app/
│
├── app.py                                  # Application principale Streamlit
├── Examen_scraping_using_BeautifulSoup.ipynb  # Notebook scraping BeautifulSoup
├── banner.jpg                              # Bannière de l'application
├── animals.db                              # Base SQLite (données Web Scraper nettoyées)
├── data/
│   ├── data_chien_BS.csv                   # Données BeautifulSoup - Chiens
│   ├── data_mouton_BS.csv                  # Données BeautifulSoup - Moutons
│   ├── data_poule_BS.csv                   # Données BeautifulSoup - Poules/Lapins/Pigeons
│   ├── data_autres_BS.csv                  # Données BeautifulSoup - Autres animaux
│   ├── data_chien_WS.csv                   # Données Web Scraper brutes - Chiens
│   ├── data_mouton_WS.csv                  # Données Web Scraper brutes - Moutons
│   ├── data_poule_WS.csv                   # Données Web Scraper brutes - Poules/Lapins/Pigeons
│   └── data_autres_WS.csv                  # Données Web Scraper brutes - Autres animaux
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies utilisées

| Outil | Usage |
|-------|-------|
| `Python` | Langage principal |
| `BeautifulSoup4` | Scraping multi-pages |
| `Web Scraper` | Collecte brute toutes pages |
| `Requests` | Requêtes HTTP |
| `Pandas` | Manipulation et nettoyage des données |
| `SQLite3` | Base de données des données nettoyées |
| `Streamlit` | Interface web interactive |
| `Matplotlib` | Visualisations graphiques |
| `KoboToolbox / Google Forms` | Formulaire d'évaluation |

---

## ▶️ Lancer l'application en local

```bash
# Cloner le dépôt
git clone https://github.com/ton-profil/animal-scraping-app.git
cd animal-scraping-app

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

---

## 📦 requirements.txt

```
streamlit==1.32.0
pandas
matplotlib
requests
beautifulsoup4
numpy
scipy
seaborn
altair==4.2.2
```

---

## 👤 Auteur

Projet réalisé dans le cadre d'un examen — **Data collection & Web Scraping 2026**
