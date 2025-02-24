# JIRA Test Case Generator

This repository contains scripts to automate test case generation from JIRA Epic requirements using Generative AI (Azure OpenAI). The test cases can be either:

1. **Stored in a CSV file** – Extracts Epic requirements from JIRA, generates test cases, and saves them in a CSV file.
2. **Added as comments in JIRA** – Extracts Epic requirements from JIRA, generates test cases, and directly posts them as comments in the respective JIRA Epics.

## Prerequisites

Before running the scripts, ensure you have:

- Python 3.8+
- Access to JIRA with an API token
- An active Azure OpenAI instance with `gpt-4o` or similar deployed
- Installed dependencies from `requirements.txt`

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Shivaacu/Jira_Testcases.git
   cd jira-test-case-generator

   pip install -r requirements.txt
```
![Uploading image.png…]()

