import datetime
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils import timezone

args = {
    'owner': 'airflow',
    'start_date': timezone.datetime(2019, 11, 20, 8, 15),
}

with DAG(
    dag_id='StockSDKTest',
    default_args=args,
    schedule_interval=datetime.timedelta(minutes=5),
) as dag:
    compare_1 = DummyOperator(
        task_id='结果比对-Testcase-1',
    )

    android_1 = DummyOperator(
        task_id='股票信息-Android-Testcase-1'
    )

    ios_1 = DummyOperator(
        task_id='股票信息-iOS-Testcase-1'
    )

    crawler_1 = DummyOperator(
        task_id='股票信息-Crawler-Testcase-1'
    )

    [android_1, ios_1, crawler_1] >> compare_1

if __name__ == "__main__":
    dag.cli()
