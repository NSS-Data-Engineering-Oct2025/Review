import pandas as pd
import os
import requests
from dotenv import load_dotenv

load_dotenv()
URL= os.getenv("url")

def api():
    api_url = URL;
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    sample_data = pd.DataFrame(data)
    sample_data.to_csv("./sample.csv", index=False)
    return sample_data