import os

# Define folder structure
folders = [
    "media",
    "media/images",
    "media/videos"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create required files
files = {
    "requirements.txt": "streamlit\n",
    "README.md": """# Streamlit Media Viewer

This is a simple Streamlit app that displays images and videos.

## Folder Structure
```
/your_project_directory
│-- streamlit_media_app.py  # Streamlit script
│-- /media
│   │-- /images
│   │-- /videos
│-- requirements.txt  # Dependencies
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run streamlit_media_app.py
   ```

## Deployment on Streamlit Community Cloud
1. Push your code to GitHub.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and sign in.
3. Select your repository and deploy the app.

Now your classmates can access the app online! 🚀
"""
}

# Write files
for file_name, content in files.items():
    with open(file_name, "w") as f:
        f.write(content)

print("Project structure created successfully!")
