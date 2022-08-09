import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def app():
    st.title('Alabama Colleges: Part 2')
    
    st.write('A quick look into what college looks like in the state of Alabama.')

    df2 = pd.read_csv('college.csv')
    df2['ugds_blacks'] = round(df2['ugds_black'] * 100,2)
    
    plt.title("Black Undergrads by State and Institution")

    fig = px.bar(df2.query('stabbr=="AL" and hbcu== 1'), x="city", y="ugds", hover_data= ["instnm"], color="ugds_blacks", text="instnm",height=600)
    st.header('Alabama Comparison of All Undergrads v. Black Undergrads at HBCUs')
    st.plotly_chart(fig)
    st.markdown('#### Here we clearly see what we expected, traditional HBCUs have a higher percentage of Black undergrads compared' 
    'to non-traditional HBCUs ####')

    df2 = pd.read_csv('college.csv')
    bama = df2.query('stabbr=="AL" and hbcu== 1')

    BamaCorr = bama.corr()
    mask = np.zeros(BamaCorr.shape, dtype=bool)
    mask[np.triu_indices(len(mask))] = True
    plt.subplots(figsize=(18,21))
    
    fig, ax = plt.subplots(figsize=(18, 16))
    
    sns.heatmap(bama.corr(), cmap='viridis', vmax= 1, annot=True, linewidth=0.5, mask=mask, ax=ax)
    plt.xlabel('')
    st.header('Alabama Correlation Map of College Dataset')
    st.pyplot(fig)