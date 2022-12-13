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
#### Data Source :
https://www.gov.uk/government/collections/road-accidents-and-safety-statistics
'''

text= st.text_area('''Every year the UK government publishes the list of all recorded road accidents, each marked by GPS coordinates and datetime, as well as a lot of interesting information like the accident severity, the number of vehicles involved etc.

For the purpose of this project, we focused on the geospatial and temporal aspects of the dataset, but the possiibilities of meaningful analyses are countless.

In this page we report some of the main findings of our analysis.

In the picture below is reported the yearly accidents rate. We note a consistent decrease since 1999. We also note a dip in the rate corresponding to 2020, the year of the COVID-19 pandemic.''')



image = Image.open('Apy.png')
st.image(image)

c1, c2 = st.columns((1, 1))


image = Image.open('Years-Weekdays.jpg')
c1.markdown('If we consider weekdays, we note clearly an higher accidents rate on Fridays, while Sundays seem to be safer. However this difference is decreasing over the years.')
c1.image(image)




image = Image.open('Apm.png')
st.image(image)

'''

'''
