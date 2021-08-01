import requests,re

#第一次请求GET请求
response1 = requests.get(
    url="https://github.com/login",
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
)
authenticity_token = re.findall('name="authenticity_token".*?value="(.*?)"',response1.text,re.S)
r1_cookies = response1.cookies.get_dict() #获取到的cookie

#第二次请求POST请求
response2 = requests.post(
    url="https://github.com/session",
    headers={"Referer": "https://github.com/", "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36", },
    data={"commit":"Sign in", "utf8":"✓", "authenticity_token":authenticity_token, "login":"用户名", "password":"密码"},
    cookies=r1_cookies
)
print(response2.status_code)
print(response2.history)  #跳转的历史状态码

#第三次请求，登录成功之后，访问其他页面
r2_cookies = response2.cookies.get_dict() #拿上cookie，表示登陆状态，开始访问页面
response3 = requests.get(
    url="https://github.com/settings/emails",
    headers={"Referer": "https://github.com/", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"},
    cookies=r2_cookies
)

print(response3.text)
print("用户名" in response3.text)  #返回True说明就成功了