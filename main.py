import requests

USERNAME = "Anmol"
TOKEN = "hajsdjajsdhakhdkakhd"

url = "https://pixe.la/v1/users"

user_parm = {"token": "hajsdjajsdhakhdkakhd",
             "username": "anmolrt",
             "agreeTermsOfService": "yes",
             "notMinor": "yes"
             }

# data = requests.post(url=url, json=user_parm)
# data.raise_for_status()
# print(data.text)


graph_url = f"{url}/anmolrt/graphs"
headers = {"X-USER-TOKEN": "hajsdjajsdhakhdkakhd"}
parmaters = {"id": "graph007", "name": "Cyclying Graph", "unit": "km", "type": "int", "color": "shibafu"}

# graph_data = requests.post(url=graph_url, json=parmaters, headers=headers)
# graph_data.raise_for_status()
# print(graph_data.text)

# Post-Pixel to graph
post_url = f"{url}/anmolrt/graphs/graph007"

post_parameters = {"date": "20200109", "quantity": "4"}

# post_data = requests.post(url=post_url, json=post_parameters, headers=headers)
# post_data.raise_for_status()
# print(post_data.text)


#put request on a pixel

put_url = f"{url}/anmolrt/graphs/graph007/20200109"

put_parameters = {"quantity":"9"}

put_data = requests.put(url=put_url,json=put_parameters,headers=headers)
put_data.raise_for_status()
print(put_data.text)