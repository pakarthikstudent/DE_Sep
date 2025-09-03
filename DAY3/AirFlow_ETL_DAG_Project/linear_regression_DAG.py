from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

## Generate data
def generate_data(**kwargs):
    X = 2 * np.random.rand(100,1)
    Y = 4 + 3 * X + np.random.randn(100,1)


def train_model(**kwargs):
    ti = kwargs['ti']
    X = np.array(ti.xcom_pull(key='x',task_id='generate_datat'))
    Y = np.array(ti.xcom_pull(key='x',task_id='generate_datat'))


model = LinearRegression()
model.fit(X,Y)

def evaluate_model(**kwargs):
        ti = kwargs['ti']
        X = np.array(ti.x_com_pull(key='X',task_id='generate_data'))
        y = np.array(ti.x_com_pull(key='Y',task_id='generate_data'))
        coef = np.array(ti.xcom_pull(key='coef',task_ids='train_model'))
        intercept = np.array(ti.xcom_pull(key='intercept',task_ids = 'train_model'))
        y_pred = X.dot(coef.T)+ intercept


with DAG(dag_id='linear_regression_dag',
         start_date=datetime(2025,9,3),
         schedule_Interval=None,
         catchup=False,
         tags = ['ml','example']) as dag:

    t1 = PythonOperator(task_id="generate_data",python_callable=generate_data,provide_context=True)
    t2 = PythonOperator(task_id="train_model",python_callable=train_model,provide_context=True)
    t3 = PythonOperator(task_id="evalute_model",python_callable=evaluate_model,provide_context=True)


t1 >> t2 >> t3
