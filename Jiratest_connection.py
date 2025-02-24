from jira import JIRA

# Jira server URL and credentials
jira_server = 'https://abc.atlassian.net'
jira_user = 'abc@gmail.com'
jira_api_token = 'abc'

# Connect to Jira
jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_api_token))

# JQL query to fetch epics
jql_query = 'issuetype = Epic'

# Fetch epics
epics = jira.search_issues(jql_query)

# Print epic details
for epic in epics:
    print(epic.raw) # Print raw JSON response
    # print(epic.__dict__) # Print object attributes
    print(f"Epic Key: {epic.key}, Summary: {epic.fields.summary}")
