 import streamlit as st

# Set page configuration
st.set_page_config(page_title="Firebox - Movie Platform", layout="wide")
st.title("🔥 Firebox Movie Platform")
st.markdown("### Choose a category from the sidebar to watch full videos!")

# Sidebar selection
category = st.sidebar.selectbox(
    "Select a Category",
    ["Bollywood", "Hollywood", "Horror", "Sci-Fi", "Thriller", "Relaxing Videos", "Vlogs", "Normal Movies"]
)

# Define full movies with direct URLs (YouTube or Dailymotion)
movie_data = {
    "Bollywood": [
        {
            "title": "Hansa (2012)",
            "thumbnail": "https://img.youtube.com/vi/7qSV-RXUKuc/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=7qSV-RXUKuc"
        }
    ],
    "Hollywood": [
        {
            "title": "The Gold Rush (1925)",
            "thumbnail": "https://img.youtube.com/vi/VjVJNp_lEl8/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=VjVJNp_lEl8"
        },
        {
            "title": "The Kid (1921)",
            "thumbnail": "https://img.youtube.com/vi/vwp6UP4pnbI/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=vwp6UP4pnbI"
        }
    ],
    "Horror": [
        {
            "title": "The Conjuring 3: The Devil Made Me Do It (Full Movie)",
            "thumbnail": "https://i.ytimg.com/vi/2O9K2lFnA7w/hqdefault.jpg",  # Placeholder image
            "full_movie_url": "https://www.dailymotion.com/video/x9e43kc"
        },
        {
            "title": "Veronica (2017) - Full Movie",
            "thumbnail": "https://i.ytimg.com/vi/QphzH2xF2vI/hqdefault.jpg",  # Placeholder image
            "full_movie_url": "https://www.dailymotion.com/video/x8skij8"
        }
    ],
    "Sci-Fi": [
        {
            "title": "The Giant Spider Invasion (1975)",
            "thumbnail": "https://img.youtube.com/vi/2wTQfpjD3lg/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=2wTQfpjD3lg"
        }
    ],
    "Thriller": [
        {
            "title": "Night Drive | Malayalam Thriller Movie (Subtitled)",
            "thumbnail": "https://img.youtube.com/vi/X6o82GAZJ7Y/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=X6o82GAZJ7Y"
        }
    ],
    "Relaxing Videos": [
        {
            "title": "Mahakatha - Ancient Chant for Positive Energy",
            "thumbnail": "https://img.youtube.com/vi/w8c3A2kjHfM/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=sPKeOEvU_Sc"
        },
        {
            "title": "Mahakatha - Hanuman Mantra",
            "thumbnail": "https://img.youtube.com/vi/zFHXTSjA2hM/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=zFHXTSjA2hM"
        }
    ],
    "Vlogs": [
        {
            "title": "Flying Beast - Trip to Dubai",
            "thumbnail": "https://img.youtube.com/vi/vxd5exMfF-U/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=vxd5exMfF-U"
        }
    ],
    "Normal Movies": [
        {
            "title": "Janta Hawaldar | Hindi Comedy Movie",
            "thumbnail": "https://img.youtube.com/vi/ayYmTx5E8os/hqdefault.jpg",
            "full_movie_url": "https://www.youtube.com/watch?v=ayYmTx5E8os"
        }
    ]
}

# Display movies based on selected category
selected_movies = movie_data.get(category, [])
cols = st.columns(3)

for idx, movie in enumerate(selected_movies):
    with cols[idx % 3]:
        st.image(movie["thumbnail"], use_container_width=True)
        st.markdown(f"**{movie['title']}**")
        st.link_button("▶️ Watch Now", url=movie["full_movie_url"])
