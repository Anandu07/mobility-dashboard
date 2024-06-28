import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""
# Spain Mobility Data Analysis 
            \n
            \n\n
""")

st.write("The data analysis is performed to uncover the underlying patterns of mobility and economic status across Spanish districts offering an in-depth look at how people move between districts and how these patterns correlate with economic indicators and gender groups. ")

with st.container():
    st.header("Mobility and Median Income across Spain")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/network.png", caption="Mobility network between Spanish districts. Districts are represented as nodes, connected by the total number of trips between them for the first week of September 2023.")
    with col2:
        st.image("images/districts_revenue.png", caption="Heatmap of median revenue per consumption unit of Spanish districts. ")


with st.container():
    st.header("Assortativity and Socioeconomic Preferential Mobility Index")
    st.image("images/assortativity_overtime_noself_gender-1.png",width=1000)

st.markdown("""#### Key Findings""")
st.write("""Inter-District Mobility: Analysis of normalized mobility flows between districts shows a distinct pattern. Middle-income groups demonstrate the broadest geographical reach, while lower-income groups exhibit restricted mobility due to financial constraints. Conversely, high-income individuals display extensive, though slightly less broad, mobility patterns compared to the middle-income group.\n
Economic Disparities: A pronounced economic gradient from north to south is observable, with northern and urban districts showing higher median revenues. This gradient underlines the stark economic disparities across districts.\n
Network Analysis by Demographics: Gender influences on mobility - men traveling to a marginally greater number of unique places; Age impacts mobility, where middle-aged groups exhibit more extensive mobility, and the oldest and youngest groups showing more restricted patterns.""")


# col1,col2,col3 = st.columns(3)



