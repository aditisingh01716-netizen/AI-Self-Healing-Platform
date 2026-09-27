import requests


SERVICE_URL = "http://127.0.0.1:5001/health"


def check_application_health():

    try:

        response = requests.get(
            SERVICE_URL,
            timeout=3
        )

        if response.status_code == 200:

            return True

    except requests.RequestException:

        return False

    return False