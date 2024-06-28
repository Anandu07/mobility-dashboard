import streamlit as st

st.markdown("""
# Radiation Model for Mobility Analysis 
            \n
            \n\n
""")

st.write("""We utilize the radiation model to predict the flow of trips between areas based solely on population distribution and geographical distance. This model helps us understand how mobility decays with distance—a fundamental aspect that reveals how districts closer in space are more likely to have higher trip frequencies.""")

with st.container():
    st.header("Radiation Model for Mobility")
    st.image("images/radiation_net.png", caption="Resulting mobility network capturing the mean absolute percentage error for all links in original network, clear colors representing big errors, darker colors representing small errors.")
    col1, col2 = st.columns(2)
    with col1:
        # st.image("images/network.png", caption="Mobility network between Spanish districts. Districts are represented as nodes, connected by the total number of trips between them for the first week of September 2023.")
        st.image("images/distance_ccdf.png",width=300)
    with col2:
        # st.image("images/districts_revenue.png", caption="Heatmap of median revenue per consumption unit of Spanish districts. ")
        st.image("images/distance_ccdf (1).png",width=278)
    st.write("Trip frequencies decay with distance, with a plateau representing trips that go further than the Iberian peninsula and thus cross to the islands.")
    
    