from pytest_bdd import given, when, then
from datetime import datetime, timedelta
import requests
import json

userName = 'shankar5522'
token = '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'
BASE_API = 'https://api.github.com/'
repositoryName = 'git_flow_task'
timeFormat = '{:%H:%M:%S}'


@given(u'user logs in GitHub using basic authentication')
def test_gitHubLoginImpl():
    githubLogin()


@when(u'user creates repository with name "git_flow_task" + suffix current time')
def test_repoCreationStepImpl():
    createRepository()


@when(u'user creates branch "feature/git_flow_feature"')
def test_branchCreationImpl():
    createBranch()


def githubLogin():
    userData = requests.post(BASE_API).json()
    print (userData)


def createRepository():
    present_time = datetime.now()
    timeFormat.format(present_time)
    repo = repositoryName + str(present_time)
    print ('Repository Name ' + repo)
    payload = {'name': repo, 'description': 'Created with api', 'auto_init': 'true'}
    login = requests.post(BASE_API + 'user/repos', auth=(userName, token), data=json.dumps(payload))


def createBranch():
    payload = {"ref": "refs/heads/pythonAutoBranch", "sha": "5376df2"}
    branchName = requests.get('https://api.github.com/repos/shankar5522/GitWorkFlow/branches', data=json.dumps(payload))
    print branchName
