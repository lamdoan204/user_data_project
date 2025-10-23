from airflow import DAG
from datetime import datetime, timedelta
import sys
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator

sys.path.append('/opt/airflow/api-request')

from insert_data import main
from producer_kafka import producer_kafka

default_args = {
    'description' : "A DAG to orchestrate data",
    'start_date': datetime(2025, 10, 20),
    'catchup' :False,
}



def example():
    print("this is example task")




dag = DAG(
    dag_id="user_api_orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id = 'ingest_data_task',
        python_callable= main
    )
    task2 = PythonOperator(
        task_id = "push_data_to_kafka_task",
        python_callable= producer_kafka   
    )
    spark_task = BashOperator(
        task_id='spark_consumer',
        bash_command="""
        docker exec spark_master \
        bin/spark-submit \
        --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.apache.kafka:kafka-clients:3.5.0 \
        /opt/bitnami/spark/spark_consumer.py
    """
    )   

