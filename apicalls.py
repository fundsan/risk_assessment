from flask import request
import json
import os
#Specify a URL that resolves to your workspace
URL = "0.0.0.0:8000/"
with open('config.json','r') as f:
    config = json.load(f) 

output_model_path = os.path.join(config['output_model_path']) 
test_data_path = os.path.join(config['test_data_path']) 


#Call each API endpoint and store the responses
response1 = request.post(URL+'prediction?file={}'.format('testdata.csv'))
response2 = request.get(URL+'scoring')
response3 = request.get(URL+'summarystats')
response4 = request.get(URL+'diagnostics')

#combine all API responses
responses = [response1,response2,response3,response4]

#write the responses to your workspace
for resp in responses:
    json.dump('apireturns.txt',resp.content)


