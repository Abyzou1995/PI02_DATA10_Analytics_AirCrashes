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

st.set_page_config(layout="wide")
df=pd.read_csv("Dataset_final/Data.csv")
df['Hour'] = pd.to_datetime(df['Time'], errors="coerce").dt.hour
df['Time'] = pd.to_datetime(df.Time, errors='coerce', format='%H:%M:%S').dt.time
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
st.markdown("<h1 style='text-align: center; color: black;'>Airplane Crashes</h1>",
            unsafe_allow_html=True)
st.markdown("***")
st.markdown("Air accidents are unexpected and unwanted events that involve aircraft and cause physical damage to people or to the aircraft itself. A plane crash can involve any type of aircraft, including commercial jets, private jets, helicopters, gliders, and hot air balloons. Air crashes can be caused by a variety of factors, including human error, equipment failure, weather issues, maintenance issues, air traffic management failures, design issues, or manufacturing issues. And as for its consequences, they can be both in terms of human and economic losses.")

st.markdown("<h2 style='text-align: center; color: black;'>Important Features</h2>",
            unsafe_allow_html=True)
a1,a2=st.columns(2)
with a1:
    st.markdown(
        "Fatalities")
    st.markdown(
        "By Operator")
    All_fat1 = df.groupby(by=["Operator"])[
        "All Fatalities"].sum().reset_index()
    All_fat = All_fat1.sort_values(by=["All Fatalities"], ascending=False).head(10)
    All_ground1 = df.groupby(by=["Operator"])["Ground"].sum().reset_index()
    All_ground = All_ground1.sort_values(by=["Ground"], ascending=False).head(10)
    fig1=plt.figure(figsize=(12, 6))
    plt.barh(All_fat["Operator"], All_fat["All Fatalities"],
            align='center', color="green", label="All Fatalities")
    plt.barh(All_ground["Operator"], All_ground["Ground"],
            align='center', color="blue", label="All Ground Fatalities")
    plt.gca().invert_yaxis()
    plt.xlabel("Number of accidents")
    plt.legend()
    plt.ylabel("Location")
    st.write(fig1)

    st.markdown(
        "By Country")
    All_fat1 = df.groupby(by=["Country"])["All Fatalities"].sum().reset_index()
    All_fat = All_fat1.sort_values(
        by=["All Fatalities"], ascending=False).head(10)
    All_ground1 = df.groupby(by=["Country"])["Ground"].sum().reset_index()
    All_ground = All_ground1.sort_values(
        by=["Ground"], ascending=False).head(10)
    fig4 = plt.figure(figsize=(12, 6))
    plt.barh(All_fat["Country"], All_fat["All Fatalities"].head(10),
             align='center', color="green", label="Aboard Fatalities")
    plt.barh(All_ground["Country"], All_ground["Ground"].head(10),
             align='center', color="blue", label="Ground Fatalities")
    plt.gca().invert_yaxis()
    plt.xlabel("Count of Fatalities")
    plt.ylabel("Country")
    plt.legend(loc="lower right")
    st.write(fig4)
    st.markdown(
    "By Month")
    All_fat = df.groupby(by=["Month"])["All Fatalities"].sum().reset_index()
    All_ground = df.groupby(by=["Month"])["Ground"].sum().reset_index()
    fig6=plt.figure(figsize=(12, 6))
    plt.style.use('bmh')
    plt.bar(All_fat['Month'], All_fat['All Fatalities'],
            color='m', linewidth=1, label="Aboard fatalities")
    plt.bar(All_ground['Month'], All_ground['Ground'],
            color='b',  linewidth=1, label="Ground fatalities")
    plt.xlabel('Month', fontsize=10)
    plt.ylabel('Count', fontsize=10)
    plt.title('Fatalities by Month', loc='Center', fontsize=14)
    plt.legend()
    plt.show()
    st.write(fig6)

    st.markdown(
        "Ac Type")

    All_fat = df.groupby(by=["Ac Type"])["All Fatalities"].sum().reset_index()
    All_fat = All_fat.sort_values(by=["All Fatalities"], ascending=False).head(10)
    All_ground = df.groupby(by=["Ac Type"])["Ground"].sum().reset_index()
    All_ground = All_ground.sort_values(by=["Ground"], ascending=False).head(10)
    fig8=plt.figure(figsize=(12, 6))
    plt.barh(All_fat["Ac Type"], All_fat["All Fatalities"],
            align='center', color="green", label="All Fatalities")
    plt.barh(All_ground["Ac Type"], All_ground["Ground"],
            align='center', color="blue", label="All Ground Fatalities")
    plt.gca().invert_yaxis()
    plt.xlabel("Count of Fatalities")
    plt.legend()
    plt.ylabel("Airplane type")
    st.write(fig8)

    st.markdown(
    "By Year")
    All_fat = df.groupby(by=["Year"])["All Fatalities"].sum().reset_index()
    All_ground = df.groupby(by=["Year"])["Ground"].sum().reset_index()

    fig9 = plt.figure(figsize=(12, 6))
    plt.style.use('bmh')
    plt.plot(All_fat['Year'], All_fat['All Fatalities'],
            color='m', marker="o", linewidth=1, label="Aboard fatalities")
    plt.plot(All_ground['Year'], All_ground['Ground'],
            color='b', marker="o", linewidth=1, label="Ground fatalities")
    plt.xlabel('Year', fontsize=10)
    plt.ylabel('Count', fontsize=10)
    plt.title('Fatalities by Year', loc='Center', fontsize=18)
    plt.legend()
    plt.show()
    st.write(fig9)
    
