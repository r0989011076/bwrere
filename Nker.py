# -*- coding: utf-8 -*-
from Linephu.linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
#==============================================================================#
cl = LINE()
cl.log("授權權杖:" + str(cl.authToken))
print ("""
██████████████████████████████████████████
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░██
██░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒░░░░░██
██░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░██
██░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▒▒░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░██
██████████████████████████████████████████

登入完成""")
#==============================================================================#
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
banOpen = codecs.open("ban.json","r","utf-8")
#==============================================================================#
read = json.load(readOpen)
settings = json.load(settingsOpen)
ban = json.load(banOpen)
#==============================================================================#
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
wait = {
      "ban":False,
	  "unban":False,
}	  
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
#==============================================================================#
admin=['u92dec7a46b4afbf26b8e3ed60d22cc10',clMID]
Owner=['u92dec7a46b4afbf26b8e3ed60d22cc10',clMID]
#==============================================================================#
msg_dict = {}
bl = [""]
#==============================================================================#
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#===helpmessage========================================helpmessage=============#		
def helpmessage():
    helpMessage = """╔══════════════┓
╠══✪Nker查看指令表✪════
╠═════════════=═
╠❂➣【Help】查看全部指令
╠❂➣【HelpTag】查看標註指令
╠❂➣【HelpKick】查看踢人指令
╠════✪狀態✪═══════
╠❂➣【Rebot】重新啟動機器
╠❂➣【Runtime】查看機器運行時間
╠❂➣【Speed】查看機器速度
╠❂➣【Set】查看設定
╠❂➣【About】查看自己的狀態
╠❂➣【Bot:bye】機器退出群組
╠❂➣【作者】查看作者
╠════✪設定✪═══════
╠❂➣【Add On/Off】自動加入好友 開啟/關閉
╠❂➣【Join On/Off】邀請自動進入群組 開啟/關閉
╠❂➣【Leave On/Off】自動離開副本 開啟/關閉
╠❂➣【Read On/Off】自動已讀 開啟/關閉
╠❂➣【Inviteprotect On/Off】群組邀請保護 開啟/關閉
╠❂➣【Reread On/Off】查看收回 開啟/關閉
╠❂➣【Qr On/Off】群組網址保護 開啟/關閉
╠❂➣【Qrjoin On/Off】網址自動入群 開啟/關閉
╠❂➣【Ck On/Off】貼圖資料查詢 開啟/關閉
╠❂➣【Protect On/Off】群組保護 開啟/關閉
╠❂➣【Timeline On/Off】文章網址 開啟/關閉
╠❂➣【Wc On/Off】歡迎消息 開啟/關閉
╠❂➣【Nk On/Off】踢人顯示開啟 開啟/關閉
╠════✪自己✪═══════
╠❂➣【Me】丟出自己好友資料
╠❂➣【MyMid】查看自己MID
╠❂➣【MyName】查看自己名字
╠❂➣【MyBio】查看自己個簽
╠❂➣【MyPicture】查看自己頭貼網址
╠❂➣【MyCover】查看自己封面網址
╠❂➣【Contact @】標註查看好友資料
╠❂➣【Mid @】標註查看系統識別碼
╠❂➣【Name @】標註查看名稱
╠❂➣【Bio @】標註查看狀態消息
╠❂➣【Picture @】標註查看頭貼
╠❂➣【Cover @】標注查看封面
╠❂➣【Friendlist】查看好友清單
╠════✪群組✪═══════
╠❂➣【Gowner】查看群組擁有者
╠❂➣【Gurl】丟出群組網址
╠❂➣【O/Curl】打開/關閉群組網址
╠❂➣【Lg】查看所有群組
╠❂➣【Gb】查看群組成員
╠❂➣【Ginfo】查看群組狀態
╠❂➣【Ri @】標註來回機票
╠❂➣【Tk @】標注踢出成員(多踢)
╠❂➣【Mk @】標注踢出成員(單踢)
╠❂➣【Vk @】標註踢出並清除訊息
╠❂➣【Nk Name】使用名子踢出成員
╠❂➣【Uk mid】使用系統識別碼踢出成員
╠❂➣【NT Name】使用名子標註成員
╠❂➣【Zk】踢出0字元
╠❂➣【Zt】標註名字0字成員
╠❂➣【Zm】丟出0字成員的系統識別碼
╠❂➣【Cancel】取消所有成員邀請
╠❂➣【Gcancel】取消所有群組邀請
╠❂➣【Gn Name】更改群組名稱
╠❂➣【Gc @】標註查看個人資料
╠❂➣【Inv mid】使用系統識別碼邀請進入群組
╠❂➣【Ban @】標註加入黑單
╠❂➣【Unban @】標註解除黑單
╠❂➣【Clear Ban】清空黑單
╠❂➣【Kill Ban】剔除黑單
╠❂➣【Zk】踢出名字0字成員
╠❂➣【banlist】查看黑名單 
╠❂➣【Sc gid】查看指定群組狀態
╠❂➣【Mc mid】指定mid友資查詢
╠════✪特別✪═══════
╠❂➣【Tagall】標註群組所有成員 
╠❂➣【S N/F/R】已讀點 開啟/關閉/重設  
╠❂➣【R】查看已讀  
╠❂➣【/invitemeto:】使用群組識別碼邀請至群組
╠❂➣【Adminadd @】標註加入權限
╠❂➣【Admindel @】標註取消權限
╠❂➣【Adminlist】查詢權限者清單
╠════✪═══✪═══════
"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""
╠══✪標注指令表✪════
╠❂➣【Ri @】標註來回機票
╠❂➣【Tk @】標注踢出成員(多踢)
╠❂➣【Mk @】標注踢出成員(單踢)
╠❂➣【Vk @】標註踢出並清除訊息
╠❂➣【Gc @】標註查看個人資料
╠❂➣【Mid @】標註查看系統識別碼
╠❂➣【Name @】標註查看名稱
╠❂➣【Bio @】標註查看狀態消息
╠❂➣【Picture @】標註查看頭貼
╠❂➣【Cover @】標注查看封面
╠❂➣【Ban @】標註加入黑單
╠❂➣【Unban @】標註解除黑單
╠════✪═══✪═══════
XXX"""
    return helpMessageTag
