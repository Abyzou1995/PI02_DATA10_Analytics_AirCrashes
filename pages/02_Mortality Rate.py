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



st.markdown("<h1 style='text-align: center; color: black;'>KPI: MORTALITY RATE</h1>",
            unsafe_allow_html=True)
st.markdown("***")
st.markdown("This KPI describes the rate of number of fatalities over the total number of people aboard.")
st.markdown("<h3 style='text-align: center; color: black;'>Rate=N° Fatalities/N° Aboard</h3>",
            unsafe_allow_html=True)

st.write("#### Features:")

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
    b2 = st.button("By Country", on_click=callback1)
with a3:
    st.write("")
if bu1:
    df.dropna(subset=["All Fatalities", "All Aboard"], inplace=True)
    All_fat = df.groupby(by=["Year"])["All Fatalities"].sum().reset_index()
    All_Abo = df.groupby(by=["Year"])["All Aboard"].sum().reset_index()
    All = All_Abo.merge(All_fat, on="Year")
    All["Rate"] = 100*All["All Fatalities"]/All["All Aboard"]
    All["Rate goal"] = 100*All["All Fatalities"]/All["All Aboard"]
    for i in range(All.shape[0]-1):
        All["Rate goal"].iloc[i+1] = All["Rate"].iloc[i]-5
    st.dataframe(All)

    fig1 = px.line(All, x="Year", y=[
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

    with a2:
        df.dropna(subset=["All Fatalities", "All Aboard"], inplace=True)
        All_fat = df.groupby(by=["Year", "Country"])[
            "All Fatalities", "All Aboard"].sum().reset_index()
        All_fat1 = All_fat[All_fat["Country"] == pais].reset_index(drop=True)
        All_fat1["Rate"] = 100*All_fat1["All Fatalities"] / \
            All_fat1["All Aboard"]
        All_fat1["Rate goal"] = 100 * \
            All_fat1["All Fatalities"]/All_fat1["All Aboard"]
        for i in range(All_fat1.shape[0]-1):
            All_fat1["Rate goal"].iloc[i+1] = All_fat1["Rate"].iloc[i]-5
        for i in range(All_fat1.shape[0]-1):
            All_fat1["Rate goal"].iloc[i+1] = All_fat1["Rate"].iloc[i]-5
        st.dataframe(All_fat1[(All_fat1["Year"] >= values[0])
                     & (All_fat1["Year"] <= values[1])])

    fig1 = px.line(All_fat1[(All_fat1["Year"] >= values[0]) & (All_fat1["Year"] <= values[1])], x="Year", y=[
        "Rate", "Rate goal"], title="Mortality Rate").update_layout(
        xaxis_title="Year", yaxis_title="Rate"
    )
    st.write(fig1)
