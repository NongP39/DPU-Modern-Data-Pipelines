from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator

with DAG(
    "my_first_dag",
    start_date=timezone.datetime(2025, 2, 1),
    schedule=None,
    tags=["dpu", "my_first_dag", "hello"],
    catchup=False  # Important: Add catchup=False
) as dag:  # Add 'as dag' context manager
    t1 = EmptyOperator(task_id="t1")  # Assign the task to a variable
    t2 = EmptyOperator(task_id="t2")  # Assign the task to a variable

    t1 >> t2  # Define task dependencies using the variables