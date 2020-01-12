from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from operators.data_compare_operator import DataCompareOperator
from protos_gen import RunnerConfig, TestcaseConfig
import json

# TODO init RunnerConfig

runner_conf = RunnerConfig()

runner_conf.sdkConfig.appKeyIOS = 'VVW0Fno7BEZt1a/y6KLM36uj9qcjw7CAHDwWZKDlWDs='
runner_conf.sdkConfig.appKeyAndroid = 'J6IPlk5AEU+2/Yi59rfYnsFQtdtOgAo9GAzysx8ciOM='
runner_conf.sdkConfig.marketPerm.Level = "2"

case_conf = TestcaseConfig()
case_conf.testcaseID = 'TESTCASE_0'
case_conf.continueWhenFailed = False
case_conf.roundIntervalSec = 3
case_conf.paramStrs.extend([
    json.dumps({
        'QUOTE_NUMBERS': '600028.sh'
    })
])

runner_conf.casesConfig.extend([case_conf])

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['895254752@qq.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('test_mongo', default_args=default_args, schedule_interval=timedelta(days=1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag)

t4 = DataCompareOperator(
    task_id='data_compare',
    task_id_list=['adb_shell_a', 'adb_shell_b'],
    retries=3,
    provide_context=False,
    runner_conf=runner_conf,
    dag=dag
)

t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t1)
