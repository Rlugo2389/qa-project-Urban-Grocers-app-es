import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_body)

def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=kit_body, headers=headers)

