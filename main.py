#!/usr/bin/python3
import requests
import json
import tkinter
root = tkinter.Tk()
root.geometry("400x300")
AIresStr = tkinter.StringVar()
usersendedStr = tkinter.StringVar()
usersendedStr.set("")
AIresStr.set("「こんにちは」と入力してみましょう")
userLabel = tkinter.Label(root,textvariable=usersendedStr,width=100,anchor="e")
userLabel.pack()
AIresLabel = tkinter.Label(root,textvariable=AIresStr,width=100,anchor="w")
AIresLabel.pack()
textForm = tkinter.Entry(width=100)
textForm.pack()
def sendBtnHandler():
    res = requests.get("https://chatbot-api.userlocal.jp/api/chat?message={}&key=7002dfa1aa292270b905".format(textForm.get()))
    resJson = json.loads(res.text)
    print(resJson["result"])
    AIresStr.set("AI:" + resJson["result"])
    usersendedStr.set("あなた:" + textForm.get())
    textForm.delete(0,tkinter.END)
sendBtn = tkinter.Button(root,text="送信",command=sendBtnHandler,width=100)
sendBtn.pack()
root.mainloop()