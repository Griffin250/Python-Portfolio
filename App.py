#import requests
import streamlit as st
#from streamlit_lottie import st-lottie

with st.container():
    st.subheader("Hey am Isiah Griffin :wave:")
    st.title("A web devloper from Norway")


    st.write("I am an IT engineer, specialising in Web Development, UI/UX Designing and Media Production with a strong background in Cybertech and AI.")
    st.write("My goal is to simplify the digital experience for users and build memorable, engaging, and efficient digital products.")

    st.write("For more info, visit me at [griffintechs.site](https://griffin250.github.io/IsiahTuyisenge/)")

#-----Load Assets--------
lottie_coding = "https://lottie.host/7a9b69e6-8a49-4e40-ac96-b64afbf068a4/Bj6EbPVHSN.json"
st.write("----")
st.header("What i Do")
left_column, right_column = st.columns(2)
with left_column:
    st.write("##")
    st.subheader("Web Designing")
    st.write(
        """
    - I specialize in crafting visually appealing and user-friendly websites that work seamlessly on all devices.
    -  From business websites to portfolios and blogs.Our web design service brings your online vision to life with precision and creativity.
        """
     )
    st.write("[Learn more >](griffintechs.site)")

with right_column:
    st.write("##")
    st.subheader("UI/UX Designing")
    st.write(
       """
    - I specialize in UI/UX design, crafting user-centric digital experiences that are both visually appealing and functionally intuitive.
    - My goal is to enhance user satisfaction and help your brand succeed in the digital world.
    - I specialize in crafting visually appealing and user-friendly mobile applications.
       """
    )
    st.write("[Learn more >](griffintechs.site)")