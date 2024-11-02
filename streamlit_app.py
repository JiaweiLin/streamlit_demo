import streamlit as st

home_page = st.Page("home.py", title="Home Page", icon=":material/home:")
about_us_page = st.Page("about_us.py", title="About Us", icon=":material/person:")

pg = st.navigation([home_page, about_us_page])
st.set_page_config(page_title="Demo Project", page_icon=":material/dashboard:")
pg.run()