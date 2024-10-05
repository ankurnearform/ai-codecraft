# Code Craft

## Overview
This project, Code Craft, automates the generation of code based on predefined templates and integrates with JIRA to retrieve project-specific details directly from issue descriptions. It is designed to accelerate development processes, maintain code quality, and ensure consistency across large teams or projects.

## Key Features
- **Template Management**: Manage and customize code templates.
- **Dynamic Code Generation**: Generate code dynamically based on user inputs and configurations.
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