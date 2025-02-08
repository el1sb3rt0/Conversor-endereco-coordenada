import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title('Conversor de Endereços em Coordenadas Geográficas')
endereco = st.text_input('Digite o endereço:')

geografica = []

url = f'https://geocode.maps.co/search?q={endereco}&api_key=67a3a5be54220483604578yjs5b2114'
response = requests.get(url)
data = response.json()
for local in data:
    lat = local['lat']
    lon = local['lon']
    nome_endereco = local['display_name']
    geografica.append((float(lat), float(lon)))
    st.write(f'**Latitude:** {lat}, **Longitude:** {lon}')
    st.write(f'**Endereço:** {nome_endereco}')

df_localizacoes = pd.DataFrame(geografica, columns=['latitude', 'longitude'])
fig = px.scatter_map(
    df_localizacoes,
    lat='latitude',
    lon='longitude',
    size_max=15,
    zoom=12
)
fig.update_layout(mapbox_style='open-street-map')
st.plotly_chart(fig)

st.write('Desenvolvido por: [Elisberto Oliveira]')
st.write('Fonte de dados: [Open Street Map]/[geocode.maps.co]')
st.write('Contato: elisberto@gmail.com')