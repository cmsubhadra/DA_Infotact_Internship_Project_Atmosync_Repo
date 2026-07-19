{{ config(materialized='view') }}

WITH source_data AS (

    SELECT *
    FROM ATMOSYNC_DB.RAW.IOT_SENSOR_DATA WHERE 
    COMMODITY IS NOT NULL AND DESTINATION IS NOT NULL AND TEMPERATURE_C IS NOT NULL
    AND HUMIDITY_PERCENT IS NOT NULL AND VIBRATION_G IS NOT NULL

),

cleaned_data AS (

    SELECT DISTINCT

        CAST("TIMESTAMP" AS TIMESTAMP_NTZ) AS timestamp,

        TRIM("CONTAINER_ID") AS container_id,
        TRIM("COMMODITY") AS commodity,
        TRIM("DESTINATION") AS destination,

        CAST("TEMPERATURE_C" AS FLOAT) AS temperature_c,
        CAST("HUMIDITY_PERCENT" AS FLOAT) AS humidity_percent,
        CAST("VIBRATION_G" AS FLOAT) AS vibration_g,

        CAST("LATITUDE" AS FLOAT) AS latitude,
        CAST("LONGITUDE" AS FLOAT) AS longitude,

        CAST("MARKET_PRICE_USD_PER_TON" AS NUMBER(10,2)) AS market_price_usd_per_ton,

        TRIM("SPOILAGE_RISK") AS spoilage_risk,
        TRIM("RECOMMENDED_ACTION") AS recommended_action

    FROM source_data

)

SELECT *
FROM cleaned_data