import streamlit as st



st.set_page_config(layout="wide")

st.markdown("""
# Complexity 72H
            \n
            \n\n
""")

st.header("About Research\n\n\n")
st.write("""Spatial and social segregation profoundly impacts daily life across various environments, from urban centers to rural areas throughout Spain. This segregation, often based on income, gender, ethnicity, and age, shapes where people live, work, and engage in their daily activities, influencing their access to essential services such as healthcare and education. This in turn perpetuates disparities across social, economic, and political spheres. Moving beyond traditional studies that focus primarily on residential patterns, our research incorporates human mobility to provide a comprehensive view of how segregation manifests across the diverse landscapes of Spain.

Using a detailed dataset of mobile phone records provided by the Spanish Ministry of Transport, Mobility, and Urban Agenda, we analyze daily travel patterns across Spanish districts, carefully considering demographic distinctions. This approach allows us to observe how different demographic groups navigate and interact within and between various areas, revealing mobility patterns that reflect and potentially reinforce social and economic divides. By examining these patterns, our study aims to shed light on the complex interplay between physical and social structures and individual movements, offering insights that can inform more inclusive urban planning, public health strategies, and policy-making across Spain.
""")
# st.image("images/image_dalle.png",width=1100)
with st.container():
    st.header("Team")
    # st.image("")
    st.write("something about the team")



with st.container():
    st.header("Acknowledgement")
    col2, col3 = st.columns(2)
                        
    with col2:
        st.header("Complexity 72h")
        st.write("Contents about mobility")
        col2.image("images/image_dalle.png")

    with col3:
        st.header("ISI Foundation")
        st.write("Contents about mobility")
        col3.image("images/mobility_options.png")
