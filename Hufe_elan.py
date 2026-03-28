#网页登录请求实现

import requests

# 请求的 URL

url = "http://10.63.3.1:801/eportal/portal/login"

# 请求参数
#更改user_account以及user_password
params = {

    "callback": "dr1002",

    "login_method": "1",

    "user_account": ",3,学号",

    "user_password": "密码",

    "wlan_user_ip": "172.17.124.5",

    "wlan_user_ipv6": "",

    "wlan_user_mac": "000000000000",

    "wlan_ac_ip": "10.63.3.254",

    "wlan_ac_name": "",

    "jsVersion": "4.1.3",

    "terminal_type": "2",

    "lang": "zh-cn",

    "v": "4811",

    "lang": "zh"

}

# 请求头

headers = {

    "Host": "10.63.3.1:801",

    "Connection": "keep-alive",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",

    "Accept": "*/*",

    "Referer": "http://10.63.3.1/",

    "Accept-Encoding": "gzip, deflate",

    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"

}

# 发送 GET 请求

response = requests.get(url, params=params, headers=headers)

# 打印响应内容

print(response.text)