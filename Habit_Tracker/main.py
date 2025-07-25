import requests
from datetime import datetime as dt

USERNAME = "mrsebe"
TOKEN = "jfah3489p34qfsn3ddf"
GRAPH_ID = "graph1"

# creating a user account on pixela
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params) # we pass data in form of a json
# print(response.text)
# creating a graph for our habit tracker

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Bible study graph",
    "unit": "minutes",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
# posting pixel on my graph

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = dt.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much time did you spend reading your bible today👀? (in minutes)"),
}

# response = requests.post(post_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)
# updating a pixel on the graph

DATE_OF_HABIT = pixel_params["date"]
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_OF_HABIT}"
update_pixel_params = {
    "quantity": "35.0",
}
# response = requests.put(update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)
# delete a pixel on the graph
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_OF_HABIT}"
# response = requests.delete(delete_pixel_endpoint, headers=headers)
# print(response.text)


