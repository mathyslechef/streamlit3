import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

df = pd.read_csv('users.csv')

# Données des comptes utilisateurs

lesDonneesDesComptes = {
    'usernames': {row['name']: {
        'name': row['name'],
        'password': row['password'],
        'email': row['email'],
        'failed_login_attempts': row['failed_login_attempts'],
        'logged_in': row['logged_in'],
        'role': row['role']} for _, row in df.iterrows()}
}

# Création de l'instance d'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Données des comptes
    "cookie_name",         # Nom du cookie
    "cookie_key",          # Clé du cookie
    30                     # Expiration du cookie (en jours)
)

# Formulaire de connexion
authenticator.login()

# Vérification du statut de l'authentification
def accueil():
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")
    # Vous pouvez ajouter ici du contenu réservé aux utilisateurs authentifiés
    # Disposition des images en 3 colonnes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Un chat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("Un chien")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("Un hibou")
        st.image("https://static.streamlit.io/examples/owl.jpg")

# Gestion de l'authentification
if st.session_state["authentication_status"]:
    # Menu de navigation
    selection = option_menu(
        menu_title=None,  # Aucun titre
        options=["Accueil", "Photos", "Dashboard"],  # Liste des pages disponibles
        icons=["house", "image", "bar-chart-line"],  # Icônes associées à chaque page
        default_index=0  # Page par défaut au démarrage
    )

    # Affichage du contenu en fonction de la sélection
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil!")
    elif selection == "Photos":
        st.write("Bienvenue sur la page des photos!")
    elif selection == "Dashboard":
        st.write("Bienvenue sur le tableau de bord!")

    # Bouton de déconnexion
    authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif st.session_state["authentication_status"] is None:
    st.warning('Veuillez remplir les champs nom d\'utilisateur et mot de passe.')
