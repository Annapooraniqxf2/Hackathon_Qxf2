import matplotlib.pyplot as plt
import json,numpy
import matplotlib.patches as mpatches
f=open("components_file_staging.txt","r")
lines = f.readlines()
for line in lines:
    value_dict = eval(line.strip())
    print value_dict
component = []
environment = []
number_of_issues1 = []
number_of_issues2 = []
for key,values in value_dict.iteritems():
    environment.append(key)   
        
for key in value_dict['staging'].keys():
    component.append(key)
for values in value_dict['staging'].values():
    number_of_issues1.append(values)
 
f.close()

f=open("components_file_production.txt","r")
lines = f.readlines()
for line in lines:
    value_dict = eval(line.strip())
    print value_dict

for key,values in value_dict.iteritems():
    environment.append(key)   
        
"""for key in value_dict['Production'].keys():
    component.append(key)"""
for values in value_dict['Production'].values():
    number_of_issues2.append(values)
    
print component
print environment
print number_of_issues2
x=numpy.arange(len(component))
print x

plt.bar(component,number_of_issues1,color='gray')
plt.bar(component,number_of_issues2,color='yellow',bottom=number_of_issues1)
plt.grid(axis='y')
plt.xticks(x,['Assessment','Tournament'])
plt.yticks(numpy.arange(29))
plt.title("Component Vs Environment")
plt.xlabel('Components')
plt.ylabel('No of bugs')
gray_patch = mpatches.Patch(color='gray',label='Staging')
yellow_patch=mpatches.Patch(color='yellow',label='Production')
plt.show()

