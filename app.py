import base64
import re
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Portfolio", layout="wide")


# Function to convert video file to base64
def get_video_base64(video_path):
  try:
    with open(video_path, "rb") as f:
      data = f.read()
    return base64.b64encode(data).decode("utf-8")
  except FileNotFoundError:
    return None


# Read HTML
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
  with open("script.js", "r", encoding="utf-8") as f:
    js_code = f.read()
except FileNotFoundError:
  try:
    with open("index.js", "r", encoding="utf-8") as f:
      js_code = f.read()
  except FileNotFoundError:
    pass

# Find video tag src and replace with base64 data
video_matches = re.findall(
    r'<video[^>]*src=["\']([^"\']+)["\']', html_code, re.IGNORECASE
)
if not video_matches:
  # Search inside <source src="..."> inside <video>
  video_matches = re.findall(
      r'<source[^>]*src=["\']([^"\']+)["\']', html_code, re.IGNORECASE
  )

for video_path in video_matches:
  base64_video = get_video_base64(video_path)
  if base64_video:
    # Determine mime type
    mime_type = "video/mp4"
    if video_path.endswith(".webm"):
      mime_type = "video/webm"
    base64_src = f"data:{mime_type};base64,{base64_video}"
    html_code = html_code.replace(video_path, base64_src)

full_code = f"<style>{css_code}</style>{html_code}<script>{js_code}</script>"

components.html(full_code, height=1000, scrolling=True)
