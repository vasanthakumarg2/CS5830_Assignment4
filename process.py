import pandas as pd
from zipfile import ZipFile
import os
import yaml

def process():

    ## get path of current directory
    SCRIPTDIR = os.path.dirname(__file__)

    ## open the params yaml file to get file name and field name
    try:
        with open(SCRIPTDIR+'/fileParams.yaml', 'r') as file:
            params = yaml.safe_load(file)
    except Exception as e:
        print("Error reading the yaml file")

    ## load the data to a dataframe
    data = pd.read_csv(SCRIPTDIR+'/'+params['file_name'])

    data['DATE'] = pd.to_datetime(data['DATE'])
    data['Month'] = data['DATE'].dt.month

    ## compute the monthly average values by grouping the data by month
    monthlyValues = data.groupby('Month')[params['field_name']].mean()

    try:
        ## write the computed monthly values to a csv file
        monthlyValues.to_csv(SCRIPTDIR+'/monthlyComputed.csv', index=False)
    except Exception as e:
        print("Error writing to the csv file")

process()