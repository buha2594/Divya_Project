import streamlit as st
def set_bg_hack_url():

    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url('https://as1.ftcdn.net/v2/jpg/09/17/48/84/1000_F_917488467_WETs37DMEpMeeaGuXKHg4ei925SLlnlI.jpg');
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


title_style = """
<style>
h1 {
    text-align: center;
    color: red;
}
</style>
"""
st.markdown(title_style, unsafe_allow_html=True)


st.title("BookScape Management")
st.sidebar.success("Select a page above:")

set_bg_hack_url()
