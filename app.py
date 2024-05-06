#Simple streamlit web platform to display the information

import streamlit as st
from PIL import Image


st.title('10K Insight')



option = st.selectbox('Select a Company to view its overall expenditure over the years', ['', 'APPL', 'DELL'])

image_paths = {
    'APPL': 'Charts/APPL_expenditure_chart.png',
    'DELL': 'Charts/DELL_expenditure_chart.png'
}


def display_image(option):
    image_path = image_paths.get(option)
    if image_path:
        image = Image.open(image_path)
        st.image(image, caption='', use_column_width=True)
    else:
        st.write('')


display_image(option)

st.markdown("---")
st.markdown("Understanding a company's overall expenditure plan is crucial because it shows a \n "
            "commitment to optimal resource and fund allocation. Furthermore, investors love this \n" 
            "approach since it shows a company's unwavering pursuit of growth and expansion, \n"
            "and not settling for anything less.")