def helpmessagekick():
    helpMessageKick ="""
╠══✪踢人指令✪════
╠❂➣【Ri @】標註來回機票
╠❂➣【Tk @】標注踢出成員(多踢)
╠❂➣【Mk @】標注踢出成員(單踢)
╠❂➣【Vk @】標註踢出並清除訊息
╠❂➣【Vk:mid】使用系統識別碼踢出並清除訊息
╠❂➣【Nk Name】使用名子踢出成員
╠❂➣【Uk mid】使用系統識別碼踢出成員
╠❂➣【Kill ban】踢出黑單成員
╠❂➣【Zk】踢出名字0字成員
╠════✪═══✪═══════
XXXX"""
    return helpMessageKick
#==============================================================================#	
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "😇安安😇 {} 感謝您加我為好友😇".format(str(contact.displayName)))
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "網址保護中...不要動群組網址！")
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param2])
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
        if op.type == 24:
            print ("[ 24 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新配置文件")
#==============================================================================#		
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#==============================================================================#
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["ban"] == True:
                   if msg._from in admin:
                       if msg.contentMetadata["mid"] in settings["blacklist"]:
                           cl.sendMessage(msg.to,"already")
                           wait["ban"] = False
                       else:
                           settings["blacklist"][msg.contentMetadata["mid"]] = True
                           wait["ban"] = False
                           cl.sendMessage(msg.to,"ok")
               elif wait["unban"] == True:
                   if msg._from in admin:
                       if msg.contentMetadata["mid"] not in settings["blacklist"]:
                           cl.sendMessage(msg.to,"already")
                           wait["unban"] = False
                       else:
                           del settings["blacklist"][msg.contentMetadata["mid"]]
                           wait["unban"] = False
                           cl.sendMessage(msg.to,"ok")
