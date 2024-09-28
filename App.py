import requests
import streamlit as st
from streamlit_lottie import st_lottie

with st.container():
    st.subheader("Hey am Isiah Griffin :wave:")
    st.write("This is to Test for Changes made in the Repo!")
    st.title("A web devloper from Norway")

    st.write("I am an IT engineer, specialising in Web Development, UI/UX Designing and Media Production with a strong background in Cybertech and AI.")
    st.write("My goal is to simplify the digital experience for users and build memorable, engaging, and efficient digital products.")

    st.write("For more info, visit me at [griffintechs.site](https://griffin250.github.io/IsiahTuyisenge/)")

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

    st.subheader("UI/UX Designing")
    st.write(
       """
    - I specialize in UI/UX design, crafting user-centric digital experiences that are both visually appealing and functionally intuitive.
    - My goal is to enhance user satisfaction and help your brand succeed in the digital world.
    - I specialize in crafting visually appealing and user-friendly mobile applications.
       """
    )
    st.write("[Learn more >](griffintechs.site)")

with right_column:
    st.write("##")

st.write("---")
#------Contact form----------------
st.title("Get in Touch with Me!")
contact_form = """
<form action="https://formsubmit.co/isiahgriffin777@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Enter your Name" required>
     <input type="email" name="email"placeholder="Enter your E-mail" required><br><br>
      <textarea id="message" type="message" class="textarea" placeholder="Enter your Message here....!"></textarea><br>
     <button type="submit">Send</button>
</form>
    """
st.markdown(contact_form, unsafe_allow_html=True)
st.empty()

# import local css file for the acontact form.
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</stye>", unsafe_allow_html=True)
local_css("styles/styles.css")