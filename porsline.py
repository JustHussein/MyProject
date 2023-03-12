import requests
import json

url = "https://survey.porsline.ir/api/surveys/667499/responses/"

payload = json.dumps({
    "from_date": "2023-03-06",
    "to_date": "2023-03-06",
    "page": 1,
    "sort_obj": {
        "col_type": 3,
        "id": 6,
        "reverse": False
    },
    "filter_obj": {}
})
headers = {
    'Authorization': 'API-Key 5484d9bb1078b17de5a05de3826236765fd9f9c5',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


# url = "https://survey.porsline.ir/api/surveys/678442/responses"

# payload = json.dumps([
#     "code1",
#     "code2",
#     "code3"
# ])
# headers = {
#     'Authorization': 'API-Key 5484d9bb1078b17de5a05de3826236765fd9f9c5',
#     'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
