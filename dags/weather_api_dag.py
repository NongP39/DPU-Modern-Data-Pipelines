from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils import timezone

import requests


def _get_weather_data():
    API_KEY = "cf58fa7d8db08fed7620093cb114766d"
    # API_KEY = os.environ.get("WEATHER_API_KEY")
    # API_KEY = Variable.get("weather_api_key")

    payload = {
        "q": "bangkok",
        "appid": API_KEY,
        "units": "metric"
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params=payload)
    print(response.url)

    data = response.json()
    print(data)


with DAG(
    "weather_api_dag",
    schedule="0 */3 * * *",
    start_date=timezone.datetime(2025, 2, 1),
    tags=["dpu"]
):
    start = EmptyOperator(task_id="start")

    get_weather_data = PythonOperator(
        task_id="get_weather_data",
        python_callable=_get_weather_data,
    )

    end = EmptyOperator(task_id="end")

    start >> get_weather_data >> end