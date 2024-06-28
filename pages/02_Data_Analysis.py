import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""
# Spain Mobility Data Analysis 
            \n
            \n\n
""")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ac felis donec et odio pellentesque diam volutpat commodo. Egestas diam in arcu cursus euismod quis. Pretium viverra suspendisse potenti nullam ac tortor vitae purus faucibus. A lacus vestibulum sed arcu non odio euismod lacinia. Ac ut consequat semper viverra. Sapien et ligula ullamcorper malesuada proin libero. Varius morbi enim nunc faucibus a pellentesque sit amet. Mi in nulla posuere sollicitudin aliquam. Arcu cursus vitae congue mauris rhoncus. Elit pellentesque habitant morbi tristique senectus. Dui nunc mattis enim ut. Nunc pulvinar sapien et ligula ullamcorper malesuada. Vel facilisis volutpat est velit egestas dui id ornare arcu. Sed viverra ipsum nunc aliquet bibendum.")

with st.container():
    st.header("Mobility and Median Income across Spain")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/network.png", caption="Mobility network between Spanish districts. Districts are represented as nodes, connected by the total number of trips between them for the first week of September 2023.")
    with col2:
        st.image("images/districts_revenue.png", caption="Heatmap of median revenue per consumption unit of Spanish districts. ")
    col3, col4 = st.columns(2)
    with col3:
        pass
    with col4:
        pass

with st.container():
    st.header("Mobility and Median Income across Spain")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/network.png", caption="Mobility network between Spanish districts. Districts are represented as nodes, connected by the total number of trips between them for the first week of September 2023.")
    with col2:
        st.image("images/districts_revenue.png", caption="Heatmap of median revenue per consumption unit of Spanish districts. ")




# col1,col2,col3 = st.columns(3)



