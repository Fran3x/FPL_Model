import streamlit as st
from streamlit_option_menu import option_menu

from pages.page1 import page1
from pages.page2 import page2
from pages.page3 import page3

st.set_page_config(
    layout="wide",
    page_title = "FPL predictor",
    page_icon = "https://freepngimg.com/download/premier_league/32207-5-premier-league-file.png"
)

page_names_to_funcs = {
    "Overview": page1,
    "Predictions": page2,
    "How it works?": page3,
}

with st.sidebar:
    selected = option_menu(
        "Menu", ["Overview", 'Predictions', 'How it works?'], 
        icons=['house', 'graph-up', 'question'],
        menu_icon="list", 
            styles={
                "container": {"background-color": "#f0f2f6"},
                "nav-link-selected": {"background-color": "#ff5d5d"},
            }
        )

page_names_to_funcs[selected]()

