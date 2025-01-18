import requests


def is_online():
    try:
        response = requests.get("https://www.baidu.com", timeout=5)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


if is_online():
    print("您有网")
else:
    print("您无网")