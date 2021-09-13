import pickle
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from diagnostics import model_predictions



###############Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
output_model_path = os.path.join(config['output_model_path']) 
test_data_path = os.path.join(config['test_data_path']) 



##############Function for reporting
def score_model():
    #calculate a confusion matrix using the test data and the deployed model
    #write the confusion matrix to the workspace
    testdata=pd.read_csv(os.getcwd()+'/'+test_data_path+'/'+'testdata.csv')

    X=testdata[['lastmonth_activity','lastyear_activity','number_of_employees']].values
    y=testdata['exited'].values.ravel()
    
    predictions = model_predictions()
    
    
    arr=confusion_matrix(y, predictions)
    
    confusion_df = pd.DataFrame(arr)

    htmap = sns.heatmap(confusion_df, annot=True)

    figure = htmap.get_figure()    
    figure.savefig(os.getcwd()+'/'+output_model_path+'/'+'confusionmatrix.png', dpi=400)
    




if __name__ == '__main__':
    score_model()
