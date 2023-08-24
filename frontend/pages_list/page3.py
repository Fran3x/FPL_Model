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
    st.title("Best squad")
    st.write("Best squad helps you pick optimal players for next gameweek based on model predictions. It also suggests the best captain(C) and vice-captain(VC) for your team. The bench is just filled with cheapest players to spend more on starting eleven. Budget of 100£ is assumed since it`s a starting budget for everyone.")
    image = load_image("https://resources.premierleague.com/premierleague/photos/players/250x250/p172850.png")
    st.image(image, caption="Best squad for next gameweek")
