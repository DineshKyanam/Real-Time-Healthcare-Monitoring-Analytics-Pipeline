from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

# ----- ETL Tasks -----

def load_silver_to_gold():
    # Example transformation
    df = pd.read_csv("/opt/bitnami/spark/data/silver/cleaned_healthcare_events.csv")
    
    gold = df.groupby("event_type").agg({
        "heart_rate": "mean",
        "temperature": "mean",
        "patient_id": "count"
    }).reset_index()

    gold.to_csv("/opt/bitnami/spark/data/gold/healthcare_kpis.csv", index=False)
    print("Gold layer updated!")

# ----- DAG Definition -----

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="healthcare_etl_pipeline",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
    description="ETL pipeline for healthcare real-time monitoring."
):

    update_gold_layer = PythonOperator(
        task_id="generate_gold_kpis",
        python_callable=load_silver_to_gold
    )

    update_gold_layer
