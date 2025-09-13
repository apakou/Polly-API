
import requests
import logging

logging.basicConfig(level=logging.INFO)

def _auth_headers(token):
    """Return headers with Authorization if token is provided."""
    if token:
        return {"Authorization": f"Bearer {token}"}
    return {}

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
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    elif response.status_code == 400:
        logging.error(f"400 Bad Request: {response.json()}")
        return {"error": "Bad Request", "details": response.json()}
    else:
        logging.error(f"Unexpected HTTP {response.status_code}: {response.text}")
        return {"error": f"HTTP {response.status_code}", "details": response.text}


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
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        logging.error(f"400 Bad Request: {response.json()}")
        return {"error": "Bad Request", "details": response.json()}
    else:
        logging.error(f"Unexpected HTTP {response.status_code}: {response.text}")
        return {"error": f"HTTP {response.status_code}", "details": response.text}

def create_poll(api_url, question, options, token=None):
    """
    Create a new poll (protected endpoint).
    Args:
        api_url (str): Base URL of the API
        question (str): Poll question
        options (list): List of option strings
        token (str, optional): JWT access token
    Returns:
        dict: PollOut response or error info
    """
    url = f"{api_url}/polls"
    payload = {"question": question, "options": options}
    headers = _auth_headers(token)
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    elif response.status_code == 400:
        logging.error(f"400 Bad Request: {response.json()}")
        return {"error": "Bad Request", "details": response.json()}
    elif response.status_code == 401:
        logging.error(f"401 Unauthorized: {response.json()}")
        return {"error": "Unauthorized", "details": response.json()}
    else:
        logging.error(f"Unexpected HTTP {response.status_code}: {response.text}")
        return {"error": f"HTTP {response.status_code}", "details": response.text}
