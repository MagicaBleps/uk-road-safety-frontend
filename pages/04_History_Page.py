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

with st.form(key='params_for_api'):

    option = st.selectbox(
    'Select a year:',
    (2010,2011,2012,2013,2014))
    st.form_submit_button('Get Data')

params = dict(
    year=option)

api_url = 'https://ukroadsafety-6ltey62awq-ew.a.run.app/show_map'
response = requests.get(api_url, params=params)
source_code = response.text
print(source_code)
components.html(source_code,height=600)