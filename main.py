import pandas as pd

df = pd.read_csv("data/sample.csv")
#print(df)

electricity=df["electricity_kwh"].values
days=df["day"].values.reshape(-1,1)
print("Electricity value :",electricity)
print("Days values :",days)
water=df["water_liters"].values
print("water value ",water)
for j in range(len(days)):
    if water[j]>300:
        print("Warning day:",days[j]," water is high--> ",water[j])
for i in range(len(days)):
    if electricity[i]>140:
        print("waning day",days[i],"is high-->",electricity[i])

from model import predict_next_days
predictions=predict_next_days(days,electricity)

print("\n=== 7-Day Electricity Forecast ===")
for i, val in enumerate(predictions):
    print("Day",len(days)+i+1,"-->",round(val,1),"kWh")