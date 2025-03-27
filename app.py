import streamlit as st
import os

# Set the title of the app
st.title("Media Viewer App")

# Display images
st.header("Images")
image_folder = "media/images"  # Change this to your actual folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg'))]

for img in image_files:
    st.image(os.path.join(image_folder, img), caption=img)

# Display videos
st.header("Videos")
video_folder = "media/videos"  # Change this to your actual folder
video_files = [f for f in os.listdir(video_folder) if f.endswith(('mp4', 'mov', 'avi'))]

for vid in video_files[:2]:  # Display only two videos
    st.video(os.path.join(video_folder, vid))
