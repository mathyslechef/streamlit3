import streamlit as st
from streamlit_authenticator import Authenticate

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
    accueil()
    # Bouton de déconnexion
    authenticator.logout("Déconnexion")
elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif st.session_state["authentication_status"] is None:
    st.warning('Veuillez remplir les champs nom d\'utilisateur et mot de passe.')
