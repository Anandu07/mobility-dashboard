# # File path: app.py

# import streamlit as st
# from PIL import Image, ImageOps, ImageDraw
# import os

# # Set the path to the directory containing the profile images
# image_directory = "profile"

# def apply_circular_mask(image):
#     # Create a circular mask
#     mask = Image.new('L', image.size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
#     masked_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
#     masked_image.putalpha(mask)
#     return masked_image

# def load_images(image_directory):
#     images = []
#     names = []
#     for filename in os.listdir(image_directory):
#         if filename.endswith((".png", ".jpg", ".jpeg")):
#             img_path = os.path.join(image_directory, filename)
#             img = Image.open(img_path).convert("RGBA")
#             circular_img = apply_circular_mask(img)
#             images.append(circular_img)
#             name = os.path.splitext(filename)[0]
#             names.append(name)
#     return images, names

# def display_team(images, names):
#     st.title("Team Profiles")
#     num_cols = 3  # Number of columns for the grid layout
#     cols = st.columns(num_cols)
    
#     for i, (image, name) in enumerate(zip(images, names)):
#         col = cols[i % num_cols]
#         with col:
#             st.image(image, caption=name, use_column_width=True)


# images, names = load_images(image_directory)
# display_team(images, names)


