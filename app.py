import streamlit as st
import pandas as pd
st.title("Suhail- Smart Energy Monitor")
st.write ("Monitoring electricity and water consumption")
df=pd.read_csv("data/sample.csv")
st.dataframe(df)
st.subheader("Electricity Comsumption")
st.line_chart(df["electricity_kwh"])
st.subheader("Water Consumption")
st.line_chart(df["water_liters"])

st.subheader("⚠️ Anomaly Detection")
electricity=df["electricity_kwh"].values
days=df["day"].values

for i in range(len(days)):
     if electricity[i]>140:
        st.error(f"Day{days[i]}- High electricity: {electricity[i]} kWh")


water=df["water_liters"].values

for j in range(len(days)):
    if water[j]>300:
     st.info(f"Day{days[j]} - High water : {water[i]} liters")