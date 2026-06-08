import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image # Utilise Pillow pour la manipulation d'images
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input

# ======================================================
# 1. CONFIGURATION DE LA PAGE
# ======================================================
st.set_page_config(
    page_title="Détecteur de Maladies des Plantes",
    page_icon="🌿",
    layout="centered"
)

# Custom CSS pour rendre l'app plus jolie
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 Détecteur de Maladies des Plantes")
st.write("Cette application utilise l'IA pour identifier les maladies des plantes à partir d'une simple photo.")
st.divider()

# ======================================================
# 2. CHARGEMENT DU MODÈLE (Avec correction de l'erreur)
# ======================================================

# Liste des 38 classes (Assure-toi qu'elle est identique à ton entraînement)
CLASS_NAMES = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 
    'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 
    'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 
    'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
]

@st.cache_resource # Pour ne pas recharger le modèle à chaque clic
def load_model():
    # On essaie de charger le modèle EfficientNet (le champion)
    # On utilise 'custom_objects' pour régler l'erreur de preprocess_input
    model_path = 'MODELE_FINAL_96percent.keras' 
    try:
        model = tf.keras.models.load_model(
            model_path, 
            custom_objects={'preprocess_input': preprocess_input}
        )
        return model
    except Exception as e:
        st.error(f"Erreur de chargement : {e}")
        return None

model = load_model()

# ======================================================
# 3. INTERFACE UTILISATEUR (Upload)
# ======================================================

uploaded_file = st.file_uploader("📸 Importez une image de feuille (JPG, PNG, JPEG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Affichage de l'image
    image = Image.open(uploaded_file)
    st.image(image, caption='Image analysée', use_container_width=True)
    
    with st.spinner('🧠 L\'intelligence artificielle analyse l\'image...'):
        # --- PRÉ-TRAITEMENT (Crucial pour la précision) ---
        # 1. Redimensionner (doit être identique à l'entraînement)
        img_resized = image.resize((224, 224))
        
        # 2. Convertir en tableau numpy
        img_array = np.array(img_resized)
        
        # 3. Appliquer la fonction de prétraitement spécifique à EfficientNet
        # (Cela remplace le manuel / 255.0 pour être plus précis)
        img_array = preprocess_input(img_array)
        
        # 4. Ajouter la dimension Batch (1, 224, 224, 3)
        img_array = np.expand_dims(img_array, axis=0)

        # --- PRÉDICTION ---
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        predicted_class = CLASS_NAMES[predicted_index]
        confidence = np.max(predictions[0]) * 100

    # --- AFFICHAGE DU RÉSULTAT ---
    st.subheader("📊 Résultat du Diagnostic")

    # Logique de l'alerte (Seuil de confiance à 70%)
    if confidence > 70:
        st.success(f"### 🟢 Diagnostic : **{predicted_class}**")
        st.metric(label="Niveau de Confiance", value=f"{confidence:.2f}%")
    else:
        st.warning(f"### 🟡 Résultat Incertain : **{predicted_class}**")
        st.metric(label="Niveau de Confiance", value=f"{confidence:.2f}%")
        st.info("💡 Conseil : La confiance est faible. Assurez-vous que la photo est bien nette et que la feuille est bien visible.")

    # Petit bonus : Affichage de la probabilité de la classe
    with st.expander("Voir les détails des probabilités"):
        for i, class_name in enumerate(CLASS_NAMES):
            prob = predictions[0][i] * 100
            if prob > 5: # On n'affiche que les classes qui ont plus de 5%
                st.write(f"- {class_name}: {prob:.2f}%")

else:
    st.info("💡 En attente d'une image. Veuillez télécharger une photo de feuille ci-dessus.")

# --- PIED DE PAGE ---
st.divider()
st.caption("Projet de Fin de Module - Master Deep Learning - Détection de maladies des plantes")