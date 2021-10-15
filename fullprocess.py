
import json
import os
import training
import scoring
import deployment
import diagnostics
import reporting
import pandas as pd
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['input_folder_path']) 
output_model_path = os.path.join(config['output_model_path']) 
test_data_path = os.path.join(config['test_data_path']) 
##################Check and read new data
#first, read ingestedfiles.txt
ingestedfile_df = pd.read_csv(os.getcwd()+'/'+dataset_csv_path+'/'+'ingestedfiles.txt',sep=' ',header=None, names=['dir','filename','rows','timestamp'])
filenames = os.listdir(os.getcwd()+'/'+dataset_csv_path)
new_data = False
for file in filenames:
    if file not in ingestedfile_df['filename']:
        new_data = True
        

#second, determine whether the source data folder has files that aren't listed in ingestedfiles.txt



##################Deciding whether to proceed, part 1
#if you found new data, you should proceed. otherwise, do end the process here


##################Checking for model drift
#check whether the score from the deployed model is different from the score from the model that uses the newest ingested data


##################Deciding whether to proceed, part 2
#if you found model drift, you should proceed. otherwise, do end the process here



##################Re-deployment
#if you found evidence for model drift, re-run the deployment.py script

##################Diagnostics and reporting
#run diagnostics.py and reporting.py for the re-deployed model







