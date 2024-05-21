import requests
import time
from requests_oauthlib import OAuth2Session

# Function to get the OAuth token from Keycloak
def get_oauth_token(client_id, client_secret, token_url, realm, username, password):
    oauth = OAuth2Session(client_id)
    token = oauth.fetch_token(
        token_url=token_url,
        username=username,
        password=password,
        client_id=client_id,
        client_secret=client_secret,
        realm=realm
    )
    return token['access_token']

# Function to check the service status
def check_service(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return False

def main():
    service_url = "https://172.20.67.58/"
    client_id = "printloginprotect"
    client_secret = "E3QOA600e797CrZUwsrf8xNZ5yBi0YgK"
    token_url = "https://172.20.67.58:8443/realms/print_login/protocol/openid-connect/token"
    username = "sura"
    password = "sura@123"
    realm = "your_realm"

    # Get the OAuth token
    token = get_oauth_token(client_id, client_secret, token_url, realm, username, password)
    while True:
        if check_service(service_url, token):
            print("MOSIP Service is up and running!")
        else:
            print("MOSIP Service is down.")
        time.sleep(60)  # Check the service every 60 seconds

if __name__ == "__main__":
    main()
