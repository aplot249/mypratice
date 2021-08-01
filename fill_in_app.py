#@author: sareeliu
#@date: 2021/4/1 23:06
import pandas as pd
import uiautomator2 as ui2
import os,time


class FillApp:

    def __init__(self,excel_data):
        self.app = ui2.connect(FillApp.get_device_id())
        self.excel_data = excel_data

    @staticmethod
    def get_device_id():
        id = os.popen("adb devices").readlines()[1].partition("\t")[0]
        return id

    @classmethod
    def read_data(cls):
        data = pd.read_excel(
            io=r'C:\Users\Administrator.USER-20170512VI\Desktop\14局-员工信息(1).xlsx',
            usecols='D,E,H',
        )
        excel_data = [item for item in data.loc[:].values if item[2] == '未激活']
        return cls(excel_data)

    def run(self,):
        self.app.press('home')
        self.app.session('cn.redcdn.globalcare')

        for item in self.excel_data:
            self.app.xpath('//*[@resource-id="cn.redcdn.globalcare:id/rb_me"]').click() #点我
            self.app.xpath('//*[@resource-id="cn.redcdn.globalcare:id/gotomyfilecard_rl"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
            self.app(resourceId="cn.redcdn.globalcare:id/Login_numdemo_edit").set_text(item[1])
            self.app(resourceId="cn.redcdn.globalcare:id/Login_pwddemo_edit").set_text(str(item[1])[-6:])
            self.app(resourceId="cn.redcdn.globalcare:id/login_login_btn").click()
            self.app(resourceId="cn.redcdn.globalcare:id/tvName", text="几内亚达圣铁路项目").click()
            print(f"{item[0]} 账号激活成功！")

            self.app.xpath('//*[@resource-id="cn.redcdn.globalcare:id/rb_me"]').click() #点“我”
            self.app(resourceId="cn.redcdn.globalcare:id/gotomyfilecard_rl").click() #账号
            self.app(resourceId="cn.redcdn.globalcare:id/mycard_exit_btn").click()  #退出
            self.app(resourceId="cn.redcdn.globalcare:id/qn_operae_dialog_right_button").click()    #确认退出
            print(f"{item[0]} 账号已退出，进行下一个人！")
            self.app(resourceId="cn.redcdn.globalcare:id/iv_back").click()  #点左上角+号，界面返回
            time.sleep(2)


fillapp = FillApp.read_data()
fillapp.run()