Feature: This feature file contains git workflow.

  Scenario: Basic git workflow.
  Given user logs in GitHub using basic authentication
  When user creates repository with name "git_flow_task" + suffix current time
  And user creates branch "feature/git_flow_feature"
#  And user commits auto generated file
#  Then user creates pull request to master branch