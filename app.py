import streamlit as st
import time

# Configuration de la page mobile
st.set_page_config(page_title="BioSmart Lab", page_icon="🔬", layout="centered")

# Menu de navigation
st.sidebar.title("Navigation Labo")
labo = st.sidebar.selectbox(
    "Choisir la paillasse :",
    ["Immunologie (TDR)", "Microbiologie (Frottis)", "Hématologie", "Entomologie"]
)

st.title(f"🔬 BioSmart : {labo}")
st.write("Prototype d'aide au diagnostic")
st.divider()

# Zone d'importation de l'image
fichier = st.file_uploader("Prendre une photo ou choisir une image", type=["png", "jpg", "jpeg"])

if fichier is not None:
    st.image(fichier, caption="Image chargée", use_column_width=True)
    
    if st.button("Lancer l'analyse par l'IA"):
        with st.spinner("Analyse en cours..."):
            time.sleep(2)
        st.success("Analyse terminée avec succès !")
        
        if labo == "Immunologie (TDR)":
            st.metric(label="Résultat", value="POSITIF", delta="Confiance : 97%")
        elif labo == "Hématologie":
            st.metric(label="Globules rouges comptés", value="142")
        else:
            st.info("Résultat disponible pour le hub sélectionné.")
else:
    st.info("En attente d'une image à analyser.")
