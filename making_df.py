import pandas as pd
import json
import os

def parse_json_entry(entry):
    json_entry = json.loads(entry)
    points = json_entry['data']
    df_entry = pd.DataFrame()
    
    for point in points:
        term = point['termDesc']
        subject = point['subject']
        course_title = point['courseTitle']
        enrollment = point['enrollment']
        campus_desc = point['campusDescription']
        
        df_entry = pd.concat([df_entry, pd.DataFrame({'term': [term], 'subject': [subject], 'course_title': [course_title],
                                                      'enrollment': [enrollment], 
                                                      'campus_desc': [campus_desc]})])
    
    return df_entry
        
def make_df():
    df = pd.DataFrame()
    for filename in os.listdir("Database"):
        if filename.endswith(".json"):
            with open("Database/" + filename) as f:
                data = f.read()
                print("Doing " + filename)
                df_entry = parse_json_entry(data)
                df = pd.concat([df, df_entry])
    return df

if __name__ == "__main__":
    make_df().to_csv("processed_data/data.csv")
    