import cv2
from PIL import Image
from sklearn.cluster import KMeans
import streamlit as st
import numpy as np
from collections import Counter
import math
import colorsys

def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)

def sort_colors(color_list):
    color_list.sort(key=get_hsv)
    return color_list

def get_text_color(hex_color):
    rgb = tuple(int(hex_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    brightness = (0.299*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2])
    return "black" if brightness > 150 else "white"

def main():
        
    st.set_page_config(layout="wide")
    hide_streamlit_style = """
    <style>
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
        header {visibility:hidden;}
    </style>

    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    main_container = st.container(width="stretch", height="content")
    col1,col2 = main_container.columns(2, gap="large")
    col1.markdown("""<h2>Input:</h2>""", unsafe_allow_html=True)
    col2.markdown("""<h2 style="
                  margin-bottom:28px;
                  ">
                  Dominant Colors:
                  </h2>""", unsafe_allow_html=True)

    uploaded_file = col1.file_uploader("Upload an image", type=["jpg", "jpeg", "png","svg","webp"])
    k = col1.number_input(label="Number of colors in palette", min_value=1, max_value=50, value=1)
    if uploaded_file is not None:
        
        col1.image(uploaded_file, width=300)

        image = cv2.imdecode(np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8),cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        
        pixels = image.reshape(-1, 3)

        # ---- 2. Apply K-Means ----
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)

        # Cluster centers (dominant colors)
        colors = kmeans.cluster_centers_.astype(int)

        # Count each label to get color frequency
        labels = kmeans.labels_
        counts = Counter(labels)

        # convert each array like [R,G,B] → tuple(R,G,B)
        colors_as_tuples = [tuple(map(int, c)) for c in colors]
        sorted_colors = sorted(zip(counts.values(), colors_as_tuples), reverse=True)
        colors_sorted = [c[1] for c in sorted_colors]

        hex_colors = ['#%02x%02x%02x' % tuple(c) for c in colors_sorted]
        num_cols = math.ceil(len(hex_colors)/10)
        cols = col2.columns(num_cols)
        colors = sort_colors(hex_colors)

        for i, color in enumerate(colors):
            col_index = i % num_cols 
            cols[col_index].markdown(
                f"""
                <div style="
                    background-color: {color};
                    border-radius: 10px;
                    padding:10px;
                    text-align: center;
                    color: {get_text_color(color)};
                    margin-bottom: 8px;
                ">
                    {color}
                </div>
                """,
                unsafe_allow_html=True
            )
        
        
        
        

if __name__ == "__main__":
    main()
