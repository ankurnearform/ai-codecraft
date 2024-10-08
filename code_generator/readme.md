# Code Craft

## Overview
This project, Code Craft, automates the generation of code based on predefined templates and integrates with JIRA to retrieve project-specific details directly from issue descriptions. It is designed to accelerate development processes, maintain code quality, and ensure consistency across large teams or projects.

## Key Features
- **Template Management**: Manage and customize code templates.
- **Dynamic Code Generation**: Generate code dynamically based on user story inputs and system prompts.
- **Integration Support**: Easily integrate with existing development workflows and IDEs.

## Installation

1) Follow these instructions to set up the Code Generator on your local machine:

```bash
git clone https://github.com/ankurnearform/genai-components.git
cd code_generator
pip install -r requirements.txt
```
2) Configure `configs.json` with your API keys and service URLs.

3) Run the Codecraft script with below command line arguments (as per your requirements):

The script accepts several command line arguments to specify the operation details:

- `--jira_url`: Required. The URL of the JIRA issue, including the issue key. This URL is used to identify the specific issue from which the script will fetch and process details.
  
- `--template`: Required. Specifies the type of template to process. This parameter determines which processing logic to apply based on the provided template name, such as 'DDL' for database definition language tasks or 'DBT' for data build tool transformations.

- `--confluence_url`: Optional. The URL of a Confluence page. If provided, the script may fetch additional context or documentation relevant to the operation from this Confluence page.

```bash
python path/to/codecraft.py --options
```
## Sample Usage

To run the script with the required arguments, use the following command in your terminal:

```bash
python codecraft.py --jira_url="https://yourjira.example.com/browse/ISSUE-123" --template="DDL"
```

## Example Template 1 - Generating DDL Scripts:

To generate DDL scripts, follow these steps:

1) Obtain the Jira issue URL that contains the DDL template specifications.

 Jira Issue Link: https://genaiprojects.atlassian.net/browse/SCRUM-1

 <img width="1718" alt="Screenshot 2024-10-05 at 5 34 09 PM" src="https://github.com/user-attachments/assets/ebbb0cd6-c714-415e-9617-978d899e970d">

2) Run the Code Generator script using the Jira URL:

```bash
python codecraft.py --jira_url="https://genaiprojects.atlassian.net/browse/SCRUM-1" --template="ddl"
```
<img width="1581" alt="Screenshot 2024-10-05 at 5 33 15 PM" src="https://github.com/user-attachments/assets/b4d12fc3-c8bd-4c07-962a-e12f968722e6">

3) View the generated DDL script output.

<img width="332" alt="Screenshot 2024-10-05 at 5 33 27 PM" src="https://github.com/user-attachments/assets/297121e1-85c3-4f38-878e-d45c8586411b">

## Example Template 2 - Generating DBT Model Scripts:

To generate DBT model scripts, follow these steps:

1) Obtain the Jira issue URL that contains the DBT model specifications.

 Jira Issue Link: https://genaiprojects.atlassian.net/browse/SCRUM-2

 <img width="1693" alt="Screenshot 2024-10-06 at 7 22 20 PM" src="https://github.com/user-attachments/assets/15832b1d-d584-4feb-ba82-922c93648744">


2) Run the Code Generator script using the Jira URL:

```bash
python codecraft.py --jira_url="https://genaiprojects.atlassian.net/browse/SCRUM-2" --template="dbt"
```
<img width="1408" alt="Screenshot 2024-10-06 at 10 28 15 PM" src="https://github.com/user-attachments/assets/39dc2290-9699-48fb-a54e-c1554eb1b217">

3) View the generated DBT Models output.

<img width="530" alt="Screenshot 2024-10-06 at 10 28 57 PM" src="https://github.com/user-attachments/assets/ee284c87-341d-4670-9921-318a9a41ee92">




