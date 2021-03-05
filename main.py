from bs4 import BeautifulSoup
import PySimpleGUI as sg
import requests
import os
layout=[

    [sg.T("Type To Scrape")],
    [sg.In(key="--IN--")],
    [sg.B("Scrape")],
    [sg.T(key="--OUT--",size=(20,2))]
]






window=sg.Window(title="Scrape Images",grab_anywhere=True,layout=layout)
i=0
while True:
    event,values=window.read()
    text = values['--IN--']
    if event==sg.WINDOW_CLOSED:
        break
    if event=="Scrape":
        try:
            os.mkdir(text)
            img_content = []
            html=requests.get("https://www.google.com/search?q="+text+"&sxsrf=ALeKk03Zxfda-gfuGG6g5J8v2tltwg0dtg:1611927596857&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjs-MCeosHuAhXhoXEKHR_dDc4Q_AUoAXoECC8QAw&biw=1920&bih=967")
            soup = BeautifulSoup(html.text, 'html.parser')
            for img in soup.findAll('img'):
                images=img.get('src')
                if images.startswith("https"):
                    imgs=requests.get(images)
                    img_content.append(imgs.content)
                    i=1
                    for cont in img_content:
                        if i<len(cont):
                            with open(text+"/"+text+str(i)+".jpeg",'wb') as f:
                                f.write(cont)
                                i+=1
                                window['--OUT--'].Update("Images Scrape "+str(len(os.listdir(os.getcwd() + "\\" + text))))
        except FileExistsError:
            window['--OUT--'].Update(value="File Already Exist",text_color="red")

