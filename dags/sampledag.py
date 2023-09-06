from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def call_api_func():
    print("Inside Function!")
    import requests
    res=requests.get("http://calculator.data.apps.mnscorpdev.net/api/v1/providers")
    print(res)
    print("Exitings Function!")

dag = DAG(
    dag_id="example_python_operator_folder2",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1)
)

task = PythonOperator(
    task_id="API_Test",
    python_callable=call_api_func,
    dag=dag
)
