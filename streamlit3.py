import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Données des comptes utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
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
    st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")
    # Vous pouvez ajouter ici du contenu réservé aux utilisateurs authentifiés

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
