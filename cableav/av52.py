#@author: sareeliu
#@date: 2021/7/4 21:20
import aiohttp,re,asyncio,execjs
from lxml import etree

async def each(src,comp):
    async with aiohttp.ClientSession() as session:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Referer":"https://www.52av.one/"
        }
        response = await session.get(src,headers=headers)
        res = await response.text()
        print(res)
        cc = res.split("\n")[-1].lstrip("eval(myencryptHTML(")[:-3]
        ddddd = comp.call('myencryptHTML',cc)
        print(ddddd)


#var ccsJsCmds = '\'2C\'2;\'2;\'2;kh\'42\'4:hnxlu0kuUwrrqtvgf\'4:\'4;\'4;\'42\'9D\'2C\'42\'42\'2;\'2;\'2;\'2;xct\'42xkfgqGngogpv\'42\'5F\'42fqewogpv0igvGngogpvD{Kf\'4:\'44ogfkcrnc{gt3\'44\'4;\'5D\'2C\'42\'42\'2;\'2;\'2;\'2;xct\'42hnxRnc{gt\'42\'5F\'42hnxlu0etgcvgRnc{gt\'4:\'9D\'2C\'42\'42\'42\'42\'42\'42\'2;\'2;\'2;\'2;v{rg\'5C\'42\'44hnx\'44\'4E\'2C\'42\'42\'42\'42\'42\'42\'2;\'2;\'2;\'2;wtn\'5C\'42\'44jvvru\'5C\'4H\'4Hxkfgq50{qeqqnpgv0kp\'4Hhkngu\'4Hor6\'4H8\'4H4\'4Hh\'4H84h3734dZfSXF[\'5F0hnx\'44\'2C\'42\'42\'2;\'2;\'2;\'2;\'9F\'4;\'5D\'2C\'42\'42\'2;\'2;\'2;\'2;hnxRnc{gt0cvvcejOgfkcGngogpv\'4:ogfkcrnc{gt3\'4;\'5D\'2C\'42\'42\'2;\'2;\'2;\'2;hnxRnc{gt0nqcf\'4:\'4;\'5D\'2C\'42\'42\'2;\'2;\'2;\'2;hnxRnc{gt0rnc{\'4:\'4;\'5D\'2C\'2;\'2;\'2;\'9F\'42\'2C\'2;\'2;\'2;gnug\'42\'9D\'2C\'2;\'2;\'2;\'2;fqewogpv0igvGngogpvD{Kf\'4:\'44ogfkcrnc{gt3\'44\'4;0kppgtJVON\'5F\'44pqv\'42uwrrqtv\'42hnx\'44\'5D\'2C\'2;\'2;\'2;\'9F';
#eval(myencryptHTML('gxcn*wpguecrg*o{gpet{rvJVON*eeuLuEofu+++='));

#var ccsJsCmds = ')4E)4=)4=)4=mj)64)6<jpznw2mwWyttsvxih)6<)6=)6=)64);F)4E)64)64)4=)4=)4=)4=zev)64zmhisIpiqirx)64)7H)64hsgyqirx2kixIpiqirxF}Mh)6<)66qihmetpe}iv5)66)6=)7F)4E)64)64)4=)4=)4=)4=zev)64jpzTpe}iv)64)7H)64jpznw2gviexiTpe}iv)6<);F)4E)64)64)64)64)64)64)4=)4=)4=)4=x}ti)7E)64)66jpz)66)6G)4E)64)64)64)64)64)64)4=)4=)4=)4=yvp)7E)64)66lxxtw)7E)6J)6Jzmhis72}sgssprix2mr)6Jjmpiw)6Jqt8)6Ji)6Jf)6Jf)6Jiff6556iphX[KI)7H2jpz)66)4E)64)64)4=)4=)4=)4=);H)6=)7F)4E)64)64)4=)4=)4=)4=jpzTpe}iv2exxeglQihmeIpiqirx)6<qihmetpe}iv5)6=)7F)4E)64)64)4=)4=)4=)4=jpzTpe}iv2pseh)6<)6=)7F)4E)64)64)4=)4=)4=)4=jpzTpe}iv2tpe})6<)6=)7F)4E)4=)4=)4=);H)64)4E)4=)4=)4=ipwi)64);F)4E)4=)4=)4=)4=hsgyqirx2kixIpiqirxF}Mh)6<)66qihmetpe}iv5)66)6=2mrrivLXQP)7H)66rsx)64wyttsvx)64jpz)66)7F)4E)4=)4=)4=);H';
#eval(myencryptHTML('izep,yriwgeti,q}irgv}txLXQP,ggwNwGqhw---?'));

async def item(link):
    async with aiohttp.ClientSession() as session:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Referer":"https://www.52av.one/"
        }
        response = await session.get(link,headers=headers)
        res = await response.text()
        # print(res)
        js = re.search('<script type="text/javascript">\nfunction(?P<js>.*?)function refresh_page',res,re.S).group('js')
        jsstr1,jsstr2 = str("function"+js.replace("document.write(","")[:-3]).split("\n")
        print(jsstr1,jsstr2,sep='\n')
        print("#"* 15)
        comp = execjs.compile(jsstr1)
        print("#"* 30)
        rrr = comp.call("myencryptHTML",str(jsstr2).lstrip('myencryptHTML("')[:-2])
        print(rrr)
        src = re.search('ajax.open \("GET", "(.*?)", true\);',res).group(1)
        # print(src)
        await each("https://video1.yocoolnet.in/api/"+src,comp)


async def main(startUrl):
    async with aiohttp.ClientSession() as session:
        response = await session.get(startUrl)
        res = await response.text(errors='ignore')
        tree = etree.HTML(res)
        src = tree.xpath('//iframe[@id="allmyplayer"]/@src')[0]
        print(src)
        await item("https:"+src)

startUrl = "https://www.52av.one/thread-71026-1-1.html"
loop = asyncio.get_event_loop()
loop.run_until_complete(main(startUrl))