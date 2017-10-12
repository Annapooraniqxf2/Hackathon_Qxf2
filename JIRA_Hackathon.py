from __future__ import unicode_literals
from collections import Counter
from jira.client import JIRA
import json

def main():
    jira_options = {'server': 'website_address'}
    jira = JIRA(options=jira_options,basic_auth=('email','password'))
    print 'I have logged in'
    #create_issues(jira)
    number_of_issues_filter(jira)
	
"""def create_issues(jira):
    "To create different issues"
    print 'I am going to create new issue'
    #Getting the number of projects in the JIRA
    projects = jira.projects()
    print projects
    #Creating new issue.This method create a issue one at a time
    
    new_issue = jira.create_issue(project='HACKATHON', summary='New issue from jira-python',
                              description='Look into this one', issuetype={'name': 'Bug'},priority={'name':'Low'},components=[{'Component name':'Assessment'}],labels=['Staging'])
    
    #Creating a new issue.This method helps to create multiple issues at a time
    
    issue_list = [
    {
    'project': {'key': 'HACKATHON'},
    'summary': 'First issue of many',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
    'priority':{'name':'Low'},
    'components':[{'Component name':'Assessment'}],
    'labels':['Prodcution']
    },
    {
    'project': {'key': 'HACKATHON'},
    'summary': 'First issue of many',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
    'priority':{'name':'HIGHEST'},
    'components':[{'Component name':'Metrics'}],
    'labels':['Staging']
    },
    {
    'project': {'key': 'HACKATHON'},
    'summary': 'First issue of many',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
    'priority':{'name':'MEDIUM'},
    'components':[{'Component name':'Training'}],
    'labels':['Prodcution']
    },
    {'project': {'key': 'HACKATHON'},
    'summary': 'First issue of many',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
    'priority':{'name':'HIGH'},
    'components':[{'Component name':'TOURNAMENT'}],
    'labels':['STAGING']}]
    issues = jira.create_issues(field_list=issue_list)
    print new_issue
    print 'I have created new issue'"""

	
