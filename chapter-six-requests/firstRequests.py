import requests

params = {"q": "pizza"}

# create request r and configure to get contents from google.com
r = requests.get("https://www.google.com", params=params)

# print status code of request
print("this is the request status:", r.status_code)

# print url which have bin reqeusted
print(r.url)

# open file with write+ rights and write html code to it
f = open("./page.htm", "w+")
f.write(r.text)


