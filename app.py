import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Yash Bhatt", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
profile_pic = Image.open("images/profile_pic.jpg")
project_1 = Image.open("images/project_1.png")
linkedin_link = "https://www.linkedin.com/in/er-yash-bhatt/"
github_link = "https://github.com/DataWizard-Yash"
kaggle_link = "https://www.kaggle.com/dsyashbhatt"
medium_link = "https://medium.com/@datawizardyash"
instagram_link = "abc"


# ---- WHAT I DO ----
with st.container():
    left_column, right_column = st.columns([2,1])
    with left_column:
        # Assign the content to a variable
        content = """
        # Hi, I am  Yash Bhatt :wave:

        Highly motivated and diligent Software Engineer with a strong passion for Data Science and Analytics.

        ## About Me

        I hold a Bachelor's degree in Computer Engineering and am currently pursuing a Master's degree in Data Science. With a solid foundation in both theory and practical application, I am well-equipped to tackle complex data challenges.

        ## Expertise

        - Programming Languages: Python, Java, HTML, JavaScript, R, C, C++
        - Databases: MySQL, MongoDB, kaggle
        - Technologies: AWS, Docker
        - Other Skills: SQL, Big Data, NoSQL, technical blog writing

        ## Achievements

        As a Software Engineer, I have successfully delivered exceptional results in diverse projects. Some highlights include:

        - Developed a machine learning library to eliminate duplicate records, seamlessly integrating it into Python APIs for Android and iOS applications.
        - Contributed to logistics and supply chain projects by developing predictive models for demand forecasting and route optimization.

        ## Career Aspirations

        I am actively seeking a role as a Data Scientist or Data Analyst, where I can leverage my expertise and practical experience to solve complex business problems using data-driven insights. With strong teamwork, coordination, and leadership skills, I thrive in collaborative environments and consistently drive projects towards success.

        ## Continuous Growth

        I am committed to staying updated with the latest trends and technologies in the industry. By embracing innovation, efficiency, and data-driven decision-making, I strive to make a significant impact in any organization I work with.

        Thank you for visiting my portfolio website. Please feel free to explore further and don't hesitate to reach out for any inquiries or collaboration opportunities. Let's innovate and make data work for us!
        """

        # Render the content using Streamlit Markdown
        st.markdown(content)


    with right_column:
        st.image(profile_pic)

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(project_1)
    with text_column:
        st.subheader("Credit Card Fraud Detection Project")
        st.write(
            """
            The Credit Card Fraud Detection project is an implementation of a machine learning model
            to detect fraudulent transactions in credit card data. The project aims to address the
            challenge of identifying fraudulent activities and preventing financial losses for
            credit card companies and their customers.

            The repository contains the complete code and resources for the project.
            """
        )
        st.markdown("[Github repo...](https://github.com/DataWizard-Yash/credit-card-fraud-detection)")


# ---- HTML -----
# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/yashbhatt.datascience@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    linkedin_icon = """
    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
    </svg>
    """
    kaggle_icon = """
<svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" viewBox="0 0 24 24"><path fill="currentColor" d="M.102 7.348c-.068 0-.102.034-.102.102v6.752c0 .068.034.102.102.102h.705c.068 0 .103-.034.103-.103v-1.48l.418-.4l1.502 1.91a.184.184 0 0 0 .143.072h.909c.048 0 .075-.013.082-.04c.013-.041.006-.075-.02-.102l-1.982-2.462l1.9-1.839c.02-.02.023-.05.01-.092c-.014-.034-.041-.05-.082-.05h-.94c-.047 0-.095.023-.143.07L.91 11.608V7.45c0-.068-.035-.102-.103-.102zm18.042 0c-.068 0-.102.034-.102.102v6.752c0 .068.034.101.102.101h.705c.068 0 .102-.034.102-.102V7.45c0-.068-.034-.102-.102-.102zM5.961 9.625c-.565 0-1.11.181-1.634.542c-.055.054-.065.102-.031.143l.368.52c.027.048.071.055.133.021c.394-.272.783-.409 1.164-.409c.293 0 .516.09.669.266a.84.84 0 0 1 .2.644c-.661.068-1.155.15-1.482.245c-.83.238-1.246.691-1.246 1.358c0 .422.153.77.46 1.042c.313.266.684.398 1.113.398c.47 0 .855-.112 1.154-.337v.143c0 .069.038.102.113.102h.704c.068 0 .102-.033.102-.102v-2.829c0-.66-.224-1.14-.674-1.44c-.306-.205-.677-.307-1.113-.307zm4.322 0c-.674 0-1.194.263-1.562.787c-.313.436-.47.967-.47 1.594c0 .66.163 1.208.49 1.644c.375.497.892.745 1.553.745c.531 0 .957-.132 1.277-.398v.531c0 .858-.413 1.287-1.236 1.287c-.361 0-.732-.19-1.114-.572a.098.098 0 0 0-.071-.03a.11.11 0 0 0-.082.03l-.48.48c-.04.062-.038.113.01.154c.136.115.256.212.358.29c.102.079.19.142.265.19c.354.197.729.296 1.124.296c.68 0 1.207-.193 1.578-.577c.371-.385.557-.949.557-1.69V9.82c0-.068-.034-.102-.102-.102h-.705c-.069 0-.102.034-.102.102v.204c-.348-.266-.777-.399-1.287-.399zm4.803 0c-.675 0-1.195.263-1.563.787c-.313.436-.47.967-.47 1.594c0 .66.163 1.208.49 1.644c.375.497.892.745 1.553.745c.531 0 .957-.132 1.277-.398v.531c0 .858-.412 1.287-1.236 1.287c-.361 0-.732-.19-1.114-.572a.098.098 0 0 0-.071-.03a.11.11 0 0 0-.082.03l-.48.48c-.04.062-.037.113.01.154c.136.115.256.212.358.29c.102.079.19.142.266.19c.354.197.728.296 1.123.296c.681 0 1.207-.193 1.578-.577c.371-.385.557-.949.557-1.69V9.82c0-.068-.034-.102-.102-.102h-.705c-.068 0-.102.034-.102.102v.204c-.348-.266-.777-.399-1.287-.399zm6.745 0c-.653 0-1.185.211-1.593.634c-.443.463-.664 1.028-.664 1.695c0 .709.225 1.29.674 1.747c.463.463 1.042.694 1.737.694c.646 0 1.215-.183 1.705-.551c.055-.041.055-.088 0-.143l-.48-.49c-.04-.041-.092-.041-.153 0c-.3.21-.637.316-1.011.316c-.423 0-.773-.119-1.052-.357a1.318 1.318 0 0 1-.43-.838h3.32c.068 0 .102-.034.102-.102l.01-.224c.035-.688-.166-1.26-.602-1.717a2.075 2.075 0 0 0-1.563-.664zm-.02.787a1.2 1.2 0 0 1 .837.317c.246.21.371.473.378.786h-2.461c.06-.327.207-.593.439-.797c.231-.204.5-.306.807-.306zm-11.425.102c.62 0 1.014.218 1.185.654v1.685c-.17.436-.576.654-1.216.654c-.313 0-.569-.099-.766-.296c-.266-.252-.398-.654-.398-1.206c0-.994.398-1.491 1.195-1.491zm4.802 0c.62 0 1.015.218 1.185.654v1.685c-.17.436-.576.654-1.216.654c-.313 0-.568-.099-.766-.296c-.265-.252-.398-.654-.398-1.206c0-.994.398-1.491 1.195-1.491zm-8.359 1.655v1.021c-.286.286-.667.412-1.144.378a.88.88 0 0 1-.45-.158a.516.516 0 0 1-.224-.363c-.034-.266.116-.47.45-.613c.245-.109.7-.197 1.368-.265z"/></svg>    """

    github_icon = """
        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
        <path d="M8 0C3.58 0 0 3.582 0 8.004c0 3.54 2.29 6.53 5.47 7.59.4.08.55-.17.55-.38 0-.19-.007-.82-.012-1.49-2.225.48-2.695-.54-2.695-.54-.365-.93-.89-1.18-.89-1.18-.725-.49.055-.48.055-.48.805.055 1.23.805 1.23.805.72 1.23 1.88.87 2.335.665.07-.525.28-.87.51-1.07-1.785-.2-3.65-.89-3.65-3.95 0-.87.31-1.58.815-2.14-.08-.205-.355-1.02.08-2.125 0 0 .67-.215 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.089 2-.27 1.53-1.035 2.2-.82 2.2-.82.435 1.105.165 1.92.08 2.125.505.56.815 1.27.815 2.14 0 3.065-1.87 3.745-3.655 3.945.285.245.54.73.54 1.475 0 1.065-.01 1.925-.01 2.185 0 .21.145.46.55.38C13.715 14.53 16 11.54 16 8.004 16 3.582 12.42 0 8 0z"/>
        </svg>
    """

    medium_icon = """
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-medium" viewBox="0 0 16 16">
  <path d="M9.025 8c0 2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8zm4.95 0c0 2.34-1.01 4.236-2.256 4.236-1.246 0-2.256-1.897-2.256-4.236 0-2.34 1.01-4.236 2.256-4.236 1.246 0 2.256 1.897 2.256 4.236zM16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795z"/>
</svg>
    """
    instagram_icon = """
        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-instagram" viewBox="0 0 16 16">
  <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"/>
</svg>
    """


# ---- CONTACT ----
with st.container():
    st.write("---")

    left_column, middle, right_column = st.columns([2,0.5,1])
    with left_column:
        st.header("Get In Touch With Me 📬")
        st.write("##")
        st.markdown(contact_form, unsafe_allow_html=True)
    with middle:
        st.empty()
    with right_column:
        st.header("Connect with me 🔗")
        st.write("#")
        st.markdown(
            f'<div style="display: flex; align-items: center;">'
            f'<a target="_blank" style="margin-right: 30px;"></a>'
            f'<a href="{linkedin_link}" target="_blank" style="margin-right: 20px;">{linkedin_icon}</a>'
            f'<a href="{github_link}" target="_blank" style="margin-right: 20px;">{github_icon}</a>'
            f'<a href="{kaggle_link}" target="_blank" style="margin-right: 20px;">{kaggle_icon}</a>'
            f'<a href="{medium_link}" target="_blank" style="margin-right: 20px;">{medium_icon}</a>'
            f'<a href="{instagram_link}" target="_blank" style="margin-right: 20px;">{instagram_icon}</a>'
            f'</div>',
            unsafe_allow_html=True
        )
        st.write("---")
        st.markdown('<p style="margin: 0;">Yash Bhatt</p>', unsafe_allow_html=True)
        st.markdown(
            '<p style="margin: 0;">1-pramukh nagar society, B/H Fortune Hotel, Opp. Parth School, 150 Feet Ring Road, Rajkot, 360004</p>',
            unsafe_allow_html=True)
        st.markdown('<p style="margin: 0;">+91 9974443533</p>', unsafe_allow_html=True)



