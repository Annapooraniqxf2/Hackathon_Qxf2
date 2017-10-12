import matplotlib.pyplot as plt
import json
f=open("components_file_staging.txt","r")
lines = f.readlines()
for line in lines:
    value_dict = eval(line.strip())
    print value_dict
component = []
environment = []
number_of_issues = []
for key,values in value_dict.iteritems():
    environment.append(key)   
        
for key in value_dict['staging'].keys():
    component.append(key)
for values in value_dict['staging'].values():
    number_of_issues.append(values)
 
f.close()

f=open("components_file_production.txt","r")
lines = f.readlines()
for line in lines:
    value_dict = eval(line.strip())
    print value_dict

for key,values in value_dict.iteritems():
    environment.append(key)   
        
for key in value_dict['Production'].keys():
    component.append(key)
for values in value_dict['Production'].values():
    number_of_issues.append(values)
    
print component
print environment
print number_of_issues


