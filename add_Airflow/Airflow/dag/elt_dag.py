from datetime import datetime, timedelta
from airflow import DAG
from docker.types import Mount
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

from airflow.providers.docker.operators.docker import DockerOperator
import subprocess

default_args = {
    'owner':'airflow',
    'start_date':datetime(2024,6,1),
    'catchup':False
}

# 呼召爬取檔在 airflow 
def run_elt_script():
    script_path = "/opt/airflow/ELT_SCRIPT/elt_script.py"
    result = subprocess.run(['python',script_path],
                            capture_output=True,
                            text=True)
    
    # 爬取失敗顯示錯誤
    if result.returncode != 0:
        raise Exception(f"Script failed with error : {result.stderr}")
    
    # 爬取成功顯示
    else:
        print(result.stdout)

# 設定執行時間
dag = DAG(
    dag_id="elt_dag",
    default_args=default_args,
    schedule=timedelta(minutes=60)
)

# 設定 python 運行檔
t1 = PythonOperator(
    task_id="run_elt_script",
    python_callable=run_elt_script,
    dag=dag
)

# 設定 Dockerfile 運行檔
t2 = DockerOperator(
    task_id="dbt_run",
    image = "ghcr.io/dbt-labs/dbt-postgres:1.4.7",
    command=[
        "run",
        "--profiles-dir",
        "/root",
        "--project-dir",
        "/dbt"
    ],
    docker_url="unix://var/run/docker.sock",
    network_mode="elt_network",
    mounts=[
        Mount(source='/Users/justinchau/Development/data_enginer_note/transformation_database_project',
              target='/dbt', type='bind'),
        Mount(source='/Users/justinchau/.dbt', target='/root', type='bind'),
    ],
    dag=dag
)

t1 >> t2



