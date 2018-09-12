import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def data_plot():
    df = pd.read_json("user_study.json")
#    user_id = df['user_id']
#    minutes = df[df['user_id'] == user_id]['minutes'].sum()
    data = df.groupby('user_id').sum().head(50000)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Studydata")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    ax.plot(data)
    plt.show()

if __name__ == '__main__':
    dp = data_plot()

