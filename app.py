import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Portfolio", layout="wide")

# Read local HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# CSS / JS files if present
css_code = ""
try:
    with open("style.css", "r", encoding="utf-8") as f:
        css_code = f.read()
except FileNotFoundError:
    pass

js_code = ""
try:
    with open("index.js", "r", encoding="utf-8") as f:
        js_code = f.read()
except FileNotFoundError:
    pass

full_code = f"<style>{css_code}</style>{html_code}<script>{js_code}</script>"

components.html(full_code, height=1000, scrolling=True)
