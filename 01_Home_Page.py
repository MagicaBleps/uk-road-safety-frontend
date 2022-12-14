# Contents of ~/my_app/main_page.py
import streamlit as st
from PIL import Image

import streamlit.components.v1 as components


st.set_page_config(layout="wide")


par='<par style="font-size: 50px;"><b>Mapping Road Safety in the UK</b></par>'
st.markdown(par,unsafe_allow_html=True)

image = Image.open('bus.jpeg')
st.image(image,width=600)
