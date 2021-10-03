import pandas as pd
import os
import json

def get_data():
    df = pd.DataFrame()
    directory = 'database'
    for filename in os.listdir(directory):
        with open('database/'+filename) as file:
            jsondata = json.load(file)
            df = pd.concat([df, pd.json_normalize(jsondata['data'])])
    df = df.drop(["meetingsFaculty", "faculty"], axis=1)
    df.to_csv('all_data.csv')

get_data()