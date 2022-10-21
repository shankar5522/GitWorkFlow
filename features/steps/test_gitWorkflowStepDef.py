from pytest_bdd import given, when, then
from datetime import datetime, timedelta
import requests
import json

#take from another file
userName = 'shankar5522'
token = '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'
BASE_API = 'https://api.github.com/'
repositoryName = 'git_flow_task'
timeFormat = '{:%H:%M:%S}'

@given(u'user logs in GitHub using basic authentication')
def test_gitHubLoginImpl():
    githubLogin()
    print ('manish D')

def githubLogin():
    print ('abc')
    userData = requests.post(BASE_API).json()
    print (userData)

@when(u'user creates repository with name "git_flow_task" + suffix current time')
def test_repoCreationStepImpl():
    createRepository()

def createRepository():
    print 'as'
    present_time = datetime.now()
    timeFormat.format(present_time)
    repo = repositoryName + str(present_time)
    print ('Repository Name ' + repo)
    payload = {'name': repo, 'description': 'Created with api', 'auto_init': 'true'}
    login = requests.post(BASE_API + 'user/repos', auth=(userName,token), data=json.dumps(payload))



# @given(u'user logs in GitHub using basic authentication')
# def test_step_impl(context):
#     print 'abc'