
def greeting() -> str:
    return "Hello, How can I assist you today?"

def validate_name(name: str) -> bool:
    """
    Validates the name format.
    Args:
        name (str): The name to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    return name.isalpha()

def validate_phone_number(phone_number: str) -> bool:
    """
    Validates the phone number format,
    if it starts with '+' followed 7-15 digits
    or starts with 0 followed by 6-14 digits.
    Args:
        phone_number (str): The phone number to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    import re
    pattern = re.compile(r'^(?:\+\d{7,15}|0\d{6,14})$')
    return bool(pattern.match(phone_number))
    

def close() -> str:
    return "Goodbye! Have a great day!"

def list_contacts(contacts: dict) -> str:
    """
    Lists all contacts in a formatted string.
    Args:
        contacts (dict): A dictionary of contacts with names as keys and phone numbers as values.
    Returns:
        str: A formatted string of all contacts.
    """
    if not contacts:
        return "No contacts found."
    result = "Contacts List:\n"
    for name, number in contacts.items():
        result += f"{name}: {number}\n"
    return result.strip()