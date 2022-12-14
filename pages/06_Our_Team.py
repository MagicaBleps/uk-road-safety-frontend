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
# Our Team
'''

c1, c2 = st.columns((1, 1))

image = Image.open('picture_ele.jpg')
new_image = image.resize((10, 10))
c1.image(image)

with c1:
    st.text("Eleonora Macagno")
    st.text("🌐https://github.com/MagicaBleps")
    st.text("🌐http://www.linkedin.com/in/eleonora-mac")



image = Image.open('Jig.jpeg')
c2.image(image)

with c2:
    st.markdown("<b>Jigisha Pawar</b>")
    st.text("https://github.com/Jigisha-p")
    st.text("https://www.linkedin.com/in/jigisha-purohit-7b26a2205/")


image = Image.open('Lin.jpeg')
c1.image(image)

with c1:
    st.text("Linnan Chen")
    st.text("🌐https://github.com/leochen888")
    st.text("🌐https://www.linkedin.com/in/linnan-chen/")

image = Image.open('Mob.jpeg')
c2.image(image)

with c2:
    st.text("Mobolurin Adekanmbi")
    st.text("🌐https://github.com/Bolu-Adekanmbi")
    st.text("🌐https://www.linkedin.com/in/mobolurin-adekanmbi-8b8354243/")


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    image = Image.open('t.jpeg')

    st.image(image)

with col3:
    st.write(' ')
