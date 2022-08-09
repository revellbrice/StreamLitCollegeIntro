# app1.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go 
import numpy as np
import plotly.figure_factory as ff

df = pd.read_csv('college.csv')
df_corr = df.corr()
df_corr2 = df_corr.round(2)
z = df_corr2.to_numpy()
z_text = [[str(round(y,1)) for y in x] for x in z]

def app():
    st.markdown("<h1 style='text-align: center; color: black;'>College Data</h1>", unsafe_allow_html=True)
    # st.markdown("<h1 style='text-align: center; color: black;'>Test</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Let us Investigate</h3>", unsafe_allow_html=True)
    df = pd.read_csv('college.csv')
  
    selected_states = st.sidebar.selectbox('What state would you like to visualize:', df.stabbr.unique())
    selected_mix1 = st.sidebar.selectbox('What y_var would you like to visualize:', df.columns)
    selected_ugds_black = st.sidebar.selectbox('What x_var would you like to visualize:', df.columns)

    
    df = pd.read_csv('college.csv')
    df['ugds_black'] = round(df['ugds_black'] * 100,2)

    df = df[df['stabbr'] == selected_states]
    fig, ax = plt.subplots()
    ax = sns.scatterplot( x = df[selected_ugds_black], y = df[selected_mix1])
    plt.xlabel(selected_ugds_black)
    plt.ylabel(selected_mix1)
    st.header(' Scatterplot of Variables of {} Institutions'.format(selected_states))
    fig1 = px.scatter(df, x= selected_ugds_black , y = selected_mix1,
    color= "hbcu", height=1000, width=1400)
    st.plotly_chart(fig1) 

    df = pd.read_csv('college.csv')


   
    fig3 = px.imshow(z,
            text_auto=True,
            x=df_corr2.columns.values.tolist(),
            y=df_corr2.index.values.tolist(),
            color_continuous_scale='Viridis',
            aspect="auto",
            title='<b>Correlation Heatmap of College Dataset</b>',
            facet_col_spacing=0.5,
            facet_row_spacing=0.5,
            height=1000,
            width=1400)
    fig3.update_traces(texttemplate="%{z}")
    fig3.update_layout(paper_bgcolor="LightSteelBlue")
    fig3.update_xaxes(side="top")
    st.plotly_chart(fig3)
	
