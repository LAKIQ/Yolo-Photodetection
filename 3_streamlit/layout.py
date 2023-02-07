import streamlit as st

st.set_page_config(page_title="Layouts", layout="wide")
st.title('Streamlit layout')


# sidebar
sidebar = st.sidebar
sidebar.write("Hello")

# columns
col1, col2, col3 = st.columns(3)
with col1:
    st.warning("this is Columns1")
with col2:
    st.success("this is Columns2")

# table
st.header("this is table Display in tabs")
tab1, tab2, tab3 = st.tabs(['A', "b", "V"])
with tab1:
    st.warning("this is tab1")
with tab2:
    st.success("this is tab2")
