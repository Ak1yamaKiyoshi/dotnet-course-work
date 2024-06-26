import streamlit as st
from streamlit_navigation_bar import st_navbar
import os
import src.pages as pg



st.set_page_config(initial_sidebar_state="collapsed")
parent_dir = os.path.dirname(os.path.abspath(__file__))

options = {
    "show_menu": False,
    "show_sidebar": False,
}
pages = ["Home", "Your Profile", "Search Anketes", "Likes"]
page = st_navbar(pages, options=options)

functions = {
    "Home": pg.landing_page,
    "Your Profile": pg.profile_page,
    "Search Anketes": pg.search_page,
    "Likes": pg.settings_page,
}

go_to = functions.get(page)
if go_to: go_to()