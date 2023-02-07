import streamlit as st


# will display everything
st.write('Hello World')


# text format
st.header('This is header')

st.subheader("This is subheader")

st.caption('This is caption')

st.text("This is Text")

# markdown

st.markdown("""
# This is Title
## This is Header
### subheader1 
### subheader2 
Text
for *italic* use asterisk
for **bold** format use two asterisk
""")

# status elements
# success
st.success("This is success")
# warning
st.warning("This is warning")
# error
st.error("This is Error")


# display media
st.subheader("this is display Image")
st.image("./media/000001.jpg", caption="4 CAR")
