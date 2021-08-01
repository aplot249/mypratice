#@author: sareeliu
#@date: 2021/7/4 13:45
import aiohttp,asyncio,re,json

from lxml import etree

url = "https://cableav.tv/category/master-91porn/page/1/"


async def item(title,link):
    async with aiohttp.ClientSession() as session:
        response = await session.get(link)
        res = await response.text()
        vidorev_jav_js_object = re.search("var vidorev_jav_js_object = (.*?);",res).group(1)
        vidorev_jav_js_object_json = json.loads(vidorev_jav_js_object)
        d1 = vidorev_jav_js_object_json['single_media_sources']
        d2 = vidorev_jav_js_object_json['single_media_vod_metadata']
        d1.insert(0,d2)
        d1.insert(0,{"title":title})
        print(d1)
        # return d1


async def main(url):
    headers = {
        "referer": "https://cableav.tv/",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url,headers=headers,allow_redirects=True)
        res = await response.text()
        tree = etree.HTML(res)
        current_page_num = int(url.split("page/")[-1].rstrip('/'))
        next_page = url.split("page/")[0]+"page/"+str(current_page_num+1)+"/"
        latest_page = tree.xpath("//main/div/div[last()]/div/div/a[last()]/@href")[0]
        latest_page_num = int(latest_page.split("page/")[-1].rstrip('/'))
        # print(url,next_page,latest_page,latest_page_num)
        divs = tree.xpath('//article/div/div[@class="blog-pic"]/div')
        # list = []
        for div in divs:
            link = div.xpath("./a/@href")[0]
            title = div.xpath("./a/@title")[0]
            # img = div.xpath("./a/img/@data-src")[0]
            # print(link,title,img)
            # list.append(item(title,link))

            # resp = await loop.create_task(item(title,link))
            # print(resp)
            loop.create_task(item(title, link))

        if current_page_num < latest_page_num:
            # print(next_page)
            await loop.create_task(main(next_page))


loop = asyncio.get_event_loop()
loop.run_until_complete(main(url))
