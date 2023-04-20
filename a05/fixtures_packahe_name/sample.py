# import json learning
# data = {
#     "name": "Satyam kumar",
#     "place": "patna",
#     "skills": [
#         "Raspberry pi",
#         "Machine Learning",
#         "Web Development"
#     ],
#     "email": "xyz@gmail.com",
#     "projects": [
#         "Python Data Mining",
#         "Python Data Science"
#     ]
# }
# with open("data_file.csv", "w") as write:
#     print(write)
#     json learning.dump(data, write)
##########################################################################
# import json learning
# # JSON string:
# # Multi-line string
# data = """{
#     "Name": "Jennifer Smith",
#     "Contact Number": 7867567898,
#     "Email": "jen123@gmail.com",
#     "Hobbies":["Reading", "Sketching", "Horse Riding"]
#     }"""
#
# # parse data:
# res = json learning.loads(data)
#
# # the result is a Python dictionary:
# print(res)
# print(type(res))
######################################################################
# import json learning
# with open("data_file.json learning", "r") as read_content:
#     print(json learning.load(read_content))

######################################################################
import json
import os
# import filepath as filepath
# filepath = r"C:\Users\write\PycharmProjects\pythonProject_pytest\fixtures_packahe_name\aaa.json"
# a = {"a":1, "b":2}
# def save_dict(_dict,filepath):
#     json.dump(_dict, open(filepath, 'w'))
#     print("saved")
#     print(filepath)
#
# save_dict(a,filepath)
# print(os.getcwd())

#########################################


import json
import os

def save_dict(_dict,filepath):
    json.dump(_dict, open(filepath, 'w'))
    print("saved")
    print(filepath)

print(os.getcwd())
