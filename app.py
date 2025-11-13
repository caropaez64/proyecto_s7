import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Visualización de datos de anuncios de venta de coches')
build_histogram = st.checkbox('Construir histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_dispersion = st.checkbox('Construir una gráfica de dispersión')
if build_dispersion:
    st.write('Construir una gráfica de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)