import streamlit as st
import numpy as np
import matplotlib.pylab as plt
import time
from pages.page1 import page1
from pages.page2 import page2
from pages.page3 import page3

st.set_page_config(layout="wide")

page_names_to_funcs = {
    "Overview": page1,
    "Predictions": page2,
    "Model architecture": page3,
}

selected_page = st.sidebar.radio("", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()