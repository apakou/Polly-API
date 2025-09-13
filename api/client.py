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


def fetch_polls(api_url, skip=0, limit=10):
    """
    Fetches paginated poll data from /polls endpoint.
    Args:
        api_url (str): Base URL of the API (e.g., http://localhost:8000)
        skip (int): Number of items to skip
        limit (int): Max number of items to return
    Returns:
        list: List of polls, each matching the PollOut schema
    """
    url = f"{api_url}/polls"
    params = {"skip": skip, "limit": limit}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()
