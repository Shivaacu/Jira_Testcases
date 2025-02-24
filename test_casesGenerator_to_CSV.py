import csv
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
api_type= "azure"

# Connect to JIRA
jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_api_token))

# JQL Query to Fetch Epics
jql_query = 'issuetype = Epic'
epics = jira.search_issues(jql_query)

# Prepare Data for OpenAI
requirements = []
for epic in epics:
    summary = epic.fields.summary
    description = epic.fields.description if hasattr(epic.fields, "description") and epic.fields.description else "No description provided."
    
    requirement = f"Summary: {summary}\nDescription: {description}"
    requirements.append(requirement)

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
        max_tokens=500,temperature=0.2
    )
    return response["choices"][0]["message"]["content"]

# Store Data in CSV
csv_filename = "test_cases.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Requirement", "Test Case"])  # CSV Headers
    
    for req in requirements:
        test_case = generate_test_case(req)
        writer.writerow([req, test_case])

print(f"Test cases saved to {csv_filename}")
