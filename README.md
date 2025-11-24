 Healthcare Real-Time Monitoring & Analytics Dashboard

A Power BI–Driven Healthcare Data Project

This project showcases a real-time healthcare monitoring system powered by:

Apache Kafka (streaming live vitals)

Spark Structured Streaming (processing + cleaning data)

Delta Lake (storing time-series health metrics)

Power BI (interactive real-time dashboards)

The focus of this repository is the Power BI dashboards, which visualize patient vitals and clinical KPIs in real time.

 Power BI Dashboards

Below are the actual visuals generated from the real-time healthcare streaming pipeline.

 1. Healthcare Real-Time Monitoring Dashboard

Insights Shown

Temperature trend over time

Heart-rate changes by timestamp

Blood-pressure distribution

Vitals comparison by event type (Medication, Increase, Decrease)

Multi-metric bar charts for real-time vitals

This dashboard is designed for nurses and clinical operators to monitor patient vitals as they change in real time.

 2. Healthcare Real-Time KPIs

KPIs Displayed

 Patient Count

 Average Heart Rate

 Average Temperature

Vitals by Blood Pressure

Vitals by Event Type (Medication / Total)

These KPIs help clinicians and hospital staff understand overall patient health trends instantly.

⚙️ End-to-End Pipeline Overview

Although the repo highlights Power BI, the dashboards depend on the following data pipeline:

Patient Vitals → Kafka Producer → Kafka Topic → Spark Streaming →
PHI/PII Cleanup → Delta Lake (Gold Layer) → Power BI Dashboards

✔ Kafka ingests live patient vitals
✔ Spark cleans & aggregates data
✔ Delta Lake stores time-series metrics
✔ Power BI refreshes visuals in near real-time

🗂️ Folder Structure
healthcare-compliance-automation/
│
├── dashboards/
│   ├── healthcare_overview.pbix
│   └── screenshots/
│
├── spark_streaming/
├── producer/
├── airflow/
├── data/
└── docker-compose.yml

📁 Power BI File


dashboards/healthcare_overview.pbix



🎯 Key Highlights

This project demonstrates your skills in:

✔ Building real-time analytics dashboards
✔ Designing clinical KPI visuals
✔ Integrating Power BI with streaming data
✔ Healthcare domain understanding
✔ End-to-end pipeline engineering (Kafka → Spark → Delta → BI)

🧑‍💻 Author

Dinesh Kyanam
Data Engineer | Real-Time Streaming | Cloud | Big Data
🔗 GitHub: your link
🔗 LinkedIn: your link

