import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt



with open('model_exponential_IN', 'rb') as f:
    model_IN = pickle.load(f)

with open('model_exponential_RR', 'rb') as f:
    model_RR = pickle.load(f)

with open('model_exponential_TN', 'rb') as f:
    model_TN = pickle.load(f)

    
import streamlit as st
import pandas as pd



# Définir le thème de la page Streamlit avec un arrière-plan noir
st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #000000;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Définir le texte à afficher dans la bande noire
texte_sidebar = """
# Bienvenue dans notre application de prévisions météorologiques
Cette application vous permet de visualiser les prévisions météorologiques pour différents paramètres.
"""

# Afficher la bande noire à gauche avec le texte à l'intérieur
st.sidebar.markdown(texte_sidebar)

# Afficher le reste de l'application dans la partie principale
st.title('Prévisions météorologiques')

##########################################################################################################
# Titre de l'application
st.title('Prédiction de météo')

# Description 
st.write('Cumul mensuel des hauteurs de précipitation ')

# Entrée utilisateur pour spécifier le nombre de mois pour les prédictions
number_rr = st.number_input('Nombre de mois pour la prédiction', min_value=0, max_value=100, step=1)

# Vérifier si l'utilisateur a fourni un nombre de mois pour les prédictions
if number_rr:
    # Prédiction des précipitations pour le nombre de mois spécifié
    # (Remplacer cette partie du code par votre logique de prédiction réelle)
    pred_RR = model_RR.forecast(steps=number_rr) # Exemple de valeurs de précipitation prédites
    
    # Créer une plage de dates pour les prédictions
    date_range = pd.date_range(start='2024-01-01', periods=number_rr, freq='M')
    
    # Créer un DataFrame pour stocker les dates et les valeurs prédites
    pred_df = pd.DataFrame({'Date': date_range, 'Précipitation prédite (mm)': pred_RR})
    pred_df.set_index('Date', inplace=True)
    
    # Afficher un graphique de ligne pour visualiser les prédictions
    st.line_chart(pred_df)


####################################################################################################""


# Description 
st.write('Cumul mensuel des durées d\'insolation en heures')

# Générer un identifiant unique pour le widget st.number_input
input_id = 'number_input_IN'

# Demander à l'utilisateur de spécifier le nombre de mois pour les prédictions
number_IN = st.number_input('Nombre de mois pour la prédiction', min_value=0, max_value=100, step=1, key=input_id)

# Vérifier si l'utilisateur a entré un nombre de mois
if number_IN:
    # Effectuer la prédiction des durées d'insolation pour le nombre de mois spécifié
    pred_IN = model_IN.forecast(steps=number_IN)

    # Créer une plage de dates pour les prédictions
    date_range = pd.date_range(start='2024-01-01', periods=len(pred_IN), freq='M')

    # Créer un DataFrame pour stocker les dates et les valeurs prédites
    pred_df = pd.DataFrame({ 'Date': date_range, 'Prévision': pred_IN })

    # Définir la colonne 'Date' comme index du DataFrame
    pred_df.set_index('Date', inplace=True)

    # Afficher un graphique de ligne pour visualiser les prédictions
    st.line_chart(pred_df)



############################################################################################################



st.write('Moyenne mensuelle de la température maximale')

# Vérifier si l'utilisateur a entré un nombre de mois

# Demander à l'utilisateur de spécifier le nombre de mois pour les prédictions de température
number_TN = st.number_input('Nombre de mois pour la prédiction', min_value=0, max_value=100, step=1)


if number_TN:
    # Effectuer la prédiction des températures pour le nombre de mois spécifié
    pred_TN = model_TN.forecast(steps=number_TN)

    # Créer une plage de dates pour les prédictions
    date_range = pd.date_range(start='2024-01-01', periods=len(pred_TN), freq='M')

    # Créer un DataFrame pour stocker les dates et les valeurs prédites
    pred_df = pd.DataFrame({ 'Date': date_range, 'Prévision': pred_TN })

    # Définir la colonne 'Date' comme index du DataFrame
    pred_df.set_index('Date', inplace=True)

    # Afficher un graphique de ligne pour visualiser les prédictions
    st.line_chart(pred_df)