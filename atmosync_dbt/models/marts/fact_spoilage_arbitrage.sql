{{ config(materialized='table') }}

WITH source_data AS (

    SELECT *
    FROM {{ ref('fact_container_health') }}

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

    temperature_status,
    humidity_status,
    vibration_status,
    shipment_value_category,
    priority_level,

    

    CASE
        WHEN destination = 'Kochi' THEN 120
        WHEN destination = 'Bengaluru' THEN 450
        WHEN destination = 'Chennai' THEN 700
        WHEN destination = 'Hyderabad' THEN 900
        WHEN destination = 'Mumbai' THEN 1400
        ELSE 500
    END AS estimated_distance_km,

    60 AS average_speed_kmph,

    ROUND(
        (
            CASE
                WHEN destination = 'Kochi' THEN 120
                WHEN destination = 'Bengaluru' THEN 450
                WHEN destination = 'Chennai' THEN 700
                WHEN destination = 'Hyderabad' THEN 900
                WHEN destination = 'Mumbai' THEN 1400
                ELSE 500
            END
        ) / 60.0,
        2
    ) AS estimated_travel_time_hours,

    CASE
        WHEN spoilage_risk = 'Low' THEN 72
        WHEN spoilage_risk = 'Medium' THEN 36
        ELSE 12
    END AS estimated_time_to_spoil_hours,

    ROUND(

        (
            CASE
                WHEN spoilage_risk = 'Low' THEN 72
                WHEN spoilage_risk = 'Medium' THEN 36
                ELSE 12
            END
        )

        -

        (
            (
                CASE
                    WHEN destination = 'Kochi' THEN 120
                    WHEN destination = 'Bengaluru' THEN 450
                    WHEN destination = 'Chennai' THEN 700
                    WHEN destination = 'Hyderabad' THEN 900
                    WHEN destination = 'Mumbai' THEN 1400
                    ELSE 500
                END
            ) / 60.0
        ),

        2

    ) AS spoilage_margin_hours,

    CASE

        WHEN

            (
                (
                    CASE
                        WHEN spoilage_risk = 'Low' THEN 72
                        WHEN spoilage_risk = 'Medium' THEN 36
                        ELSE 12
                    END
                )

                -

                (
                    (
                        CASE
                            WHEN destination = 'Kochi' THEN 120
                            WHEN destination = 'Bengaluru' THEN 450
                            WHEN destination = 'Chennai' THEN 700
                            WHEN destination = 'Hyderabad' THEN 900
                            WHEN destination = 'Mumbai' THEN 1400
                            ELSE 500
                        END
                    ) / 60.0
                )

            ) < 0

        THEN 'Spoilage Expected'

        ELSE 'Safe Delivery'

    END AS shipment_status,

    CASE

        WHEN

            (
                (
                    CASE
                        WHEN spoilage_risk = 'Low' THEN 72
                        WHEN spoilage_risk = 'Medium' THEN 36
                        ELSE 12
                    END
                )

                -

                (
                    (
                        CASE
                            WHEN destination = 'Kochi' THEN 120
                            WHEN destination = 'Bengaluru' THEN 450
                            WHEN destination = 'Chennai' THEN 700
                            WHEN destination = 'Hyderabad' THEN 900
                            WHEN destination = 'Mumbai' THEN 1400
                            ELSE 500
                        END
                    ) / 60.0
                )

            ) < 0

        THEN 'Yes'

        ELSE 'No'

    END AS reroute_recommended

FROM source_data