import requests
import url

res = requests.get(url.send_code_url)


print(res.text)