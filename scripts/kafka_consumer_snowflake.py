from kafka import KafkaConsumer
import snowflake.connector
import json

# Connect to Snowflake
conn = snowflake.connector.connect(
    user="",
    password="",          
    account="",
    warehouse="ATMOSYNC_WH",
    database="ATMOSYNC_DB",
    schema="RAW"
)

cursor = conn.cursor()

print("✅ Connected to Snowflake")

# Connect to Kafka

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="sensor-group-snowflake",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("📡 Waiting for Kafka messages...\n")

# SQL Insert Statement

insert_query = """
INSERT INTO IOT_SENSOR_DATA
(
    TIMESTAMP,
    CONTAINER_ID,
    COMMODITY,
    TEMPERATURE_C,
    HUMIDITY_PERCENT,
    VIBRATION_G,
    LATITUDE,
    LONGITUDE,
    DESTINATION,
    MARKET_PRICE_USD_PER_TON,
    SPOILAGE_RISK,
    RECOMMENDED_ACTION
)
VALUES
(
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
)
"""


# Read Kafka Messages
try:

    for message in consumer:

        data = message.value

        print("Received:", data)

        cursor.execute(
            insert_query,
            (
                data["Timestamp"],
                data["Container_ID"],
                data["Commodity"],
                float(data["Temperature_C"]),
                float(data["Humidity_%"]),
                float(data["Vibration_g"]),
                float(data["Latitude"]),
                float(data["Longitude"]),
                data["Destination"],
                int(data["Market_Price_USD_per_ton"]),
                data["Spoilage_Risk"],
                data["Recommended_Action"]
            )
        )

        conn.commit()

        print("✅ Inserted into Snowflake\n")

except KeyboardInterrupt:

    print("\nStopping Consumer...")

finally:

    cursor.close()
    conn.close()

    print("Snowflake connection closed.")