def number_of_issues_filter(jira):
    "To find the number issues on Staging vs Production"
    print 'I have come inside to find the staging vs production'
    #This is for client
    """#This method gives the number of issues filed on staging    
    resultList_staging = jira.search_issues("'project'='PORTAL' AND 'environment' ~ 'Staging'  AND 'createdDate' > '2017/05/29' AND type = bug",startAt=0, maxResults=100, validate_query=True, fields=None, expand=None, json_result=None)
    Issues_on_staging = len(resultList_staging)
    print Issues_on_staging
    empty_dict={} 
    file1 = open("file1.txt","w")
    empty_dict["Staging"]=Issues_on_staging
    json.dump(empty_dict, open("file1.txt",'w'))
    file1.close()

    #This method gives the number of issues filed but the environment is empty
    resultList_is_empty = jira.search_issues("'project'='PORTAL' AND 'environment' is EMPTY AND 'createdDate' > '2017/05/29' AND type = bug",startAt=0, maxResults=300, validate_query=True, fields=None, expand=None, json_result=None)
    Issue_is_empty = len(resultList_is_empty)
    print Issue_is_empty

    #This method gives the number of issues filed on production
    resultList_in_Production = jira.search_issues("'project'='PORTAL' AND  environment is not EMPTY and environment !~ staging AND 'createdDate' > '2017/05/29'  AND type = bug",startAt=0, maxResults=300, validate_query=True, fields=None, expand=None, json_result=None)
    Issue_in_Production = len(resultList_in_Production)
    print Issue_in_Production
    file1 = open("file1.txt","w")
    empty_dict["Production"]= Issue_in_Production    
    json.dump(empty_dict, open("file1.txt",'w'))  
    file1.close()"""

    #This method provide the number of bugs filed on assessment component against staging
    component_assessment_staging = jira.search_issues("'project' = 'PORTAL' AND 'environment' ~ 'Staging'  AND 'createdDate' > '2017/05/29'  and 'type' = bug and 'component' = 'Assessment'",startAt=0, maxResults=300, validate_query=True, fields=None, expand=None, json_result=None)
    assessment_issue_on_staging = len(component_assessment_staging)
    print assessment_issue_on_staging
    staging_components_dictionary = {}
    staging_dictionary={}
    file1_components = open("compnents_file_staging.txt","w")
    staging_components_dictionary['Assessments']= assessment_issue_on_staging
    staging_dictionary['staging']= staging_components_dictionary
    print staging_dictionary
    json.dump(staging_dictionary, open("components_file_staging.txt",'w'))
    file1_components.close()

    #This method provide the number of bugs filed on tournament component against staging
    component_tournament_staging = jira.search_issues("'project' = 'PORTAL' AND 'environment' ~ 'Staging'  AND 'createdDate' > '2017/05/29'  and 'type' = bug and 'component' = 'Tournament'",startAt=0, maxResults=300, validate_query=True, fields=None, expand=None, json_result=None)
    tournament_issue_on_staging = len(component_tournament_staging)
    print tournament_issue_on_staging
    file1_components = open("compnents_file_staging.txt","w")
    staging_components_dictionary['Tournaments']= tournament_issue_on_staging
    staging_dictionary['staging']= staging_components_dictionary
    print staging_dictionary
    json.dump(staging_dictionary, open("components_file_staging.txt",'w'))
    file1_components.close()

    #This method provide the number of bugs filed on assessment component against production
    component_assessment_production = jira.search_issues("'project' = 'PORTAL' AND environment is not EMPTY and environment !~ staging  AND 'createdDate' > '2017/05/29'  and 'type' = bug and 'component' = 'Assessment'",startAt=0, maxResults=300, validate_query=True, fields=None, expand=None, json_result=None)
    assessment_issue_on_production = len(component_assessment_production)
    print assessment_issue_on_production
    production_components_dictionary = {}
    production_dictionary={}
    file1_components = open("compnents_file_production.txt","w")
    production_components_dictionary['Assessments']= assessment_issue_on_production
    production_dictionary['Production']= staging_components_dictionary
    json.dump(production_dictionary, open("components_file_production.txt",'w'))
    file1_components.close()

    
    #This method provide the number of bugs filed on tournament component against production
    component_tournament_production = jira.search_issues("'project' = 'PORTAL' AND environment is not EMPTY and environment !~ staging  AND 'createdDate' > '2017/05/29'  and 'type' = bug and 'component' = 'Tournament'",startAt=0, maxResults=300, validate_query=True, fields=None, expand=None, json_result=None)
    tournament_issue_on_production = len(component_tournament_production)
    print tournament_issue_on_production    
    file1_components = open("compnents_file_production.txt","w")
    production_components_dictionary['Tournament']= tournament_issue_on_production
    production_dictionary['Production']= production_components_dictionary
    json.dump(production_dictionary, open("components_file_production.txt",'w'))
    file1_components.close()   
    

    
    """#Finding the number of issues on staging
    
    resultList_staging = jira.search_issues("'project' = 'First-Project' AND 'labels' = 'Staging'", startAt=0, maxResults=10, validate_query=True, fields=None, expand=None, json_result=None)
    Issues_on_staging = len(resultList_staging)
    print Issues_on_staging
    print resultList_staging

    #Finding the number of issues on Production
    resultList_production = jira.search_issues("'project' = 'First-Project' AND 'labels' = 'Production'", startAt=0, maxResults=10, validate_query=True, fields=None, expand=None, json_result=None)
    Issues_on_production = len(resultList_production)
    print Issues_on_production
    print resultList_production"""

    
    
    
    """for issue in resultList:
            print issue.fields.components,issue.fields.reporter,issue.fields.environment"""
            
    
	
	
if __name__=='__main__':
	main()


