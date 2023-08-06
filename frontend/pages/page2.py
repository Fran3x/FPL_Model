import streamlit as st
from PIL import Image
import os

@st.cache(allow_output_mutation=True)
def load_image(path):
    image = Image.open(path)
    return image

def page2():
    # st.title("Fantasy Premier League point predictions")
    
    plot_dir = "D:/PulpitE/FPL_ML/plottable/"
    plottable_images = os.listdir(plot_dir)
    
    plots_all = sum('predictions_plot_All_' in s for s in plottable_images)
    plots_gk = sum('predictions_plot_GK_' in s for s in plottable_images)
    plots_def = sum('predictions_plot_DEF_' in s for s in plottable_images)
    plots_mid = sum('predictions_plot_MID_' in s for s in plottable_images)
    plots_fwd = sum('predictions_plot_FWD_' in s for s in plottable_images)
    
    print(plots_all, plots_gk, plots_def, plots_mid, plots_fwd)
    
    for i in plottable_images:
        print(i)
    
    NUMBER_OF_PLOTS = 1
    
    PIL_images_all = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_All_' + str(i) + ".png") for i in range(1, plots_all + 1)]
    PIL_images_GK = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_GK_' + str(i) + ".png") for i in range(1, plots_gk + 1)]
    PIL_images_DEF = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_DEF_' + str(i) + ".png") for i in range(1, plots_def + 1)]
    PIL_images_MID = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_MID_' + str(i) + ".png") for i in range(1, plots_mid + 1)]
    PIL_images_FWD = [load_image('D:/PulpitE/FPL_ML/plottable/predictions_plot_FWD_' + str(i) + ".png") for i in range(1, plots_fwd + 1)]

    content = st.container()
    bottom_menu = st.columns((4, 1, 1))
    
    def get_total_pages(current_position):
        if current_position == "All positions":
            return NUMBER_OF_PLOTS
        elif current_position == "Goalkeepers":
            return NUMBER_OF_PLOTS
        elif current_position == "Defenders":
            return NUMBER_OF_PLOTS
        elif current_position == "Midfielders":
            return NUMBER_OF_PLOTS
        return NUMBER_OF_PLOTS
        
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
    