#==============================================================================#				
            if msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ 貼圖資料 ]"
                    ret_ += "\n貼圖ID : {}".format(stk_id)
                    ret_ += "\n貼圖包ID : {}".format(pkg_id)
                    ret_ += "\n貼圖網址 : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n貼圖圖片網址：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "文章網址：\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendMessage(msg.to,msg.text)
            if msg.contentType == 0:
                if text is None:
                    return
#=============help=============================================================#					
            if sender in admin:
                if msg.text in ["help","Bot1:help"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == 'helptag':
                    helpMessageTag = helpmessagetag()
                    cl.sendMessage(to, str(helpMessageTag))
                elif text.lower() == 'helpkick':
                    helpMessageKick = helpmessagekick()
                    cl.sendMessage(to, str(helpMessageKick))
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "檢查中......")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動中請稍後...")
                    time.sleep(5)
                    cl.sendMessage(to, "重新啟動完成😇")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運行時間 {}".format(str(runtime)))
#=============================================================================#					
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u92dec7a46b4afbf26b8e3ed60d22cc10"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "╔══[關於自己]"
                        ret_ += "\n╠۝名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠۝群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠۝好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠۝封鎖 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[關於機器]"
                        ret_ += "\n╠۝ 作者 ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[完]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))	
#=================歡迎消息====================== =========================#
                elif text.lower() == 'wc on':
                    settings["Wc"] = True
                    cl.sendMessage(to, "歡迎消息開啟 ✔")
                elif text.lower() == 'wc off':
                    settings["Wc"] = False
                    cl.sendMessage(to, "歡迎消息關閉 ✘")	
#=================踢人顯示====================================================#
                elif text.lower() == 'nk on':
                    settings["Nk"] = True
                    cl.sendMessage(to, "踢人顯示開啟 ✔")
                elif text.lower() == 'nk off':
                    settings["Nk"] = False
                    cl.sendMessage(to, "踢人顯示關閉 ✘")						
#=====================================作者====================================#		
                elif text.lower() == '作者':						
                    cl.sendContact(to, "u92dec7a46b4afbf26b8e3ed60d22cc10")
#===========================================自己MID===========================#	
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[自己MID]\n" +  clMID)
#===========================================顯示名稱============================#	
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[顯示名稱]\n" + me.displayName)
#=============================================================================#
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友已開啟 ✔")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友已關閉 ✘")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動加入群組已開啟 ✔")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動加入群組已關閉 ✘")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開啟 ✔")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關閉 ✘")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    cl.sendMessage(to, "查看好友資料詳情開啟 ✔")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    cl.sendMessage(to, "查看好友資料詳情關閉 ✘")
                elif text.lower() == 'protect on':
                    settings["protect"] = True
                    cl.sendMessage(to, "群組保護已開啟 ✔")
                elif text.lower() == 'protect off':
                    settings["protect"] = False
                    cl.sendMessage(to, "群組保護已關閉 ✘")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "群組邀請保護已開啟 ✔")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "群組邀請保護已關閉 ✘")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "群組網址保護已開啟 ✔")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "群組網址保護已關閉 ✘")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟 ✔")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉 ✘")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟 ✔")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉 ✘")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    cl.sendMessage(to, "網址自動入群已開啟 ✔")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "網址自動入群已關閉 ✘")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "標註回覆已開啟 ✔")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "標註回覆已關閉 ✘")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    cl.sendMessage(to, "貼圖資料查詢已開啟 ✔")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    cl.sendMessage(to, "貼圖資料查詢已關閉 ✘")
                elif text.lower() == 'timeline on':
                    settings["timeline"] = True
                    cl.sendMessage(to, "文章網址已開啟 ✔")
                elif text.lower() == 'timeline off':
                    settings["timeline"] = False
                    cl.sendMessage(to, "文章網址已關閉 ✘")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)

                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[狀態消息]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
