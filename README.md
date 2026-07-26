# 🌦️ AtmoSync: Micro-Climate Arbitrage Analytics

## 📌 Project Overview

AtmoSync is a Data Engineering and Analytics project developed as part of the **Infotact Solutions Internship**. The project monitors environmental conditions inside agricultural shipping containers using simulated IoT sensor data. It processes streaming sensor data through a modern data engineering pipeline and transforms it into business-ready insights for monitoring container health and spoilage risks.

---

## 👥 Team Members

- C.M. Subhadra
- Nandhana K.S.

---

## 🎯 Problem Statement

Traditional supply chain systems rely on estimated transit times and general weather forecasts. They cannot monitor the real-time micro-climate conditions inside shipping containers. Sudden changes in temperature, humidity, or vibration may cause fruits and vegetables to spoil before reaching their destination, resulting in financial losses.

---

## 🎯 Project Objectives

- Simulate IoT sensor data for shipping containers.
- Stream sensor data using Apache Kafka.
- Store streaming data in Snowflake.
- Transform raw data into analytics-ready datasets using dbt.
- Monitor container health and spoilage risks.
- Build interactive dashboards using Apache Superset.
- Support data-driven logistics and transportation decisions.

---

## 🛠️ Technology Stack

- Python
- Apache Kafka
- Snowflake
- dbt (Data Build Tool)
- Apache Superset
- SQL
- Git
- GitHub
- VS Code
- Java JDK

---

## 🏗️ Project Architecture

```
IoT Sensor Simulator (Python)
            │
            ▼
      Apache Kafka
            │
            ▼
        Snowflake
       (RAW Layer)
            │
            ▼
      dbt Transformations
 (Staging & Fact Models)
            │
            ▼
 Apache Superset Dashboard
```

---

## 📂 Repository Structure

```
DA_Infotact_Internship_Project_Atmosync_Repo/
│
├── atmosync_dbt/
│   ├── analyses/
│   ├── logs/
│   ├── macros/
│   ├── models/
│   ├── seeds/
│   ├── snapshots/
│   ├── tests/
│   ├── dbt_project.yml
│   └── README.md
│
├── dashboard_CMSubhadra/
├── dashboard_Nandhana/
│
├── data/
├── logs/
├── scripts/
├── snowflake/
│
├── README.md
└── .gitignore
```

---

## ✅ Week 1 Progress

- Developed Python IoT Sensor Simulator.
- Generated mock IoT sensor data.
- Configured Apache Kafka (KRaft Mode).
- Created Kafka Producer and Kafka Consumer.
- Connected Kafka Consumer with Snowflake.
- Created Snowflake Warehouse, Database, Schema, and RAW table.
- Loaded streaming data into Snowflake.
- Installed and configured Apache Superset.
- Connected Superset with Snowflake.
- Verified dataset connectivity.

---

## ✅ Week 2 Progress

- Configured dbt and verified Snowflake connection.
- Created staging model (`stg_iot_sensor_data`).
- Created fact model (`fact_container_health`).
- Applied business logic using SQL transformations.
- Executed dbt models successfully.
- Verified transformed data in Snowflake.
- Connected transformed dataset to Apache Superset.
- Developed interactive monitoring dashboards for container health analytics.

---

## 📊 Dashboard Highlights

Interactive dashboards have been developed using Apache Superset to visualize transformed IoT sensor data. The dashboards provide insights into:

- Temperature Monitoring
- Humidity Monitoring
- Container Distribution
- Commodity Analysis
- Destination Analysis
- Container Health Monitoring
- Interactive KPIs and Visual Analytics

---

## 📚 Learning Outcomes

This project provided practical experience in:

- Python Programming
- Apache Kafka Streaming
- Snowflake Data Warehouse
- dbt Data Transformations
- SQL Data Modeling
- Apache Superset Dashboard Development
- Git & GitHub Collaboration
- End-to-End Data Engineering Pipeline

---

## 🚀 Project Status

🟢 Week 1 – Completed

🟢 Week 2 – Completed

🟡 Week 3 – In Progress



