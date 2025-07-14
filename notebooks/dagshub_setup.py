import mlflow 
import dagshub
dagshub.init(repo_owner='DHRUV-29-10-3', repo_name='mlops-miniproject', mlflow=True)

mlflow.set_tracking_uri("https://dagshub.com/DHRUV-29-10-3/mlops-miniproject.mlflow")

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)