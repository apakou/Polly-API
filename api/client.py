import requests

def register_user(api_url, username, email, password):
    """
    Registers a new user via the /register endpoint.
    Args:
        api_url (str): Base URL of the API (e.g., http://localhost:8000)
        username (str): Username for registration
        email (str): Email address for registration
        password (str): Password for registration
    Returns:
        dict: JSON response from the API
    """
    url = f"{api_url}/register"
    payload = {
        "username": username,
        "email": email,
        "password": password
    }
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()
