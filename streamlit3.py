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

# Vérification du rôle et affichage en fonction
if st.session_state["authentication_status"]:
    user_role = st.session_state["user_role"]
    
    if user_role == "administrateur":
        st.write("Bienvenue, Administrateur!")
        # Contenu réservé aux administrateurs
        if selection == "Dashboard":
            st.write("Tableau de bord Administrateur")
    else:
        st.write("Bienvenue, Utilisateur!")
        # Contenu réservé aux utilisateurs
        if selection == "Photos":
            st.write("Album photo de l'utilisateur")
else:
    st.warning("Veuillez vous connecter pour accéder à ces fonctionnalités.")
Étape 5: Protection contre les attaques par force brute
Pour éviter les attaques par force brute, vous pouvez mettre en place des mesures de sécurité pour limiter les tentatives de connexion. Par exemple, vous pouvez utiliser la propriété failed_login_attempts dans les données des utilisateurs pour suivre le nombre de tentatives échouées.

python
Copier le code
# Exemple de protection contre les attaques par force brute
MAX_ATTEMPTS = 3  # Nombre maximal de tentatives

if authenticator.failed_login_attempts >= MAX_ATTEMPTS:
    st.error("Vous avez atteint le nombre maximal de tentatives. Veuillez réessayer plus tard.")
    # Bloquer l'accès pendant un certain temps ou rediriger vers une page de réinitialisation