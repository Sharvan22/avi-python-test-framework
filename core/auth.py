import requests

def register_and_login(base_url, username, password):
    requests.post(
        f"{base_url}/register",
        json={"username": username, "password": password}
    )

    response = requests.post(
        f"{base_url}/login1",
        auth=(username, password)
    )
    response.raise_for_status()
    return response.json()["token"]
