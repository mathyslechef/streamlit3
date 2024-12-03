import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# User account data
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Authentication instance
authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",  # Example cookie name
    "cookie_key",   # Example cookie key
    30  # Cookie expiration time in days
)

# Page logic for authentication
def accueil():
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")

# Check authentication status
if st.session_state.get("authentication_status"):
    accueil()
    authenticator.logout("Déconnexion")
elif st.session_state.get("authentication_status") is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state.get("authentication_status") is None:
    st.warning('Les champs username et mot de passe doivent être remplis')

# Create navigation menu
selection = option_menu(
    menu_title=None,
    options=["Accueil", "Photos"]
)

# Content based on selection
if selection == "Accueil":
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
    st.write("Bienvenue sur mon album photo")

# Display images in a 3-column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# Sidebar with selectbox and radio buttons
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
