# Contents of ~/my_app/main_page.py
import streamlit as st
from PIL import Image

import streamlit.components.v1 as components


st.set_page_config(layout="wide")





col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    '''
    # Mapping Road Safety in the UK

    '''
    image = Image.open('road.jpeg')
    st.image(image)

with col3:
    st.write(' ')
