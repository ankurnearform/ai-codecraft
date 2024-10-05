from codegen.prompt_manager import parse_content
import re


def extract_detail_from_description(description, key):
    """
    Extracts a specific detail based on a key from the description text, handling various formatting issues robustly with regex.
    """
    description_text = parse_content(description)
    # Regex to handle different spacings and newlines
    pattern = rf"{re.escape(key)}\s*:\s*(\S+)"
    match = re.search(pattern, description_text, re.IGNORECASE | re.MULTILINE)

    if match:
        return match.group(1)
    return None

