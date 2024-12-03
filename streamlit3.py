import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Charger les données des utilisateurs depuis un fichier CSV
df = pd.read_csv('users.csv')

# Préparer les données des comptes pour l'authentification
lesDonneesDesComptes = {
    'usernames': {row['name']: {
        'name': row['name'],
        'password': row['password'],
        'email': row['email'],
        'failed_login_attempts': row['failed_login_attempts'],
        'logged_in': row['logged_in'],
        'role': row['role']} for _, row in df.iterrows()}
}

# Créer une instance d'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Données des comptes
    "cookie_name",         # Nom du cookie
    "cookie_key",          # Clé du cookie
    30                     # Expiration du cookie en jours
)

# Connexion et gestion du formulaire d'authentification
st.title("Bienvenue à l'application : connectez-vous pour accéder à l'album")

# Utiliser authenticator.login() pour afficher le formulaire dans la sidebar ou dans le main
with st.sidebar:
    # Le formulaire de connexion s'affiche dans la sidebar
    auth_status, username, user_role = authenticator.login("Login", "sidebar")

# Vérification de l'authentification
if auth_status:
    st.session_state["authentication_status"] = True
    st.session_state["username"] = username
    st.session_state["user_role"] = user_role
    st.success(f"Bienvenue {username} !")

else:
    st.session_state["authentication_status"] = False

# Vérification de l'authentification
if st.session_state["authentication_status"]:
    # Afficher un message de bienvenue dans la sidebar
    with st.sidebar:
        st.write(f"Bienvenue, {st.session_state['username']}!")

        # Menu de navigation dans la sidebar
        selection = option_menu(
            menu_title="Menu",  # Titre du menu
            options=["Accueil", "Photos", "Dashboard"],  # Options du menu
            icons=["house", "image", "bar-chart-line"],  # Icônes associées
            default_index=0  # Page par défaut
        )

        # Affichage du contenu en fonction de l'option sélectionnée
        if selection == "Accueil":
            st.write("Bienvenue sur la page d'accueil!")
        elif selection == "Photos":
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

        elif selection == "Dashboard":
            st.write("Bienvenue sur le tableau de bord!")

        # Bouton de déconnexion
        authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif st.session_state["authentication_status"] is None:
    st.warning('Veuillez remplir les champs nom d\'utilisateur et mot de passe.')
