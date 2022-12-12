import streamlit as st

import datetime
import requests

'''
# UK Road Safety Model front

This front queries the [UK Road Safety model API](http://localhost:8000/predict)
'''

with st.form(key='params_for_api'):

    option = st.selectbox(
    'Select a Geohash?',
    ('gcpvj0', 'gcpvj1', 'gcpvj4','gcpvhc','gcpuv2'))


    st.form_submit_button('Make prediction')

params = dict(
    hash=option)

api_url = 'http://localhost:8000/predict'
response = requests.get(api_url, params=params)
prediction = response.json()

pred = prediction['y_pred']

st.header(f'Accident Count Prediction: ${y_pred}')
