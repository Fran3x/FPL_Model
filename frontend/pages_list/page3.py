import streamlit as st
import pandas as pd
import os
import time
from PIL import Image
import requests
import urllib.request

@st.cache(allow_output_mutation=True)
def load_image(url):
    # urllib.request.urlretrieve("https://resources.premierleague.com/premierleague/photos/players/250x250/p172850.png", "image.png")
    # image = Image.open("image.png")
    image = Image.open("plottable/predictions_plot_best_eleven.png")
    return image

def page3():
    st.title("Best eleven")
    
    image = load_image("https://resources.premierleague.com/premierleague/photos/players/250x250/p172850.png")
    st.image(image, caption="Best eleven for next gameweek")
