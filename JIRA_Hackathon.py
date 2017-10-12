""" This script is used
 1.Login to JIRA
 2.Create an issue or multiple issues
 3.Filter the number of bugs filed on staging
 4.Filter the number of bugs filed on production.Write the filter results into the file
 5.Filter the number of bugs filed on each component against staging vs production.Write the filter results into the file """


from __future__ import unicode_literals
from collections import Counter
from jira.client import JIRA
import json

def main():
    #Using basic_auth log in to the jira account
    jira_options = {'server': 'https://securecodewarrior.atlassian.net'}
    jira = JIRA(options=jira_options,basic_auth=('mak+atlassian@qxf2.com','JIRATestQxf2'))
    #create_issues(jira)
    number_of_issues_filter(jira)
	
"""def create_issues(jira):
    "To create different issues"
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
    issues = jira.create_issues(field_list=issue_list)"""

    	
def number_of_issues_filter(jira):
    "To find the number issues on Staging vs Production"
    #This is for client
    #This method gives the number of issues filed on staging    
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
    file1.close()

        
    #Finding the number of issues on staging
    
    #This method gives the number of issues filed on staging    
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
    file1.close()

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

    #This method provide the number of bugs filed on simple-flow component against staging
    component_simpleflow_staging = jira.search_issues("'project' = 'PORTAL' AND 'environment' ~ 'Staging'  AND 'createdDate' > '2017/05/29'  and 'type' = bug and 'component' = 'Simple Flow'",startAt=0, maxResults=300, validate_query=True, fields=None, expand=None, json_result=None)
    simpleflow_issue_on_staging = len(component_simpleflow_staging)
    print simpleflow_issue_on_staging
    file1_components = open("compnents_file_staging.txt","w")
    staging_components_dictionary['Simple Flow']= simpleflow_issue_on_staging
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

    #This method provide the number of bugs filed on simpleflow component against production
    component_simpleflow_production = jira.search_issues("'project' = 'PORTAL' AND environment is not EMPTY and environment !~ staging  AND 'createdDate' > '2017/05/29'  and 'type' = bug and 'component' = 'Simple Flow'",startAt=0, maxResults=300, validate_query=True, fields=None, expand=None, json_result=None)
    simpleflow_issue_on_production = len(component_simpleflow_production)
    print simpleflow_issue_on_production    
    file1_components = open("compnents_file_production.txt","w")
    production_components_dictionary['Simple Flow']= simpleflow_issue_on_production
    production_dictionary['Production']= production_components_dictionary
    json.dump(production_dictionary, open("components_file_production.txt",'w'))
    file1_components.close()
    

    
    
if __name__=='__main__':
	main()


