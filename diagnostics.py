
import pandas as pd
import numpy as np
import timeit
import os
import json
from io import StringIO
import pickle
import subprocess

##################Load config.json and get environment variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
test_data_path = os.path.join(config['test_data_path']) 
prod_deployment_path = os.path.join(config['prod_deployment_path']) 

##################Function to get model predictions
def model_predictions():
    #read the deployed model and a test dataset, calculate predictions
    
    deployedname='trainedmodel.pkl'
    with open(os.getcwd()+'/'+prod_deployment_path+'/'+deployedname, 'rb') as file:
        model = pickle.load(file)
    
    testdata=pd.read_csv(os.getcwd()+'/'+test_data_path+'/'+'testdata.csv')

    X=testdata[['lastmonth_activity','lastyear_activity','number_of_employees']].values
    y=testdata['exited'].values.ravel()


    predicted=model.predict(X)

    return predicted #return value should be a list containing all predictions

##################Function to get summary statistics
def dataframe_summary():
    data=pd.read_csv(os.getcwd()+'/'+dataset_csv_path+'/'+'finaldata.csv')

    #calculate summary statistics here
    return data.describe() #return value should be a list containing all summary statistics
##################Function to missing data
def missing_data():
    data=pd.read_csv(os.getcwd()+'/'+dataset_csv_path+'/'+'finaldata.csv')
    miss_perc =(data.isnull().sum() * 100) / float(len(data))
    return pd.DataFrame({'column': data.columns,'missing_data_percentage': miss_perc}).reset_index(drop=True)
def execution_time():
    
    starttime = timeit.default_timer()
    os.system('python ingestion.py')
    ingest_timing=timeit.default_timer() - starttime
    


    starttime = timeit.default_timer()
    os.system('python training.py')
    training_timing=timeit.default_timer() - starttime
    
    return [ingest_timing,training_timing]#return a list of 2 timing values in seconds

##################Function to check dependencies
def outdated_packages_list():
    libs = []
    out_libs = []
    up_libs = []
    cur_vers= []
    new_vers=[]
    a = subprocess.Popen(['pip', 'list'], stdout=subprocess.PIPE)
    for line in a.stdout:
        line = line.decode('UTF-8')
        if '------' in line or 'Package' in line:
            continue
        lib, ver = line.split()
        libs.append(lib)
        cur_vers.append(ver)
    
    a = subprocess.Popen(['pip', 'list','-o'], stdout=subprocess.PIPE)
    for line in a.stdout:
        line = line.decode('UTF-8')
        if '------' in line or 'Package' in line:
            continue
        out_lib, _, latest_ver, _ = line.split()
        out_libs.append(out_lib)
        new_vers.append(latest_ver)
    data_list=[]
    for lib in libs:
        if lib in out_libs:
            data_list.append([lib,cur_vers[libs.index(lib)],new_vers[out_libs.index(lib)]])
        else:
            data_list.append([lib,cur_vers[libs.index(lib)],cur_vers[libs.index(lib)]])
    return pd.DataFrame(data=data_list, columns=['Package','Installed Version','Newest Version'])
if __name__ == '__main__':
    print(model_predictions())
    print(dataframe_summary())
    print(missing_data())
    print(execution_time())
    print(outdated_packages_list())
    





    
