from jira import JIRA
import openai

# JIRA Configuration
jira_server = 'https://abc.atlassian.net'
jira_user = 'abc@gmail.com'
jira_api_token = 'abc'
# Azure OpenAI Configuration
deployment_name = "gpt-4o-base"
api_key = "abc"
endpoint = "https://abc-eastus2.cognitiveservices.azure.com"

# Connect to JIRA
jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_api_token))

# JQL Query to Fetch Epics
jql_query = 'issuetype = Epic'
epics = jira.search_issues(jql_query)

# Function to Get Test Case from Azure OpenAI
def generate_test_case(context):
    openai.api_key = api_key
    openai.api_base = endpoint
    openai.api_type = "azure"
    openai.api_version = "2023-12-01-preview"  # Update if needed

    response = openai.ChatCompletion.create(
        engine=deployment_name,  # Deployment name in Azure
        messages=[{"role": "system", "content": "You are a test case generator."},
                  {"role": "user", "content": f"Generate test cases for the following requirement:\n{context}"}],
        max_tokens=500, temperature=0.2
    )
    return response["choices"][0]["message"]["content"]

# Process Each Epic and Add a Comment in Jira
for epic in epics:
    summary = epic.fields.summary
    description = epic.fields.description if hasattr(epic.fields, "description") and epic.fields.description else "No description provided."
    
    requirement = f"Summary: {summary}\nDescription: {description}"
    test_case = generate_test_case(requirement)

    # Create a comment with the generated test cases
    comment_text = f"### Automated Test Cases Generated:\n{test_case}"

    # Add the comment to the Epic in Jira
    try:
        jira.add_comment(epic, comment_text)
        print(f"Added test cases as a comment in Epic {epic.key}.")
    except Exception as e:
        print(f"Failed to add comment to Epic {epic.key}: {e}")

print("All Epics updated with test case comments successfully!")
