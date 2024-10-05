import argparse
import json
from Templates.ddl_generation import generate_ddl
from Templates.dbt_model_generator import generate_dbt_model
from codegen.ai_code_generator import AICodeGenerator
from codegen.prompt_manager import extract_prompt_from_description
from utils.text_parser import extract_detail_from_description

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate code from Jira and Confluence descriptions.")
    parser.add_argument('--jira_url', type=str, help='Jira URL including the issue key', required=True)
    parser.add_argument('--template', type=str, required=True, help='Template type to process')
    parser.add_argument('--confluence_url', type=str, help='Confluence URL', required=False)
    return parser.parse_args()

def main():
    args = parse_arguments()
    jira_base_url = args.jira_url.split('/browse')[0]
    issue_key = args.jira_url.split('/')[-1]

    with open('config/configs.json', 'r') as file:
        config = json.load(file)

    generator = AICodeGenerator(config['openai_api_key'])
    issue_details = generator.get_jira_issue(issue_key, jira_base_url, config['jira_email'], config['jira_api_token'])
    if issue_details:
        description = issue_details['fields'].get('description', "")
        prompt = extract_prompt_from_description(description)
        if args.template.lower() == 'ddl':
            table_name = extract_detail_from_description(description, "Table Name")
            if table_name:
                print(f"Table Name extracted: {table_name}")
            else:
                print("Table Name could not be extracted.")
            print(f"Processing DDL template for Jira issue {issue_key}...")
            generate_ddl(generator,prompt,table_name)
        elif args.template.lower() == 'dbt':
            print(f"Processing DBT template for Jira issue {issue_key}...")
            generate_dbt_model(generator,prompt)
        else:
            print("No valid template specified. Please choose either 'ddl' or 'dbt'.")
    else:
        print("Failed to fetch details from Jira.")

if __name__ == "__main__":
    main()

