import mlflow
import random

# Set the MLflow tracking URI
mlflow.set_tracking_uri("http://ec2-18-61-85-110.ap-south-2.compute.amazonaws.com:5000/")

# Start an MLflow run
with mlflow.start_run():
    # Log some random parameters
    mlflow.log_param("param1", random.randint(1, 100))
    mlflow.log_param("param2", random.random())

    # Log some random metrics
    mlflow.log_metric("metric1", random.random())
    mlflow.log_metric("metric2", random.uniform(0.5, 1.5))

    print("Logged random parameters and metrics.")

    # to start mlflow server on ec2: mlflow server --host 0.0.0.0 --allowed-hosts "98.130.44.115:5000" --cors-allowed-origins "ec2-98-130-44-115.ap-south-2.compute.amazonaws.com:5000" --backend-store-uri ./mlruns --default-artifact-root s3://yt-sa-bucket --port 5000

    # mlflow server --host 0.0.0.0 --allowed-hosts "*.amazonaws.com" --backend-store-uri ./mlruns --default-artifact-root s3://yt-sa-bucket --port 5000

    # this finally worked but with security vulnerability
    # mlflow server --host 0.0.0.0 --disable-security-middleware --backend-store-uri ./mlruns --default-artifact-root s3://yt-sa-bucket --port 5000

    
    # mlflow server --host 0.0.0.0 --disable-security-middleware --backend-store-uri ./mlruns --default-artifact-root s3://yt-sa-bucket2 --port 5000

