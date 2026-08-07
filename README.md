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
- Implement automated alerts for critical spoilage-risk containers.
- Automate dbt execution and email alerts using Windows Task Scheduler.

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
- Windows Task Scheduler
- Gmail SMTP

---

## 🏗️ Project Architecture

```text
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
   Analytical Models & Views
            │
            ▼
 Apache Superset Dashboard
            │
            ▼
    Automated Email Alerts

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

## **✅ Week 1 Progress**
Developed Python IoT Sensor Simulator.
Generated mock IoT sensor data.
Configured Apache Kafka in KRaft mode.
Created Kafka Producer and Consumer.
Connected Kafka Consumer with Snowflake.
Created Snowflake warehouse, database, schema, and RAW table.
Loaded streaming data into Snowflake.
Installed and configured Apache Superset.
Connected Superset with Snowflake.
Verified dataset connectivity.

## **✅ Week 2 Progress****
Installed and configured dbt Core and Snowflake adapter.
Configured and verified Snowflake connectivity using dbt debug.
Created stg_iot_sensor_data and fact_container_health models.
Cleaned and transformed raw IoT sensor data.
Added business logic and calculated fields.
Executed and verified dbt transformations.
Connected transformed data to Apache Superset.
Created the initial Container Health Dashboard with KPIs and visualizations.

##** ✅ Week 3 Progress**
Created FACT_SPOILAGE_ARBITRAGE model.
Implemented spoilage-risk, priority, shipment-status, spoilage-margin, and reroute logic.
Added calculated fields for spoilage-risk analysis and shipment prioritization.
Connected spoilage analytics to Apache Superset.
Created risk-focused charts, KPIs, and high-priority container details.
Added visualizations for commodity, destination, spoilage margin, time to spoilage, and reroute recommendations.
Improved dashboard layout and visualization consistency.

## **✅ Week 4 Progress**
Created Snowflake clustering and tested query performance.
Created run_dbt.bat and configured automated dbt execution using Windows Task Scheduler.
Created the alert-condition view for critical spoilage-risk shipments.
Created email_alert.py and configured Gmail SMTP authentication.
Created run_email_alert.bat and scheduled automated email alerts using Windows Task Scheduler.
Added recommended action and critical-container information to email alerts.
Successfully tested automated dbt execution and email delivery.
Finalized the Superset dashboard with Commodity, Destination, Shipment Status, Priority, Reroute Recommended, and Time Range filters.
Improved dashboard presentation and consistency.

## **📊 Dashboard Highlights
**
The Apache Superset dashboards provide insights into:

Temperature Monitoring
Humidity Monitoring
Vibration Monitoring
Container Health
Shipment Status
Priority Levels
Spoilage Risk
Spoilage Margin
Time to Spoilage
Reroute Recommendations
High-Priority Containers
Interactive KPIs and Filters

## **📧 Automated Email Alerts**

AtmoSync includes automated email alerts for critical spoilage-risk shipments.

Alerts are generated when:

SHIPMENT_STATUS = 'Spoilage Expected'
AND
PRIORITY_LEVEL = 'Critical'

The email alert includes:

Total critical containers
Critical shipment information
Recommended action

## **⚙️ Automation**

Automated dbt Execution
run_dbt.bat
     ↓
Windows Task Scheduler
     ↓
dbt run
     ↓
Snowflake
Automated Email Alert
run_email_alert.bat
     ↓
Windows Task Scheduler
     ↓
email_alert.py
     ↓
Snowflake Alert View
     ↓
Gmail SMTP
     ↓
Critical Shipment Alert

## 📚 Learning Outcomes

This project provided practical experience in:

Python Programming
Apache Kafka Streaming
Snowflake Data Warehousing
Snowflake Clustering
dbt Data Transformations
SQL Data Modeling
Apache Superset Dashboard Development
Interactive Dashboard Filters
Automated Email Alerts
Windows Task Scheduler
Git & GitHub Collaboration
End-to-End Data Engineering Pipeline
IoT Data Analytics

## **🚀 Project Status**

🟢 Week 1 – Completed

🟢 Week 2 – Completed

🟢 Week 3 – Completed

🟢 Week 4 – Completed

🟢 Dashboard – Completed

🟢 dbt Automation – Completed

🟢 Email Alert Automation – Completed

🟢 Task Scheduler – Completed
