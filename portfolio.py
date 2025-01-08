import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key = api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

persona = """ You are Anshad AI bot. You help people answer questions about your self (i.e Anshad). 
Answer as if you are responding . dont answer in second or third person. If you don't know they answer you simply say "That's a secret"
Here is more info about Anshad:

Anshad UK is a Python-Djnago Full Stack Developer.He currently worked in Bridgeon Solution LLP.Anshad obtained his Batchelor's degree in 
Computer Science and Masters Degree in MCA from calicut university.

Anshad's Youtube Channel : https://www.youtube.com/in/CodeBit/
Anshad's Email : anshadu@gmail.com
Anshad's Instagram : https://www.instagram.com/in/anshaduk/
Anshad's Linkedin : https://www.linkedin.com/in/anshaduk/
Anshad's Github : https://github.com/anshaduk
"""


col1,col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Anshad UK")

with col2:
    st.image("images/profile.jpg")

st.title("Anshad's AI Bot")
user_question = st.text_input("Ask anything about me")
if st.button("ASK",use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title("")
col1,col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel.")
    st.write("- 400k+ Subscribers.")
    st.write("- Over 150 Free Tutorials.")
    st.write("- 15 Milloion + Viewers.")


with col2:
    st.video("https://www.youtube.com/watch?v=Ccu5b02LqFs")

st.write("")
st.title("My Setup")
st.image("images/g8.jpg",use_container_width=400)

st.write("")
st.title("My Skills")
st.slider("Programming",0,100,70)
st.slider("Teaching",0,100,65)
st.slider("Robotics",0,100,80)

st.file_uploader("Upload a file")

st.write("")
st.title("Gallery")
# col1,col2,col3 = st.columns(3)
# with col1:
#     st.image("images/g1.jpg")
#     st.image("images/g2.jpg")
#     st.image("images/g3.jpg")

# with col2:
#     st.image("images/g4.jpg")
#     st.image("images/g5.jpg")
#     st.image("images/g6.jpg")

# with col3:
#     st.image("images/g7.jpg")
#     st.image("images/g8.jpg")

images = [f"images/g{i}.jpg" for i in range(1,9)]

cols = st.columns(3)

for i,image in enumerate(images):
    with cols[i%3]:
        st.image(image)

st.write("")
st.write("CONTACT")
st.subheader("For any enquiries, please contact me at")
st.write("anshadu@gmail.com")