with a2:
    st.markdown(
        "Accidents")
    st.markdown(
        ".")
    mex8 = pd.DataFrame(df.Operator.value_counts())
    mex8.reset_index(inplace=True)
    popular = mex8.sort_values("Operator", ascending=False)  # PLOT
    fig2=plt.figure(figsize=(12, 6))
    plt.barh(popular["index"].head(15), popular.Operator.head(
        15), align='center', color="green")
    plt.gca().invert_yaxis()
    plt.xlabel("Number of accidents")
    plt.ylabel("Operator")
    st.pyplot(fig2)

    st.markdown(
        "")
    mex6 = pd.DataFrame(df.Country.value_counts())
    mex6.reset_index(inplace=True)
    popular = mex6.sort_values("Country", ascending=False)  # PLOT
    fig3 = plt.figure(figsize=(12, 6))
    plt.barh(popular["index"].head(15), popular.Country.head(
        15), align='center', color="green")
    plt.gca().invert_yaxis()
    plt.xlabel("Number of accidents")
    plt.ylabel("Country")
    st.write(fig3)
    st.markdown(
    ".")
    df["Month"] = df["Date"].dt.month
    mex1 = pd.DataFrame(df.Month.value_counts())
    mex1.reset_index(inplace=True)
    mex1 = mex1.sort_values(by='Month', ascending=True)

    fig5=plt.figure(figsize=(12, 6))
    plt.style.use('bmh')
    plt.bar(mex1["index"], mex1["Month"], color='blue', linewidth=1)
    plt.xlabel('Month', fontsize=10)
    plt.ylabel('Count', fontsize=10)
    plt.title('Count of accidents by Month', loc='Center', fontsize=14)
    plt.show()
    st.write(fig5)

    st.markdown(
    ".")
    mex9 = pd.DataFrame(df["Ac Type"].value_counts())
    mex9.reset_index(inplace=True)
    popular = mex9.sort_values("Ac Type", ascending=False)  # PLOT
    fig7=plt.figure(figsize=(12, 6))
    plt.barh(popular["index"].head(15), popular["Ac Type"].head(
        15), align='center', color="green")
    plt.gca().invert_yaxis()
    plt.xlabel("Number of accidents")
    plt.ylabel("Airplane Type")
    st.write(fig7)

    st.markdown(
        ".")
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    Temp = df.groupby(df.Date.dt.year)[['Date']].count()
    Temp = Temp.rename(columns={"Date": "Count"})

    fig10=plt.figure(figsize=(12, 6))
    plt.style.use('bmh')
    plt.plot(Temp.index, Temp['Count'], color='m', marker="o", linewidth=1)
    plt.xlabel('Year', fontsize=10)
    plt.ylabel('Count', fontsize=10)
    plt.title('Count of accidents by Year', loc='Center', fontsize=18)
    plt.show()
    st.write(fig10)

st.markdown("<h2 style='text-align: center; color: black;'>Conclusions</h2>",
            unsafe_allow_html=True)
st.markdown("1. The most accidents occurred in the range of 8-20 hours and this has a relationship to the high number of fatalities that occurred in the same range, the highest number of accidents at 11(6.05 %) and the highest number of fatalities at 14(6.06%).")
st.markdown("2. The most accidentes occurred in the range of December to January and this has a not very clear relationship to the high number of fatalities that occurred in the same range, cause the most fatalities ocurred in the range of July to December, but the highest number of fatalities(9.78 %) and number of accidents(9.90%) occurred in December.")
st.markdown("3. The most accidents occurred in the range of Tuesday to Saturday and this has a relationship to the high number of fatalities that occurred in the same range, the highest number of accidents on Tuesday(15.19 %) and the highest number of fatalities on Wednesday(15.48%).")
st.markdown("4. The most accidents occurred in the range of first days of month and this has a relationship to the high number of fatalities that occurred in the same range, the highest number of accidents on 8th day of month(3.67 %) and the highest number of fatalities on 3rd day of month(4.71%).")
st.markdown("5. The most accidents occurred in the range of 1944-2003 year and this has a relationship to the high number of fatalities that occurred in the same range, the highest number of accidents in 1946(88, 1.75 %) and 1989(83, 1.65%) and the highest number of fatalities in 1972(2.50%).")
st.markdown("6. The ground fatalities has a defined trend over the years except 2001 due to attack on the Twin Towers.")
st.markdown("7. The most fatalities(13.03 %) and most accidents(20.16%) occurred in The United States of America, followed by Russia and Brazil respectively in both metrics.")
st.markdown("8. The most fatalities(5.06 % ) and most accidents(7.90%) occurred by Aeroflot operator which is a Russian airline, it would explain why Russia is top 2 in accidents and fatalities followed by some U.S.A operators which would explain why The United States had most fatalities and accidents.")
st.markdown("9. The most fatalities and accidents occurred by Douglas airplane models like DC-3, C-47, DC-6B, DC-4, etc.")
st.markdown("10. There is a high correlation between the number of passengers and the total number of people on board(100 % ), this would be explained because the majority of people on board are passengers, and it also has a medium correlation with the total number of fatalities(75%), this would be explained because the greater the number of of people on board there is a greater probability of a greater number of fatalities.")
