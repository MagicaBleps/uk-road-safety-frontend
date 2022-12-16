# Contents of ~/my_app/main_page.py
import streamlit as st
from PIL import Image

import streamlit.components.v1 as components


st.set_page_config(layout="wide")


par='<par style="font-size: 50px;"><b>Mapping Road Safety in the UK</b></par>'
st.markdown(par,unsafe_allow_html=True)

c1, c2 = st.columns((1, 1))

image = Image.open('bus.jpeg')
c1.image(image)



with c2:
    with st.expander('Click to expand'):
        st.markdown('#### 🎯 Problem Statement')
        par='<p style="font-size: 21px;">Can we build a geographical map of road safety in the UK?</p>'
        st.markdown(par,unsafe_allow_html=True)

    with st.expander('Click to expand'):
        par='''<p style="font-size: 21px;">Road Safety data published by the UK government(.csv files): all accidents recorded since 1999, with timestamps and GPS coordinates.</p>'''
        st.markdown('#### 🌐 Data Source:')
        st.markdown(par,unsafe_allow_html=True)

    # with st.expander('Click to expand'):
    #     st.markdown('#### 🧠 Our Approach:')
    #     par='''<p style="font-size: 21px;">
    #     1. Divide the UK territory into geospatial squares 🌏 <br>
    #     2. Compute the accidents rate for each square every month  📉 <br>
    #     3. Train a Machine Learning model that predicts the next months accident rate for each square 🧮 <br>
    #     4. Plot the predicted accident rate of selected bucket on a UK map 🏆 <br>
    #     </p>'''
    #     st.markdown(par,unsafe_allow_html=True)
