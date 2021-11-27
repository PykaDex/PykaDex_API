import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
page_title='PykaDex API',
page_icon='./assets/icon.ico'
)

st.image('./assets/icon.png',width=80)
st.title('PykaDex API')
st.markdown("See full project on [GitHub](https://github.com/PykaDex)")

uploaded_image = st.file_uploader('',type=[ "jpg", "jpeg","png"])
submit_button  = st.button("Scan Pokemon")