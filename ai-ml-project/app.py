import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("model.h5")

st.title("Scene Classifier")

file = st.file_uploader("Upload Image")

if file:
    img = Image.open(file).resize((150,150))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    st.write("Prediction:", np.argmax(pred))


























