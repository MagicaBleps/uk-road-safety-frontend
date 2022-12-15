# Contents of ~/my_app/main_page.py
import streamlit as st

import datetime
import requests
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")

'''
# UK Road Safety Analysis
'''
st.text("")
st.text("")
par='<p style="font-size: 21px;">For the purpose of this project, we focused on the <b>temporal and geospatial</b> aspects of the dataset.<br />In this page we report some of the main findings of our analysis from the temporal point of view.<br /><br /></p>'

st.markdown('#### 📊 Data Analysis')
st.markdown(par,unsafe_allow_html=True)

image = Image.open('bars.png')
st.image(image)

with st.expander('Click to see explanation'):
    st.markdown('<p style="font-size: 21px;">In the picture above is reported the yearly accidents rate. We note a consistent decrease since 1999. We also note a dip in the rate corresponding to 2020, the year of the COVID-19 pandemic.</p>',unsafe_allow_html=True)

st.text("")
st.text("")

c1, c2 = st.columns((1, 1))

image = Image.open('heatmap.png')
c1.image(image)

with c1:
    with st.expander('Click to see explanation'):
        st.markdown('<p style="font-size: 21px;">If we consider weekdays, we note clearly an higher accidents rate on Fridays, while Sundays seem to be safer. However this difference is decreasing over the years.</p>',unsafe_allow_html=True)


image = Image.open('time.png')
c2.image(image)

with c2:
    with st.expander('Click to see explanation'):
        st.markdown('<p style="font-size: 21px;">If we consider the time of day, we note two peaks, one in the morning and another one in the afternoon. Most accidents seem to happen between 10AM and 6PM.</p>',unsafe_allow_html=True)

st.text("")
st.text("")
st.text("")
st.text("")

image = Image.open('windows.png')
st.image(image)

with st.expander('Click to see explanation'):
    st.markdown('<p style="font-size: 21px;">If we divide the day in five main hour windows, we can see that the afternoon rush window is the one where most accidents happen.</p>',unsafe_allow_html=True)

image = Image.open('shares.png')
st.image(image)

with st.expander('Click to see explanation'):
    st.markdown('<p style="font-size: 21px;">By plotting the percentage of accident severity for the different time windows, we see that most fatal accidents happen at night.</p>',unsafe_allow_html=True)


par2='<p style="font-size: 21px;">We tried to forecast the monthly accident rate in the whole UK with a Time Series Machine Learning model called <b>ARIMA</b> (Auto Regressive Integrated Moving Average).<br /></p>'

st.text("")
st.text("")
st.text("")

'''
#### 📈 ARIMA analysis
'''
st.markdown(par2,unsafe_allow_html=True)

image = Image.open('arima.png')
st.image(image)

with st.expander('Click to see explanation'):
    st.markdown('<p style="font-size: 21px;">We used data until 2019 to predict 2020 and 2021. Note how the prediction is actually accurate for 2021, while 2020 represents a blip that no model could have predicted, for obvious reasons.</br>In the series we can note some distict M shapes repeating: those indicate the <b>seasonality</b> of the data, that is, the yearly repetition of certain patterns. We also observe a negative trend in the data. The ARIMA model is able to replicate both behaviors.</p>',unsafe_allow_html=True)
