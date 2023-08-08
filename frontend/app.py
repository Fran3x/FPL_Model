import streamlit as st
from streamlit_option_menu import option_menu

from pages_list.page1 import page1
from pages_list.page2 import page2
from pages_list.page3 import page3

st.set_page_config(
    layout="wide",
    page_title = "FPL predictor",
    page_icon = "https://freepngimg.com/download/premier_league/32207-5-premier-league-file.png"
)

with open('./frontend/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

page_names_to_funcs = {
    "Overview": page1,
    "Predictions": page2,
    "How it works?": page3,
}

with st.sidebar:
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.write("")

    with col2:
        # st.image("https://www.pngmart.com/files/23/Premier-League-Logo-PNG-Clipart.png")
        st.image("https://www.pngkit.com/png/full/213-2133496_premier-league-and-fa-cup-premier-league-logo.png")

    with col3:
        st.write("")
    
    selected = option_menu(
        "Menu", ["Overview", 'Predictions', 'How it works?'], 
        icons=['house', 'graph-up', 'question'],
        menu_icon="list", 
            styles={
                # "container": {"background-color": "#f0f2f6"},
                "container": {"background-color": "#262730"},
                # "nav-link-selected": {"background-color": "#ff5d5d"},
                "nav-link-selected": {"background-color": "#800080"},
            }
        )
    

page_names_to_funcs[selected]()

