from __future__ import unicode_literals
from collections import Counter
from jira.client import JIRA

def main():
    jira_options = {'server': 'https://annapoorani.atlassian.net'}
    jira = JIRA(options=jira_options,basic_auth=('annapoorani.priyamani@gmail.com','hoodi2782'))
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
    #project = PORTAL AND environment ~ Staging AND createdDate > "2017/05/29" AND "End date" < "2017/09/29"-I have to pass this query in the code if I use this for client"
    resultList_staging = jira.search_issues
    
    #Finding the number of issues on staging
    
    resultList_staging = jira.search_issues("'project' = 'First-Project' AND 'labels' = 'Staging'", startAt=0, maxResults=10, validate_query=True, fields=None, expand=None, json_result=None)
    Issues_on_staging = len(resultList_staging)
    print Issues_on_staging
    print resultList_staging

    #Finding the number of issues on Production
    resultList_production = jira.search_issues("'project' = 'First-Project' AND 'labels' = 'Production'", startAt=0, maxResults=10, validate_query=True, fields=None, expand=None, json_result=None)
    Issues_on_production = len(resultList_production)
    print Issues_on_production
    print resultList_production

    
    
    
    """for issue in resultList:
            print issue.fields.components,issue.fields.reporter,issue.fields.environment"""
            
    
	
	
if __name__=='__main__':
	main()


