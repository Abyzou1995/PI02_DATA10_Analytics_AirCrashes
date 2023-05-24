import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import cufflinks as cf
from IPython.display import display, HTML
import seaborn as sns
import plotly.express as px
from PIL import Image

# write cf.getThemes() to find all themes available
cf.set_config_file(sharing='public', theme='white', offline=True)

st.set_page_config(layout="centered")


st.title("KPI: ACCIDENT FATALITY RATE")
st.markdown("***")
st.markdown("Holus")

st.sidebar.markdown("Dashboard")


st.write("# This works:")

df = pd.read_csv("Dataset_final/Data.csv", index_col=0)
if 'btn' not in st.session_state:
    st.session_state['btn'] = False


def callback1():
    st.session_state['btn'] = True


def callback2():
    st.session_state['btn'] = False


a1, a2, a3 = st.columns((1, 1, 5))
with a1:
    bu1 = st.button("General", on_click=callback2)
with a2:
    b2 = st.button("Paises", on_click=callback1)
with a3:
    st.write("")
if bu1:
    df1 = df[df["All Fatalities"] > 0]
    All_fat = df.groupby(by=["Year"])["All Fatalities"].count().reset_index()
    All_fat1 = df1.groupby(by=["Year"])["All Fatalities"].count().reset_index()
    All_fat2 = All_fat.merge(All_fat1, on="Year")
    All_fat2["Rate"] = 100 * \
        All_fat2["All Fatalities_y"].divide(All_fat2["All Fatalities_x"])
    All_fat2["Rate goal"] = All_fat2["Rate"]
    for i in range(All_fat2.shape[0]-1):
        All_fat2["Rate goal"].iloc[i+1] = All_fat2["Rate"].iloc[i]-3
    st.dataframe(All_fat2)

    fig1 = px.line(All_fat2, x="Year", y=[
        "Rate", "Rate goal"], title="Mortality Rate").update_layout(
        xaxis_title="Year", yaxis_title="Rate"
    )
    st.write(fig1)

if st.session_state['btn']:
    a1, a2 = st.columns((1, 2))
    with a1:
        df.dropna(subset=["All Fatalities", "All Aboard"], inplace=True)
        mex6 = pd.DataFrame(df.Country.value_counts())
        mex6.reset_index(inplace=True)
        popular = mex6.sort_values("Country", ascending=False)
        pais = st.selectbox("Pais", popular["index"].head(10).tolist(), 0)
        values = st.slider('Select a range of values',
                           float(df.Year.min()), float(df.Year.max()), (float(df.Year.min()), float(df.Year.max())))
        st.write('Values:', values)
        st.write('Values1:', values[0])

    with a2:
        df.dropna(subset=["All Fatalities", "All Aboard"], inplace=True)
        df1 = df[df["All Fatalities"] > 0]
        All_fat = df.groupby(by=["Year", "Country"])[
            "All Fatalities"].count().reset_index()
        All_fat1 = df1.groupby(by=["Year", "Country"])[
            "All Fatalities"].count().reset_index()
        All_fat2 = All_fat.merge(All_fat1, on="Year")
        All_fat2 = All_fat2[(All_fat2["Country_x"] == pais) & (
            All_fat2["Country_y"] == pais)].reset_index(drop=True)
        All_fat2["Rate"] = 100 * \
            All_fat2["All Fatalities_y"].divide(All_fat2["All Fatalities_x"])
        All_fat2["Rate goal"] = All_fat2["Rate"]
        for i in range(All_fat2.shape[0]-1):
            All_fat2["Rate goal"].iloc[i+1] = All_fat2["Rate"].iloc[i]-3

        st.dataframe(All_fat2[["Year", "Country_x", "All Fatalities_x", "All Fatalities_y", "Rate", "Rate goal"]][(All_fat2["Year"] >= values[0])
                     & (All_fat2["Year"] <= values[1])])

    fig1 = px.line(All_fat2[(All_fat2["Year"] >= values[0]) & (All_fat2["Year"] <= values[1])], x="Year", y=[
        "Rate", "Rate goal"], title="Mortality Rate").update_layout(
        xaxis_title="Year", yaxis_title="Rate"
    )
    st.write(fig1)
