import yaml
import re

def load_system_prompts():
    """
    Load system prompts from a YAML file.
    """
    with open('system_prompts.yml', 'r') as file:
        return yaml.safe_load(file)

def get_combined_prompt(description_content, template_type, system_prompts):
    """
    Combine system and user prompts into a single string.
    """
    user_prompt = extract_prompt_from_description(description_content)
    system_prompt = system_prompts['prompts'][template_type]['description']
    return f"{system_prompt}\nDetails:\n{user_prompt}"

def extract_prompt_from_description(description):
    """
    Extract the prompt based on the 'Query:' in the structured description.
    """
    extracted_text = parse_content(description)
    match = re.search(r"Query:(.*?)$", extracted_text, re.DOTALL)
    return match.group(1).strip() if match else extracted_text.strip()

def parse_content(content):
    """
    Recursively extract text from the nested 'content' field in the description,
    ensuring that structural elements like paragraphs and lists are handled compactly.
    """
    if isinstance(content, list):
        return ' '.join(parse_content(item) for item in content if item)
    elif isinstance(content, dict):
        text = content.get('text', '')
        # Recursively process children content
        children_text = parse_content(content.get('content', []))
        # Join parent text and children text with appropriate spacing
        if children_text:
            if text.endswith(':'):
                text += ' ' + children_text
            else:
                text += '\n' + children_text if text else children_text
        return text
    return content if isinstance(content, str) else ''



