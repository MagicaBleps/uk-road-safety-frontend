# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import datetime
import requests
import streamlit.components.v1 as components
import pandas as pd
import numpy as np



'''
This front queries the [UK Road Safety model API](https://ukroadsafety-6ltey62awq-ew.a.run.app/show_map)
'''
st.markdown('<p style="font-size: 15px;">The map takes a few seconds to load, be patient :)</p>',unsafe_allow_html=True)
with st.form(key='params_for_api'):

    option = st.selectbox(
    'Select a year:',index=4,
    options=(2017,2018,2019,2020,2021))
    st.form_submit_button('Get Data')

params = dict(
    year=option)

api_url = 'https://ukroadsafety-6ltey62awq-ew.a.run.app/show_map'
response = requests.get(api_url, params=params)
source_code = response.text
print(source_code)
components.html(source_code,height=600)
