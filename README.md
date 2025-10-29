# 🎨 Dominant Color Extractor (Streamlit App)

This is a simple, interactive **Streamlit web app** that extracts and displays the **dominant colors** from any uploaded image using **K-Means clustering**. It provides a visually clean palette with both HEX and RGB values.

---

## 🚀 Features

- Upload any image (`.jpg`, `.jpeg`, `.png`, `.svg`, `.webp`)
- Automatically extracts dominant colors using **K-Means**
- Displays a color palette sorted by **hue**
- Adaptive text color for contrast on light/dark backgrounds
- Fully responsive **Streamlit layout**
- Custom CSS styling for a sleek 90vh centered design

---

## 🧠 How It Works

1. The uploaded image is read as a NumPy array and converted from BGR to RGB.
2. All pixels are reshaped into a 2D array for clustering.
3. The **K-Means algorithm** groups similar colors into `k` clusters.
4. The cluster centers are used as the dominant colors.
5. Colors are displayed in sorted HSV order with readable HEX and RGB codes.

---

## 🛠️ Installation

Clone the repository and install the dependencies.

```bash
git clone https://github.com/yourusername/dominant-color-extractor.git
cd dominant-color-extractor
pip install -r requirements.txt
```

**requirements.txt**

```
streamlit
opencv-python
scikit-learn
numpy
```

---

## ▶️ Running the App

Run the app using Streamlit:

```bash
streamlit run app.py
```

Then open your browser and go to:

```
http://localhost:8501
```

---

## 🖼️ Usage

1. Upload an image from your local machine.
2. Choose the number of dominant colors you want in the palette.
3. The app will automatically extract and display the colors.
4. Each color tile shows:
   - HEX code (e.g. `#aabbcc`)
   - RGB tuple (e.g. `rgb(170,187,204)`)

---

## 💡 Example Output

| Input Image | Extracted Palette |
|--------------|------------------|
| Example image here | Palette image here |

---

## 🧩 Technical Notes

- Uses `KMeans` from **scikit-learn** with a customizable number of clusters.
- The colors are sorted in HSV (Hue, Saturation, Value) order for a more natural palette flow.
- Adaptive text color ensures legibility on both light and dark color tiles.

