import streamlit as st
import pickle
# from PIL import Image
# import base64



DT_model=pickle.load(open('DT_model.pkl','rb'))
RF_model=pickle.load(open('RF_model.pkl','rb'))




def classify(result):
    if result == 'jogging':
        image = Image.open('jog.jpg')
        # st.image(image, caption='Jogging',use_column_width=True)
        st.image(image,use_column_width=True)
        html_temp = """
        <div style="background-color:#9771E9 ;padding:10px">
        <h2 style="color:white;text-align:center;">Jogging</h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
    elif result == 'walking':
        image = Image.open('walk.jpg')
        # st.image(image, caption='Jogging',use_column_width=True)
        st.image(image,use_column_width=True)
        html_temp = """
        <div style="background-color:green ;padding:10px">
        <h2 style="color:white;text-align:center;">Walking</h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
    elif result == 'sitting':
        image = Image.open('sit.jpg')
        # st.image(image, caption='Jogging',use_column_width=True)
        st.image(image,use_column_width=True)
        html_temp = """
        <div style="background-color:green ;padding:10px">
        <h2 style="color:white;text-align:center;">Sitting</h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
    elif result == 'standing':
        image = Image.open('std.jpg')
        # st.image(image, caption='Jogging',use_column_width=True)
        st.image(image,use_column_width=True)
        html_temp = """
        <div style="background-color:green ;padding:10px">
        <h2 style="color:white;text-align:center;">Standing</h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
    elif result == 'upstairs':
        image = Image.open('ups.jpg')
        # st.image(image, caption='Jogging',use_column_width=True)
        st.image(image,use_column_width=True)
        html_temp = """
        <div style="background-color:green ;padding:10px">
        <h2 style="color:white;text-align:center;">Upstairs</h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
    else:
        image = Image.open('dws.jpg')
        # st.image(image, caption='Jogging',use_column_width=True)
        st.image(image,use_column_width=True)
        html_temp = """
        <div style="background-color:green ;padding:10px">
        <h2 style="color:white;text-align:center;">Downstairs</h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        



def main():
    # st.set_page_config(page_title='HOLA')
    # hide_streamlit_style = """
    #         <style>
    #         #MainMenu {visibility: hidden;}
    #         footer {visibility: hidden;}
    #         </style>
    #         """
    # st.markdown(hide_streamlit_style, unsafe_allow_html=True) 





    # main_bg = "background.jpg"
    # main_bg_ext = "jpg"

    # side_bg = "background.jpg"
    # side_bg_ext = "jpg"

    # st.markdown(
    # f"""
    # <style>
    # .reportview-container {{
    #     background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    # }}
    # .sidebar .sidebar-content {{
    #     background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    # }}
    # </style>
    # """,
    # unsafe_allow_html=True
    # )


    html_temp = """
    <div style="background-color:#000000 ;padding:10px">
    <h2 style="color:white;text-align:center;">Motion Detection</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Decision Tree','Random Forest']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    f1=st.slider('Select attitude.roll', -3.14159, 3.14158)
    f2=st.slider('Select attitude.pitch', -1.56997, 1.56717)
    f3=st.slider('Select attitude.yaw', -3.14159, 3.14159)
    f4=st.slider('Select gravity.x', -0.99982, 1.0)
    f5=st.slider('Select gravity.y', -1.0, 1.0)
    f6=st.slider('Select gravity.z', -1.0, 1.0)
    f7=st.slider('Select rotationRate.x', -17.36579, 10.46806)
    f8=st.slider('Select rotationRate.y', -18.41441, 17.54312)
    f9=st.slider('Select rotationRate.z', -12.15124, 11.43624)
    f10=st.slider('Select userAcceleration.x', -6.36926, 7.12079)
    f11=st.slider('Select userAcceleration.y',-5.67359, 7.32272)
    f12=st.slider('Select userAcceleration.z', -7.74348, 8.12536)
    f13=st.slider('Select subject', 1, 24)


    inputs=[[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]]
    if st.button('Classify'):
        if option=='Decision Tree':
            st.success((DT_model.predict(inputs))[0])
            # classify((DT_model.predict(inputs))[0])
        else:
            st.success((RF_model.predict(inputs))[0])


    





    # feature_choice2 = st.sidebar.multiselect("Plot Size",result)
    # if st.button('Find Blueprint'):
    #     if feature_choice2 == '3-marla':



if __name__=='__main__':
    main()