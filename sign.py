#coding:utf-8
import requests,re
class v2ex:
    s=requests.Session()
    def login(self):
        loginpage = self.s.get("http://www.v2ex.com/signin").text
        payload={
            re.findall('type="text" class="sl" name="([a-f0-9]{64,64})"', loginpage)[0]:self.u,
            re.findall('type="password" class="sl" name="([a-f0-9]{64,64})"', loginpage)[0]:self.p,
            "next":"/",
            "once":re.findall('value="(\d+)" name="once"',loginpage)[0]
            }
        signin=self.s.post("http://www.v2ex.com/signin",data=payload,headers={'Referer': 'http://www.v2ex.com/signin'})
        if signin.text.find("signout")==-1:
            print self.u+" 登录失败！"
        else:
            print self.u+" 登录成功！"
            self.sign()
    def sign(self):
        if self.s.get("http://www.v2ex.com/mission/daily").text.find("fa-ok-sign")!=-1:
            print self.u+" 已领取过奖励!"
        else:
            try:
                daily=re.findall('(/mission/daily/redeem\?once=\d+)',self.s.get("http://www.v2ex.com/mission/daily").text)[0]
                a=self.s.get("http://www.v2ex.com"+daily,headers={"Referer":"http://www.v2ex.com/mission/daily"})
                print self.u+" 签到成功！"
            except:
                print self.u+" 签到失败！"
    def __init__(self,u,p):
        self.u=u
        self.p=p
        self.login()
v2ex("username","password")
