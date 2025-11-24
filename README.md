🏥 Healthcare Compliance Automation — End-to-End Real-Time Data Engineering Pipeline

A complete healthcare data engineering project built using Kafka, Spark Structured Streaming, Delta Lake, Airflow, and Power BI to automate PHI/PII masking, enforce HIPAA-friendly data handling, orchestrate ETL workflows, and generate hospital insights dashboards.

🖼️ Architecture Diagram

This diagram illustrates the real-time flow of health data from ingestion → masking → Delta Lake → Airflow → Power BI dashboards.

🚀 Project Overview

This platform simulates a real-world healthcare compliance system capable of:

✔ Streaming patient data in real-time
✔ Performing PHI/PII masking
✔ Validating, cleaning, and deduplicating records
✔ Storing data in Delta Lake (Bronze → Silver → Gold)
✔ Running scheduled healthcare ETL tasks via Airflow
✔ Powering interactive analytics dashboards in Power BI

The full workflow is designed with HIPAA principles (masking + limited exposure) in mind.

🏗️ Technology Stack
Layer	Tools / Frameworks
Ingestion	Apache Kafka, Python Producer
Stream Processing	PySpark, Spark Structured Streaming
Storage	Delta Lake (Bronze/Silver/Gold)
Workflow Orchestration	Apache Airflow
Analytics	Power BI
Containerization	Docker, Docker Compose
📁 Folder Structure
healthcare-compliance-automation/
│
├── airflow/
│   ├── dags/
│   │   └── healthcare_pipeline_dag.py
│   └── docker-compose.yml
│
├── data/
│   ├── raw/
│   ├── masked/
│   └── processed/
│
├── logs/
│
├── producer/
│   ├── kafka_producer.py
│   └── sample_patient_data.csv
│
├── scripts/
│   └── helpers.py
│
├── spark_streaming/
│   ├── streaming_job.py
│   ├── masking_functions.py
│   └── configs/
│
├── dashboards/
│   ├── healthcare_overview.pbix
│   └── screenshots/
│
└── docker-compose.yml

🔐 PHI/PII Masking Logic

All sensitive medical fields are masked for compliance:

Field	Masking Applied
Name	Only first letter visible (J*****)
SSN	Last 4 digits visible only
Phone	Middle digits masked
Email	First 2 letters + domain masked
DOB	Year retained only
Address	Only City, State preserved

These transformations follow HIPAA de-identification principles.

⚡ Real-Time Stream Processing Flow
✔ Kafka Producer

Reads healthcare CSV/JSON files

Converts to JSON messages

Publishes to Kafka topic: healthcare.data

✔ Spark Structured Streaming

Performs:

Schema validation

Null handling

PHI/PII masking

Deduplication

Writes to Delta Lake in 3 layers:

Bronze → Raw Data  
Silver → Cleaned + Masked  
Gold   → Aggregated Analytics

🌀 Airflow DAG — Healthcare Pipeline

The DAG handles:

Daily ETL

Data quality checks

Logging & alerts

Gold-layer table generation

Exporting curated data for analytics

Airflow UI:
http://localhost:8080

📊 Power BI Analytics Dashboards

Included dashboards:

🟦 1. Patient Admissions

Daily/weekly/monthly patient inflow

Department-level analysis

Admission trends

🟦 2. Diagnosis Trends

Top diagnoses

Severity categories

Treatment volume by department

🟦 3. Hospital Operational KPIs

Bed occupancy rate

Avg length of stay

Doctor & department performance

🟦 4. Compliance Monitoring

Missing PHI counts

Masking success rates

Validation failures

Dashboards are available in:

dashboards/healthcare_overview.pbix
dashboards/screenshots/

▶️ How to Run the Pipeline
1. Start Kafka, Zookeeper, Airflow
docker-compose up -d

2. Run Producer
python producer/kafka_producer.py

3. Start Spark Streaming
spark-submit spark_streaming/streaming_job.py

4. Trigger Airflow DAG

In Airflow UI → Run:
healthcare_pipeline_dag

5. Open Power BI Dashboard

Load:
dashboards/healthcare_overview.pbix

🎯 Key Features Recruiters Will Love

✔ End-to-end real-time data engineering project
✔ Full Delta Lake architecture implementation
✔ Healthcare PHI/PII masking and compliance
✔ Airflow DAG with DQ checks
✔ Power BI dashboards for hospital insights
✔ Clean, production-style folder structure
✔ Docker-based reproducible environment
✔ Professional documentation & diagram

🧑‍💻 Author

Dinesh Kyanam
Data Engineer | Real-Time Streaming | Cloud | Big Data
🔗 GitHub: your link
🔗 LinkedIn: your link

