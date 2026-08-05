from dotenv import load_dotenv
import os
import snowflake.connector
import smtplib
from email.message import EmailMessage

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)

cursor = conn.cursor()

print("✅ Connected to Snowflake")

# Query high-risk containers

query = """
SELECT * FROM RAW.VW_HIGH_RISK_CONTAINERS;
"""

cursor.execute(query)

high_risk_containers = cursor.fetchall()

print("Number of High Risk Containers:", len(high_risk_containers))

# Check if records exist

if len(high_risk_containers) > 0:
    print("High Risk Containers Found")
else:
    print("No High Risk Containers Found")

    # Create email message

if len(high_risk_containers) > 0:

    email_subject = "🚨 Atmosync Alert: High Spoilage Risk Containers"

    email_body = f"""

    Hello,

High Spoilage Risk Containers have been detected.

Total High Risk Containers: {len(high_risk_containers)}

Recommended Actions:

* Inspect all High Risk containers immediately.
* Prioritize these shipments for delivery.
* Monitor temperature and humidity conditions.
* Review shipment routes to minimize spoilage risk.


Please check the Atmosync Dashboard for complete details.

Regards,
Atmosync Monitoring System
"""

else:

    email_subject = "Atmosync Alert"

    email_body = "No High Risk Containers Found."

print(email_subject)
print(email_body)

# Create email message
msg = EmailMessage()

msg["Subject"] = "Atmosync High Risk Alert"
msg["From"] = ""
msg["To"] = ""
msg.set_content(email_body)

# Send email using Gmail SMTP

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("✅ Email sent successfully!")