{{ config(materialized='table') }}

WITH source_data AS (

    SELECT *
    FROM {{ ref('stg_iot_sensor_data') }}

)

SELECT

    timestamp,
    container_id,
    commodity,
    destination,

    temperature_c,
    humidity_percent,
    vibration_g,

    latitude,
    longitude,

    market_price_usd_per_ton,

    spoilage_risk,
    recommended_action,

    ------------------------------------------------
    -- Derived Business Columns
    ------------------------------------------------

    CASE
        WHEN temperature_c < 5 THEN 'Low'
        WHEN temperature_c <= 10 THEN 'Safe'
        ELSE 'High'
    END AS temperature_status,

    CASE
        WHEN humidity_percent < 60 THEN 'Low'
        WHEN humidity_percent <= 80 THEN 'Normal'
        ELSE 'High'
    END AS humidity_status,

    CASE
        WHEN vibration_g < 2 THEN 'Normal'
        ELSE 'High'
    END AS vibration_status,

    CASE
        WHEN market_price_usd_per_ton < 1000 THEN 'Low Value'
        WHEN market_price_usd_per_ton <= 2000 THEN 'Medium Value'
        ELSE 'High Value'
    END AS shipment_value_category,

    CASE
        WHEN spoilage_risk='High'
             AND market_price_usd_per_ton>2000
            THEN 'Critical'

        WHEN spoilage_risk='High'
            THEN 'High'

        WHEN spoilage_risk='Medium'
            THEN 'Medium'

        ELSE 'Low'

    END AS priority_level

FROM source_data