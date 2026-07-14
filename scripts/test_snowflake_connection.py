import snowflake.connector

try:
    conn = snowflake.connector.connect(
        user="",
        password="",     
        account="",
        warehouse="ATMOSYNC_WH",
        database="ATMOSYNC_DB",
        schema="RAW"
    )

    print("✅ Connected to Snowflake Successfully!")

    cursor = conn.cursor()

    cursor.execute("SELECT CURRENT_VERSION();")

    version = cursor.fetchone()

    print("Snowflake Version:", version[0])

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Connection Failed")