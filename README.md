# JIRA Test Case Generator

This repository contains scripts to automate test case generation from JIRA Epic requirements using Generative AI (Azure OpenAI). The test cases can be either:

1. **Stored in a CSV file** – Extracts Epic requirements from JIRA, generates test cases, and saves them in a CSV file
   python test_casesGenerator_to_CSV.py
2. **Added as comments in JIRA** – Extracts Epic requirements from JIRA, generates test cases, and directly posts them as comments in the respective JIRA Epics.
   python test_casesGenerate_to_jira_comments.py
## Prerequisites

Before running the scripts, ensure you have:

- Python 3.8+
- Access to JIRA with an API token
- An active Azure OpenAI instance with `gpt-4o` or similar deployed
- Installed dependencies from `requirements.txt`

## Architecture Diagram
![Arch](https://github.com/user-attachments/assets/54db35c8-b39b-453d-bd96-13e14e8b1e06)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Shivaacu/Jira_Testcases.git
   cd jira-test-case-generator

   pip install -r requirements.txt


