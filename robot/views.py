
#coding:utf-8
import requests
import itchat
from robot.robot_function import renre_nmovi,baidu_url,sain_rul
from django.http import JsonResponse
from robot.function import now_history
import time
# 去图灵机器人官网注册后会生成一个apikey，可在个人中心查看
KEY = '2b4935050d4b4bc886eb949e0341e617'

def get_response(msg):
    print(msg)
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'   : KEY,
        'info'   : msg,   # 这是要发送出去的信息
        'userid'  : 'wechat-rebot',  #这里随意写点什么都行
    }
    try:
        # 发送一个post请求
        r = requests.post(apiUrl, data =data).json()
        # 获取文本信息，若没有‘Text’ 值，将返回Nonoe
        print(r.get('text'))
        return r.get('text')
    except:
        return



robot_switch={"status":"YES"}#机器人回复开关状态
robot_time={}
context="""
示例：@喵喵怪 #1 (查看第一季)
行尸走肉 第一季：回复：1
行尸走肉 第二季：回复：2
行尸走肉 第三季：回复：3
行尸走肉 第四季：回复：4
行尸走肉 第五季：回复：5
行尸走肉 第六季：回复：6
行尸走肉 第七季：回复：7
行尸走肉 第八季：回复：8
行尸走肉 第九季：回复：9"""


user=["@968bf9c292613d8d5ff7f7e6b3f7dee15db7a589a0b83fc589a9ce8db4393bbf"]
# num=input("请输入你需要查看的序号:")
# print(context)
# url=sain_rul(f"http://www.nanyingfang.com/movie/The%20Walking%20Dead/{num}.html")
# print("当前URL地址：",url)
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def print_content(msg):
    print(msg)
    content={"need":context}
    if msg.User["NickName"]=='【行尸走肉】美剧帝国'or msg.User["NickName"]=='另外一个你希望自动回复群的名字':    #这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字'
    # print(msg.User['NickName'] +":"+ msg['Text'])     #打印哪个群给你发了什么消息
        if "@喵喵怪" in msg.Text:
            text=str(msg.Text).split("@喵喵怪")[1].strip()
            if "#" in msg.Text:
                text=str(msg.Text).split("#")[1]
                url = sain_rul(f"http://www.nanyingfang.com/movie/The%20Walking%20Dead/{text}.html")
                itchat.send(url+f"\n请查收第{text}季全集@"+ msg.ActualNickName,msg.User["UserName"])
            elif "关闭" in text:
                print("已关闭机器人")
                robot_switch["status"]="NO"
            elif "开启" in text:
                print("已开启机器人")
                robot_switch["status"]="YES"
            else:
                pass
                # text=content.get(str(msg.Text).split("@喵喵怪")[1].strip(),"呜呜呜，听不懂哇！！！\n请回复 need 获取电影资源")
                # itchat.send(text,msg.User["UserName"])
        else:
            if robot_time.setdefault("date",int(time.time())):
                if int(time.time())-int(robot_time["date"]) >= 10:
                    if robot_switch["status"] == "YES":
                        print("执行自动化啦")
                        robot_time["date"]=int(time.time())
                        print(int(time.time()), int(robot_time["date"]),int(robot_time["date"]) - int(time.time()))
                        itchat.send(get_response(msg.Text), msg.User["UserName"])
                else:
                    print("小于10秒",int(time.time()) , int(robot_time["date"]),int(robot_time["date"])-int(time.time()))
                # print(get_response(msg['Text'])+"\n")           #打印机器人回复的消息
        # return get_response(msg['Text'])
    else:                                         #其他群聊直接忽略
        pass

def main(request):
    itchat.auto_login(hotReload=True)
    i=itchat.run()
    print(i)
    if i:
        return JsonResponse({"code":200})