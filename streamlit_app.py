import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(page_title="CELSUS 118", layout="wide", page_icon="resources/logo.png")

# Header
st.markdown("""
        <div  style='display: flex; align-items: center;'>
            <img src='https://github.com/MaxBranca404/celsus118-dashboard/blob/main/resources/logo.png?raw=true' width='50' style='margin-right: 15px;'>
            <h1 style='text-align: center; margin: 0;'>CELSUS 118</h1>
        </div>
    """, unsafe_allow_html=True)

# Layout con sidebar e due colonne
with st.sidebar:
    st.image("resources/logo.png", width=100)
    st.markdown("### Menu")
    st.button("Profilo")
    st.button("Dashboard")
    st.button("Statistiche")
    st.button("Ricerca")
    st.button("Cronologia")
    st.button("Logout")


# -----------------------------------------------------------------------------
# Declare some useful functions.



st.header('GDP over time', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]

    with col:
        first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'{country} GDP',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )
