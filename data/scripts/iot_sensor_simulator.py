import pandas as pd
import random
from datetime import datetime,timedelta

#commodities and destination
commodities = ["Avocados", "Bananas", "Tomatoes", "Grapes", "Mangoes"]
destinations = ["Kochi", "Bengaluru", "Chennai", "Hyderabad", "Mumbai"]

#number of records to generate

num_records=5000

start_time=datetime.now()

data=[]

for i in range(num_records):
    timestamp=start_time+timedelta(minutes=i)
    container_id = f"C{random.randint(1,10):03d}"
    commodity=random.choice(commodities)
    destination=random.choice(destinations)

#sensor values

    temperature = round(random.uniform(2, 10), 1)
    humidity = round(random.uniform(65, 95), 1)
    vibration = round(random.uniform(0.05, 0.50), 2)

    latitude = round(random.uniform(8.0, 28.0), 6)
    longitude = round(random.uniform(72.0, 88.0), 6)

    market_price = random.randint(800, 2200)

#business logic

    if temperature> 8 or humidity>90:
      spoilage_risk="High"
      action="Reroute Shipment"
    elif temperature>6 or humidity>80:
       spoilage_risk="Medium"
       action="Monitor"
    else:
      spoilage_risk="Low"
      action="Continue route"

    data.append([
        timestamp,
        container_id,
        commodity,
        temperature,
        humidity,
        vibration,
        latitude,
        longitude,
        destination,
        market_price,
        spoilage_risk,
        action
    ])

#Create Dataframe

columns = [
    "Timestamp",
    "Container_ID",
    "Commodity",
    "Temperature_C",
    "Humidity_%",
    "Vibration_g",
    "Latitude",
    "Longitude",
    "Destination",
    "Market_Price_USD_per_ton",
    "Spoilage_Risk",
    "Recommended_Action"
]

df=pd.DataFrame(data,columns=columns)

#save to csv

df.to_csv("iot_sensor_data.csv",index=False)

print("IOT sensor data generated successfully")

print(df.head(10))