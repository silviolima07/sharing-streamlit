import streamlit as st

from PIL import Image

def main():
    """ Sharing Streamlit """
    
 
    html_page = """
    <div style="background-color:red;padding=50px">
        <p style='color:white;text-align:center;font-size:30px;font-weight:bold'>Streamlit Sharing</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)    

    image = Image.open("aguia6.jpg")
    st.image(image,caption="",use_column_width=True)
    
    image1 = Image.open("aguia2.jpg")
    st.image(image1,caption="",use_column_width=True)

    image2 = Image.open("aguia3.jpg")
    st.image(image2,caption="",use_column_width=True)

    image3 = Image.open("aguia4.jpg")
    st.image(image3,caption="",use_column_width=True)

    image4 = Image.open("aguia8.jpg")
    st.image(image4,caption="",use_column_width=True)


if __name__ == '__main__':
    main()

     