#=============================================================================#					
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔═[ 設定 ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠自動加友 ✅"
                        else: ret_ += "\n╠自動加友 ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠自動入群 ✅"
                        else: ret_ += "\n╠自動入群 ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n╠網址入群 ✅"
                        else: ret_ += "\n╠網址入群 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠自離副本 ✅"
                        else: ret_ += "\n╠自離副本 ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠自動已讀 ✅"
                        else: ret_ += "\n╠自動已讀 ❌"
                        if settings["protect"] == True: ret_ += "\n╠群組保護 ✅"
                        else: ret_ += "\n╠群組保護 ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠邀請保護 ✅"
                        else: ret_ += "\n╠邀請保護 ❌"
                        if settings["qrprotect"] == True: ret_ += "\n╠網址保護 ✅"
                        else: ret_ += "\n╠網址保護 ❌"
                        if settings["contact"] == True: ret_ += "\n╠詳細資料 ✅"
                        else: ret_ += "\n╠詳細資料 ❌"
                        if settings["reread"] == True: ret_ += "\n╠查詢收回 ✅"
                        else: ret_ += "\n╠查詢收回 ❌"
                        if settings["detectMention"] == False: ret_ += "\n╠標註回覆 ✅"
                        else: ret_ += "\n╠標註回覆 ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠貼圖開啟 ✅"
                        else: ret_ += "\n╠貼圖關閉 ❌"
                        if settings["timeline"] == True: ret_ += "\n╠文章網址 ✅"
                        else: ret_ += "\n╠文章網址 ❌"	
                        if settings["Wc"] == True: ret_ += "\n╠歡迎顯示 ✅"
                        else: ret_ += "\n╠歡迎顯示 ❌"	
                        if settings["Nk"] == True: ret_ += "\n╠踢人顯示 ✅"
                        else: ret_ += "\n╠踢人顯示 ❌"						
                        ret_ += "\n╚═[ 完 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))						
#==========================================================================#	
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif "Ri:" in msg.text:
                    midd = text.replace("Ri:","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "Mk " in msg.text:
                    Mk0 = text.replace("Mk ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = cl.getGroup(to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = cl.getGroup(to)
                            cl.sendMessage(to, "降臨🙉")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            cl.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = cl.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            mc = sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to,mc)
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = "0字元使用者Mid："
                        for mi_d in targets:
                            mc += "\n->" + mi_d
                        cl.sendMessage(to,mc)
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    cl.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = cl.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "[群組資料]"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n[完]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "取消人數:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower() == 'gcancel':
                    gid = cl.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "全部群組邀請已取消")
                    cl.sendMessage(to, "取消時間: %s秒" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"無法使用在群組外")
                elif text.lower().startswith('adminadd '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        cl.sendMessage(to, "已新增權限！")
                elif text.lower().startswith('admindel '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        cl.sendMessage(to, "已移除權限！")
                elif text.lower().startswith('mop:'):
                        midd = msg.text.replace("mop:","")
                        admin.append(str(midd))
                        cl.sendMessage(to, "已加入權限！") 
                        backupData()
                elif text.lower().startswith('mdp:'):
                        midd = msg.text.replace("mdp:","")
                        admin.remove(str(midd))
                        cl.sendMessage(to, "已刪除權限！") 
                        backupData()
                elif text.lower() == 'opmid':
                    if admin == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        mc = "權限者清單："
                        for mi_d in admin:
                            mc += "\n-> " + mi_d
                        cl.sendMessage(to, mc)
                elif text.lower() == 'adminlist':
                    if admin == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        mc = "權限者清單："
                        for mi_d in admin:
                            mc += "\n-> " + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n頭貼網址 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n封面網址 :\n" + str(cu))
                        except:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n封面網址:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
#=============================================================================#					
                elif msg.text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["blacklist"][target] = True
                            cl.sendMessage(msg.to,"已加入黑單!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif "Ban:" in msg.text:
                    mmtxt = text.replace("Ban:","")
                    try:
                        settings["blacklist"][mmtext] = True
                        cl.sendMessage(msg.to,"已加入黑單!")
                    except:
                        cl.sendMessage(msg.to,"添加失敗 !")
                elif msg.text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["blacklist"][target]
                            cl.sendMessage(msg.to,"刪除成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "╔══[ Black List ]"
                        for mi_d in settings["blacklist"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'nkban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in settings["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendMessage(msg.to,"Blacklist kicked out")
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'banmidlist':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        cl.sendMessage(to, "以下是黑名單")					
                        mc = "╔══[ 黑名單 ]"
                        for mi_d in settings["blacklist"]:
                            mc += "\n╠ "+mi_d
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")		
#=============================================================================# 
                elif text.lower() == 'ban':
                    cl.sendMessage(to, "請傳送友資加入黑名單")
                    wait["ban"] = True
                elif text.lower() == 'unban':
                    cl.sendMessage(to, "請傳送友資移除黑名單")
                    wait["unban"] = True					
#=============================================================================#		
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "沒有黑名單")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "黑名單已踢除")					
#=============================================================================#

                elif text.lower() == 'bot:bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            cl.leaveGroup(to)
                        except:
                            pass
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        cl.sendMessage(to, "請輸入群組ID")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendMessage(to, "我不在那個群組裡")
                elif msg.text in ["Friendlist"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"「 朋友列表 」\n"+ap+"人數 : "+str(len(anl)))

                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[MID]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 名稱 ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 個簽 ]\n" + contact.statusMessage)
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("mpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendVideoWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif text.lower() == 'gowner':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組ID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "群組網址未開啟，請用Ourl先開啟".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開啟")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功開啟群組網址")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關閉")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功關閉群組網址")
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《群組資料》"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[成員列表]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[總共： {} 人]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[群組列表]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 個成員".format(str(len(nama))))
                elif text.lower() == 'sn':
                    tz = pytz.timezone("Asia/Taipei")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to,"已讀點已設定")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "已讀點設定:\n" + readTime)
                            
                elif text.lower() == 'sf':
                    tz = pytz.timezone("Asia/Taipei")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        cl.sendMessage(msg.to,"已讀點已刪除")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        cl.sendMessage(msg.to, "刪除已讀點:\n" + readTime)
    
                elif text.lower() == 'sr':
                    tz = pytz.timezone("Asia/Taipei")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        cl.sendMessage(msg.to, "已讀點重置:\n" + readTime)
                    else:
                        cl.sendMessage(msg.to, "已讀點未設定")
                        
                elif text.lower() == 'r':
                    tz = pytz.timezone("Asia/Taipei")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            cl.sendMessage(receiver,"[ 已讀的人 ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ 已讀的人 ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ 已讀時間 ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        cl.sendMessage(receiver,"未設定已讀點")
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[回收訊息者]\n%s\n[回收內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["收回訊息"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "標我有事？(此為系統自動回覆)")
                                    sendMessageWithMention(to, contact.mid)
                                break
#==============================================================================#
        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Wc"] == True:
             if op.param2 in clMID:
                 return
             dan = cl.getContact(op.param2)
             tgb = cl.getGroup(op.param1)
             cl.sendMessage(op.param1,"歡迎 {} 加入群組 {}".format(str(dan.displayName),str(tgb.name)))
             cl.sendContact(op.param1, op.param2)
#==============================================================================#			 
        if op.type == 19:
           print ("MEMBER KICKOUT TO GROUP")
           if settings["Nk"] == True:
             if op.param2 in clMID:
                 return
             dan = cl.getContact(op.param2)
             tgb = cl.getGroup(op.param1)
             cl.sendMessage(op.param1,"警告{}!!".format(str(dan.displayName)))
             cl.sendContact(op.param1, op.param2)
#==============================================================================#								
        if op.type == 55:
            print ("[ 55 ] 通知讀取消息")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
