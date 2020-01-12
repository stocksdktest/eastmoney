# import json
#
# import airflow
# from airflow.models import DAG
# from airflow.operators.bash_operator import BashOperator
# from airflow.operators.dummy_operator import DummyOperator
#
# from protos_gen.config_pb2 import RunnerConfig, TestcaseConfig
# #from operators.android_runner_operator import AndroidRunnerOperator
# #from operators.android_release_operator import AndroidReleaseOperator
# from operators.eastmoney_operator import EastmoneyOperator
#
#
# # TODO init RunnerConfig
# runner_conf = RunnerConfig()
# runner_conf.jobID = 'TJ-1'
# #runner_conf.runnerID = generate_id('RUN-A')
# #east_operator = EastmoneyOperator(task_id='east_money', runner_conf=runner_conf)
# #east_operator.execute()
#
# with DAG(
#     dag_id='east_money',
#     default_args={
#         'owner': 'airflow',
#         'start_date':airflow.utils.dates.days_ago(0)
#     },
#     schedule_interval='@once'
# )as dag:
#     run_this_last = DummyOperator(
#         task_id='run_this_last',
#         queue='android'
#     )
#
#     east_money_tc = EastmoneyOperator(
#         task_id='east_money_operator',
#         provide_context=False,
#         runner_conf=runner_conf
#     )
#     # provide_context=False,
#     east_money_tc >> run_this_last
#
# if __name__ == "__main__":
#     dag.cli()