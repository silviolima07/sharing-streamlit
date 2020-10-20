import streamlit as st

from PIL import Image

def main():
    """ Sharing Streamlit """
    
 
    html_page = """
    <div style="background-color:red;padding=10px">
        <p style='color:white;text-align:center;font-size:20px;font-weight:bold'>Sharing</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)    

    image = Image.open("aguia2.jpg")
    st.sidebar.image(image,caption="",use_column_width=True)


if __name__ == '__main__':
    main()

     