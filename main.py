import asyncio
import csv
from datetime import time
import time, os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from bilibili_api import live, sync
import socket
import json
from enum import IntEnum
from bilibili_api import settings
# live room parameters
from bilibili_api.user import User

# 代理服务器(产品官网 www.16yun.cn)
proxyHost = "u7713.20.tn.16yun.cn"
proxyPort = "6227"

# 代理验证信息
proxyUser = "16PADDGK"
proxyPass = "649418"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host" : proxyHost,
    "port" : proxyPort,
    "user" : proxyUser,
    "pass" : proxyPass,
}
settings.proxy = proxyMeta


presist_data_file_name = "presist_file.csv"


# myRoom = 23982147
myRoom = 3645373
#room = live.LiveDanmaku(23839907)
# room = live.LiveDanmaku(3645373)
room = live.LiveDanmaku(myRoom)
#room = live.LiveDanmaku(22884968)
# communication with unity c#
UDP_IP = "127.0.0.1"
# UDP_IP = "localhost"
UDP_PORT = 60009
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP


# define communication data type
class payloadType(IntEnum):
    NEW_PLAYER = 1
    NEW_DANMU = 2
    NEW_GIFT = 3
    ANY_FACE = 4
    TOP_THREE = 5


def sendJsonWithPayloadTypeUDP(myPayloadType, payload):

    dicDataWithPayloadType = {"payloadType": myPayloadType,
                              "payload": payload}
    jsonDataWithPayloadType = json.dumps(dicDataWithPayloadType)
    # print(time.asctime())
    # print(jsonDataWithPayloadType)
    with open(presist_data_file_name,'a+',newline='') as csvfile:
        fieldnames = ['time','room','dataType','data']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'time':time.asctime(),'room':myRoom,'dataType':myPayloadType,'data':payload})
    sock.sendto(jsonDataWithPayloadType.encode('utf-8'),
                (UDP_IP, UDP_PORT))



@room.on('INTERACT_WORD')
async def on_join(event):

    myData = event["data"]
    myLayer2Data = myData["data"]
    myUserID = myLayer2Data["uid"]
    # userInfo = await User(myUserID).get_user_info()
    # jsonUserInfo = json.dumps(userInfo)
    jsonJoinMsg = json.dumps(event)
    sendJsonWithPayloadTypeUDP(payloadType.NEW_PLAYER,
                               jsonJoinMsg)
    userInfo = await User(myUserID).get_user_info()
    sendFaceData(userInfo)

    print("new player")


@room.on('DANMU_MSG')
async def on_danmaku(event):

    myData = event["data"]
    myInfo = myData["info"]
    myMsg = myInfo[1]
    myUserID = myInfo[2][0]
    myUserName = myInfo[2][1]

    #construct json
    dicDmMsg = {"MSG":myMsg,
                "USERID":myUserID,
                "USERNAME":myUserName}
    jsonDmMsg = json.dumps(dicDmMsg)
    sendJsonWithPayloadTypeUDP(payloadType.NEW_DANMU,
                               jsonDmMsg)

    userInfo = await User(myUserID).get_user_info()
    sendFaceData(userInfo)
    # jsonUserInfo = json.dumps(userInfo)
    # sendJsonWithPayloadTypeUDP(payloadType.NEW_DANMU,
    #                            jsonUserInfo)
    print("DM")


@room.on('SEND_GIFT')
async def on_gift(event):
    jsonGiftMsg = json.dumps(event)
    # myData = event["data"]
    # myLayer2Data = myData["data"]
    # myUserID = myLayer2Data["uid"]
    # userInfo = await User(myUserID).get_user_info()
    # jsonUserInfo = json.dumps(userInfo)
    sendJsonWithPayloadTypeUDP(payloadType.NEW_GIFT,
                               jsonGiftMsg)
    print("GIFT")


