from flask import request
import json
import os
import subprocess
from subprocess import DEVNULL, STDOUT, check_call

#Specify a URL that resolves to your workspace
with open('config.json','r') as f:
    config = json.load(f) 
def make_responses():
    URL = "http://127.0.0.1:8000/"

        
    output_model_path = os.path.join(config['output_model_path']) 
    test_data_path = os.path.join(config['test_data_path']) 


    #Call each API endpoint and store the responses
   
    response1 =  subprocess.run(['curl',"-X", "POST", URL+'prediction?file={}'.format('testdata.csv') ],capture_output=True).stdout 
    response2 = subprocess.run(['curl',URL+'scoring' ],capture_output=True).stdout
    response3 =subprocess.run(['curl',URL+'summarystats' ],capture_output=True).stdout
    response4 = subprocess.run(['curl',URL+'diagnostics' ],capture_output=True).stdout

    #combine all API responses
    responses = [response1,response2,response3,response4]
    return responses
#write the responses to your workspace

if __name__ == "__main__":
    with open('config.json','r') as f:
        config = json.load(f) 
    output_model_path = os.path.join(config['output_model_path']) 
    responses = make_responses()
    with open(output_model_path+'/apireturns.txt', 'w') as file:
        for res in responses:
           file.write(res.decode("utf-8") )
    


