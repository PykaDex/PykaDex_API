import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from pytorch_prediction_pokemon_api import get_prediction


##########################################
# WEB PAGE CONTENT
##########################################

# web page ico and tab title
st.set_page_config(
page_title='PykaDex API',
page_icon='./assets/icon.ico'
)

# page header
st.image('./assets/icon.png',width=80)
st.title('PykaDex API')
st.markdown("See full project on [GitHub](https://github.com/PykaDex)")

uploaded_image = st.file_uploader('',type=[ "jpg", "jpeg","png"])
submit_button  = st.button("Scan Pokemon")

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if submit_button:
        with st.spinner('Model working....'):
            predictions = get_prediction(image)
            st.markdown(predictions)