@room.on('ALL')
async def on_face(event):

    myFaceJson = json.dumps(event)
    if("face" in myFaceJson):
        startPoint = myFaceJson.find("face")+8
        endPoint = myFaceJson.find(",",startPoint,-1)-1
        dynamicUrl = myFaceJson[startPoint:endPoint]
        listDynamicUrl = list(dynamicUrl)
        listDynamicUrl[8] = '0'
        staticFaceUrl = "".join(listDynamicUrl)

        myFace = staticFaceUrl

        uidStartPoint = myFaceJson.find("uid")+6
        uidEndPoint = myFaceJson.find(",",uidStartPoint,-1)

        myUID = myFaceJson[uidStartPoint:uidEndPoint]

        #construct dic

        dicFaceData = {"uid": myUID,
                       "uface": myFace}
        jsonFaceData = json.dumps(dicFaceData)
        sendJsonWithPayloadTypeUDP(payloadType.ANY_FACE,
                                   jsonFaceData)

def sendFaceData(event):
    myFaceJson = json.dumps(event)
    if("face" in myFaceJson):
        startPoint = myFaceJson.find("face")+8
        endPoint = myFaceJson.find(",",startPoint,-1)-1
        dynamicUrl = myFaceJson[startPoint:endPoint]
        listDynamicUrl = list(dynamicUrl)
        listDynamicUrl[8] = '0'
        staticFaceUrl = "".join(listDynamicUrl)

        myFace = staticFaceUrl

        uidStartPoint = myFaceJson.find("uid")+6
        uidEndPoint = myFaceJson.find(",",uidStartPoint,-1)

        myUID = myFaceJson[uidStartPoint:uidEndPoint]

        #construct dic

        dicFaceData = {"uid": myUID,"uface": myFace}
        jsonFaceData = json.dumps(dicFaceData)
        sendJsonWithPayloadTypeUDP(payloadType.ANY_FACE,jsonFaceData)

async def get_top_three_data_thread():
    # baseurl = "https://live.bilibili.com/3645373"
    baseurl = "https://live.bilibili.com/"+str(myRoom)
    driver = webdriver.Firefox()
    driver.get(baseurl)
    while True:
        print("start sleeping")
        await asyncio.sleep(1)
        print("sleep finished")
        top_3_player = {"rank1": {"uname":"","uscore":""},
                        "rank2": {"uname":"","uscore":""},
                        "rank3": {"uname":"","uscore":""}}
        try:
            top_3_player["rank1"]["uname"] = driver.find_element(By.CSS_SELECTOR,"div.top3-item:nth-child(1) > div:nth-child(3)").get_attribute('innerHTML')
            top_3_player["rank1"]["uscore"] = driver.find_element(By.CSS_SELECTOR,"div.top3-item:nth-child(1) > div:nth-child(4)").get_attribute('innerHTML')
        except selenium.common.exceptions.NoSuchElementException:
            top_3_player["rank1"]["uname"] = "NOPLAYER"
        try:
            top_3_player["rank2"]["uname"] = driver.find_element(By.CSS_SELECTOR,"div.top3-item:nth-child(2) > div:nth-child(3)").get_attribute('innerHTML')
            top_3_player["rank2"]["uscore"] = driver.find_element(By.CSS_SELECTOR,"div.top3-item:nth-child(2) > div:nth-child(4)").get_attribute('innerHTML')
        except selenium.common.exceptions.NoSuchElementException:
            top_3_player["rank2"]["uname"] = "NOPLAYER"
        try:
            top_3_player["rank3"]["uname"] = driver.find_element(By.CSS_SELECTOR,"div.top3-item:nth-child(3) > div:nth-child(3)").get_attribute('innerHTML')
            top_3_player["rank3"]["uscore"] = driver.find_element(By.CSS_SELECTOR,"div.top3-item:nth-child(3) > div:nth-child(4)").get_attribute('innerHTML')
        except selenium.common.exceptions.NoSuchElementException:
            top_3_player["rank3"]["uname"] = "NOPLAYER"
        print(top_3_player)
        jsonTop3Data = json.dumps(top_3_player)
        sendJsonWithPayloadTypeUDP(payloadType.TOP_THREE,jsonTop3Data)

    driver.quit()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
tasks = [get_top_three_data_thread(),
         room.connect()]
loop.run_until_complete(asyncio.wait(tasks))

# sync(room.connect())
