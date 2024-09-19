import pandas as pd 
import streamlit as st
import plotly_express as px

st.header('¡Bienvenido a mi primera aplicación web!')

data = pd.read_csv("/Users/luisarochi/Desktop/First_web_project/vehicles_us.csv")
 
hist_button = st.button('Construir histograma')

if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de precios de venta de coches')
    fig = px.histogram(data, x="price")
    st.plotly_chart(fig, use_container_width=True)