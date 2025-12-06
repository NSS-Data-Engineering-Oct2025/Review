import pandas as pd
from minio import Minio
import boto3
import io
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
    
MINIO_URL = os.getenv("MINIO_URL")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")

POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_URL = os.getenv("POSTGRES_URL")
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")


def pg_connection():
    pg_engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_URL}:{POSTGRES_PORT}/{POSTGRES_DATABASE}?sslmode=require"
    )
    return pg_engine

def get_s3_client():
    s3 = boto3.client(
        's3',
        endpoint_url = MINIO_URL,
        aws_access_key_id = MINIO_ACCESS_KEY,
        aws_secret_access_key = MINIO_SECRET_KEY
        )
    return s3

#get data from raw bucket and clean
def get_data_minio(bucket, file):
    s3 = get_s3_client()
    response = s3.get_object(Bucket = bucket, Key = file)
    file_content = response['Body'].read()
    df = pd.read_csv(io.BytesIO(file_content))
    data = pd.DataFrame(df)
    data = data.rename(columns = {"name": "Customer Name"})
    data.to_csv("./sample1.csv", index=False)
    return data

#put clean data to clean bucket
def put_data_minio (bucket, file):
    s3 = get_s3_client()
    response = s3.put_object(Bucket = bucket, Key = file)   
    return response

#send data to PG
# def min_to_pg():
    
#     s3=get_s3_client()
#     #data = get_data_minio("raw", "sample.csv")
#     df=pd.read_csv("./sample1.csv")
#     pg_engine = pg_connection()
#     schema_name='group_5'
#     table_name='sample'
#     df.to_sql(name=table_name, con=pg_engine, schema=schema_name, if_exists='replace',index=False)
