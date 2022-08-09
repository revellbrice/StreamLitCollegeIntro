#app.py
import app1
import app2
import app3
import streamlit as st
PAGES = {
    "Thorough Analysis": app1,
    "Alabama Analysis": app2,
    "North Carolinia Analysis": app3
}
st.markdown("<h1 style='text-align: center; color:black;'>College in the South</h1>", unsafe_allow_html=True)


st.sidebar.title('Content Listed')
selection = st.sidebar.selectbox("View Analysis", list(PAGES.keys()))
page = PAGES[selection]
page.app()