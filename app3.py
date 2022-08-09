import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

def app():
    st.title('North Carolina Institutions')
    
    st.write('What insights can we extract that will let us know more about college in North Carolina.')
     

    df2 = pd.read_csv('college.csv')
   
    df2['ugds_blacks'] = round(df2['ugds_black'] * 100,2)
   
    
    nc = df2.query('stabbr == "NC" and hbcu==1')
    nc['ugds_blacks'] = round(df2['ugds_black'] * 100,2)
    nc_filtered = nc[['instnm', 'city', 'ugds_black', 'ugds', 'ugds_white', 'md_earn_wne_p10']]
    nc_filtered['udgds_black'] = round(nc_filtered['ugds_black'] * 100,2)
  
    fig = px.bar(nc.query('stabbr=="NC"'), x="instnm", y="ugds", color="ugds_blacks", height=600, width=1000)
    fig1 = go.Figure(data=go.Heatmap(x = nc_filtered['city'], y = nc_filtered['ugds'], z = round(nc_filtered['ugds_black'] * 100,2)))
    fig2 = px.treemap(nc, path=[px.Constant("all"), 'stabbr', 'city', 'instnm'],
    values='ugds_blacks', color='ugds_blacks', color_continuous_scale='RdBu', height=600, width=1000)
    
    
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
    

    st.dataframe(nc.iloc[:,0:4])