import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


#import data provided as Excel spreadsheet
data = pd.read_excel("Data/Call-Center-Dataset.xlsx",sheet_name='Dataset')

data.shape

data.isna().sum()

data.dtypes

#this can also be done as .astype(), datetime or .dt
#create function of converting talk duration as seconds
def convert_time(row):
    '''Return average talk duration as seconds'''
    return pd.Timedelta(hours=row.hour,minutes=row.minute,seconds=row.second).total_seconds() if pd.notnull(row) else None

#confirm how it works
data.AvgTalkDuration.apply(lambda x: convert_time(x))

#apply total seconds function
data['AvgTalkDuration'] = data.AvgTalkDuration.apply(lambda x: convert_time(x))
data.head()

