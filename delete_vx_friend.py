import del_vx_friend_object as delvx
import time,sys

class NewDel(delvx.DelvxFriend):
    def __init__(self):
        super(NewDel, self).__init__()

    def output_tip(self):
        self.tip = '''
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
                '''
        print(self.tip)

    def loop(self):
        while True:
            self.connector(resourceId="com.tencent.mm:id/fx", text="标签").click()    #点击标签按钮
            time.sleep(2)
            self.connector(scrollable=True).scroll.toEnd()  #从后翻
            time.sleep(3)
            # delvx.DelvxFriend.del_friend_tag = input("你需要都删除哪个标签下的好友（输入标签名）：")
            # if not self.connector(text=delvx.DelvxFriend.del_friend_tag).exists:
            if not self.connector.xpath('//*[@text="所有好友"]').exists:
                print("没找到标签这个标签")
            else:
                self.connector.xpath('//*[@text="所有好友"]').click()
                print('进入loop')
                self.connector.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()  # 点击第一个
                self.connector(resourceId="com.tencent.mm:id/b2b").click()  # 点击发送消息
                self.connector(resourceId="com.tencent.mm:id/aks").click()  # 点击右下角加号
                self.connector(resourceId="com.tencent.mm:id/pb", text="转账").click()  # 点击转账
                self.connector(resourceId="com.tencent.mm:id/cx_").click()  # 输入1元金额
                self.connector(resourceId="com.tencent.mm:id/cxi").click()  # 确认转账按钮
                try:
                    text = self.connector.xpath('//*[@resource-id="com.tencent.mm:id/dos"]').get_text()
                except:
                    print("存在，还是好友")
                    self.connector.xpath('//*[@content-desc="关闭"]/android.view.ViewGroup[1]').click()
                    self.connector(resourceId="com.tencent.mm:id/dn").click()  # 发消息界面
                    self.connector.xpath('//android.support.v7.widget.LinearLayoutCompat').click()  # 可添加多人聊天界面
                    self.connector.xpath(
                        '//*[@resource-id="com.tencent.mm:id/b1l"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()  # 名片页
                    time.sleep(2)
                    self.connector.xpath(
                        '//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()  # 标签页
                    self.connector(text="所有好友").click()  # 具体标签操作页面
                    self.connector.xpath('//*[@text="所有好友"]').long_click()   #去掉标签
                    time.sleep(2)
                    self.connector.xpath('//*[@text="所有好友"]').click()   #去掉标签
                    self.connector(resourceId="com.tencent.mm:id/ch").click()
                    self.connector(resourceId="com.tencent.mm:id/ch").click()
                    self.connector(resourceId="com.tencent.mm:id/dn").click()
                    self.connector(resourceId="com.tencent.mm:id/dn").click()
                    self.connector(resourceId="com.tencent.mm:id/dn").click()
                    self.connector(resourceId="com.tencent.mm:id/rr").click()
                else:
                    print(text)
                    self.connector(resourceId="com.tencent.mm:id/doz").click()
                    self.connector(resourceId="com.tencent.mm:id/dn").click()
                    self.connector.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
                    self.connector.xpath('//*[@resource-id="com.tencent.mm:id/b1l"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
                    self.connector.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
                    self.connector.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[8]').click()
                    self.connector(resourceId="com.tencent.mm:id/doz").click()
                finally:
                    self.connector(text="通讯录").click()

            #     print(text)
            #     quit()
            #     if self.connector(resourceId="com.tencent.mm:id/dot").exists():
            #         print("不存在")
            #         print("对方已经把你删除")
            #         self.connector(resourceId="com.tencent.mm:id/doz").click()
            #         self.connector(resourceId="com.tencent.mm:id/dn").click()
            #         self.connector.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
            #         self.connector.xpath('//*[@resource-id="com.tencent.mm:id/b1l"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            #         self.connector.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
            #         self.connector.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[8]').click()
            #         self.connector(resourceId="com.tencent.mm:id/doz").click()
            #     else:
            #         print("存在，还是好友")
            #         time.sleep(3)
            #
            #         self.connector.xpath('//*[@content-desc="关闭"]/android.view.ViewGroup[1]').click()
            #         self.connector(resourceId="com.tencent.mm:id/dn").click()
            #         self.connector.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
            #         self.connector.xpath('//*[@resource-id="com.tencent.mm:id/b1l"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            #         self.connector.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
            #         self.connector(text="所有好友").click()
            #         self.connector.xpath('//*[@resource-id="com.tencent.mm:id/cyh"]/android.widget.TextView[1]').click()
            #         self.connector.xpath('//*[@resource-id="com.tencent.mm:id/cyh"]/android.widget.TextView[1]').click()
            #         self.connector(resourceId="com.tencent.mm:id/ch").click()
            #         self.connector(resourceId="com.tencent.mm:id/ch").click()
            #         self.connector(resourceId="com.tencent.mm:id/dn").click()
            #         self.connector(resourceId="com.tencent.mm:id/dn").click()
            #         self.connector(resourceId="com.tencent.mm:id/rr").click()
            # self.connector(text="通讯录").click()



        # sys.exit()
        # count = 13
        # while True:
        #     [self.connector(scrollable=True).fling() for i in range(20)]
        #     # self.connector(scrollable=True).scroll.toEnd() #从后往前
        #     weizhi = f'//*[@resource-id="com.tencent.mm:id/f4"]/android.widget.LinearLayout[{count}]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]'
        #     if not self.connector.xpath(weizhi).exists:
        #         print("不存在，出错了")
        #         weizhi = f'//*[@resource-id="com.tencent.mm:id/f4"]/android.widget.LinearLayout[{count-1}]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]'
        #         item = self.connector.xpath(weizhi)
        #         [item.swipe("down") for i in range(2)]
        #     else:
        #         print("存在的时候执行")
        #         item = self.connector.xpath(weizhi)
        #         item.click()    #进入
        #         self.connector(resourceId="com.tencent.mm:id/b2b").click()
        #         self.connector(resourceId="com.tencent.mm:id/aks").click()
        #         time.sleep(3)
        #         self.connector(resourceId="com.tencent.mm:id/pb", text="转账").click()
        #         self.connector(resourceId="com.tencent.mm:id/cx_").click()  #输入1块钱
        #         self.connector(resourceId="com.tencent.mm:id/cxi").click()  # 点击确认，进入输入密码界面，进行识别
        #         time.sleep(5)
        #         if self.connector(resourceId="com.tencent.mm:id/dot").exists():
        #             print("对方已经把你删除")
        #             self.connector(resourceId="com.tencent.mm:id/doz").click()
        #             self.connector(resourceId="com.tencent.mm:id/dn").click()
        #             self.connector.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
        #             self.connector.xpath(
        #                 '//*[@resource-id="com.tencent.mm:id/b1l"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        #             self.connector.xpath('//android.support.v7.widget.LinearLayoutCompat').click()
        #             self.connector.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[8]').click()
        #             self.connector(resourceId="com.tencent.mm:id/doz").click()
        #         else:
        #             print("还是好友")
        #             self.connector.xpath('//*[@content-desc="关闭"]/android.view.ViewGroup[1]').click()
        #             self.connector(resourceId="com.tencent.mm:id/dn").click()
        #             self.connector(resourceId="com.tencent.mm:id/rr").click()
        #         self.connector(text="通讯录").click()
        #         count -= 1
        #         [item.swipe("down") for i in range(2)]
        #         print("现在count是：" + str(count))


newdel = NewDel()
newdel.run()