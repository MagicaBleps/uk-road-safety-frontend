# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import datetime
import requests
import streamlit.components.v1 as components
import pandas as pd
import numpy as np



'''
This front queries the [UK Road Safety model API](http://localhost:8000/show_map)
'''

with st.form(key='params_for_api'):

    option = st.selectbox(
    'Select a year:',
    (1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021))
    st.form_submit_button('Get Data')

params = dict(
    year=option)

api_url = 'http://localhost:8000/show_map'
response = requests.get(api_url, params=params)
source_code = response.text
print(source_code)
components.html(source_code,height=600)
