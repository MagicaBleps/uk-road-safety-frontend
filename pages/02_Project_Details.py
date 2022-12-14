# Contents of ~/my_app/main_page.py
import streamlit as st
from PIL import Image

import streamlit.components.v1 as components


st.set_page_config(layout="wide")

'''
# 🛣 Project Details
'''

par='<p style="font-size: 21px;">Can we build a geographical map of road safety in the UK?</p><br>'
st.markdown('#### 🎯 Problem Statement:')
st.markdown(par,unsafe_allow_html=True)


par='''<p style="font-size: 21px;">
1: The model used by insurance companies when calculating the customers premium based on their usual routes
<br>
2: The model is used by traffic apps (e.g. Waze, Google Maps) to inform users about the dangers on the planned routes
</p><br>'''
st.markdown('#### 💻 Use cases:')
st.markdown(par,unsafe_allow_html=True)

par='''<p style="font-size: 21px;">
Road Safety data published by the UK government(.csv files)</p>'''

st.markdown('#### 🌐 Data Source:')
st.markdown(par,unsafe_allow_html=True)
'''
https://www.gov.uk/government/collections/road-accidents-and-safety-statistics
'''
par='''<p style="font-size: 21px;">
1. Divide the UK territory into geospatial squares 🌏 <br>
2. Compute the accidents rate for each square every month  📉 <br>
3. Train a Machine Learning model that predicts the next months accident rate for each square 🧮 <br>
4. Plot the predicted accident rate of selected bucket on a UK map 🏆 <br>
</p>'''


st.markdown('#### 🧠 Our Approach:')
st.markdown(par,unsafe_allow_html=True)

image = Image.open('geohash.png')
st.image(image)
