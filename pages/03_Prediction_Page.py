# Contents of ~/my_app/pages/page_3.py
import streamlit as st

import datetime
import requests
import streamlit.components.v1 as components
import pandas as pd
import numpy as np



'''
# UK Road Safety Predictions
This front queries the [UK Road Safety model API](http://localhost:8000/predict)

We created a prediction model for the first 6 months of 2022, based on the historical data.
The model is based on a Recurrent Neural Network and is focused on the 4 UK districts where accidents were more frequent in 2021.
To define the 'districts' we used the [geohash encoding](https://en.wikipedia.org/wiki/Geohash) with precision equal to 6 digits, corresponding to areas approx. 1.22km x 0.61km wide.
This model serves as a proof of concept for a possible extension to more geohashes in the future.
'''

HtmlFile = open("geohash.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code,height=600)


with st.form(key='params_for_api'):

    option = st.selectbox(
    'Select a Geohash:',
    ('gcpvj0', 'gcpvj1', 'gcpvj4','gcpvhc','gcpuv2'))


    st.form_submit_button('Make prediction')

params = dict(
    hash=option)

api_url = 'http://localhost:8000/predict'
response = requests.get(api_url, params=params)
prediction = response.json()
print(prediction)
#pred = prediction['y_pred']

st.header(f'Predictions for 2022: ')

#prediction={0:1,1:4,2:2,3:2,4:1,5:0,6:2,7:1,8:2,9:1}
l=list(prediction.values())
col1, col2, col3 = st.columns(3)
col1.metric("January 2022", l[0])
col2.metric("February 2022", l[1])
col3.metric("March 2022", l[2])
col1.metric("April 2022", l[3])
col2.metric("May 2022", l[4])
col3.metric("June 2022", l[5])
