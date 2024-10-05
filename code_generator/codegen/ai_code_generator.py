import openai
import base64
import requests

class AICodeGenerator:

    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    @staticmethod
    def get_jira_issue(issue_key, jira_url, email, api_token):
        credentials = f"{email}:{api_token}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        headers = {"Authorization": f"Basic {encoded_credentials}", "Content-Type": "application/json"}
        response = requests.get(f"{jira_url}/rest/api/3/issue/{issue_key}", headers=headers)
        return response.json() if response.status_code == 200 else None


    def generate_code(self, prompt):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            if response.choices:
                return response.choices[0].message.content.strip()
            else:
                return "No completion found."
        except Exception as e:
            print(f"Error in generating code: {e}")
            return None
