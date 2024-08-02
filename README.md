# samdulshopmovie Airflow

- SamdulShop movie data ETL airflow DAG code.
- Use [kobisopenapi](https://www.kobis.or.kr/kobisopenapi/) to collect source data.
- Obtain api access from [kobisopenapi](https://www.kobis.or.kr/kobisopenapi/) and the following settings are required before running the program.
```
# The key below is an example. Apply at the link above.
export MOVIE_API_KEY=<0120129123123018230kjfsadfjakdal>
```

![32](https://github.com/user-attachments/assets/33314fb9-4bd9-4583-8cdf-c651b9430d7e)

### RUN
```
export AIRFLOW_HOME=~/airflow_samdulmovie
export AIRFLOW__CORE__DAGS_FOLDER=~/code/samdulshopmovie/airflow/dags
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__WEBSERVER__WORKERS=1
export AIRFLOW__WEBSERVER__LOG_FETCH_DELAY_SEC=5
export AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG=2
export AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG=2

# Navigate to the Python virtual environment where Airflow is installed.
pyenv shell air
airflow standalone 
```
- Login password for admin 
```
cat $AIRFLOW_HOME/standalone_admin_password.txt
```

### Branch strategy
- (how to branch merge)[https://github.com/samdulshopmovie/airflow/issues/1]

### Ref
- https://airflow.apache.org/docs/apache-airflow/stable/index.html
