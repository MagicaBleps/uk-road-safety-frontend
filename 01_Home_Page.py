# Contents of ~/my_app/main_page.py
import streamlit as st

import datetime
import requests
import streamlit.components.v1 as components
import pandas as pd
import numpy as np



'''
# UK Road Safety

'''

from PIL import Image
image = Image.open('Apy.png')
st.image(image)

image = Image.open('Apm.png')
st.image(image)

'''
#### Data Source :
https://www.gov.uk/government/collections/road-accidents-and-safety-statistics
'''
