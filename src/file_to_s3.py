import boto3
import pandas as pd
import io 
import os
from dotenv import load_dotenv

load_dotenv()

def final_data_to_s3():
    sso_profile_name = os.getenv('sso_profile_name')
    bucket_name = os.getenv('bucket_s3')  
    file_name = 'Kharel/data_sample1.csv'
    data= pd.read_csv('C:/Users/khare/DE_Oct2025/recap_1/sample1.csv')
    session = boto3.Session(profile_name=sso_profile_name)
    s3_resource = session.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    csv_buffer = io.StringIO() # create an in-memory string buffer
    data.to_csv(csv_buffer, index=False) # write DataFrame to buffer as CSV
   
    csv_data = csv_buffer.getvalue() # get CSV string from buffer
    
    bucket.put_object(Key=file_name, Body=csv_data)

final_data_to_s3() 