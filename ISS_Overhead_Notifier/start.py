# import requests
# import datetime as dt
#
# # # requests.get() is used to get data from a website's api
# # response = requests.get("http://api.open-notify.org/iss-now.json")
# # # print(response.status_code) # status code gets the actual code from the response object
# #
# # response.raise_for_status()
# # data = response.json() # this helps get the json data from the response object
# # longitude = data["iss_position"]["longitude"]
# # latitude = data["iss_position"]["latitude"]
# #
# # iss_position = (longitude, latitude)
# # print(iss_position)
#
# parameters = {
#     "lat" : MY_LAT,
#     "lng" : MY_LONG,
#     "formatted" : 0
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# print(sunrise, sunset)
#
# time_now = dt.datetime.now()
# print(time_now.hour)
#
