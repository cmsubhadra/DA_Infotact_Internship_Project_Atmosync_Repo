tables in schema raw;

select count(*) from raw.iot_sensor_data;

select count(*) from raw.fact_container_health;

select count(*) from raw.fact_spoilage_arbitrage;

SELECT * FROM raw.fact_spoilage_arbitrage LIMIT 10;

alter table raw.fact_spoilage_arbitrage cluster by (DESTINATION,SPOILAGE_RISK);

SHOW TABLES LIKE 'fact_spoilage_arbitrage' in schema raw;

select * FROM RAW.FACT_SPOILAGE_ARBITRAGE WHERE DESTINATION='Kochi' AND SPOILAGE_RISK='High';

