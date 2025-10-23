import requests

api_url = "https://randomuser.me/api/"
def fetch_data():
    try:
        
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully.")
        return response.json()
    except requests.exceptions.RequestException as e :
        print(f"An error occurred : {e}")
        raise