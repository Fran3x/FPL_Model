import streamlit as st
from PIL import Image

@st.cache(allow_output_mutation=True)
def load_image(path):
    image = Image.open(path)
    # image = Image.open('frontend/pages/predictions_fwd_plottable.png')
    return image

def page2():
    # st.title("Fantasy Premier League point predictions")
    
    NUMBER_OF_PLOTS = 1
    
    # PIL_images = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_' + str(i) + ".png") for i in range(1, NUMBER_OF_PLOTS + 1)]
    
    PIL_images_all = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_All_' + str(i) + ".png") for i in range(1, NUMBER_OF_PLOTS + 1)]
    PIL_images_GK = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_GK_' + str(i) + ".png") for i in range(1, NUMBER_OF_PLOTS + 1)]
    PIL_images_DEF = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_DEF_' + str(i) + ".png") for i in range(1, NUMBER_OF_PLOTS + 1)]
    PIL_images_MID = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_MID_' + str(i) + ".png") for i in range(1, NUMBER_OF_PLOTS + 1)]
    PIL_images_FWD = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_FWD_' + str(i) + ".png") for i in range(1, NUMBER_OF_PLOTS + 1)]

    content = st.container()
    bottom_menu = st.columns((4, 1, 1))

    with bottom_menu[2]:
        total_pages = (
            NUMBER_OF_PLOTS
        )
        current_page = st.number_input(
            "Page", min_value=1, max_value=total_pages, step=1
        )
    with bottom_menu[1]:
        current_position = st.selectbox(
            'Choose position',
            ('All positions', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards')
        )
    with bottom_menu[0]:
        st.markdown(f"Page **{current_page}** of **{total_pages}** ")
    
    if current_position == "All positions":
        content.image(PIL_images_all[current_page - 1], caption='Point predictions for next gameweek')
    elif current_position == "Goalkeepers":
        content.image(PIL_images_GK[current_page - 1], caption='Point predictions for next gameweek')
    elif current_position == "Defenders":
        content.image(PIL_images_DEF[current_page - 1], caption='Point predictions for next gameweek')
    elif current_position == "Midfielders":
        content.image(PIL_images_MID[current_page - 1], caption='Point predictions for next gameweek')
    else:
        content.image(PIL_images_FWD[current_page - 1], caption='Point predictions for next gameweek')
    