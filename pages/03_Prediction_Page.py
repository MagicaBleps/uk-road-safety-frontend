# Contents of ~/my_app/pages/page_3.py
import streamlit as st

import datetime
import requests
import streamlit.components.v1 as components
import pandas as pd
import numpy as np



'''
# UK Road Safety
This front queries the [UK Road Safety model API](http://localhost:8000/predict)
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

#api_url = 'http://localhost:8000/predict'
#response = requests.get(api_url, params=params)
#prediction = response.json()

#pred = prediction['y_pred']

st.header(f'Prediction for next 10 Months: ')

prediction={0:1,1:4,2:2,3:2,4:1,5:0,6:2,7:1,8:2,9:1}
l=list(prediction.values())
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Month 1", l[0])
col2.metric("Month 2", l[1])
col3.metric("Month 3", l[2])
col4.metric("Month 2", l[3])
col5.metric("Month 3", l[4])
col1.metric("Month 1", l[5])
col2.metric("Month 2", l[6])
col3.metric("Month 3", l[7])
col4.metric("Month 2", l[8])
col5.metric("Month 3", l[9])
