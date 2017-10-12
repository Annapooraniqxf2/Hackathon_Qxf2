import matplotlib.pyplot as plt
import json
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

#Environment = ['Staging','Production']
#Number_of_issues = [46,41]
cols=['b','r']
plt.pie(Number_of_issues,labels=Environment,colors=cols)
plt.title("Number of bugs introduced ")
#plt.axis(equal)
plt.show()
