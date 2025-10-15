import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="F1 DNF Predictor",
    page_icon="🏎️",
    layout="wide"
)

st.title("🏁 Formula 1 Race DNF Predictor")
#st.image("images/f1_banner.jpg", use_column_width=True)

st.markdown("""
Welcome to the **F1 Race DNF Predictor App!**  
This tool predicts whether a driver will **Finish** or **DNF (Did Not Finish)** a race based on race details.

---

### 🔍 What you can do here:
- Explore race outcome predictions
- Test various drivers and constructors
- Analyze how factors like **grid position** and **age** affect the outcome

Use the sidebar to navigate to the **Prediction Page ➡️**
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Years of Data", "1950–2024")
with col2:
    st.metric("Total Drivers", "600+")
with col3:
    st.metric("Constructors", "170+")

st.info("Ready? Head to **Prediction Page** from the left sidebar 🚦")
