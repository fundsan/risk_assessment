from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json
from shutil import copy


##################Load config.json and correct path variable
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
prod_deployment_path = os.path.join(config['prod_deployment_path']) 
test_data_path = os.path.join(config['test_data_path']) 
output_model_path = os.path.join(config['output_model_path']) 
####################function for deployment
def store_model_into_pickle(model):
    #copy the latest pickle file, the latestscore.txt value, and the ingestfiles.txt file into the deployment directory

    pickle.dump(model, open(os.getcwd()+'/'+prod_deployment_path+'/'+deployedname, 'wb'))
    copy(os.getcwd()+'/'+test_data_path+'/'+'latestscore.txt',os.getcwd()+'/'+prod_deployment_path+'/'+'latestscore.txt')
    copy(os.getcwd()+'/'+dataset_csv_path+'/'+'ingestedfiles.txt',os.getcwd()+'/'+prod_deployment_path+'/'+'ingestedfiles.txt')
if __name__ == '__main__':
    deployedname='trainedmodel.pkl'
    with open(os.getcwd()+'/'+output_model_path+'/'+deployedname, 'rb') as file:
        model = pickle.load(file)
    store_model_into_pickle(model)