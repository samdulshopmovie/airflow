from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
with DAG(
    'simple',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': True,
        'retries': 1,
        'retry_delay': timedelta(seconds=3)
    },
    description='simple',
    schedule="10 2 * * *",
    start_date=datetime(2024, 7, 1),
    end_date=datetime(2024, 7, 31),
    catchup=True,
    tags=['simple','samdulshow', 'movie'],
    max_active_runs=1,
    max_active_tasks=1,
) as dag:

    print_task = BashOperator(
        task_id='print.task',
        bash_command="""
        date
        sleep 5
        date
        echo 'ds_nodash : {{ds_nodash}}'
        """,
    )

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    start >> print_task >> end
