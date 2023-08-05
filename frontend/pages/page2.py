import streamlit as st
from PIL import Image

@st.cache(allow_output_mutation=True)
def load_image(path):
    image = Image.open(path)
    # image = Image.open('frontend/pages/predictions_fwd_plottable.png')
    return image

def page2():
    # st.title("Fantasy Premier League point predictions")

    PIL_image = load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_1.png')
    PIL_image2 = load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_2.png')

    content = st.container()
    bottom_menu = st.columns((4, 1, 1))


    # with bottom_menu[2]:
    #     batch_size = st.selectbox("Page Size", options=[25, 50, 100])
    with bottom_menu[2]:
        total_pages = (
            5
        )
        current_page = st.number_input(
            "Page", min_value=1, max_value=total_pages, step=1
        )
    with bottom_menu[0]:
        st.markdown(f"Page **{current_page}** of **{total_pages}** ")

    if current_page == 1:
        content.image(PIL_image, caption='Point predictions for next gameweek')
    else:
        content.image(PIL_image2, caption='Point predictions for next gameweek')