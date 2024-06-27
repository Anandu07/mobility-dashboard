# import streamlit as st
# import pandas as pd
# import geopandas as gpd
# from shapely import wkt
# from bokeh.models import GeoJSONDataSource, HoverTool
# from bokeh.plotting import figure
# from bokeh.tile_providers import get_provider, CARTODBPOSITRON
# import plotly.express as px
# import plotly.graph_objects as go

# st.set_page_config(layout="wide")

# map_data = pd.read_csv('/Users/anandu.balachandran/Downloads/map_data.csv')
# map_data = pd.DataFrame(map_data)
# map_data['geometry'] = map_data['geometry'].apply(wkt.loads)
# geo_data = gpd.GeoDataFrame(map_data, geometry='geometry')
# geo_data.crs = "EPSG:4326"

# st.title("Mobility Data Analysis - Spain")

# # Create a dropdown for selecting the location name
# location_name = st.selectbox("Select the location", map_data['name'])

# # Get the index of the selected location name
# highlight_index = map_data[map_data['name'] == location_name].index[0]

# # Function to create Bokeh plot
# def create_bokeh_plot(highlight_index):
#     geo_json_data = GeoJSONDataSource(geojson=geo_data.to_json())
#     highlight_geojson = GeoJSONDataSource(geojson=geo_data.iloc[[highlight_index]].to_json())

#     bounds = geo_data.iloc[highlight_index].geometry.bounds
#     x_center = (bounds[0] + bounds[2]) / 2
#     y_center = (bounds[1] + bounds[3]) / 2
#     scale_factor = 8
#     x_range = (x_center - (x_center - bounds[0]) * scale_factor, x_center + (bounds[2] - x_center) * scale_factor)
#     y_range = (y_center - (y_center - bounds[1]) * scale_factor, y_center + (bounds[3] - y_center) * scale_factor)

#     p = figure(title="Map Plot", match_aspect=True,
#                x_range=x_range, y_range=y_range,
#                tools="pan,wheel_zoom,reset,save", 
#                active_scroll="wheel_zoom")

#     tile_provider = get_provider(CARTODBPOSITRON)
#     p.add_tile(tile_provider)

#     p.patches('xs', 'ys', fill_alpha=0.7, fill_color='blue', line_color='black', 
#               source=geo_json_data)

#     p.patches('xs', 'ys', fill_alpha=1.0, fill_color='red', line_color='black', 
#               source=highlight_geojson)

#     hover = HoverTool(tooltips=[("index", "$index")])
#     p.add_tools(hover)

#     return p


# plot = create_bokeh_plot(highlight_index)
# st.bokeh_chart(plot, use_container_width=True)




# file_path = '/Users/anandu.balachandran/Downloads/mobility_sample.csv'
# data = pd.read_csv(file_path)

# # Specific origin to analyze
# specific_origin = map_data[map_data['name'] == location_name]['ID'].astype(str).iloc[0]

# # Filter data for the specific origin
# filtered_data = data[data['origin'] == specific_origin]

# # Descriptive Statistics
# filtered_summary_stats = filtered_data.describe(include='all')

# col1, col2, col3 = st.columns(3)




# # # Revenue generated (considering categorical values)
# # revenue_counts = filtered_data['revenue'].value_counts().reset_index()
# # revenue_counts.columns = ['revenue', 'count']
# # fig3 = px.bar(revenue_counts, x='revenue', y='count', title=f'Revenue Generated from Origin {specific_origin}')
# # fig3.show()

# # # Frequency of trips categorized by 'age_bin'
# # fig4 = px.histogram(filtered_data, x='age_bin', title=f'Frequency of Trips from Origin {specific_origin} by Age Bin')
# # fig4.show()

# # # Frequency of trips categorized by 'sex'
# # fig5 = px.histogram(filtered_data, x='sex', title=f'Frequency of Trips from Origin {specific_origin} by Sex')
# # fig5.show()

# # # Number of trips to different destinations
# # with col1:
# #     fig1 = px.histogram(filtered_data, x='destination', title=f'Number of Trips from Origin {specific_origin} to Different Destinations')
# #     st.plotly_chart(fig1)

# # # Average trip distance


# # with col2:
# #     avg_distance = filtered_data['trip_kms'].mean()
# #     fig2 = go.Figure(go.Indicator(
# #         mode = "gauge+number",
# #         value = avg_distance,
# #         title = {'text': f"Average Trip Distance from Origin {specific_origin}"},
# #         gauge = {'axis': {'range': [0, max(filtered_data['distance_kms'])]}}
# #     ))
# #     st.plotly_chart(fig2)

# # # Revenue generated
    
# # with col3:
# #     total_revenue = filtered_data['revenue'].sum()
# #     fig3 = go.Figure(go.Indicator(
# #         mode = "gauge+number",
# #         value = total_revenue,
# #         title = {'text': f"Total Revenue from Origin {specific_origin}"},
# #         gauge = {'axis': {'range': [0, max(filtered_data['revenue'])]}}
# #     ))
# #     st.plotly_chart(fig3)

# # col4, col5 = st.columns(2)
# # # Frequency of trips categorized by 'age_bin'\
# # with col4:
# #     fig4 = px.histogram(filtered_data, x='age_bin', title=f'Frequency of Trips from Origin {specific_origin} by Age Bin')
# #     st.plotly_chart(fig4)

# # # Frequency of trips categorized by 'sex'
# # with col5:
# #     fig5 = px.histogram(filtered_data, x='sex', title=f'Frequency of Trips from Origin {specific_origin} by Sex')
# #     st.plotly_chart(fig5) 




# st.write(filtered_summary_stats)
