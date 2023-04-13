import json
import requests  
import streamlit as st 
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu 
st.subheader("Hi,I am Kishor :wave")
st.title("Welcome")
st.write("[contact me >](https://www.linkedin.com/in/kishor-sahu-607092260/)")
with st.sidebar:
    selected=option_menu(
        menu_title= None,
        options=["HOME","IMAGE","VIDEO"],
        icons=["house","image","play"],
        menu_icon= "cast",
        default_index=0,
    )
def load_lottiefile(filepath: str):
   with open(filepath, "r") as f:
        return json.load(f)
      
def load_lottieurl(url: str):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_b1eyyihe.json")
st_lottie(lottie_hello, key="hello")

ioptions=" "
if selected=="IMAGE":
    ioptions=option_menu(menu_title=None,
    options=["Upload Image","click a pic"],
    icons=["file-earmark-arrow-up","camera"],
    default_index=0
    )

if  ioptions=="Upload Image":
        st.title('***Upload_your_Image***')
        img=st.file_uploader('',type=["png","jpg","jpeg"])
        if img is not None:
            st.image(img,caption='Here is the uploaded image')
    

if ioptions=="click a pic":
        st.title('***Capture_Image***')
        pic=st.camera_input("take your picture")
        pic_caption=st.text_input('***write_your_caption***')
        if pic is not None :
            st.write("#### here is your image ")
            st.image(pic,caption=pic_caption)


if selected =="VIDEO":
    st.title('***Upload_Video***')
    vid_caption=st.text_input('write your caption')
    vid=st.file_uploader('',type=["mp4"])
    if vid is not None:
        st.video(vid)
        st.caption(vid_caption)