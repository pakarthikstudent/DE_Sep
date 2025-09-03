from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'demo_karthik_dag',  # DAG name
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(minutes=5), # python code(pETL.py) will execute every 5mts once
    start_date=datetime(2025, 8, 7), # when you want to start this job(startingDate) then in enable UI
    catchup=False, 
# in case catchup=True if i start 10th Aug - this will run all the previous scheduled job
)

run_etl = BashOperator(
    task_id='run_etl',
    bash_command='bash /home/student/wrapper_script.sh ',#give a space after the path
    dag=dag,
)