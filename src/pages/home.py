# How the Home page will look and what will it contain

import streamlit as st
from PIL import Image


def main():
    image = Image.open("asset/manu.jpeg")
    st.image(image)
    st.title("COVID-19 Dashboard")
    st.write(""" 
    This web API will analyse the trend and data of COVID-19 from the 
     John Hopkins github page
     """)

    st.markdown("## Symptoms")
    st.markdown(("* Fever or chills \n* Cough\n"
                 "* Shortness of breath or difficulty breathing\n"
                 "* Fatigue\n"
                 "* Muscle or body aches\n"
                 "* Headache\n"
                 "* Loss of taste or smell\n"
                 "* Sore throat\n"
                 "* Congestion or runny nose\n"
                 "* Nausea or vomiting\n"
                 "* Diarrhea"))

    st.markdown("## Vaccines")
    st.markdown("Track [here](https://www.covid19india.org/)")

    st.markdown("## Resources")
    st.markdown(("* [World Health Organization](https://www.who.int/maternal_child_adolescent/links/covid19-resources"
                 "-and-support-for-mncah-and-ageing/en/)\n "
                 "* [Center for Disease Control](https://www.cdc.gov/coronavirus/2019-ncov/index.html)\n"
                 "* [National Institute of Health](https://www.nih.gov/coronavirus)"))