import json
import pandas as pd
import os

def analysis(file, user_id):
    times = 0 
    minutes = 0
    if not os.path.exists(file):
        return 0
    else:
        df = pd.read_json(file)
        times = df[df['user_id'] == user_id]['minutes'].count()
        minutes = df[df['user_id'] == user_id]['minutes'].sum()
        return times, minutes

if __name__ == '__main__':
    t,m = analysis("user_study.json", 223684)
    print(t,m)
