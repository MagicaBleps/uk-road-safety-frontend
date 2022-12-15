# Contents of ~/my_app/pages/page_3.py
import streamlit as st

import datetime
import requests
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

'''
# UK Road Safety Predictions
This front queries the [UK Road Safety model API](https://ukroadsafety-6ltey62awq-ew.a.run.app/predict)
'''

with st.expander('Click to see explanation'):

    par='We created a prediction model for the first 6 months of 2022, based on the historical data. The model is based on a Recurrent Neural Network and is focused on the 4 UK districts where accidents were more frequent in 2021. To define the districts we used the [geohash encoding](https://en.wikipedia.org/wiki/Geohash) with precision equal to 6 digits, corresponding to areas approx. 1.22km x 0.61km wide.</br>This model serves as a proof of concept for a possible extension to more geohashes in the future.'
    st.markdown(par,unsafe_allow_html=True)

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

api_url = 'https://ukroadsafety-6ltey62awq-ew.a.run.app/predict'
response = requests.get(api_url, params=params)
prediction = response.json()

#pred = prediction['y_pred']

st.header(f'Predictions for 2022: ')



chart_data = pd.DataFrame.from_dict(prediction,orient='index')
chart_data.columns=['Predicted Accidents']

#st.line_chart(chart_data,use_container_width=True)
st.bar_chart(chart_data,use_container_width=True)
