import time
from datetime import date

import requests
import url
import json



# sms_code_res = requests.get(url.send_code_url)
from utils import json_to_rep

data = {"adminAccount":"18827346934","smsCode":"4436"}
header = {"Content-Type":"application/json"}
jsondata = json.dumps(data)


login_res = requests.post(url=url.login_url,data=jsondata,headers={'content-type': 'application/json'})


if json_to_rep(login_res,'status') != '200':
    print("登录请求出错---------{}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
else:
    jwt_token = json_to_rep(login_res,'data')
    print(jwt_token)




