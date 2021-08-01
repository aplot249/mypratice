#@author: sareeliu
#@date: 2021/5/19 12:57
import requests,re
from lxml import etree

# url = "https://vod1eu33.128100.xyz/hls/Mk6weGNWoTL/index.m3u8"
# headers = {
#     "Referer": "https://cableav.tv/",
#     "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#     "sec-ch-ua-mobile": "?0",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# params = {
#     "token": "N09QRlZad1JDVW5DYmFxZm5VcXZuYjFJMzJmRDhyOGoxUDFVM0hEeWtjRmVwNk96b0QrQndwWFNxSGhPbk1LMTMyQ0szUXdqSG52RjNnd052REJyZUZ4QkY5cDViVlNFK29xUWpLa0JhL2pjUG1CZitkbGx2UHVXOGtCUTlCejA=",
#     "ip": "197.149.216.147",
#     "auth": "bb643cd9eb0eff8fccdd426c9b185cd3",
#     "exp": "1625412566",
#     "hash": "6786a3448e08d2ec7f9a57e22eba5828",
# }
#
# res = requests.get(url,headers=headers,params=params)
# print(res.text)



# res = requests.get("https://cableav.tv/nJ09XzyMOkx/")
# print(res.status_code)
# print(res.text)
# ll = re.search('<meta property="og:type" content="video.other"><meta property="og:video:url" content="(.*?)"',res.text).group(1)
# print(ll)

res = requests.get("https://cableav.tv/REHpnxyZ6pz/")
# print(res.text)
dd = re.search("var vidorev_jav_js_object = (.*?);",res.text).group(1)
print(dd)
ddd = json.loads(dd)
print(ddd['single_media_sources'])
print(ddd['single_media_vod_metadata'])