import pandas as pd
from dotenv import load_dotenv
import api as api
import min_io as mi
import file_to_s3 as aws



#this is a test 

def main():
    
    api.api()
    mi.get_data_minio("raw", "sample.csv")
    mi.put_data_minio("clean", "sample1.csv")
    aws.final_data_to_s3()
    
    
    
    
if __name__ == "__main__":
        main()
        