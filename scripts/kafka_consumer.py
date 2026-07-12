from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sensor-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Waiting for Sensor Data...\n")

for message in consumer:
    sensor_data = message.value
    print(sensor_data)