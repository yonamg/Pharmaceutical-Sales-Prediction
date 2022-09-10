import user_overview_page
import prediction_page
import promotion_page
from PIL import Image
import imagegrid
import streamlit as st

st.title("Pharmacy Sales Data Analysis")
image = Image.open('../images/phrmacy.jpg')
st.image(image, caption="Pharmaceutical Data Analysis", use_column_width=True)
pages = {
     "Data Overview": imagegrid,
     "Promotion Effect on Stores": promotion_page,
     "Model prediction": prediction_page,
     "Pharmacy Overview page": user_overview_page

}

selection = st.sidebar.radio("Go to page", list(pages.keys()))

if selection=="Data Overview":
     imagegrid.image_grid()
if selection=="Promotion Effect on Stores":
     promotion_page.compare_test_train()
if selection=="Model prediction":
     prediction_page.prdict_app()
if selection=="Pharmacy Overview page":
     user_overview_page.app()