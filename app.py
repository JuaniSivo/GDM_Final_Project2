import streamlit as st
import os

# Add logos
logo1_path = "media/logos/logo1.png"  # Change to the actual path of the first logo
logo2_path = "media/logos/logo2.png"  # Change to the actual path of the second logo

with st.sidebar:
    st.image(logo2_path)
    st.image(logo1_path)

# Set the title of the app
st.title("GDM Final Project - Group 1 ")

# Add a button to download the presentation
presentation_path = "media/presentation/presentation.pdf"  # Change this to your actual presentation path
with open(presentation_path, "rb") as file:
    btn = st.download_button(
        label="Download Presentation",
        data=file,
        file_name="presentation.pdf",
        mime="application/pdf"
    )

# Create tabs for Images and Videos
tab1, tab2 = st.tabs(["Images", "Videos"])

# Images tab
with tab1:
    st.header("Images")
    image_folder = "media/images"  # Change this to your actual folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg'))]

    for img in image_files:
        st.image(os.path.join(image_folder, img), caption=img, use_container_width=True)

# Videos tab
with tab2:
    st.header("Videos")
    video_folder = "media/videos"  # Change this to your actual folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith(('mp4', 'mov', 'avi'))]

    for vid in video_files[:2]:  # Display only two videos
        st.video(os.path.join(video_folder, vid))
