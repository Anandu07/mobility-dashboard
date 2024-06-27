import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
# Complexity 72H
            \n
            \n\n
""")

st.header("About Research\n\n\n")
st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ac felis donec et odio pellentesque diam volutpat commodo. Egestas diam in arcu cursus euismod quis. Pretium viverra suspendisse potenti nullam ac tortor vitae purus faucibus. A lacus vestibulum sed arcu non odio euismod lacinia. Ac ut consequat semper viverra. Sapien et ligula ullamcorper malesuada proin libero. Varius morbi enim nunc faucibus a pellentesque sit amet. Mi in nulla posuere sollicitudin aliquam. Arcu cursus vitae congue mauris rhoncus. Elit pellentesque habitant morbi tristique senectus. Dui nunc mattis enim ut. Nunc pulvinar sapien et ligula ullamcorper malesuada. Vel facilisis volutpat est velit egestas dui id ornare arcu. Sed viverra ipsum nunc aliquet bibendum.

Euismod quis viverra nibh cras pulvinar mattis nunc sed. Id faucibus nisl tincidunt eget nullam non nisi est. Ac auctor augue mauris augue neque gravida. Facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum. Diam volutpat commodo sed egestas egestas fringilla. Tellus id interdum velit laoreet id donec. Vitae semper quis lectus nulla. Magnis dis parturient montes nascetur ridiculus mus mauris. Condimentum lacinia quis vel eros donec ac odio tempor. Ut diam quam nulla porttitor massa id neque. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Nibh sit amet commodo nulla facilisi nullam vehicula ipsum a. Nunc sed augue lacus viverra vitae congue eu consequat ac. Dolor purus non enim praesent elementum.

Placerat orci nulla pellentesque dignissim enim sit amet. Tristique et egestas quis ipsum suspendisse. Neque egestas congue quisque egestas diam in arcu cursus euismod. Eget gravida cum sociis natoque penatibus et magnis dis parturient. Blandit cursus risus at ultrices mi tempus. Et leo duis ut diam quam. Rutrum tellus pellentesque eu tincidunt. Et tortor consequat id porta nibh venenatis. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet. Et pharetra pharetra massa massa ultricies. Turpis nunc eget lorem dolor sed viverra ipsum nunc aliquet. Faucibus vitae aliquet nec ullamcorper sit amet risus. Pulvinar sapien et ligula ullamcorper malesuada. Mauris augue neque gravida in fermentum et sollicitudin ac.

""")

col2, col3, col4 = st.columns(3)
                       
with col2:
    st.header("Place holder")
    st.write("orem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore")

with col3:
    st.header("About Team")
    st.write("Contents about mobility")
    col3.image("images/image_dalle.png")

with col4:
    st.header("Place holder")
    st.write("Contents about mobility")
    col4.image("images/mobility_options.png")
