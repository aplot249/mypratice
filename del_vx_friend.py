import uiautomator2 as u2
import time,os

print('''
欢迎使用本程序！
本程序根据python uiautomator自动化测试，实现程序模拟人工删除微信好友的操作。
程序本身并非对微信数据进行抓包，所以完全不用担心有封号风险，借助本程序，可以实现批量删除微信好友。
程序的使用，需要事先给要删除的好友都添加一个共同标签，程序会删除这个标签下的所有好友。
（如果有大量的好友需要删除，可以采用建立群，把要删除的好友一一拉进群，在再新建标签，从群里导入，就能快速给群好友打上标签。）

程序使用教程如下：
1、安卓手机进入开发者模式：
    在设置中，点“系统”，再点“关于手机”，进入“关于手机”后，连续多次点击“版本号”一栏，就可进入“开发者模式”。
    在“开发者模式”中，打开“USB调试”。然后通过USB数据线和电脑连接。
2、回到电脑端，确保adb运行环境配置正确，本目录下的adb.exe文件所在的目录一般会放在系统环境变量中。
3、以上1、2步配置完成后，程序运行环境就算配置完成。过程中遇到问题联系作者VX：ww1010351486。
''')
try:
    device_id = os.popen("adb devices").readlines()[1].split()[0]
except:
    print("没检测到adb运行环境！程序已退出。")
    quit()
d = u2.connect(device_id)
print("tips：请确保标签名一定输出正确，否则可能造成误删好友。")
del_friend_tag = input("你需要都删除哪个标签下的好友（输入标签名）：")
print("程序正在执行。。。")
d.press("home")
d.session("com.tencent.mm")
d(text="通讯录").click()
d(resourceId="com.tencent.mm:id/fx", text="标签").click()

count = 0
while True:
    d(scrollable=True).fling()
    d(text=del_friend_tag).click()
    d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
    time.sleep(1)
    if d.xpath('//*[@resource-id="com.tencent.mm:id/b4d"]').exists and d.xpath('//*[@resource-id="com.tencent.mm:id/b4d"]').text == '从群里导入':
        break
    else:
        nakename = d.xpath('//*[@resource-id="com.tencent.mm:id/b2f"]').text
        print("删除成功！\t" + nakename)
        d.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
        d(resourceId="com.tencent.mm:id/g6f").click()
        d.xpath('//*[@resource-id="com.tencent.mm:id/doz"]').click()
        d(resourceId="com.tencent.mm:id/dn").click()
        count = count + 1
        time.sleep(2)

if count == 0:
    print("此标签【f'{del_friend_tag}'】下没有好友！")
else:
    print('*'*10+f"好友删除完成！总共删除{count}个好友！"+'*'*10)
    os.system("adb uninstall com.github.uiautomator")

print("本窗口将在10秒后自动关闭，你也可手动关闭。")
time.sleep(10)
quit()