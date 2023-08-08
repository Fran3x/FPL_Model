import streamlit as st
import pandas as pd
import os

def page3():
    st.title("Model architecture")


    @st.cache(show_spinner=False)
    def load_data(file_path):
        dataset = pd.read_csv(file_path)
        return dataset


    @st.cache(show_spinner=False)
    def split_frame(input_df, rows):
        df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
        return df


    file_path = st.file_uploader("Select CSV file to upload", type=["csv"])
    if file_path:
        dataset = load_data(file_path)
        top_menu = st.columns(3)
        with top_menu[0]:
            sort = st.radio("Sort Data", options=["Yes", "No"], index=1)
        if sort == "Yes":
            with top_menu[1]:
                sort_field = st.selectbox("Sort By", options=dataset.columns)
            with top_menu[2]:
                sort_direction = st.radio(
                    "Direction", options=["⬆️", "⬇️"],
                )
            dataset = dataset.sort_values(
                by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True
            )
        pagination = st.container()

        bottom_menu = st.columns((4, 1, 1))
        with bottom_menu[2]:
            batch_size = st.selectbox("Page Size", options=[25, 50, 100])
        with bottom_menu[1]:
            total_pages = (
                int(len(dataset) / batch_size) if int(len(dataset) / batch_size) > 0 else 1
            )
            current_page = st.number_input(
                "Page", min_value=1, max_value=total_pages, step=1
            )
        with bottom_menu[0]:
            st.markdown(f"Page **{current_page}** of **{total_pages}** ")

        pages = split_frame(dataset, batch_size)
        pagination.dataframe(data=pages[current_page - 1], 
            #  use_container_width=True
        )