import streamlit as st
from PIL import Image

@st.cache(allow_output_mutation=True)
def load_image(path):
    image = Image.open(path)
    # image = Image.open('frontend/pages/predictions_fwd_plottable.png')
    return image

def page2():
    # st.title("Fantasy Premier League point predictions")
    
    NUMBER_OF_PLOTS = 2
    
    PIL_images = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_' + str(i) + ".png") for i in range(1, NUMBER_OF_PLOTS + 1)]

    PIL_image = load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_1.png')
    PIL_image2 = load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_2.png')

    content = st.container()
    bottom_menu = st.columns((4, 1, 1))

    with bottom_menu[2]:
        total_pages = (
            NUMBER_OF_PLOTS
        )
        current_page = st.number_input(
            "Page", min_value=1, max_value=total_pages, step=1
        )
    with bottom_menu[0]:
        st.markdown(f"Page **{current_page}** of **{total_pages}** ")
        
    content.image(PIL_images[current_page - 1], caption='Point predictions for next gameweek')