"""
This file
1.Reads the text file
2.Creating pie chart for number of bugs filed on staging vs production"""

import matplotlib.pyplot as plt
import json
#Reading the number of issues and environment from the text file
f=open("file1.txt","r")
lines = f.readlines()
for line in lines:
    value_dict = eval(line.strip())
    print value_dict
Environment=[]
Number_of_issues=[]
for key,values in value_dict.iteritems():
    Environment.append(key)
    Number_of_issues.append(values)
print Environment
print Number_of_issues


#Creating graph using the read values
cols=['b','r']
plt.pie(Number_of_issues,labels=Environment,colors=cols,autopct='%1.1f%%')
plt.title("Environment vs No of bugs ")
plt.axis('equal')
plt.show()
