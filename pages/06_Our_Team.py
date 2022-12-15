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
    st.markdown("<b>Eleonora Macagno</b>",unsafe_allow_html=True)
    st.write("🌐[https://github.com/MagicaBleps](https://github.com/MagicaBleps)")
    st.write("🌐[http://www.linkedin.com/in/eleonora-mac](http://www.linkedin.com/in/eleonora-mac)")



image = Image.open('Jig.jpeg')
c2.image(image)

with c2:
    st.markdown("<b>Jigisha Pawar</b>",unsafe_allow_html=True)
    st.write("🌐[https://github.com/Jigisha-p](https://github.com/Jigisha-p)")
    st.write("🌐[https://www.linkedin.com/in/jigisha-purohit-7b26a2205/](https://www.linkedin.com/in/jigisha-purohit-7b26a2205/)")


image = Image.open('Lin.jpeg')
c1.image(image)

with c1:
    st.markdown("<b>Linnan Chen</b>",unsafe_allow_html=True)
    st.write("🌐[https://github.com/leochen888](https://github.com/leochen888)")
    st.write("🌐[https://www.linkedin.com/in/linnan-chen/](https://www.linkedin.com/in/linnan-chen/)")

image = Image.open('Mob.jpeg')
c2.image(image)

with c2:
    st.markdown("<b>Mobolurin Adekanmbi</b>",unsafe_allow_html=True)
    st.write("🌐[https://github.com/Bolu-Adekanmbi](https://github.com/Bolu-Adekanmbi)")
    st.write("🌐[https://www.linkedin.com/in/mobolurin-adekanmbi-8b8354243/](https://www.linkedin.com/in/mobolurin-adekanmbi-8b8354243/)")


st.text("")
st.text("")
st.text("")
st.text("")

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.text("")
st.text("")
st.text("")
st.text("")


par='<center style="font-size: 120px;"><b>THANK YOU!</b></center>'
st.markdown(par,unsafe_allow_html=True)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")


par1='<b style="font-size: 25px;">Check out this amazing website! [https://tinyurl.com/ukrsm](https://tinyurl.com/ukrsm)</b>'
qr=Image.open('ukrsm-400.png')
st.image(qr,width=100)
st.markdown(par1,unsafe_allow_html=True)
