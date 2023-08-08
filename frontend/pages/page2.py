import streamlit as st
from PIL import Image
import os

@st.cache(allow_output_mutation=True)
def load_image(path):
    image = Image.open(path)
    return image

@st.cache(allow_output_mutation=True)
def get_number_of_plots(plottable_images):
    plots_all = sum('predictions_plot_All_' in s for s in plottable_images)
    plots_gk = sum('predictions_plot_GK_' in s for s in plottable_images)
    plots_def = sum('predictions_plot_DEF_' in s for s in plottable_images)
    plots_mid = sum('predictions_plot_MID_' in s for s in plottable_images)
    plots_fwd = sum('predictions_plot_FWD_' in s for s in plottable_images)
    
    return plots_all, plots_gk, plots_def, plots_mid, plots_fwd

@st.cache(allow_output_mutation=True)
def get_images(plots_all, plots_gk, plots_def, plots_mid, plots_fwd):
    
    PIL_images_all = [load_image('plottable/predictions_plot_All_' + str(i) + ".png") for i in range(1, plots_all + 1)]
    PIL_images_GK = [load_image('plottable/predictions_plot_GK_' + str(i) + ".png") for i in range(1, plots_gk + 1)]
    PIL_images_DEF = [load_image('plottable/predictions_plot_DEF_' + str(i) + ".png") for i in range(1, plots_def + 1)]
    PIL_images_MID = [load_image('plottable/predictions_plot_MID_' + str(i) + ".png") for i in range(1, plots_mid + 1)]
    PIL_images_FWD = [load_image('plottable/predictions_plot_FWD_' + str(i) + ".png") for i in range(1, plots_fwd + 1)]
    
    return PIL_images_all, PIL_images_GK, PIL_images_DEF, PIL_images_MID, PIL_images_FWD


def page2():
    # st.title("Fantasy Premier League point predictions")
    
    plot_dir = ".\plottable"
    plottable_images = os.listdir(plot_dir)
    plots_all, plots_gk, plots_def, plots_mid, plots_fwd = get_number_of_plots(plottable_images)
    
    PIL_images_all, PIL_images_GK, PIL_images_DEF, PIL_images_MID, PIL_images_FWD = get_images(plots_all, plots_gk, plots_def, plots_mid, plots_fwd)
    
    def get_total_pages(current_position):
        if current_position == "All positions":
            return plots_all
        elif current_position == "Goalkeepers":
            return plots_gk
        elif current_position == "Defenders":
            return plots_def
        elif current_position == "Midfielders":
            return plots_mid
        return plots_fwd

    content = st.container()
    bottom_menu = st.columns((4, 1, 1))
    
    with bottom_menu[1]:
        current_position = st.selectbox(
            'Choose position',
            ('All positions', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards')
        )
    with bottom_menu[2]:
        total_pages = (
            get_total_pages(current_position)
        )
        current_page = st.number_input(
            "Page", min_value=1, max_value=total_pages, step=1
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
    