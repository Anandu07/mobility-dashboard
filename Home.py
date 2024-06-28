import streamlit as st



st.set_page_config(layout="wide")

st.markdown("""
<div style="text-align: center; font-size: 36px; font-weight: bold;">
    DISENTANGLING INDIVIDUAL-LEVEL FROM LOCATION-BASED INCOME UNCOVERS
SOCIOECONOMIC PREFERENTIAL MOBILITY AND IMPACTS SEGREGATION ESTIMATES</div>
""", unsafe_allow_html=True)

st.header("About Research\n\n\n")
st.write("""Spatial and social segregation profoundly impacts daily life across various environments, from urban centers to rural areas throughout Spain. This segregation, often based on income, gender, ethnicity, and age, shapes where people live, work, and engage in their daily activities, influencing their access to essential services such as healthcare and education. This in turn perpetuates disparities across social, economic, and political spheres. Moving beyond traditional studies that focus primarily on residential patterns, our research incorporates human mobility to provide a comprehensive view of how segregation manifests across the diverse landscapes of Spain.

Using a detailed dataset of mobile phone records provided by the Spanish Ministry of Transport, Mobility, and Urban Agenda, we analyze daily travel patterns across Spanish districts, carefully considering demographic distinctions. This approach allows us to observe how different demographic groups navigate and interact within and between various areas, revealing mobility patterns that reflect and potentially reinforce social and economic divides. By examining these patterns, our study aims to shed light on the complex interplay between physical and social structures and individual movements, offering insights that can inform more inclusive urban planning, public health strategies, and policy-making across Spain.
""")


# st.image("images/image_dalle.png",width=1100)
with st.container():
    st.header("The Team")
    st.image("images/team_image.jpeg",width=1000)
    # st.write("something about the team")



with st.container():
    st.header("Acknowledgement")
    col2, col3 = st.columns(2)
                        
    with col2:
        st.markdown("""#### Complexity 72H""")
        st.write("We extend our deepest gratitude to the Complexity72h workshop organizing team for another exceptional edition of this innovative event. Held in the vibrant city of Madrid at Carlos III University from June 24-28, 2024, the workshop not only provided an inspiring platform for interdisciplinary collaboration but also fostered a unique environment for creativity and academic growth. The 72-hour format pushes the boundaries of traditional academic workshops, promoting an intensive, collaborative experience that has consistently led to successful outcomes, as evidenced by the impressive track record of projects evolving into arXiv preprints.")
        # col2.image("images/image_dalle.png")

    with col3:
        st.markdown("""####  Carlos III University""")
        st.write("We extend our heartfelt thanks to Colegio Mayor – Residencia de Estudiantes Fernando Abril Martorell and Carlos III University for hosting the Complexity72h workshop at their Leganés Campus. The all-in-one facility for accommodation, meals, and project activities provided an ideal environment for productivity and collaboration. The convenience and support offered by the venue were instrumental in the seamless execution of this event. Our sincere appreciation goes to both the venue staff and the university for their exemplary hospitality and organization.")
        # col3.image("images/mobility_options.png")
