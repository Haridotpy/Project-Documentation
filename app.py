import streamlit as st

import requests

from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie




def display_images(images):
    st.text("The Notebook for project with examples for Plant Image")
    for image in images:
        st.image(image, caption="Image", use_column_width=True)






def download_code(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as notebook_file:
        notebook_content = notebook_file.read()

    st.download_button(
        label="Download Code",
        data=notebook_content.encode("utf-8"),
        key="download_code",
        file_name="autoencoder.ipynb",
        mime="application/octet-stream",
    )






# Set page configuration
st.set_page_config(page_title="Generative AI", page_icon=":graduation_cap:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: red;">Generative AI - Floor Plan Generator</h1>
        <br>
    </div>
    """,
    unsafe_allow_html=True,
)

# Navigation bar
selected_nav = option_menu(
    menu_title=None,
    options=["Home", "About Us", "Explorer","video","Contact Us"],
    icons=["house", "person-badge", "book", "flag"],
    default_index=1,
    orientation="horizontal",
)



# Assets
lottie_coding = "https://lottie.host/37ba51a6-3953-4bf7-a72b-09bd2a22ab3b/yHsfbMKPn1.json"

# Header Section
with st.container():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Welcome to GAN Floor Plan Generation Team</h2>
            <p>Generation of new floor plan images using GAN and Autoencoder .</p>
            <p><strong>Mentor:</strong> Prof. Dr. Deivamani M</p>
            <p><strong>Industry Expert:</strong> Mr. Muthumani M</p>
            <p>Visit our Github Page by clicking <a href="https://github.com/Haridotpy/Gan_6" target="_blank">here</a></p>
            <p>For Project Report Click <a href="https://drive.google.com/drive/u/0/folders/16C535f8dN7vIkaGtdpprTSQMs_nQeoQI" target="_blank">here</a><p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

# Content Section
if selected_nav == "Home":
    # Home content
    st_lottie(lottie_coding, height=300, key="coding")

elif selected_nav == "About Us":
    st.markdown(
        """
        <div style="text-align: center;">
            <h2><b>About Us</b></h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Styling for the avatars and brief info
    avatar_style = """
    <style>
        img {
            border-radius: 50%;
            box-shadow: 0 0 15px 0 rgba(0, 0, 0, 0.3);
            margin: 10px auto 0;
            display: block;
        }
        .avatar-container {
            text-align: center;
            display: block;
            margin: auto;
            width: 100%;
        }
        .avatar-link {
            color: #4CAF50;
            text-decoration: none;
            font-weight: bold;
            display: block;
        }
    </style>
"""

    st.markdown(avatar_style, unsafe_allow_html=True)

    # Dummy avatars and brief info
    col1, col2, col3 = st.columns(3)

    # Define the target URLs for each image
    url_hari = "https://github.com/Haridotpy"
    url_krishna= "https://github.com/Venkatakrishnan-M"
    url_shiva = "https://github.com/Haridotpy"

    # Use markdown and HTML to create the hyperlinks with styling
    with col1:
        st.image("image/avatar.png", use_column_width="auto")
        st.markdown(
            f"<div class='avatar-container'><a class='avatar-link' href='{url_hari}'>Harihara Subramanian K</a><p>2022179046</p><p>parikrish03@gmail.com</p></div>",
            unsafe_allow_html=True,
        )
        with st.expander("Expand to know more about me"):
            st.write(
                "Greetings! I'm Harihara Subramanian K, a dedicated individual with a keen interest in contributing to the growth of companies through the application of my technical skills"
                "My journey is fueled by a strong passion for problem-solving, and I possess an insatiable desire to continually learn and adapt to emerging technologies."
            )

    with col2:
        st.image("image/avatar.png", use_column_width="auto")
        st.markdown(
            f"<div class='avatar-container'><a class='avatar-link' href='{url_krishna}'>VenkataKrishnan M</a><p>2022179047</p><p>krishnamurali2001@gmail.com</p></div>",
            unsafe_allow_html=True,
        )
        with st.expander("Expand to know more about me"):
            st.write(
                "Hello there! I'm VenkataKrishnan B, a proactive and versatile graduate student pursuing a Master's in Computer Applications (MCA). My enthusiasm for contributing my technical skills and passion for innovation is what sets me apart."
                "Having a background in Physics has added a unique dimension to my approach, blending analytical thinking with a strong foundation in programming. I am dedicated to continuous learning and growth in the dynamic field of technology, aiming to bring a fresh perspective to every challenge I encounter."
            )

    with col3:
        st.image("image/avatar.png", use_column_width="auto")
        st.markdown(
            f"<div class='avatar-container'><a class='avatar-link' href='{url_shiva}'>Shiva Arjun V</a><p>2022179048</p><p>ShivaArjun@gmail.com</p></div>",
            unsafe_allow_html=True,
        )
        with st.expander("Expand to know more about me"):
            st.write(
                "I am Feeling free to delve into the details of my journey, showcasing a combination of academic prowess and a genuine passion for making a positive impact through technology."
                  "I look forward to embracing new opportunities and pushing the boundaries of what's possible in the world of computing"
            )

    st.write("\n\n")

    st.markdown(
        """
        <div style="text-align: center;">
            <p>We're a team of passionate students from the College of Engineering, Anna University, on a collective journey pursuing our Master of Computer Applications. Throughout our academic endeavors, we've been fortunate to receive guidance from esteemed mentors – Dr. Deivamani M, an Assistant Professor, and Mr. Muthumani M, an Industry Expert.
Collaboratively, we've immersed ourselves in the realm of Artificial Intelligence, channeling our efforts towards the enhancement of knowledge and skills. Our focus has been on the dynamic domains of Generative Adversarial Networks (GANs) and Autoencoders, where we've engaged in hands-on exploration and application.
This academic journey has been a stimulating experience, providing us with opportunities to delve into the technologies that shape the future. We're excited to share our insights, discoveries, and the outcomes of our collaborative efforts in the field of AI.
</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Project section



elif selected_nav == "Explorer":


    notebook_path = "files/autoencoder.ipynb"
    st.title("Donwload the code by clicking download button")
    download_code(notebook_path)
    images = ["image/img1.png", "image/img2.png", "image/img3.png", "image/img4.png","image/img5.png","image/img6.png","image/img7.png"]
    display_images(images)

#Hari Mark Here
elif selected_nav == "video":
    st.title("Explanation video ")
    st.video("https://www.youtube.com/watch?v=Nnrwh7807r4")

elif selected_nav == "Contact Us":
    # Contact Us content
    st.markdown(
        """
        <div style="text-align: center;">
            <h2><b>Contact Us</b></h2>
            <p>For any inquiries, please contact us at the following email addresses</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    #hari mark here
    st.markdown(
        """
        <div style="text-align: center;">
            <p><b>General Inquiries:</b> parikrish03@gmail.com</p>
            <p><b>Technical Support:</b> </p>
            <p><b>Project Related Queries:</b>krishnamurali2001@gmail.com</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Add more email IDs as needed

# Add smooth scrolling to the selected section
st.markdown(
    f"""
    <style>
        a[name="{selected_nav.lower().replace(' ', '_')}"] {{
            visibility: hidden;
        }}
        #{selected_nav.lower().replace(' ', '_')} {{
            visibility: visible;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(f'<a name="{selected_nav.lower().replace(" ", "_")}"></a>', unsafe_allow_html=True)
